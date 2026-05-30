# HTML Dashboard Design

The final report should feel like a decision dashboard, not a generated essay.

## Layout

- Start with a compact input-boundary strip, then a management executive summary band containing expected weekly sales range, sales-driver decomposition, simple MKT budget posture, channel priority and channel capability, competitor advantage/weakness and response, evidence confidence, and top next validation action.
- Use clear report sections with dense but readable cards, tables, and charts.
- Keep data gaps visible in context, not only at the end.
- Separate measured evidence, modeled estimates, and assumptions with badges.
- Use a final appendix for evidence ledger, assumptions, methods, and source limitations.

## Visual Components

Use these components consistently:

```text
verdict_card
metric_card
status_panel
ranked_bar
matrix_heatmap
range_chart
confidence_badge
evidence_badge
data_gap_callout
segment_priority_table
competitor_matrix
price_corridor_chart
nps_composition_chart
journey_curve
driver_tornado
handoff_summary_card
validation_roadmap_table
```

## Evidence Badges

```text
Evidence
Strong Inference
Weak Inference
Assumption
Needs Validation
Risk
```

Badges must appear near the claim they qualify.

## Chart Rules

- Use a chart only when the underlying data is structured enough.
- Do not imply precision for assumption-based TAM, NPS proxy, or earned growth proxy.
- Label proxy metrics clearly.
- Show sample size and source type when available.
- Include citation refs in chart notes.

## Narrative Rules

- Lead each section with the decision implication.
- Follow with evidence, not general explanation.
- Keep section summaries concise enough for executive scanning.
- Preserve local consumer language where it matters for messaging or JTBD.
- Do not hide uncertainty to make the report look cleaner.

## Executive Summary Content

Before the executive summary, show a compact input-boundary strip. It should be small and practical, not a full product spec section:

- Product/category, target country, price band, and run mode.
- Supplied product claims/spec groups.
- Commercial inputs provided or missing: MKT budget, channel plan, previous generation, benchmark competitors, brand positioning.
- Evidence coverage: local ecommerce, local search terms, reviews/forums/video comments, private NSS/NPS, and web status.
- Private-data boundary: COGS, margin, channel terms, internal sales, and raw private materials are blank/excluded unless explicitly approved.

The top summary should not describe the skill chain. It should synthesize the report into business decisions:

- Expected weekly sales range, derived from S08 launch forecast and labeled by confidence.
- Why the sales range is plausible: market space, brand strength, price competitiveness, and product competitiveness.
- MKT spend posture: minimum test, base launch, and stretch/upside budget when supported by inputs.
- Channel priority: rank channels by reach, conversion readiness, commercial access, proof fit, margin/price constraints, and validation need.
- Competitor response: show top competitor/substitute strengths, weaknesses, price pressure, proof gaps, and response strategy.
- Evidence risks: show the top gaps or S13 validation tests that could change the recommendation.

If market size, brand strength, conversion, or channel readiness is not supported by evidence, keep the summary but mark the affected driver as hypothesis or data gap.

## HTML Composition Guardrails

- Do not invent missing analysis during rendering.
- Do not rewrite upstream conclusions unless a decision record says so.
- Do not merge conflicting conclusions silently; show the conflict and data gap.
- Do not use raw consumer quotes in public-facing materials unless usage is allowed.
- Keep the dashboard self-contained: charts, citations, and notes should render without external dependencies unless explicitly approved.
