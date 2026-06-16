from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
MASTER_REFS = SKILLS_DIR / "gtm-master" / "references"
TOOLS_DIR = ROOT / "tools"
RENDERER_SCRIPT = ROOT / "scripts" / "render-gtm-dashboard-from-report-state.py"
GOLDEN_DASHBOARD = ROOT / "artifacts" / "dry-runs" / "generic-hardware-s00-s08-s13-s14-dashboard.html"


class VisibleTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.skip = False
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style"}:
            self.skip = True

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style"}:
            self.skip = False

    def handle_data(self, data: str) -> None:
        if not self.skip and data.strip():
            self.parts.append(re.sub(r"\s+", " ", data.strip()))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def add_error(errors: list[str], path: Path, message: str) -> None:
    rel = path.relative_to(ROOT)
    errors.append(f"{rel}: {message}")


def check_skill_frontmatter(errors: list[str]) -> None:
    for skill_file in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        text = read_text(skill_file)
        match = re.match(r"^---\s*\r?\n(.*?)\r?\n---\s*\r?\n", text, re.DOTALL)
        if not match:
            add_error(errors, skill_file, "missing YAML frontmatter")
            continue

        frontmatter = match.group(1)
        if not re.search(r"^name:\s*\S+", frontmatter, re.MULTILINE):
            add_error(errors, skill_file, "frontmatter missing name")
        if not re.search(r"^description:\s*\S+", frontmatter, re.MULTILINE):
            add_error(errors, skill_file, "frontmatter missing description")


def load_yaml(path: Path, errors: list[str]) -> object | None:
    try:
        return yaml.safe_load(read_text(path))
    except Exception as exc:  # noqa: BLE001 - validation should report parser detail.
        add_error(errors, path, f"YAML parse failed: {exc}")
        return None


def check_master_yaml(errors: list[str]) -> tuple[dict, dict]:
    loaded: dict[str, object] = {}
    for yaml_file in sorted(MASTER_REFS.glob("*.yaml")):
        loaded[yaml_file.name] = load_yaml(yaml_file, errors)

    codegraph = loaded.get("codegraph.yaml")
    method_cards = loaded.get("method-cards.yaml")
    return (
        codegraph if isinstance(codegraph, dict) else {},
        method_cards if isinstance(method_cards, dict) else {},
    )


def implemented_graph_skills(codegraph: dict) -> list[tuple[str, dict]]:
    graph_skills = codegraph.get("skills", {})
    if not isinstance(graph_skills, dict):
        return []

    folders = {p.parent.name for p in SKILLS_DIR.glob("*/SKILL.md")}
    implemented: list[tuple[str, dict]] = []
    for skill_id, node in sorted(graph_skills.items()):
        if isinstance(node, dict) and node.get("name") in folders:
            implemented.append((skill_id, node))
    return implemented


def check_method_cards_and_output_contracts(codegraph: dict, method_cards_doc: dict, errors: list[str]) -> None:
    if not codegraph:
        add_error(errors, MASTER_REFS / "codegraph.yaml", "missing or invalid codegraph skills")
        return

    method_cards = method_cards_doc.get("method_cards", {})
    if not isinstance(method_cards, dict):
        add_error(errors, MASTER_REFS / "method-cards.yaml", "missing method_cards map")
        method_cards = {}

    for skill_id, node in implemented_graph_skills(codegraph):
        name = str(node.get("name"))
        skill_type = str(node.get("type", ""))
        skill_dir = SKILLS_DIR / name
        skill_file = skill_dir / "SKILL.md"
        contract_file = skill_dir / "references" / "output-contract.md"

        if "post_skill_isolation_record" not in read_text(skill_file):
            add_error(errors, skill_file, "missing post_skill_isolation_record")

        if skill_type == "MASTER":
            continue

        method_key = f"{skill_id}.{name}"
        if method_key not in method_cards:
            add_error(errors, MASTER_REFS / "method-cards.yaml", f"missing method card for {method_key}")

        if not contract_file.exists():
            add_error(errors, contract_file, "missing output contract")
            continue

        contract_text = read_text(contract_file)
        if "post_skill_isolation_record" not in contract_text:
            add_error(errors, contract_file, "missing post_skill_isolation_record")


