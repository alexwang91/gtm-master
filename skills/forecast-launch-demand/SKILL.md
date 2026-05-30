---
name: forecast-launch-demand
description: Use when forecasting launch unit sales, sell-through, sell-in, channel split, inventory risk, lifecycle phase sales curves, marketing investment response, or sales assumptions for a 2C hardware GTM report using market sizing, segment priority, channel fit, pricing, optional DTC conversion, optional creator/KOL traffic, MKT spend, and historical or private sales inputs without false precision.
---

# Forecast Launch Demand

## Role

Use this skill as S08 in the GTM intelligence report suite. Its essence is launch sales forecasting: estimate how many units may sell, through which channels, under which assumptions, and with what inventory risk. It converts market sizing seeds, segment priorities, channel fit, pricing assumptions, optional DTC conversion assumptions, optional creator/KOL traffic, and historical/private launch evidence into conservative/base/upside launch sales scenarios.

Demand is an upstream driver inside S08, not the final answer. S08 forecasts decision ranges, not certainty. It must separate:

- demand potential
- reachable launch demand
- launch unit sales
- constrained supply or inventory allocation
- sell-in commitments
- sell-through expectations
- private internal inputs that should not appear in public HTML

S08 must not invent market size, precise unit sales, revenue, ROAS, profit, channel commitments, or stockout risk. It produces assumption trees, ranges, confidence caps, sensitivity views, and validation needs.

## Required Inputs

```json
{
  "project_brief": {},
  "market_context_pack": {},
  "price_sensitivity_model": {},
  "pricing_handoff_summary": {},
  "pricing_decision_gate": {}
}
```

High-value upstream fields:

```json
{
  "tam_sam_som_seed": {},
  "tam_sam_som_assumption_tree": {},
  "segment_priority_ranking": [],
  "segment_level_tam_sam_som": [],
  "segment_channel_touchpoint_map": [],
  "channel_fit_scores": [],
  "retailer_marketplace_candidates": [],
  "market_sizing_confidence": {},
  "market_sizing_data_gaps": [],
  "local_price_corridor": {},
  "segment_wtp_hypothesis": [],
  "elasticity_assumption_seed": {},
  "pricing_decision_options": [],
  "price_risk_guardrail": [],
  "retail_price_integrity_map": {},
  "dtc_conversion_model": {},
  "cvr_assumption_ladder": [],
  "funnel_friction_scorecard": [],
  "tracking_readiness_audit": {},
  "creator_budget_estimate": [],
  "creator_expected_outcome_estimate": [],
  "creator_budget_expectation_confidence": {},
  "review_approved_candidate_set": []
}
```

Optional user inputs:

```json
{
  "forecast_input_scenario": "A_directional_forecast | B_channel_allocation | C_inventory_decision | D_dtc_preorder_waitlist | E_previous_generation_calibration | F_media_creator_launch | G_lifecycle_marketing_investment",
  "structured_forecast_input_pack": {},
  "product_lifecycle_stage": "prelaunch | launch | early_growth | growth | maturity | decline | unknown",
  "launch_phase_calendar": [],
  "lifecycle_curve_assumption": "phase_multiplier_curve | S_curve | Bass_diffusion_proxy | cohort_curve | unknown",
  "marketing_investment_plan": [],
  "marketing_spend_by_phase": [],
  "marketing_response_assumptions": {},
  "historical_marketing_response_data": "",
  "baseline_calibration": {},
  "baseline_vs_incremental_sales_policy": "separate | aggregate_only",
  "constraints": {},
  "launch_timing": "",
  "forecast_horizon": "launch_week | 30_days | 60_days | 90_days | custom",
  "target_sellout_window": "",
  "planned_channel_mix": [],
  "channel_capacity_constraints": [],
  "launch_inventory_available": "",
  "inventory_allocation_plan": [],
  "supply_lead_time_or_replenishment_constraints": "",
  "retail_sell_in_commitments_or_purchase_orders": "",
  "preorder_or_waitlist_counts": "",
  "marketing_budget_range": "",
  "media_plan_or_reach_assumptions": [],
  "historical_launch_sales_or_sellthrough": "",
  "previous_generation_sales_price_channel_performance": "",
  "seasonality_or_retail_calendar_notes": "",
  "target_revenue_or_unit_goal": "",
  "forecast_output_granularity": "total | segment | channel | segment_x_channel",
  "private_forecast_inputs_public_html_policy": "exclude_raw | aggregate | approved"
}
```

