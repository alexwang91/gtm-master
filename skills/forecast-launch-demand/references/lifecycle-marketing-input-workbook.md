# S08 Lifecycle + Marketing Input Workbook

Use this when `forecast_input_scenario = G_lifecycle_marketing_investment`, or when the user asks how marketing spend changes launch sales over time.

This workbook turns private or incomplete business inputs into a structured forecast pack. It is designed for prelaunch use: the product may not have a live PDP, final channel contracts, or measured sales yet.

## Core Rule

S08 forecasts launch unit sales, not "marketing impact" in isolation. Marketing investment may only affect the forecast through an explicit bridge:

```text
spend / activity
-> effective reach, traffic, leads, retail visibility, or proof
-> conversion action
-> incremental unit sales
-> total unit sales after baseline, pull-forward, cannibalization, and stockout effects
```

Never turn budget directly into unit sales with a simple linear multiplier unless the user supplies measured response data and asks for a local linear approximation.

## Minimum Fillable Pack

Ask for this compact pack when the user wants the model to use MKT investment but has limited time.

```json
{
  "forecast_input_scenario": "G_lifecycle_marketing_investment",
  "forecast_horizon": "30_days | 60_days | 90_days | custom",
  "forecast_boundary": "launch_unit_sales | sell_through | supply_constrained_shipments",
  "target_country_or_region": "",
  "target_price_range": "",
  "planned_channels": [],
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
      "conversion_or_action_basis": "measured | benchmark | S07_handoff | user_assumption | missing",
      "response_basis": "measured_internal | historical_proxy | platform_estimate | S06_creator_estimate | user_assumption | AI_heuristic | missing"
    }
  ],
  "baseline_calibration": {
    "baseline_source": "previous_generation | historical_launch | market_sizing_proxy | channel_commitment | user_target | missing",
    "baseline_unit_or_velocity_note": "",
    "what_changed_vs_baseline": ""
  },
  "marketing_response_assumptions": {
    "adstock_or_lag_note": "",
    "saturation_or_diminishing_return_note": "",
    "pull_forward_or_cannibalization_note": "",
    "creative_fatigue_or_frequency_note": ""
  },
  "constraints": {
    "launch_inventory_available": "",
    "supply_lead_time_or_replenishment_constraints": "",
    "retail_sell_in_commitments_or_purchase_orders": "",
    "known_launch_constraints": ""
  },
  "private_forecast_inputs_public_html_policy": "exclude_raw | aggregate | approved"
}
```

## Expanded Workbook

Use the expanded version when the forecast will inform budget, inventory, sell-in, or a board-level launch plan.

### G0. Decision Target

```json
{
  "decision_to_support": "budget_sizing | inventory_buy | channel_allocation | launch_readiness | scenario_planning",
  "forecast_horizon": "launch_week | 30_days | 60_days | 90_days | custom",
  "forecast_boundary": "launch_unit_sales | sell_through | sell_in | supply_constrained_shipments",
  "forecast_output_granularity": "total | segment | channel | segment_x_channel | phase_x_channel",
  "public_html_policy": "exclude_raw | aggregate | approved",
  "private_values_allowed_in_model": true
}
```

Required interpretation:

```text
budget_sizing
  Needs marketing response sensitivity and validation needs. Exact unit forecast can stay broad.

inventory_buy
  Needs sell-through boundary, inventory constraints, replenishment timing, and stockout/overstock risk.

channel_allocation
  Needs channel readiness, capacity, and expected traffic/sell-through by channel.

launch_readiness
  Needs proof, PDP, retail listing, review, and tracking readiness by phase.

scenario_planning
  Can proceed with assumptions but must show confidence caps and sensitivity.
```

### G1. Lifecycle Phase Calendar

```json
{
  "launch_phase_calendar": [
    {
      "phase": "prelaunch_warmup",
      "date_or_week_range": "T-4 to T-1 weeks",
      "major_gtm_activity": "teaser, waitlist, review seeding, retailer listing preparation",
      "channel_availability": "tentative",
      "proof_or_review_readiness": "partial",
      "tracking_readiness": "partial",
      "inventory_status": "unknown",
      "expected_sales_role": "build demand, collect leads, convert preorders if enabled"
    }
  ]
}
```