def fenced_json_blocks(text: str) -> list[str]:
    return re.findall(r"```json\s*(.*?)```", text, flags=re.DOTALL | re.IGNORECASE)


def check_json_fences(errors: list[str]) -> None:
    roots = [SKILLS_DIR, ROOT / "docs", ROOT / ".scratch"]
    for root in roots:
        if not root.exists():
            continue
        for md_file in sorted(root.rglob("*.md")):
            text = read_text(md_file)
            for index, block in enumerate(fenced_json_blocks(text), start=1):
                try:
                    json.loads(block)
                except json.JSONDecodeError as exc:
                    add_error(errors, md_file, f"JSON fence {index} parse failed: {exc}")


def json_fence_by_heading(path: Path, heading: str) -> object | None:
    text = read_text(path)
    start = text.find(heading)
    if start == -1:
        return None
    block_match = re.search(r"```json\s*(.*?)```", text[start:], flags=re.DOTALL | re.IGNORECASE)
    if not block_match:
        return None
    return json.loads(block_match.group(1))


def check_s14_section_registry(codegraph: dict, errors: list[str]) -> None:
    registry_path = SKILLS_DIR / "compose-html-gtm-dashboard" / "references" / "section-registry.md"
    try:
        section_doc = json_fence_by_heading(registry_path, "## Section Mapping")
    except json.JSONDecodeError as exc:
        add_error(errors, registry_path, f"section mapping JSON parse failed: {exc}")
        return

    if not isinstance(section_doc, dict) or not isinstance(section_doc.get("section_map"), list):
        add_error(errors, registry_path, "missing section_map")
        return

    graph_skills = codegraph.get("skills", {}) if isinstance(codegraph, dict) else {}
    valid_source_skills = {
        f"{skill_id}.{node.get('name')}"
        for skill_id, node in graph_skills.items()
        if isinstance(node, dict)
    }

    required_sections = {
        "market_context",
        "jtbd_scenarios",
        "message_architecture",
        "pricing",
        "copy_assets",
        "creator_kol",
        "dtc_conversion",
        "launch_forecast",
        "validation_roadmap",
    }
    seen_sections: set[str] = set()
    seen_inputs: set[str] = set()

    for entry in section_doc["section_map"]:
        if not isinstance(entry, dict):
            add_error(errors, registry_path, "section_map contains non-object entry")
            continue
        section_id = entry.get("section_id")
        source_skill = entry.get("source_skill")
        input_ref = entry.get("input_ref")
        seen_sections.add(str(section_id))
        seen_inputs.add(str(input_ref))
        if source_skill not in valid_source_skills:
            add_error(errors, registry_path, f"unknown source_skill for section {section_id}: {source_skill}")
        if not isinstance(input_ref, str) or not input_ref.startswith("html_"):
            add_error(errors, registry_path, f"section {section_id} input_ref must be an html_* field")

    missing_sections = required_sections - seen_sections
    for section_id in sorted(missing_sections):
        add_error(errors, registry_path, f"missing section mapping for {section_id}")

    if "html_validation_section" not in seen_inputs:
        add_error(errors, registry_path, "missing html_validation_section mapping")


