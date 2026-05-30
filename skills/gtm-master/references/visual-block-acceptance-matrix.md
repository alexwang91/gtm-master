# Visual Block Acceptance Matrix

Use this when auditing S01-S08/S13 section drafts, S14 rendering readiness, or report-state compatibility.

## Canonical Contract

`html_section_draft.visual_blocks` may only use the S14-renderable block types below:

```text
status_panel
ranked_bar
matrix_heatmap
range_chart
```

Canonical block shape:

```json
{
  "visual_block_id": "",
  "source_skill": "",
  "type": "status_panel | ranked_bar | matrix_heatmap | range_chart",
  "title": "",
  "subtitle": "",
  "data_source": "",
  "items": [],
  "rows": [],
  "columns": [],
  "scale_min": 0,
  "scale_max": 100,
  "note": "",
  "evidence_refs": [],
  "citations": [],
  "confidence": "high | medium | low | hypothesis_only | blocked | unknown"
}
```

Required fields for every block:

```text
type
title
data_source
confidence
evidence_refs or citations or a source note in `note`
```

## Namespace Rule

Method-level visual names can remain in `Recommended Visuals`, `Default Visuals`, or analysis notes. They must not be emitted as `visual_blocks.type` unless they are mapped to a canonical type.

```text
decision_status_panel -> status_panel
horizontal_range_chart -> range_chart
matrix_or_heatmap -> matrix_heatmap
heatmap -> matrix_heatmap
matrix -> matrix_heatmap only when rows x columns are numeric/comparable
ranked_table -> ranked_bar only when rows have comparable numeric scores; otherwise use tables
ranked_bars -> ranked_bar
scorecard_table -> tables or status_panel, depending on whether it is a gate/status view
risk_table -> tables or ranked_bar, depending on whether numeric/severity ranking exists
action_table -> tables
language_table -> tables
card_grid -> tables or metric_cards unless S14 adds a card visual block later
client_side_calculator -> privatePricingCalculator component, not visual_blocks
```

Fail compatibility if an upstream section emits any non-canonical `visual_blocks.type`.

## Required Blocks

### S01 build-consumer-market-map

```text
Evidence Coverage Gate -> status_panel
Product Capability To Local Selling-Point Fit -> matrix_heatmap
Competitor And Substitute Threat Ranking -> ranked_bar
Local Price Corridor Seed -> range_chart
Segment Priority And Evidence Strength -> ranked_bar
Segment Channel Touchpoint Fit -> matrix_heatmap
```

### S02 mine-jtbd-scenarios

```text
Upstream Input Coverage Gate -> status_panel
Scenario Priority Scorecard -> ranked_bar
Scenario To Segment Matrix -> matrix_heatmap
Product Job Fit And Proof Readiness -> matrix_heatmap
Proof Requirement Urgency Ranking -> ranked_bar
Anti-JTBD And Non-Consumption Risk Ranking -> ranked_bar
```

### S03 match-messages-to-segments

```text
Message Input Coverage Gate -> status_panel
Segment Message Fit -> matrix_heatmap
Feature Benefit Proof Readiness -> matrix_heatmap
Claim Risk And Proof Gate -> status_panel
Objection Severity Ranking -> ranked_bar
Price Message Readiness -> status_panel
```

### S04 model-price-sensitivity

```text
Pricing Decision Gate -> status_panel
Local Price Credibility Corridor -> range_chart
Segment WTP And Sensitivity -> matrix_heatmap
Price Value Proof Readiness -> matrix_heatmap
Price Risk Guardrails -> ranked_bar
WTP Test And Evidence Plan -> status_panel
Private Pricing Calculator Readiness -> status_panel
```

### S05 score-creative-assets

```text
Copy Input Coverage Gate -> status_panel
Copy Priority Scorecard -> ranked_bar
Segment Message Copy Fit -> matrix_heatmap
Proof And Claim Risk Gate -> status_panel
Channel Copy Fit Matrix -> matrix_heatmap
Revision And Test Priority -> ranked_bar
```

