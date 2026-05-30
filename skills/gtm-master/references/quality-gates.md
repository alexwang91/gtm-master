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

- selected run mode is `quick`, `standard`, or `deep`
- the graph breadth matches `references/run-modes-and-context-budgets.md`
- each skill handoff keeps roughly 20-40 canonical fields unless a context escalation explains why more is needed
- main report sections stay within the selected visual-block budget or record `rendered_too_thin`, `missing_required_view`, or `context_budget_report`
- S13 external lookup budget is 0 by default and 1-8 targeted lookups only when justified
- S14 upstream full artifact budget is 0 by default

Fail the gate when a skill exceeds budget without:

- `context_escalation`
- `targeted_lookup_log` when lookup occurred
- `context_budget_report`
- `post_skill_isolation_record`

## Competitor Gate

For S01, competitor outputs must include:

- A candidate review list of 5-10 potential competitors/substitutes in standard/deep mode, unless the source coverage is too thin.
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