def check_architecture_expansion_contract(errors: list[str]) -> None:
    required_reference_tokens = {
        "recoverable-state-machine.md": [
            "GTM Run State",
            "phase: intake | evidence | skill_run | review | finalize | finalized",
            "resume_pointer",
            "idempotency_key",
            "S14 is not a visible business module",
        ],
        "hardware-current-state-rubric.md": [
            "17-Section Hardware GTM Readiness Rubric",
            "Total = sum of all scored sections",
            "Positioning",
            "Localized consumer voice",
            "Channel readiness",
        ],
        "budget-and-growth-models.md": [
            "Revenue-Based",
            "Goal-Based",
            "blended CAC",
            "S-curve",
            "hardware adaptation",
        ],
        "skill-evals-policy.md": [
            "evals/evals.json",
            "must_include",
            "must_not_include",
            "architecture_contract",
        ],
        "marketing-skills-adaptation-map.md": [
            "product-marketing",
            "customer-research",
            "competitor-profiling",
            "ab-testing",
            "copy-editing",
        ],
        "suite-output-tree.md": [
            "GTM Master Suite Output Tree",
            "Dashboard-Level Output Tree",
            "S00 gtm-master Outputs",
            "hardware_current_state_scorecard",
            "source_accessibility_matrix",
            "four_forces_switching_map",
            "maxdiff_feature_value_tradeoff_test_design",
            "budget_posture_model",
            "aarrr_orb_channel_architecture",
            "S13 plan-validation-experiments Outputs",
            "S14 compose-html-gtm-dashboard Outputs",
        ],
        "run-modes-and-context-budgets.md": [
            "real_product_pilot",
            "competitor_review_gate",
            "deep_voice_collection_scope",
            "S13_visibility",
        ],
    }

    for filename, tokens in required_reference_tokens.items():
        path = MASTER_REFS / filename
        if not path.exists():
            add_error(errors, path, "missing architecture reference")
            continue
        text = read_text(path)
        for token in tokens:
            if token not in text:
                add_error(errors, path, f"missing required architecture token: {token}")

    crosswalk_path = MASTER_REFS / "methodology-crosswalk.yaml"
    crosswalk = load_yaml(crosswalk_path, errors) if crosswalk_path.exists() else None
    if not isinstance(crosswalk, dict):
        add_error(errors, crosswalk_path, "missing or invalid methodology crosswalk")
        return

    frameworks = crosswalk.get("frameworks")
    if not isinstance(frameworks, dict):
        add_error(errors, crosswalk_path, "methodology crosswalk missing frameworks map")
        return

    required_frameworks = {
        "product_marketing_context",
        "aarrr_hardware",
        "jtbd",
        "four_forces",
        "voc",
        "van_westendorp",
        "maxdiff",
        "ice",
        "orb",
        "hardware_current_state_17",
        "budget_formula",
        "growth_s_curve",
        "evidence_snapshot",
        "recoverable_state_machine",
        "copy_sweeps",
    }
    for framework in sorted(required_frameworks - set(frameworks)):
        add_error(errors, crosswalk_path, f"missing framework mapping: {framework}")

    for framework_name, spec in frameworks.items():
        if not isinstance(spec, dict):
            add_error(errors, crosswalk_path, f"framework {framework_name} must be an object")
            continue
        for field in ("primary_skills", "hardware_adaptation", "output_contract_hooks"):
            if field not in spec:
                add_error(errors, crosswalk_path, f"framework {framework_name} missing {field}")


def check_suite_manifest_expansion(errors: list[str]) -> None:
    manifest_path = MASTER_REFS / "suite-manifest.yaml"
    manifest = load_yaml(manifest_path, errors)
    if not isinstance(manifest, dict):
        return

    runtime_model = manifest.get("runtime_model", {})
    if not isinstance(runtime_model, dict):
        add_error(errors, manifest_path, "runtime_model must be an object")
        return

    required_runtime_sources = {
        "state_machine_source": "references/recoverable-state-machine.md",
        "methodology_crosswalk_source": "references/methodology-crosswalk.yaml",
        "skill_evals_policy_source": "references/skill-evals-policy.md",
        "hardware_current_state_rubric_source": "references/hardware-current-state-rubric.md",
        "suite_output_tree_source": "references/suite-output-tree.md",
    }
    for key, expected_value in required_runtime_sources.items():
        if runtime_model.get(key) != expected_value:
            add_error(errors, manifest_path, f"runtime_model.{key} must be {expected_value}")

    available_depth_modes = runtime_model.get("available_depth_modes", [])
    if isinstance(available_depth_modes, list) and "real_product_pilot" not in available_depth_modes:
        add_error(errors, manifest_path, "available_depth_modes missing real_product_pilot")

    principles = manifest.get("global_principles", [])
    if not isinstance(principles, list):
        add_error(errors, manifest_path, "global_principles must be a list")
        return
    for principle in [
        "recoverable_state_machine",
        "methodology_crosswalk",
        "evals_before_architecture_stable",
        "hardware_current_state_scoring",
        "S14_hidden_composer_not_visible_business_module",
    ]:
        if principle not in principles:
            add_error(errors, manifest_path, f"global_principles missing {principle}")


