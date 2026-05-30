# GTM Suite Stabilization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn the current GTM skill suite from a documented architecture into a repeatably verifiable, context-safe, Chinese HTML report workflow.

**Architecture:** Keep S00 as the orchestrator, S01-S08/S13 as analysis modules, and S14 as the only renderer. Every module must emit `compressed_handoff_pack`, `html_section_draft`, ledger updates, and `post_skill_isolation_record`; downstream modules must not reopen upstream full artifacts without a recorded escalation.

**Tech Stack:** Codex skills as Markdown contracts, YAML graph/method cards, JSON-like output envelopes, static HTML dashboard assets, PowerShell/Python validation commands.

---

## File Map

- `skills/gtm-master/SKILL.md`: suite operating rules, run protocol, handoff-only runtime, isolation rule.
- `skills/gtm-master/references/suite-implementation-roadmap.md`: public build status and default next sequence.
- `skills/gtm-master/references/codegraph.yaml`: machine-readable skill graph, context/search policies, runtime rules.
- `skills/gtm-master/references/method-cards.yaml`: method cards for implemented skills.
- `skills/gtm-master/references/quality-gates.md`: global gates, handoff gate, HTML gate, isolation gate.
- `skills/gtm-master/references/post-skill-isolation-policy.md`: canonical isolation policy.
- `skills/compose-html-gtm-dashboard/references/*`: S14 rendering, section registry, visual system, quality gates.
- `skills/compose-html-gtm-dashboard/assets/dashboard-shell.html`: default dashboard shell.
- `skills/compose-html-gtm-dashboard/assets/dashboard-shell-mat.html`: Mat-style dashboard shell.
- `artifacts/dry-runs/*`: dry-run report states and validation summaries.
- `docs/superpowers/plans/2026-05-25-gtm-suite-stabilization.md`: this execution plan.

---

### Task 1: Golden Dry-Run For S00-S08-S13-S14

**Purpose:** Prove the current implemented chain can produce a complete isolated report state without live web search or product-specific contamination.

**Files:**
- Create: `artifacts/dry-runs/generic-hardware-s00-s08-s13-s14-report-state.json`
- Create: `artifacts/dry-runs/generic-hardware-s00-s08-s13-s14-validation-summary.md`
- Modify if needed: `skills/gtm-master/references/quality-gates.md`
- Modify if needed: `skills/gtm-master/references/report-data-contract.md`

- [ ] **Step 1: Build the fixture scope**

Use this fixture:

```json
{
  "product_features_and_specs": "Generic 2C hardware product with three concrete feature bullets, one measurable specification, one setup constraint, and one privacy or safety caveat.",
  "launch_country_or_region": "Example target country",
  "target_price_range": "Example local currency price band",
  "report_depth": "standard",
  "output_language": "zh-CN",
  "web_policy": "no_live_web_for_dry_run"
}
```

Expected included sections:

```text
market_context
jtbd_scenarios
message_architecture
pricing
launch_forecast
validation_roadmap
data_gap_panel
citation_index
```

Expected skipped sections:

```text
copy_assets
creator_kol
dtc_conversion
activation_return_risk
insight_guardrails
subscription_churn
review_quality_feedback
```

- [ ] **Step 2: Create the report-state artifact**

Create `artifacts/dry-runs/generic-hardware-s00-s08-s13-s14-report-state.json` with:

```json
{
  "report_id": "dryrun-generic-hardware-s00-s08-s13-s14",
  "project_brief": {},
  "sections": [],
  "html_section_drafts": [],
  "evidence_ledger_refs": [],
  "citation_index": [],
  "data_gap_log": [],
  "decision_log": [],
  "post_skill_isolation_records": [],
  "quality_gate_summary": {}
}
```

Each included section must have at least:

```json
{
  "section_id": "",
  "source_skill": "",
  "status": "rendered_with_gaps",
  "executive_takeaway": "",
  "visual_blocks": [],
  "tables": [],
  "confidence_badges": [],
  "data_gaps": []
}
```

- [ ] **Step 3: Add isolation records to the dry-run**

Every rendered or skipped implemented skill must have:

```json
{
  "skill_id": "",
  "status": "isolated_with_gaps",
  "full_artifact_ref": "",
  "compressed_handoff_ref": "",
  "html_section_ref": "",
  "allowed_downstream_refs": [],
  "withheld_context": [],
  "reopen_conditions": [],
  "quality_gate_status": "pass_with_caveats"
}
```