## Load Order

Read only what the current task needs:

1. Read `references/input-scenarios.md` before asking the user for S08 inputs or deciding which fields are necessary.
2. Read `references/lifecycle-marketing-input-workbook.md` when the selected scenario is `G_lifecycle_marketing_investment` or when marketing spend should affect sales over time.
3. Read `references/output-contract.md` before producing artifacts, handoffs, or report sections.
4. Read `references/upstream-input-map.md` before deciding whether S08 can produce a forecast or only a planning shell.
5. Read `references/lifecycle-marketing-models.md` before modeling lifecycle phases, launch curves, marketing spend, adstock, saturation, or incremental sales.
6. Read `references/forecast-methods.md` before building scenarios, channel split, inventory risk, or sensitivity analysis.
7. Read `references/scoring-rubrics.md` before assigning confidence, risk, or sensitivity scores.
8. Read `references/evidence-usage-policy.md` before using public benchmarks, historical sales, private channel data, or revenue-like fields.
9. Read `references/html-visual-block-generation.md` before producing S14-ready `visual_blocks`.
10. Read `references/html-section-contract.md` before producing the HTML forecast section draft.

## Depth Modes

```text
quick
  Produce input coverage, forecast feasibility, broad conservative/base/upside ranges, top sensitivity drivers, and data gaps.

standard
  Produce core outputs: assumption tree, scenario forecast, segment split, channel split, price/conversion bridge, inventory risk, sensitivity drivers, confidence caps, decision gate, and HTML section.

deep
  Add sell-in vs sell-through split, media reach bridge, creator traffic bridge, DTC conversion bridge, previous-generation calibration, supply constraints, seasonality/calendar adjustment, and validation roadmap inputs.
```

Default to `standard`.

## Output Tiers

Core outputs:

```text
forecast_input_coverage_gate
forecast_scope_boundary
forecast_assumption_tree
scenario_sales_forecast
segment_sales_split
launch_sales_forecast
lifecycle_phase_sales_curve
marketing_investment_response_model
baseline_incremental_sales_bridge
channel_split_forecast
price_conversion_assumption_bridge
sensitivity_driver_tornado
inventory_risk_map
forecast_confidence_caps
forecast_decision_gate
validation_need_map
html_forecast_section
```

Conditional outputs:

```text
launch_calendar_seasonality_adjustment
retail_sell_in_sell_through_split
media_reach_to_demand_bridge
marketing_spend_sensitivity_curve
creator_traffic_demand_bridge
dtc_conversion_scenario_bridge
previous_generation_calibration
supply_constraint_scenario
preorder_waitlist_projection
gross_revenue_range_estimate
regional_channel_allocation
forecast_review_gate
```

Audit outputs:

```text
forecast_evidence_trace
forecast_assumption_log
source_basis_matrix
formula_trace
excluded_private_data_log
scenario_change_log
```

## Conditional Triggers

```text
forecast_review_gate
  Trigger when S08 uses private goals, inventory limits, purchase orders, historical sales, media plans, or user-provided assumptions.

lifecycle_phase_sales_curve
  Trigger whenever forecast_horizon spans multiple phases or launch timing matters.

marketing_investment_response_model
  Trigger when marketing_investment_plan, marketing_budget_range, media_plan_or_reach_assumptions, creator spend, retail media, or promo spend is supplied.

baseline_incremental_sales_bridge
  Trigger when marketing investment is supplied or when the user asks how MKT spend affects sales.

previous_generation_calibration
  Trigger when previous-generation sales, price, channel, or launch performance is supplied.

retail_sell_in_sell_through_split
  Trigger when retail, distributor, marketplace, PO, channel allocation, or sell-in commitments matter.

dtc_conversion_scenario_bridge
  Trigger when S07 ran or when DTC/PDP/preorder/waitlist conversion is a meaningful channel.

creator_traffic_demand_bridge
  Trigger when S06 ran or creator/KOL traffic is part of the channel plan.

marketing_spend_sensitivity_curve
  Trigger when spend ranges, channel spend, or budget scenarios are supplied.

supply_constraint_scenario
  Trigger when inventory, allocation, lead time, replenishment, or manufacturing constraints are supplied.

gross_revenue_range_estimate
  Trigger only when unit range, price/currency, channel price policy, and public/private display permission are explicit.
```