def check_cross_agent_tooling_contract(errors: list[str]) -> None:
    registry_path = TOOLS_DIR / "REGISTRY.md"
    required_registry_tokens = [
        "GTM Master Tool Registry",
        "platform_targets",
        "codex",
        "claude_code",
        "capability_slots",
        "primary_search",
        "site_specific_comment_collection",
        "private_file_upload",
        "Connector implementations are optional",
    ]
    if not registry_path.exists():
        add_error(errors, registry_path, "missing cross-agent tool registry")
    else:
        registry_text = read_text(registry_path)
        for token in required_registry_tokens:
            if token not in registry_text:
                add_error(errors, registry_path, f"missing required tool registry token: {token}")

    integration_requirements = {
        "platform-setup.md": ["Codex", "Claude Code", "MCP", "CLI", "user-side setup"],
        "search-and-serp.md": ["primary_search", "web_search", "serp_search"],
        "web-extraction.md": ["primary_web_extractor", "web_scraping", "structured_extraction"],
        "browser-automation.md": ["browser_automation", "JavaScript", "pagination"],
        "review-comment-mining.md": ["marketplace_reviews", "video_comment_mining", "site_specific_comment_collection"],
        "price-intelligence.md": ["price_intelligence", "local_price_corridor", "promo floor"],
        "translation-local-language.md": ["translation_and_local_language_processing", "local-language queries"],
        "private-file-upload.md": ["private_file_upload", "manual_upload", "private data"],
    }
    for filename, tokens in integration_requirements.items():
        path = TOOLS_DIR / "integrations" / filename
        if not path.exists():
            add_error(errors, path, "missing tool integration guide")
            continue
        text = read_text(path)
        for token in tokens:
            if token not in text:
                add_error(errors, path, f"missing required integration token: {token}")

    tooling_ref = MASTER_REFS / "tooling-and-connectors.md"
    if not tooling_ref.exists():
        add_error(errors, tooling_ref, "missing master tooling reference")
    else:
        text = read_text(tooling_ref)
        for token in ["tools/REGISTRY.md", "capability slot", "MCP", "CLI", "Codex", "Claude Code"]:
            if token not in text:
                add_error(errors, tooling_ref, f"missing required tooling reference token: {token}")

    s00_skill = SKILLS_DIR / "gtm-master" / "SKILL.md"
    if "references/tooling-and-connectors.md" not in read_text(s00_skill):
        add_error(errors, s00_skill, "missing tooling-and-connectors load order reference")

    s01_connectors = SKILLS_DIR / "build-consumer-market-map" / "references" / "mcp-connectors.md"
    s01_text = read_text(s01_connectors)
    for token in ["tools/REGISTRY.md", "capability slot", "platform-neutral"]:
        if token not in s01_text:
            add_error(errors, s01_connectors, f"missing cross-agent connector token: {token}")

    manifest_path = MASTER_REFS / "suite-manifest.yaml"
    manifest = load_yaml(manifest_path, errors)
    if isinstance(manifest, dict):
        runtime_model = manifest.get("runtime_model", {})
        if not isinstance(runtime_model, dict):
            add_error(errors, manifest_path, "runtime_model must be an object")
        else:
            required_sources = {
                "tool_registry_source": "tools/REGISTRY.md",
                "connector_policy_source": "references/tooling-and-connectors.md",
            }
            for key, expected_value in required_sources.items():
                if runtime_model.get(key) != expected_value:
                    add_error(errors, manifest_path, f"runtime_model.{key} must be {expected_value}")

        principles = manifest.get("global_principles", [])
        if isinstance(principles, list) and "platform_neutral_tool_layer" not in principles:
            add_error(errors, manifest_path, "global_principles missing platform_neutral_tool_layer")


