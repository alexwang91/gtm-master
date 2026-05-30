# Render Architecture

S14 is a deterministic composition layer. It turns structured section drafts into a static HTML dashboard.

## Core Principle

Render what upstream skills produced. Do not create new analysis to make the page look complete.

## Section Draft Schema

Each upstream section should look like:

```json
{
  "section_id": "",
  "source_skill": "",
  "section_title": "",
  "executive_takeaway": "",
  "narrative_blocks": [],
  "metric_cards": [],
  "tables": [],
  "visual_blocks": [],
  "charts": [],
  "callouts": [],
  "confidence_badges": [],
  "citations": [],
  "data_gaps": [],
  "next_actions": []
}
```

S14 may normalize names but must preserve original source refs.

## Render Pipeline

```text
input_gate
  Check required groups, available sections, private data policy, citation availability, and data gaps.

normalize
  Convert section drafts into registry entries with stable IDs, titles, source skill, confidence, citations, and display blocks.

render_input_boundary
  Render a compact top-of-report input boundary strip before or inside the executive summary. It should show only the inputs that constrain interpretation: product/category, key selling points or specs, launch country, price band, run mode, channel/MKT/private-data availability, evidence coverage, and critical missing inputs. Keep it small enough that it does not compete with the management summary.

compose_summary
  Build a management decision summary from upstream executive_takeaway, decision_updates, S08 forecast outputs, S04 pricing outputs, S01/S03 competitor and product-fit outputs, channel readiness signals, marketing assumptions, and highest-severity data gaps only.

render_navigation
  Generate sticky navigation from rendered section IDs. Include status badges for missing or low-confidence sections.

render_sections
  Render text, metric cards, visual blocks, tables, simple charts, callouts, next actions, citations, and data gaps.

render_validation_roadmap
  When `validation_roadmap` is present, render supplied S13 data only: validation input coverage, experiment priority, assumption risk versus test feasibility, timeline and decision unlocks, validation decision gate, and experiment portfolio by module. Render `targeted_lookup_log`, `context_budget_report`, `post_skill_isolation_record`, and `excluded_or_deferred_tests_log` as audit tables when present.

render_private_tools
  Render local calculators only from approved specs, with blank inputs and no storage by default.

render_appendices
  Include citation index, data gaps, decision log, artifact index, and methodology notes only when triggered.

quality_gate
  Run coverage, privacy, citation, layout, accessibility, and offline checks.
```

## Executive Summary Rules

## Input Boundary Rules

The input boundary is a compact trust/context strip at the top of the report. It should answer:

```text
What product, country, price band, and run mode is this report analyzing?
Which product claims/specs were supplied by the user?
Which commercial inputs were supplied or missing: MKT budget, channels, previous generation, benchmark competitors, brand positioning?
Which evidence sources were actually collected: web, local ecommerce, local search terms, reviews, forums, video comments, private NSS/NPS?
Which private inputs were intentionally excluded from the public HTML: COGS, margin, channel terms, internal sales, raw private materials?
Which 3-5 missing inputs most limit the executive summary?
```

Display rules:

- Place the input boundary at the very top, before the main management summary or as a slim strip inside the summary band.
- Keep it visually compact: 4-6 small cards, chips, or a single dense table row.
- Use status labels such as `已提供`, `未提供`, `系统推断`, `仅样例`, `私密未嵌入`, or `需要补充`.
- Do not render the full product-spec list when it is long; show grouped chips and move detail to an appendix or expandable table.
- Do not expose raw private values.

## Executive Summary Rules

The executive summary is a management decision surface, not a workflow recap. It should answer:

```text
How much can this product sell per week?
Why, based on market space, brand strength, price competitiveness, and product competitiveness?
What simple marketing spend and budget posture is recommended?
Which channels should be prioritized, and what is each channel capable of contributing?
Which competitors matter most, where are they stronger/weaker, and how should the launch respond?
What evidence gaps could materially change the answer?
```

Required views:

```text
expected_weekly_sales_range
  Use S08 scenario forecast normalized to a weekly range. If S08 has 30/60/90-day ranges, show week-1/early-launch weekly expectation or a derived weekly range with an assumption badge. Never present it as actual demand when market size, channel, or conversion evidence is missing.

sales_driver_decomposition
  Decompose the expected weekly range into market-space, brand strength, price competitiveness, and product competitiveness. Use scorecards or compact bars, not long prose. Missing brand or market data must show as hypothesis or data gap.

marketing_budget_recommendation
  Show a simple MKT budget posture: minimum viable test spend, base launch spend, and stretch/upside spend when the data supports it. Tie each budget posture to expected visits, consideration, or conversion signal when available. If spend is user-provided, show it as input; if inferred, label it as assumption.

channel_priority_and_capacity
  Rank launch channels by priority and ability: reach, conversion readiness, commercial access, proof fit, margin/price constraints, and validation need. Use S01 `local_channel_priority`, S01 channel map, S08 channel readiness, S04 channel constraints, and S07 only when triggered. The visible management summary should show concrete local channel names, not only generic categories such as local ecommerce, retail, or DTC. If names are unverified or user-planned, keep the name but label the evidence status.

competitor_response_summary
  Summarize the top competitors/substitutes with advantage, weakness, decision threat, price pressure, proof gap, and recommended response. Use S01 local search term map, competitor candidate scoring, user calibration status, competitor threat, S03 objection/proof maps, and S04 price corridor.

confidence_and_next_validation
  Show the top 3 data gaps or S13 tests that could change the weekly sales, channel, budget, or competitor-response recommendation.
```

