# S07 HTML Section Contract

S07 contributes the DTC/PDP conversion section of the final GTM dashboard.

## Section Role

The S07 section should answer:

```text
If the launch page/funnel does not exist yet, what should the page/PDP/checkout/waitlist need to prove based on competitors, previous-generation learnings, and upstream GTM evidence? If it does exist, can the planned traffic, message, price, proof, trust, page, and checkout flow plausibly convert, where is friction highest, what CVR assumptions may feed S08, and what tests must run first?
```

Dashboard-facing text should be Simplified Chinese unless the user requests another language.

## Required Section Shape

```json
{
  "section_id": "dtc_conversion",
  "source_skill": "S07.predict-dtc-conversion",
  "section_title": "DTC/PDP 转化规划与实验计划",
  "status": "rendered | rendered_with_gaps | skipped",
  "confidence": "high | medium | low | hypothesis_only | blocked | unknown",
  "executive_takeaway": "",
  "narrative_blocks": [],
  "metric_cards": [],
  "visual_blocks": [],
  "tables": [],
  "callouts": [],
  "citations": [],
  "data_gaps": [],
  "next_actions": []
}
```

## Default Visual Blocks

```yaml
required_visual_blocks:
  - name: Conversion Input Coverage Gate
    type: status_panel
    data_source: conversion_input_coverage_gate

  - name: Prelaunch Page Requirement Readiness
    type: status_panel
    data_source: prelaunch_conversion_planning_mode + category_page_requirement_brief

  - name: Competitor And Previous-Gen Page Benchmark
    type: matrix_heatmap
    data_source: competitor_landing_pdp_benchmark + previous_generation_funnel_learnings

  - name: Funnel Friction Ranking
    type: ranked_bar
    data_source: funnel_friction_scorecard

  - name: Segment Landing Page Fit
    type: matrix_heatmap
    data_source: segment_landing_page_fit_matrix

  - name: Proof Price Trust Friction
    type: matrix_heatmap
    data_source: proof_objection_friction_map + price_trust_checkout_friction_map

  - name: CVR Assumption Ladder
    type: range_chart
    data_source: cvr_assumption_ladder

  - name: Tracking Readiness
    type: status_panel
    data_source: tracking_readiness_audit

  - name: Experiment Priority
    type: ranked_bar
    data_source: page_experiment_plan
```

Use `tables` for funnel stage inventories, traffic-source maps, page material request lists, analytics event schemas, experiment details, performance interpretation, and compliance queues.

In prelaunch mode, use tables for competitor benchmarks, previous-generation learnings, page requirements, and recommendation details when the evidence is heterogeneous or not scoreable.

## Thin Output Rules

Mark the S07 HTML section as `rendered_too_thin` if it lacks any of:

```text
input coverage or explicit blocked status
funnel friction ranking or prelaunch page requirement readiness
segment/page fit or explicit prelaunch_no_owned_page gap
proof/price/trust friction
CVR assumption ladder or explicit missing_cvr_basis gap
tracking readiness or explicit missing_tracking_context gap
experiment plan
```

## Data Gap Codes

```text
missing_page_or_funnel_text
prelaunch_no_owned_page
missing_competitor_page_benchmark
missing_previous_generation_funnel_data
prelaunch_recommendations_hypothesis_only
missing_offer_details
missing_checkout_or_policy_context
missing_tracking_context
missing_traffic_source_context
missing_performance_data
missing_cvr_basis
cvr_confidence_capped
private_analytics_excluded
missing_visual_block
missing_visual_block_score
rendered_too_thin
```