- [ ] **Step 4: Create the validation summary**

Create `artifacts/dry-runs/generic-hardware-s00-s08-s13-s14-validation-summary.md` with:

```text
Rendered sections
Skipped sections
Future sections omitted
Visual block count
Isolation record count
Validation warnings
Validation failures
Next fixes
```

- [ ] **Step 5: Verify dry-run structure**

Run:

```powershell
@'
import json
from pathlib import Path
p = Path(r"artifacts/dry-runs/generic-hardware-s00-s08-s13-s14-report-state.json")
data = json.loads(p.read_text(encoding="utf-8"))
required = ["project_brief", "sections", "html_section_drafts", "data_gap_log", "decision_log", "post_skill_isolation_records"]
missing = [k for k in required if k not in data]
assert not missing, missing
assert any(s.get("section_id") == "validation_roadmap" for s in data["sections"])
assert data["post_skill_isolation_records"]
print("dry-run structure OK")
'@ | python -
```

Expected: `dry-run structure OK`

---

### Task 2: S14 Validation Roadmap Rendering Contract

**Purpose:** Make the final dashboard visibly explain validation priorities, context budget, and data gaps in Chinese.

**Files:**
- Modify: `skills/compose-html-gtm-dashboard/references/section-registry.md`
- Modify: `skills/compose-html-gtm-dashboard/references/render-architecture.md`
- Modify: `skills/compose-html-gtm-dashboard/references/quality-gates.md`
- Modify if needed: `skills/compose-html-gtm-dashboard/assets/dashboard-shell.html`
- Modify if needed: `skills/compose-html-gtm-dashboard/assets/dashboard-shell-mat.html`

- [ ] **Step 1: Confirm section registry includes `validation_roadmap`**

Run:

```powershell
rg -n "validation_roadmap|html_validation_section|S13.plan-validation-experiments" skills\compose-html-gtm-dashboard\references\section-registry.md
```

Expected: all three tokens appear.

- [ ] **Step 2: Define visible S13 views**

Ensure S14 expects these visual blocks:

```text
Validation Input Coverage Gate -> status_panel
Experiment Priority Scorecard -> ranked_bar
Assumption Risk vs Test Feasibility -> matrix_heatmap
Timeline And Decision Unlock Map -> matrix_heatmap
Validation Decision Gate -> status_panel
Experiment Portfolio By Module -> ranked_bar
```

- [ ] **Step 3: Add context audit display requirement**

S14 must render these as audit tables when present:

```text
targeted_lookup_log
context_budget_report
post_skill_isolation_record
excluded_or_deferred_tests_log
```

- [ ] **Step 4: Verify no invented validation content**

Run:

```powershell
rg -n "invent|validation_roadmap|context_budget|targeted_lookup|post_skill_isolation" skills\compose-html-gtm-dashboard
```

Expected: quality rules say S14 renders supplied S13 data only.

---

### Task 3: Suite Contract Validator

**Purpose:** Add one deterministic validation command so future changes do not silently break handoff, isolation, or render contracts.

**Files:**
- Create: `scripts/validate-gtm-suite-contracts.py`
- Modify if needed: `skills/gtm-master/references/quality-gates.md`

- [ ] **Step 1: Create validator script**

The script should check:

```text
all skill folders pass quick_validate-compatible frontmatter basics
S00 YAML files parse
implemented skills have method cards
implemented skills have output-contract.md
implemented skills mention post_skill_isolation_record
S14 registry maps available html_section fields
all json fenced blocks parse
no forbidden example residue appears
```

- [ ] **Step 2: Run validator**

Run:

```powershell
python scripts\validate-gtm-suite-contracts.py
```

Expected:

```text
GTM suite contracts OK
```

- [ ] **Step 3: Document validator in quality gates**

Add the command to `skills/gtm-master/references/quality-gates.md` under a "Suite Contract Validation" section.

---

### Task 4: Run Modes And Context Budgets

**Purpose:** Make quick/standard/deep behavior explicit across the suite, so long reports do not exceed context.

**Files:**
- Create: `skills/gtm-master/references/run-modes-and-context-budgets.md`
- Modify: `skills/gtm-master/SKILL.md`
- Modify: `skills/gtm-master/references/codegraph.yaml`
- Modify: `skills/gtm-master/references/quality-gates.md`

- [ ] **Step 1: Define run modes**

Use:

```text
quick
  S01 -> S02 -> S03 -> S04 -> S08 -> S13 -> S14, minimal visuals, no optional branches unless triggered.

standard
  Core chain plus optional S05/S06/S07 when user inputs or decision relevance trigger them.

deep
  Core chain plus triggered optional modules, richer evidence, appendices, and S13 validation audit.
```

- [ ] **Step 2: Define context budgets**

Use:

```text
per_skill_main_handoff_fields: 20-40 canonical fields
main_visual_blocks_per_section: 4-8
default_full_artifact_opening: forbidden without escalation
S13_external_lookup_budget: 0 by default, 1-8 targeted lookups when justified
S14_upstream_full_artifact_budget: 0 by default
```

- [ ] **Step 3: Add gate**

Quality gate should fail when a skill exceeds budget without:

```text
context_escalation
targeted_lookup_log
context_budget_report
post_skill_isolation_record
```

---

### Task 5: S09-S12 Trigger Matrix Before Building

**Purpose:** Prevent premature expansion. S09-S12 should only run when product category or user materials justify them.

**Files:**
- Create: `skills/gtm-master/references/s09-s12-trigger-matrix.md`
- Modify: `skills/gtm-master/references/suite-implementation-roadmap.md`
- Modify: `skills/gtm-master/references/codegraph.yaml`

- [ ] **Step 1: Define trigger matrix**

Use:

```text
S09 activation/return risk
  Trigger: setup, onboarding, app pairing, sizing, installation, expectation mismatch, return risk.

S10 insight/claim guardrails
  Trigger: health, wellness, AI insight, safety, children, elderly, regulated-adjacent claims.

S11 subscription/churn
  Trigger: subscription, paid app, recurring service, consumable, warranty/service plan, retention loop.

S12 review quality feedback
  Trigger: post-launch reviews, support tickets, returns, NSS/NPS, RMA, app store reviews.
```

- [ ] **Step 2: Add skip policy**

Every S09-S12 future node should have:

```text
skip_when_not_triggered
skip_when_missing_required_private_or_post_launch_materials
```

- [ ] **Step 3: Verify S14 omission policy**

S14 should omit S09-S12 body sections unless triggered or user requested.

---

### Task 6: Matt-Style Local Work Queue

**Purpose:** Let future work proceed without the user asking one step at a time, while avoiding GitHub setup friction in this non-git workspace.

**Files:**
- Create: `.scratch/gtm-suite-stabilization/001-golden-dry-run.md`
- Create: `.scratch/gtm-suite-stabilization/002-s14-validation-rendering.md`
- Create: `.scratch/gtm-suite-stabilization/003-suite-contract-validator.md`
- Create: `.scratch/gtm-suite-stabilization/004-run-modes-context-budgets.md`
- Create: `.scratch/gtm-suite-stabilization/005-s09-s12-trigger-matrix.md`

- [ ] **Step 1: Create local markdown issue directory**

Run:

```powershell
New-Item -ItemType Directory -Force -Path ".scratch\gtm-suite-stabilization" | Out-Null
```

- [ ] **Step 2: Publish one issue per vertical slice**

Each local issue should include:

```text
What to build
Acceptance criteria
Blocked by
Verification command
```

- [ ] **Step 3: Keep dependencies clear**

Use:

```text
001 Golden dry-run -> no blocker
002 S14 validation rendering -> blocked by 001
003 Suite contract validator -> no blocker
004 Run modes/context budgets -> blocked by 001 and 003
005 S09-S12 trigger matrix -> blocked by 004
```

---

## Default Execution Order

```text
1. Task 1 Golden Dry-Run
2. Task 3 Suite Contract Validator
3. Task 2 S14 Validation Roadmap Rendering Contract
4. Task 4 Run Modes And Context Budgets
5. Task 5 S09-S12 Trigger Matrix
6. Task 6 Matt-Style Local Work Queue
```

Reasoning: prove the current chain first, then automate contract checks, then improve rendering, then expand runtime controls, then decide whether post-purchase modules deserve build effort.

## Self-Review

- Spec coverage: covers dry-run, S13/S14 integration, contract validation, context budgets, conditional future modules, and Matt-style local work queue.
- Placeholder scan: no placeholder markers are used.
- Type consistency: all plan fields match current suite terms: `compressed_handoff_pack`, `html_section_draft`, `post_skill_isolation_record`, `context_budget_report`, `targeted_lookup_log`.