def check_skill_evals_contract(codegraph: dict, errors: list[str]) -> None:
    for skill_id, node in implemented_graph_skills(codegraph):
        name = str(node.get("name"))
        evals_path = SKILLS_DIR / name / "evals" / "evals.json"
        if not evals_path.exists():
            add_error(errors, evals_path, f"missing evals for {skill_id}.{name}")
            continue

        try:
            payload = json.loads(read_text(evals_path))
        except json.JSONDecodeError as exc:
            add_error(errors, evals_path, f"evals JSON parse failed: {exc}")
            continue

        evals = payload.get("evals") if isinstance(payload, dict) else None
        if not isinstance(evals, list) or not evals:
            add_error(errors, evals_path, "evals must contain a non-empty evals list")
            continue

        if not any(isinstance(item, dict) and item.get("name") == "architecture_contract" for item in evals):
            add_error(errors, evals_path, "evals must include an architecture_contract scenario")

        for index, item in enumerate(evals, start=1):
            if not isinstance(item, dict):
                add_error(errors, evals_path, f"eval {index} must be an object")
                continue
            for field in ("name", "prompt", "must_include", "must_not_include"):
                if field not in item:
                    add_error(errors, evals_path, f"eval {index} missing {field}")
            if not isinstance(item.get("must_include"), list):
                add_error(errors, evals_path, f"eval {index} must_include must be a list")
            if not isinstance(item.get("must_not_include"), list):
                add_error(errors, evals_path, f"eval {index} must_not_include must be a list")


def check_dashboard_renderer_contract(errors: list[str]) -> None:
    s14_skill = SKILLS_DIR / "compose-html-gtm-dashboard" / "SKILL.md"
    render_arch = SKILLS_DIR / "compose-html-gtm-dashboard" / "references" / "render-architecture.md"
    s14_quality = SKILLS_DIR / "compose-html-gtm-dashboard" / "references" / "quality-gates.md"
    master_quality = MASTER_REFS / "quality-gates.md"

    if not RENDERER_SCRIPT.exists():
        add_error(errors, RENDERER_SCRIPT, "missing dashboard renderer script")
        return

    renderer_text = read_text(RENDERER_SCRIPT)
    renderer_tokens = [
        "DEFAULT_INPUT",
        "DEFAULT_OUTPUT",
        "build_html",
        "render_private_calculator",
        "post_skill_isolation_records",
    ]
    for token in renderer_tokens:
        if token not in renderer_text:
            add_error(errors, RENDERER_SCRIPT, f"renderer missing token {token}")

    doc_paths = [s14_skill, render_arch, s14_quality, master_quality]
    for path in doc_paths:
        text = read_text(path)
        if "render-gtm-dashboard-from-report-state.py" not in text:
            add_error(errors, path, "missing renderer command reference")

    if not GOLDEN_DASHBOARD.exists():
        add_error(errors, GOLDEN_DASHBOARD, "missing generated golden dashboard HTML")
        return

    html_text = read_text(GOLDEN_DASHBOARD)
    required_html_tokens = [
        "GTM Master GTM 报告",
        "激活、退货与上手风险",
        "交付范围说明",
        "数据缺口",
        "引用与证据索引",
        "来源与生成审计",
        "私密定价计算器",
    ]
    for token in required_html_tokens:
        if token not in html_text:
            add_error(errors, GOLDEN_DASHBOARD, f"dashboard missing required text: {token}")

    forbidden_html_tokens = [
        "https://",
        "http://",
        "<script src=",
        "<link rel=\"stylesheet\"",
        "fetch(",
        "navigator.sendBeacon",
    ]
    for token in forbidden_html_tokens:
        if token in html_text:
            add_error(errors, GOLDEN_DASHBOARD, f"dashboard contains forbidden offline token: {token}")

    check_dashboard_language_gate(html_text, errors)