### S06 score-kol-fit

```text
Creator Input Coverage Gate -> status_panel
Creator Archetype Fit -> ranked_bar
Trust Proof Fit Matrix -> matrix_heatmap
Platform Relevance Map -> matrix_heatmap
Creator Budget And Expected Outcome Range -> range_chart
Candidate Review Gate -> status_panel
Candidate Fit Ranking -> ranked_bar
Creator Risk Gate -> status_panel
```

### S07 predict-dtc-conversion

```text
Conversion Input Coverage Gate -> status_panel
Prelaunch Page Requirement Readiness -> status_panel
Competitor And Previous-Gen Page Benchmark -> matrix_heatmap
Funnel Friction Ranking -> ranked_bar
Segment Landing Page Fit -> matrix_heatmap
Proof Price Trust Friction -> matrix_heatmap
CVR Assumption Ladder -> range_chart
Tracking Readiness -> status_panel
Experiment Priority -> ranked_bar
```

### S08 forecast-launch-demand

```text
Forecast Input Coverage Gate -> status_panel
Scenario Sales Forecast -> range_chart
Lifecycle Phase Sales Curve -> range_chart
Baseline vs Marketing Incremental Sales -> range_chart
Segment Sales Split -> ranked_bar
Channel Split Forecast -> matrix_heatmap
Inventory Risk Map -> matrix_heatmap
Sensitivity Driver Tornado -> ranked_bar
Marketing Spend Sensitivity -> ranked_bar
Forecast Decision Gate -> status_panel
Validation Need Priority -> ranked_bar
```

### S13 plan-validation-experiments

```text
Validation Input Coverage Gate -> status_panel
Experiment Priority Scorecard -> ranked_bar
Assumption Risk vs Test Feasibility -> matrix_heatmap
Timeline And Decision Unlock Map -> matrix_heatmap
Test Cost Effort vs Impact -> matrix_heatmap
Validation Decision Gate -> status_panel
Experiment Portfolio By Module -> ranked_bar
```

## Thin Output And Gap Codes

Use these cross-suite codes consistently:

```text
rendered_too_thin
  The section has prose/cards/tables but lacks enough required decision views.

missing_required_view
  Required analysis data for a main view is absent.

missing_visual_block
  Required analysis data exists, but the upstream section did not provide a visual block.

missing_visual_block_score
  Data exists, but numeric/comparable scores needed for the requested visual are absent.

non_comparable_range_data
  Range data is not normalized enough for `range_chart`.

missing_evidence_ref
  A material visual claim lacks evidence refs, citation refs, or a source note.

section_confidence_capped
  A confidence cap limits how strongly the visual can be interpreted.

private_data_excluded
  Private COGS, margin, channel, sales, or uploaded data was intentionally excluded from public HTML.
```

Domain-specific gap codes may be added after the generic code, for example:

```text
price_range_chart_not_comparable
segment_gap
proof_gap
localization_gap
```

## Acceptance Checks

Before S00 marks S01-S08/S13 ready for S14:

```text
1. Each standard-mode S01-S08/S13 section that ran has at least 4 required visual_blocks or a visible `skipped` / `rendered_too_thin` gap.

2. Every `visual_blocks.type` is one of:
   status_panel, ranked_bar, matrix_heatmap, range_chart.

3. Every block has title, data_source, confidence, and evidence_refs/citations/source note.

4. Numeric visuals use comparable scores only. Missing scores become tables plus `missing_visual_block_score`.

5. Range visuals use normalized comparable units only. Non-comparable ranges become tables plus `non_comparable_range_data`.

6. User-provided hypotheses, weak public proxies, and synthetic personas remain labeled as hypotheses.

7. Private pricing data is not embedded in public HTML; private calculator specs use blank local fields.

8. S14 must not invent values to satisfy missing blocks. It may render conservative tables and record `missing_visual_block`.
```