## Execution Workflow

```text
1. Select the smallest `forecast_input_scenario` that matches the user's decision. Ask only for that template's fields when missing.
2. Validate forecast objective, horizon, geography, product category, price basis, and public/private output policy.
3. Map available evidence by basis type: market sizing seed, segment seed, channel signal, price model, conversion proxy, creator proxy, historical internal data, user assumption.
4. Establish forecast boundary: demand potential, reachable demand, launch unit sales, sell-in, sell-through, or supply-constrained shipment.
5. Build product lifecycle phase model: prelaunch warmup, launch spike, early ramp, sustain, and plateau/decay where relevant.
6. Build assumption tree from segment size, segment priority, channel reach/availability, price acceptance, conversion/action rate, timing, competition, marketing investment, and supply constraints.
7. Separate baseline sales from marketing incremental sales. Apply adstock/lag and saturation/diminishing returns when modeling marketing spend.
8. Build conservative/base/upside scenarios with ranges and confidence caps.
9. Split sales by segment and channel only when upstream evidence supports the split; otherwise use explicit assumptions and gaps.
10. Bridge price and conversion assumptions without double-counting S04 price risk or S07 CVR ranges.
11. Model inventory risk as stockout/overstock exposure by scenario and channel; do not imply a supply decision without user-supplied inventory constraints.
12. Build sensitivity driver tornado to show which assumptions move the forecast most.
13. Add retail sell-in/sell-through, creator traffic, DTC conversion, previous-generation, media reach, lifecycle phase, marketing response, seasonality, or supply modules only when triggered.
14. Produce forecast decision gate: usable_for_direction, usable_for_budget, usable_for_inventory, or not_ready.
15. Produce compressed handoff pack for S09/S13/S14.
16. Produce HTML forecast section draft with S14-ready visual blocks.
```

## Scope Boundary

S08 owns:

- Launch unit sales scenario ranges
- Product lifecycle phase sales curve
- Marketing investment response and incremental sales assumptions
- Segment and channel split assumptions
- Sell-in vs sell-through distinction
- Inventory stockout/overstock risk ranges
- Sensitivity analysis and confidence caps
- Forecast validation needs for S13

S08 does not own:

- Final market sizing collection from scratch
- Final pricing decision
- Final media budget approval
- Final channel contract or purchase order validation
- Final inventory purchase order
- Profit, margin, or COGS analysis
- Treating heuristic scenarios as measured sales forecast
- Final HTML composition

## Required Output

Always return the S08 output envelope from `references/output-contract.md`:

```json
{
  "full_artifact": {},
  "compressed_handoff_pack": {},
  "html_section_draft": {},
  "evidence_updates": [],
  "decision_updates": [],
  "data_gaps": [],
  "post_skill_isolation_record": {},
  "recommended_next_skills": []
}
```

## Quality Rules

- Do not output single-point unit sales; use ranges and scenarios.
- Do not ask for every optional input. Use `references/input-scenarios.md` and request only the smallest scenario template needed for the user's decision.
- Do not model marketing spend as linear sales lift by default. Use diminishing returns and confidence caps.
- Separate baseline sales from marketing incremental sales when MKT input is supplied.
- Do not exceed S01 market size ceilings unless explicitly modeling an alternative assumption and marking it.
- Separate demand potential, reachable demand, sell-in, sell-through, and supply-constrained shipments.
- Separate measured internal data, public benchmark proxy, upstream model output, user hypothesis, and AI heuristic judgment.
- Do not multiply unrelated scores into a fake precise number. Use formulas as scaffolds and show confidence caps.
- Do not show revenue unless price/currency and display permission are explicit; never show profit or margin.
- Default dashboard-facing outputs to Simplified Chinese unless the user requests another report language.