If the user does not provide a phase calendar, default to:

```text
prelaunch_warmup: T-4 to T-1 weeks
launch_spike: launch week
early_ramp: week 2 to week 4
sustain: week 5 to week 12
plateau_or_decay: after week 12, only if horizon exceeds 90 days
```

Mark this default as `AI_heuristic` and cap confidence at `low` unless historical launch timing supports it.

### G2. Marketing Investment Plan

```json
{
  "marketing_investment_plan": [
    {
      "phase": "launch_spike",
      "channel": "paid_social",
      "objective": "traffic",
      "spend_range": "EUR 15000-25000",
      "expected_reach_or_traffic": "platform estimate or historical proxy",
      "landing_or_conversion_path": "DTC PDP | marketplace PDP | retailer PDP | waitlist | store visit",
      "response_basis": "platform_estimate",
      "conversion_or_action_basis": "S07_handoff",
      "owner": "marketing"
    }
  ]
}
```

Each row must answer four questions:

```text
What phase does it affect?
What behavior does it try to move?
What evidence supports the reach/traffic/action assumption?
Can that action be translated to sales, or only to a validation need?
```

### G3. Response Assumptions

```json
{
  "marketing_response_assumptions": {
    "response_model_type_preference": "phase_multiplier_curve | log_response | hill_saturation | adstock_saturation | measured_model | let_S08_choose",
    "adstock_or_lag_note": "",
    "saturation_or_diminishing_return_note": "",
    "conversion_basis": "measured | benchmark | S07_handoff | user_assumption | missing",
    "promo_pull_forward_risk": "none | low | medium | high | unknown",
    "creative_fatigue_risk": "none | low | medium | high | unknown",
    "search_lift_or_brand_carryover_note": ""
  }
}
```

Model choice:

```text
measured_model
  Use only with measured spend and sales/traffic response data.

adstock_saturation
  Use when spend spans multiple weeks and lag/carryover matters.

hill_saturation
  Use when spend has plausible saturation but lag evidence is weak.

log_response
  Use when evidence is thin but the user needs a directional spend sensitivity curve.

phase_multiplier_curve
  Use when only phase-level GTM intensity is known.
```

### G4. Baseline Calibration

```json
{
  "baseline_calibration": {
    "previous_generation_sales_price_channel_performance": "",
    "historical_launch_sales_or_sellthrough": "",
    "preorder_or_waitlist_counts": "",
    "retail_sell_in_commitments_or_purchase_orders": "",
    "market_sizing_proxy_from_S01": "",
    "baseline_vs_incremental_sales_policy": "separate | aggregate_only",
    "what_changed_for_new_generation": ""
  }
}
```

Required interpretation:

```text
previous_generation
  Best for velocity calibration and channel mix, but keep raw private values out of public HTML unless approved.

historical_launch
  Best for launch curve shape and seasonality.

preorder_or_waitlist
  Best for near-term conversion, but must adjust for intent quality and duplicate leads.

retail_sell_in_or_PO
  Useful for sell-in and allocation, not proof of consumer sell-through.

market_sizing_proxy
  Useful as ceiling and sanity check, not a sales forecast by itself.
```

### G5. Supply And Channel Constraints

```json
{
  "constraints": {
    "launch_inventory_available": "",
    "inventory_allocation_plan": [],
    "supply_lead_time_or_replenishment_constraints": "",
    "retail_sell_in_commitments_or_purchase_orders": "",
    "channel_capacity_constraints": [],
    "listing_or_availability_risks": [],
    "seasonality_or_retail_calendar_notes": ""
  }
}
```

If inventory is missing, S08 may forecast sales potential but must mark inventory risk as `hypothesis_only`.

### G6. Public HTML Policy

```json
{
  "private_forecast_inputs_public_html_policy": "exclude_raw | aggregate | approved",
  "sensitive_fields": [
    "COGS",
    "margin",
    "raw unit sales",
    "purchase orders",
    "inventory",
    "media spend",
    "channel terms"
  ],
  "approved_public_aggregations": [
    "low / medium / high budget band",
    "indexed previous-generation baseline",
    "scenario ranges",
    "confidence level",
    "data gap"
  ]
}
```