def check_dashboard_language_gate(html_text: str, errors: list[str]) -> None:
    parser = VisibleTextParser()
    parser.feed(html_text)

    allowed_without_chinese = re.compile(
        r"^(?:"
        r"C-DRY-\d+|"
        r"DG-\d+|"
        r"dryrun://\S+|"
        r"https?://\S+|"
        r"[A-Z]\d{2}|"
        r"GTM|JTBD|HTML|NSS|NPS|WTP|COGS|BOM|MKT|DTC|KOL|RMA|PDP|URL|ID|"
        r"[0-9 .:/_+\-]+"
        r")$",
        re.IGNORECASE,
    )
    allowed_mixed_terms = re.compile(
        r"\b(?:GTM|JTBD|HTML|NSS|NPS|WTP|COGS|BOM|MKT|DTC|KOL|RMA|PDP|URL|ID|S\d{2})\b|dryrun://\S+|C-DRY-\d+|DG-\d+"
    )
    forbidden_visible_english = [
        "Golden Dry-run",
        "Generic Hardware Fixture",
        "Example target country",
        "Example local currency price band",
        "Post-skill",
        "Local Tool",
        "Input",
        "status panel",
        "matrix heatmap",
        "ranked bar",
        "range chart",
        "optional and should",
        "Omitted unless",
        "Omitted because",
        "No real ",
        "Run S01 with live",
        "Validation roadmap is generated",
    ]

    unexpected_without_chinese: list[str] = []
    forbidden_hits: list[str] = []
    for text in parser.parts:
        if not re.search(r"[A-Za-z]{3,}", text):
            continue
        if any(token in text for token in forbidden_visible_english):
            forbidden_hits.append(text)
            continue
        if not re.search(r"[\u4e00-\u9fff]", text) and not allowed_without_chinese.fullmatch(text):
            unexpected_without_chinese.append(text)
            continue
        mixed_without_allowed_terms = allowed_mixed_terms.sub("", text)
        if re.search(r"[A-Za-z]{3,}", mixed_without_allowed_terms) and not re.search(r"[\u4e00-\u9fff]", mixed_without_allowed_terms):
            unexpected_without_chinese.append(text)

    for text in forbidden_hits[:10]:
        add_error(errors, GOLDEN_DASHBOARD, f"dashboard language gate found untranslated visible text: {text}")
    for text in unexpected_without_chinese[:10]:
        add_error(errors, GOLDEN_DASHBOARD, f"dashboard language gate found unexpected non-Chinese visible text: {text}")


def check_forbidden_residue(errors: list[str]) -> None:
    scan_roots = [SKILLS_DIR, ROOT / "docs", ROOT / ".scratch", ROOT / "artifacts" / "dry-runs"]
    forbidden = [
        re.compile(r"\bTODO\b"),
        re.compile(r"\bTBD\b"),
        re.compile(r"Huawei", re.IGNORECASE),
        re.compile(r"smart ring", re.IGNORECASE),
        re.compile(r"华为"),
        re.compile(r"戒指"),
        re.compile(r"鈮"),
        re.compile(r"\ufffd"),
    ]
    suffixes = {".md", ".json", ".yaml", ".yml"}

    for root in scan_roots:
        if not root.exists():
            continue
        for path in sorted(root.rglob("*")):
            if not path.is_file() or path.suffix.lower() not in suffixes:
                continue
            text = read_text(path)
            for pattern in forbidden:
                match = pattern.search(text)
                if match:
                    add_error(errors, path, f"forbidden residue found: {match.group(0)!r}")
                    break


def main() -> int:
    errors: list[str] = []

    check_skill_frontmatter(errors)
    codegraph, method_cards_doc = check_master_yaml(errors)
    check_architecture_expansion_contract(errors)
    check_suite_manifest_expansion(errors)
    check_cross_agent_tooling_contract(errors)
    check_skill_evals_contract(codegraph, errors)
    check_method_cards_and_output_contracts(codegraph, method_cards_doc, errors)
    check_json_fences(errors)
    check_s14_section_registry(codegraph, errors)
    check_dashboard_renderer_contract(errors)
    check_forbidden_residue(errors)

    if errors:
        print("GTM suite contract validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("GTM suite contracts OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
