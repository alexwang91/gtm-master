# Quality Gates

Run these gates before advancing to another sub-skill or claiming a report section is ready.

## Global Gate

```yaml
checks:
  one_active_skill:
    pass_if: Only one active sub-skill is being executed or edited.
  required_inputs_present:
    pass_if: Project brief has product specs, country/region, and target price range.
  method_declared:
    pass_if: The active method card and analysis procedure are named.
  schema_declared:
    pass_if: The expected output contract is known before content is generated.
  evidence_labeled:
    pass_if: Material conclusions have evidence level, confidence, and evidence refs.
  handoff_present:
    pass_if: A compressed handoff pack exists for downstream skills.
  post_skill_isolation_ready:
    pass_if: The active skill has full_artifact_ref, compressed_handoff_pack, html_section_draft or skipped status, evidence/decision/data-gap updates, and post_skill_isolation_record before S00 advances.
  html_section_present:
    pass_if: The skill contributes a report section draft or explains why not applicable/skipped.
  visual_block_compatibility:
    pass_if: S01-S08/S13 html_section_draft.visual_blocks use only canonical S14 types from visual-block-acceptance-matrix.md, or missing/unsupported views are recorded as data gaps.
  dashboard_language_gate:
    pass_if: Dashboard-facing titles, labels, takeaways, table values, skipped-section notes, data-gap explanations, and audit text are Simplified Chinese by default; only stable IDs, source refs, URLs, common GTM acronyms, product or brand names, and original evidence phrases may remain non-Chinese.
  data_gaps_recorded:
    pass_if: Missing, stale, or unavailable evidence is recorded.
  context_budget_controlled:
    pass_if: The selected quick/standard/deep mode is recorded; S13 uses handoff-only context by default; S14 has upstream full artifact budget 0 by default; any full artifact, local file, RAG retrieval, web, or MCP lookup has a recorded context escalation or targeted_lookup_log plus context_budget_report.
  platform_neutral_tool_layer:
    pass_if: Evidence collection requests a capability slot from tools/REGISTRY.md before naming a concrete MCP server, CLI, browser tool, API, or manual-upload path; missing connectors become data gaps or fallback instructions.
  recoverable_state_machine_ready:
    pass_if: The run has a persisted phase, current_skill, resume_pointer, selected_run_mode, skill_status, state_artifacts, and idempotency_key before any long evidence collection, review wait, or final render.
  methodology_crosswalk_declared:
    pass_if: Any named framework such as AARRR, JTBD, Four Forces, VOC, Van Westendorp, MaxDiff, ICE, ORB, budget formula, growth S-curve, or copy sweeps is mapped through methodology-crosswalk.yaml to the active skill and output hooks.
  evals_contract_present:
    pass_if: Every implemented skill has evals/evals.json with at least one pressure scenario covering scope boundaries and forbidden outputs.
  hidden_composer_contract:
    pass_if: S14 renders the dashboard from report_state and html_section_drafts without appearing as a visible strategic business module.
  no_forbidden_scope:
    pass_if: The active skill did not perform work assigned to downstream skills.
  no_unsupported_claims:
    pass_if: Risky claims are marked as assumptions, needs validation, or avoid/risk.
```

## Pass States

```text
pass
  All required checks pass.

pass_with_caveats
  Output is usable, but data gaps or low-confidence areas are explicit.

fail
  Required input, evidence, handoff, schema, or compliance condition is missing.
```

## Minimal Verification Fixture

Use this fixture to sanity-check S00/S01 behavior after architecture changes.

```json
{
  "product_features_and_specs": "Generic 2C hardware product with three concrete feature bullets, one measurable specification, and one setup or usage constraint.",
  "launch_country_or_region": "Example target country",
  "target_price_range": "Example local currency price band",
  "report_depth": "quick"
}
```

Expected minimal outputs:

```text
S00 Project Brief
S01 Product-Market Search Preflight
S01 Evidence Research Design in quick mode
S01 Handoff Pack with required fields present or explicit gaps
S01 HTML section draft skeleton
Quality gate result: pass_with_caveats or pass
```

Fail the fixture if the system:

- asks for non-critical inputs before starting
- opens unrelated downstream methods
- treats trend signals as market size
- produces conclusions without evidence labels or data gaps
- cannot produce a compressed handoff pack

## Suite Contract Validation

Run this after any suite, skill, graph, contract, or renderer documentation change:

```powershell
python scripts\validate-gtm-suite-contracts.py
```

The validator must pass before claiming the suite contract is stable. It checks:

- skill frontmatter basics
- S00 YAML parsing
- implemented skill method-card coverage
- implemented skill `output-contract.md` coverage
- `post_skill_isolation_record` coverage
- S14 section registry mapping to `html_*` inputs
- S14 dry-run dashboard renderer contract
- S14 Chinese dashboard language gate
- JSON fenced-block parsing
- forbidden example residue

For S14 dashboard rendering smoke tests, run:

```powershell
python scripts\render-gtm-dashboard-from-report-state.py
```

The generated HTML must remain single-file, offline-first, Chinese by default, pass the dashboard language gate, and show module coverage, S13 validation roadmap, data gaps, citation index, post-skill isolation audit, and the local-only private pricing calculator.

## Handoff Gate

The compressed handoff pack must include:

