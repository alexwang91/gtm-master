# S08 Upstream Input Map

Use this before deciding whether S08 can forecast launch unit sales, should produce a directional planning shell, or must request missing inputs.

## Scenario Input Gate

Before checking every possible field, classify the user's input with `input-scenarios.md`:

```text
A_directional_forecast
  Requires only forecast horizon, forecast boundary, target country/price, planned channels, and upstream S01/S04 handoffs.

B_channel_allocation
  Requires planned channel mix, channel capacity/readiness, and local channel evidence.

C_inventory_decision
  Requires inventory, allocation, sellout window, and replenishment/PO constraints.

D_dtc_preorder_waitlist
  Requires conversion action, page stage, traffic source plan, and preorder/waitlist/tracking context when available.

E_previous_generation_calibration
  Requires previous-generation launch, sales, price, channel, and change notes.

F_media_creator_launch
  Requires media/creator budget, reach or traffic assumptions, and basis labels.

G_lifecycle_marketing_investment
  Requires product lifecycle stage, launch phase calendar, marketing investment plan, marketing response assumptions, baseline calibration, and private/public display policy. Read lifecycle-marketing-input-workbook.md before asking detailed fields.
```

Only the selected scenario's fields should be treated as user-facing asks. Other fields remain optional enrichment.

## Minimum Proceed Gate

S08 can produce a directional forecast when these groups exist:

```text
market_scope
  project_brief, launch country/region, product category, forecast horizon, and target price range

market_size_seed
  tam_sam_som_seed, segment_level_tam_sam_som, segment_priority_ranking, or explicit data gaps from S01

price_context
  price_sensitivity_model, pricing_handoff_summary, pricing_decision_gate, price_risk_guardrail, or explicit price assumption

channel_context
  segment_channel_touchpoint_map, channel_fit_scores, planned_channels, retailer_marketplace_candidates, or explicit channel hypothesis
```

S08 can produce stronger forecast ranges when:

```text
calibration_inputs
  previous_generation_sales_price_channel_performance, historical_launch_sales_or_sellthrough,
  retail_sell_in_commitments_or_purchase_orders, preorder_or_waitlist_counts, media plan, or inventory constraints.
```

S08 can use optional conversion and creator inputs when:

```text
conversion_or_traffic_inputs
  cvr_assumption_ladder, dtc_conversion_model, funnel_friction_scorecard,
  creator_expected_outcome_estimate, creator_budget_estimate, review_approved_candidate_set.
```

## Missing Input Handling

```text
missing_market_size_seed
  Do not forecast sales units. Produce forecast_input_coverage_gate, required evidence request, and validation_need_map.

missing_segment_split
  Produce total range only; cap segment split confidence at low.

missing_channel_context
  Produce demand potential, not channel split. Record missing_channel_context.

missing_price_context
  Do not produce revenue ranges. Cap demand confidence because price acceptance is unknown.

missing_conversion_basis
  Do not use precise CVR. Use scenario action-rate assumptions only when labeled hypothesis_only.

missing_inventory_context
  Produce sales range, but inventory_risk_map must be hypothesis_only or omitted with gap.

missing_forecast_horizon
  Default to 90-day launch window and record assumption.

missing_lifecycle_phase_calendar
  Use the default lifecycle calendar from lifecycle-marketing-input-workbook.md and mark the phase curve low-confidence planning only.

missing_marketing_investment_plan
  Can forecast baseline sales, but do not estimate marketing incremental sales.

missing_marketing_response_basis
  Marketing incremental sales must be hypothesis_only and rendered as sensitivity, not confident lift.

missing_marketing_conversion_basis
  Convert spend to reach, traffic, leads, proof, or retail visibility only. Do not convert to unit sales except as hypothesis_only scenario.

missing_baseline_calibration_for_G
  Use S01/S02/S03/S04/S07 proxies and mark the unit forecast directional_only.

missing_private_public_display_policy
  Default to exclude_raw. Public HTML may show only aggregate/indexed ranges and data gaps.
```

## High-Value Inputs

```text
tam_sam_som_assumption_tree
  Use as ceiling and sanity check, not as a sales forecast by itself.

segment_priority_ranking, segment_level_tam_sam_som
  Use to allocate reachable demand by segment.

channel_fit_scores, segment_channel_touchpoint_map
  Use to allocate demand by reachable channel and local buying behavior.

pricing_handoff_summary, price_sensitivity_model, elasticity_assumption_seed
  Use to set price acceptance and downside/upside price risk.

cvr_assumption_ladder
  Use only as scenario input with confidence caps. Do not treat S07 CVR as measured demand.

creator_expected_outcome_estimate
  Use only as traffic/reach assumption, not as sales guarantee.

previous_generation_sales_price_channel_performance
  Use to calibrate velocity, channel mix, and price-response assumptions, keeping private raw values out of public HTML unless approved.
```