Use only these inputs:

```text
section.executive_takeaway
decision_updates
S01 competitor, channel, product-fit, and local-market outputs
S03 feature-benefit-proof and objection outputs
S04 price corridor, WTP, and price-risk outputs
S08 forecast, marketing response, channel readiness, and sensitivity outputs
S13 validation roadmap and decision gates
pricing_decision_gate.status
data_gap_log.high_severity_items
confidence_badge_map
```

Do not:

- Combine weak signals into a stronger claim.
- Convert hypotheses into recommendations.
- Hide high-severity blockers.
- Write final pricing, demand, compliance, or financial approval language.
- Show skill-chain process notes in the main executive summary.
- Present expected weekly sales as a precise number without range, confidence label, and evidence/source note.

## Component Types

```text
metric_cards
  Use for 1-6 compact metrics with confidence and source refs.

tables
  Use for comparisons, matrices, evidence summaries, options, and risks.

charts
  Use only when the data is numeric, complete, and labeled. If not, render a table.

visual_blocks
  Preferred structured visuals for S01-S08: status_panel, ranked_bar, matrix_heatmap, and range_chart. These must remain data-backed and labeled.
  If upstream sends a method-level alias, map it only when the data shape is compatible. Otherwise render a table and add `missing_visual_block`.
  For S13 validation_roadmap, the main body should show Validation Input Coverage Gate, Experiment Priority Scorecard, Assumption Risk vs Test Feasibility, Timeline And Decision Unlock Map, Validation Decision Gate, and Experiment Portfolio By Module when provided.

callouts
  Use for blockers, key decisions, caveats, privacy notices, and next actions.

confidence_badges
  Use high, medium, low, hypothesis_only, blocked, or unknown.
```

## Section Completeness Rules

For S01-S04, read `s01-s04-display-contract.md` before rendering. For S05-S08, use their section-specific HTML contracts. A section is complete only when it has:

```text
executive_takeaway
confidence_or_coverage_signal
primary_visual_proof_block
risk_or_data_gap_block
downstream_implication_or_next_action
```

If a section draft is too thin:

```text
1. Render only the factual content provided.
2. Add `rendered_too_thin` to render_quality_report.
3. Add missing required subviews to data_gap_panel.
4. Recommend upstream section enrichment instead of inventing charts or claims.
```

## Text Versus Visual Rules

```text
Use text
  For interpretation, caveats, executive takeaways, and why the evidence matters.

Use a table
  When rows have heterogeneous facts, actions, owners, proof, confidence, or evidence refs.

Use a chart
  Only when numeric values are comparable, labeled, and complete enough to avoid false precision.

Use cards
  For a small set of lead scenarios, personas, or options where each item needs a compact narrative.

Use appendices
  For auditability, not persuasion: source maps, raw refs, candidate pools, collection logs, assumption traces.
```

## S13 Validation Rendering Rules

For `validation_roadmap`, S14 must:

- render dashboard-facing text in Simplified Chinese unless the user requested another language
- preserve S13 experiment names, scores, pass/fail rules, decision gates, confidence labels, and citations
- render `targeted_lookup_log`, `context_budget_report`, `post_skill_isolation_record`, and `excluded_or_deferred_tests_log` as audit tables when present
- mark missing S13 required views as `missing_required_view`
- move missing S13 inputs into the data-gap panel with source skill `S13.plan-validation-experiments`

S14 must not:

- create new validation experiments that S13 did not supply
- change experiment priority scores or pass/fail criteria
- convert a dry-run or synthetic validation plan into real market evidence
- hide context-budget or targeted-lookup warnings because they make the page less persuasive

## HTML Output Rules

```text
single_file_static_html
  Preferred default for easy sharing.

offline_first
  No external requests in default mode.

data_embedding
  Embed sanitized JSON or render server-side into static HTML. Do not embed raw private values.

stable_ids
  Every section and table should have stable IDs for comments and future diffs.
```

## Reference Renderer

Current deterministic smoke-test renderer:

```powershell
python scripts\render-gtm-dashboard-from-report-state.py
```

It renders:

```text
artifacts/dry-runs/generic-hardware-s00-s08-s13-s14-report-state.json
  -> artifacts/dry-runs/generic-hardware-s00-s08-s13-s14-dashboard.html
```

Acceptance rules:

- single-file HTML
- no external script, stylesheet, font, analytics, telemetry, fetch, or network dependency
- Chinese dashboard structure and section labels by default
- visible module coverage, data-gap audit, citation/index treatment, S13 validation roadmap, and post-skill isolation audit
- private pricing calculator has blank local-only inputs
- S14 does not change upstream findings or create missing analysis