- `handoff_id`
- `from_skill`
- `to_skills`
- `summary`
- `canonical_fields`
- `key_findings`
- `required_downstream_use`
- `data_gaps`
- `full_artifact_ref`

Fail the gate if downstream skills would need to read the full artifact for normal operation.

## Post-Skill Isolation Gate

Before S00 advances, the active skill must have:

- `full_artifact_ref` or an explicit blocked/skipped reason
- `compressed_handoff_pack`
- `html_section_draft` or visible skipped/not-triggered section state
- `evidence_updates`, `decision_updates`, and `data_gaps` merged or explicitly empty
- `post_skill_isolation_record`
- `reopen_conditions` for any withheld context that may be needed later

Fail the gate if:

- downstream normal operation requires reopening the full artifact
- raw private data leaks into handoff or HTML
- data gaps are hidden instead of recorded
- the next skill receives broad prior working context rather than its allowed runtime input

## Run Mode And Context Budget Gate

Before S00 advances to the next skill, confirm:

- selected run mode is `quick`, `standard`, `real_product_pilot`, or `deep`
- the graph breadth matches `references/run-modes-and-context-budgets.md`
- each skill handoff keeps roughly 20-40 canonical fields unless a context escalation explains why more is needed
- main report sections stay within the selected visual-block budget or record `rendered_too_thin`, `missing_required_view`, or `context_budget_report`
- S13 external lookup budget is 0 by default and 1-8 targeted lookups only when justified
- S14 upstream full artifact budget is 0 by default
- recoverable run state has a valid resume pointer before pausing, switching skills, or rendering

Fail the gate when a skill exceeds budget without:

- `context_escalation`
- `targeted_lookup_log` when lookup occurred
- `context_budget_report`
- `post_skill_isolation_record`

## Tooling And Connector Gate

Before any web, MCP, CLI, browser, API, or private-upload collection, confirm:

- the evidence need maps to a `tools/REGISTRY.md` capability slot
- the selected concrete connector is available in the current runtime, or a fallback is declared
- the operation is least-invasive for the research question
- credentials, OAuth, API keys, and private files are outside skill files and public HTML
- collection output will produce evidence records and a collection log

Fail the gate when a skill hard-codes a provider without a slot, asks the user to
understand MCP internals, or hides a missing connector instead of recording a
data gap.

## Recoverable State Gate

Before a long run pauses, resumes, advances, or finalizes, confirm:

- `phase` is one of `intake`, `evidence`, `skill_run`, `review`, `finalize`, or `finalized`
- `current_skill` and `resume_pointer` agree with the next graph step
- each completed skill has `full_artifact_ref`, `compressed_handoff_ref`, `html_section_ref`, and `post_skill_isolation_record`
- rerunning the same evidence or render step uses an `idempotency_key`
- finalized versions are never overwritten without a decision log entry

Fail the gate when the next step would require broad upstream context instead of the stored handoff and report state.

## Methodology Crosswalk Gate

Before using an imported method, confirm it appears in `references/methodology-crosswalk.yaml` and that the active skill emits one of that method's output hooks. If the method is useful but not mapped, update the crosswalk and add an eval before relying on it.

## Evals Gate

Run this after any suite, skill, graph, contract, method, or renderer change:

```powershell
python scripts\validate-gtm-suite-contracts.py
```

The validator checks that every implemented graph node has `evals/evals.json`, that the master architecture references exist, and that the methodology crosswalk contains the required frameworks.

## Competitor Gate

For S01, competitor outputs must include:

- A candidate review list of 5-10 potential competitors/substitutes in standard/deep mode, unless the source coverage is too thin.
- A `competitor_candidate_review_gate` before deep TOP1/previous-generation voice mining in real_product_pilot mode.
- Competitor role labels such as direct, substitute, premium anchor, budget anchor, previous generation, or ecosystem anchor.
- Competitor Threat Score formula or score breakdown.
- At least two local evidence signals for each top competitor, or an explicit hypothesis label.
- User include/exclude/unsure notes when Gate 2 review is used.

## Evidence Gate

Fail or caveat the output when:

- Evidence is not from the target country or a clearly comparable market.
- Pricing, competitor, channel, or creator evidence is stale.
- NPS proxy is presented as surveyed NPS.
- TAM/SAM/SOM is shown as precise without an assumption tree.
- Consumer quotes lack source provenance or usage permission.
- Creator budget or expected outcome estimates are presented without basis, confidence, and scenario range.
- Creator visits, likes, sales, or conversion lift are presented as guaranteed.
- Candidate creator recommendations are treated as final while `creator_candidate_review_gate` is pending.
- Web collection violated or may violate source policy.
- Source accessibility is missing for a local forum, retailer, marketplace, or video/comment source used as material evidence.
- S13 used broad search, broad local/RAG ingestion, or full upstream artifacts without a targeted validation question and context budget report.

## HTML Gate

The section draft must include:

- Section title
- Narrative summary
- S01-S08/S13 required `visual_blocks` in standard/deep mode for sections that ran, or explicit `skipped`, `rendered_too_thin`, or `missing_required_view` gaps
- Only canonical `visual_blocks.type` values: `status_panel`, `ranked_bar`, `matrix_heatmap`, `range_chart`
- At least one structured table, card, or chart data object when useful
- Confidence badges for major conclusions
- Citation refs
- Data gap notes

Final HTML composition must not change upstream conclusions without a decision record.