Default policy is `exclude_raw`. Use aggregated or indexed display unless the user explicitly approves raw values.

## Missing Input Degradation

```text
missing_phase_calendar
  Use default phase calendar, output phase curve as low-confidence planning curve.

missing_marketing_spend
  Forecast baseline sales only. Do not produce marketing incremental sales.

missing_response_basis
  Produce spend sensitivity and validation need, not confident lift.

missing_conversion_or_action_basis
  Convert spend to traffic/reach only. Do not convert to unit sales except as hypothesis_only scenario.

missing_baseline_calibration
  Use S01/S02/S03/S04/S07 proxies and mark unit forecast as directional_only.

missing_inventory_constraints
  Forecast unconstrained sell-through potential; inventory risk remains hypothesis_only.

missing_public_html_policy
  Exclude raw private values from HTML and show aggregate scenario ranges only.
```

## Validation Rules

```text
1. Every spend/activity row needs a basis label.
2. Every conversion-to-sales bridge needs a conversion or action basis.
3. Baseline sales and marketing incremental sales must be separated when MKT investment is supplied.
4. Promo spend must flag pull-forward or cannibalization risk.
5. Retail sell-in or PO values must not be treated as consumer sell-through.
6. S06 creator outputs are reach/traffic/proof inputs, not guaranteed sales.
7. S07 conversion outputs are scenario assumptions, not measured sales unless explicitly measured.
8. Revenue requires price, currency, channel price policy, and public display permission.
9. Profit, margin, and COGS do not belong in S08 public output.
10. Confidence cannot exceed the weakest critical bridge: baseline, reach/traffic, conversion/action, supply, or channel availability.
```

## Example Structured Pack

Use this shape as an example only. Do not copy the numbers into a real forecast.

```json
{
  "forecast_input_scenario": "G_lifecycle_marketing_investment",
  "forecast_horizon": "90_days",
  "forecast_boundary": "sell_through",
  "target_country_or_region": "Hungary",
  "target_price_range": "EUR 199-249",
  "planned_channels": ["retailer_ecommerce", "marketplace", "DTC"],
  "launch_phase_calendar": [
    {
      "phase": "prelaunch_warmup",
      "date_or_week_range": "T-4 to T-1 weeks",
      "major_gtm_activity": "local review seeding, waitlist, retailer listing preparation",
      "channel_availability": "tentative",
      "proof_or_review_readiness": "partial",
      "inventory_status": "unknown"
    },
    {
      "phase": "launch_spike",
      "date_or_week_range": "week 1",
      "major_gtm_activity": "launch PR, paid social burst, creator reviews, retailer homepage slot if available",
      "channel_availability": "likely",
      "proof_or_review_readiness": "partial",
      "inventory_status": "constrained"
    }
  ],
  "marketing_investment_plan": [
    {
      "phase": "launch_spike",
      "channel": "paid_social",
      "objective": "traffic",
      "spend_range": "EUR 12000-20000",
      "expected_reach_or_traffic": "platform estimate",
      "landing_or_conversion_path": "retailer PDP and DTC PDP",
      "response_basis": "platform_estimate",
      "conversion_or_action_basis": "S07_handoff"
    },
    {
      "phase": "early_ramp",
      "channel": "retail_media",
      "objective": "retail_visibility",
      "spend_range": "EUR 5000-10000",
      "expected_reach_or_traffic": "retailer media kit or category benchmark",
      "landing_or_conversion_path": "retailer PDP",
      "response_basis": "historical_proxy",
      "conversion_or_action_basis": "benchmark"
    }
  ],
  "baseline_calibration": {
    "baseline_source": "previous_generation",
    "baseline_unit_or_velocity_note": "private raw values excluded from HTML",
    "what_changed_vs_baseline": "higher price, improved feature set, broader retail availability"
  },
  "marketing_response_assumptions": {
    "response_model_type_preference": "log_response",
    "adstock_or_lag_note": "brand and creator effects may carry into weeks 2-4",
    "saturation_or_diminishing_return_note": "paid social and retail media should saturate at high spend",
    "conversion_basis": "S07_handoff",
    "promo_pull_forward_risk": "medium",
    "creative_fatigue_risk": "medium"
  },
  "private_forecast_inputs_public_html_policy": "aggregate"
}
```
