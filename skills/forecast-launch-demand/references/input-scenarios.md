# S08 Formatted Input Scenarios

Use this when asking the user for S08 inputs. Do not ask for every field. Select the smallest scenario that matches the decision the user wants to make.

## Scenario Selector

```text
A_directional_forecast
  Use when the user only wants a broad launch unit-sales range for strategy.

B_channel_allocation
  Use when the user needs unit-sales split by DTC, marketplace, retail, distributor, or creator/referral channel.

C_inventory_decision
  Use when the forecast will influence production, launch inventory, allocation, replenishment, or stockout/overstock risk.

D_dtc_preorder_waitlist
  Use when DTC, PDP, preorder, waitlist, lead collection, or retailer clickout is a major path.

E_previous_generation_calibration
  Use when the user can provide previous-generation sales, price, channel, or launch performance.

F_media_creator_launch
  Use when paid media, KOL/creator, affiliate, or launch traffic plan materially affects sales.

G_lifecycle_marketing_investment
  Use when the user wants sales forecast by launch phase and wants MKT spend to affect expected unit sales.
```

## A. Directional Forecast

Minimum user fields:

```json
{
  "forecast_input_scenario": "A_directional_forecast",
  "forecast_horizon": "launch_week | 30_days | 60_days | 90_days | custom",
  "forecast_boundary": "launch_unit_sales | reachable_launch_demand",
  "target_country_or_region": "",
  "target_price_range": "",
  "planned_channels": [],
  "known_launch_constraints": "",
  "private_forecast_inputs_public_html_policy": "exclude_raw"
}
```

Use this with S01/S04 handoffs to produce directional unit-sales ranges and data gaps.

## B. Channel Allocation

Minimum user fields:

```json
{
  "forecast_input_scenario": "B_channel_allocation",
  "forecast_horizon": "30_days | 60_days | 90_days | custom",
  "forecast_boundary": "launch_unit_sales | sell_through",
  "planned_channel_mix": [
    {
      "channel": "DTC | marketplace | retailer_ecommerce | offline_retail | distributor | creator_affiliate | other",
      "role": "primary | secondary | test | fallback",
      "coverage_or_capacity_note": "",
      "launch_readiness": "confirmed | likely | tentative | unknown"
    }
  ],
  "channel_capacity_constraints": [],
  "retailer_or_marketplace_priority": [],
  "private_forecast_inputs_public_html_policy": "exclude_raw | aggregate"
}
```

Use this when the decision is where to place inventory, budget, or operational effort.

## C. Inventory Decision

Minimum user fields:

```json
{
  "forecast_input_scenario": "C_inventory_decision",
  "forecast_horizon": "launch_week | 30_days | 60_days | 90_days | custom",
  "forecast_boundary": "sell_through | supply_constrained_shipments",
  "target_sellout_window": "",
  "launch_inventory_available": "",
  "inventory_allocation_plan": [
    {
      "channel": "",
      "allocated_units": "",
      "allocation_basis": ""
    }
  ],
  "supply_lead_time_or_replenishment_constraints": "",
  "retail_sell_in_commitments_or_purchase_orders": "",
  "private_forecast_inputs_public_html_policy": "exclude_raw | aggregate | approved"
}
```

Required warning: if inventory values are not supplied, S08 may forecast sales but must mark inventory risk as `hypothesis_only`.

## D. DTC / Preorder / Waitlist

Minimum user fields:

```json
{
  "forecast_input_scenario": "D_dtc_preorder_waitlist",
  "forecast_horizon": "launch_week | 30_days | 60_days | 90_days | custom",
  "forecast_boundary": "launch_unit_sales | sell_through",
  "target_conversion_action": "purchase | preorder | waitlist | lead | retailer_clickout",
  "launch_page_planning_stage": "none | concept | draft | live | post_launch",
  "preorder_or_waitlist_counts": "",
  "traffic_source_plan": [],
  "tracking_or_analytics_context": "",
  "dtc_conversion_basis": "S07_handoff | measured | benchmark | user_assumption | missing"
}
```

Use S07 handoff when available. If S07 did not run, keep conversion assumptions broad and confidence-capped.

## E. Previous-Generation Calibration

Minimum user fields:

```json
{
  "forecast_input_scenario": "E_previous_generation_calibration",
  "forecast_horizon": "30_days | 60_days | 90_days | custom",
  "forecast_boundary": "sell_in | sell_through | launch_unit_sales",
  "previous_generation_sales_price_channel_performance": {
    "country_or_region": "",
    "product_or_generation": "",
    "launch_window": "",
    "price_range": "",
    "channel_mix_summary": "",
    "unit_sales_or_sellthrough_summary": "",
    "stockout_or_overstock_notes": "",
    "promotion_or_media_notes": "",
    "what_changed_for_new_generation": ""
  },
  "private_forecast_inputs_public_html_policy": "exclude_raw | aggregate | approved"
}
```

Best use: calibrate velocity, channel mix, price sensitivity, lifecycle curve, and inventory risk. Public HTML should use aggregated learnings unless approval is explicit.

## F. Media / Creator Launch

Minimum user fields:

```json
{
  "forecast_input_scenario": "F_media_creator_launch",
  "forecast_horizon": "launch_week | 30_days | 60_days | 90_days | custom",
  "forecast_boundary": "launch_unit_sales",
  "marketing_budget_range": "",
  "media_plan_or_reach_assumptions": [
    {
      "source": "paid_social | search | retail_media | creator | affiliate | email | other",
      "budget_or_reach": "",
      "traffic_or_click_assumption": "",
      "basis": "historical | platform_estimate | S06_handoff | user_assumption | missing"
    }
  ],
  "creator_budget_range": "",
  "creator_expected_outcome_estimate": [],
  "private_forecast_inputs_public_html_policy": "exclude_raw | aggregate"
}
```

Use S06 only as traffic/reach input. Do not convert creator reach to sales without a conversion basis.

## G. Lifecycle + Marketing Investment

Use this when MKT investment is central and the forecast needs to explain how launch-phase spending changes expected unit sales.

Read `lifecycle-marketing-input-workbook.md` before asking detailed questions. Start with the compact pack below; use the expanded workbook only when the decision affects budget, inventory, sell-in, or a board-level launch plan.

Minimum user fields:

```json
{
  "forecast_input_scenario": "G_lifecycle_marketing_investment",
  "forecast_horizon": "launch_week | 30_days | 60_days | 90_days | custom",
  "forecast_boundary": "launch_unit_sales | sell_through | supply_constrained_shipments",
  "product_lifecycle_stage": "prelaunch | launch | early_growth | growth | maturity | decline | unknown",
  "launch_phase_calendar": [
    {
      "phase": "prelaunch_warmup | launch_spike | early_ramp | sustain | plateau_or_decay",
      "date_or_week_range": "",
      "major_gtm_activity": "",
      "channel_availability": "confirmed | likely | tentative | unknown",
      "proof_or_review_readiness": "ready | partial | missing | unknown",
      "inventory_status": "confirmed | constrained | unknown"
    }
  ],
  "marketing_investment_plan": [
    {
      "phase": "",
      "channel": "brand | performance | search | paid_social | retail_media | creator | affiliate | PR | promo | other",
      "objective": "awareness | traffic | preorder | purchase | retail_visibility | proof | retargeting",
      "spend_range": "",
      "expected_reach_or_traffic": "",
      "response_basis": "measured_internal | historical_proxy | platform_estimate | S06_creator_estimate | user_assumption | AI_heuristic | missing",
      "conversion_or_action_basis": "measured | benchmark | S07_handoff | user_assumption | missing"
    }
  ],
  "marketing_response_assumptions": {
    "adstock_or_lag_note": "",
    "saturation_or_diminishing_return_note": "",
    "conversion_basis": "measured | benchmark | S07_handoff | user_assumption | missing",
    "pull_forward_or_cannibalization_note": "",
    "creative_fatigue_or_frequency_note": ""
  },
  "baseline_calibration": {
    "baseline_source": "previous_generation | historical_launch | market_sizing_proxy | channel_commitment | user_target | missing",
    "baseline_unit_or_velocity_note": "",
    "what_changed_vs_baseline": ""
  },
  "baseline_vs_incremental_sales_policy": "separate | aggregate_only",
  "private_forecast_inputs_public_html_policy": "exclude_raw | aggregate | approved"
}
```

S08 must show baseline sales, incremental marketing-driven sales, and confidence caps separately. If response or conversion basis is missing, output sensitivity and validation needs instead of confident MKT lift.

## Minimal User Prompt

If the user has not chosen a scenario, ask one concise question:

```text
这次 S08 主要要支持哪个决策？A 方向性销量范围；B 渠道分配；
C 库存/补货；D DTC/预售/waitlist；E 上一代校准；
F 媒体/KOL 发售流量；G 生命周期 + MKT 投入销量预测。
```

Then request only the selected template's fields and mark every missing field as a data gap instead of blocking the whole report.