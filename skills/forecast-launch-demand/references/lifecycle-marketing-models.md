# S08 Lifecycle And Marketing Investment Models

Use this when S08 forecasts sales across launch phases or when marketing spend materially affects expected unit sales.

## Input To Model Mapping

When `G_lifecycle_marketing_investment` is selected, first parse `lifecycle-marketing-input-workbook.md` into these model blocks:

```text
launch_phase_calendar
  Defines the time buckets for lifecycle_phase_sales_curve.

marketing_investment_plan
  Defines which spend/activity rows may create reach, traffic, leads, proof, retail visibility, or conversion actions.

baseline_calibration
  Defines baseline sales or velocity before incremental marketing effects.

marketing_response_assumptions
  Defines lag, saturation, conversion basis, promo pull-forward, and confidence caps.

constraints
  Defines whether the model should output unconstrained sell-through potential or supply-constrained shipments.
```

If any block is missing, use the workbook's degradation rules before choosing a curve.

## Product Lifecycle Sales Curve

For launch GTM, use a phase curve rather than a single average-rate assumption:

```text
prelaunch_warmup
  Awareness, waitlist, preorders, reviews, retail readiness, creator seeding.

launch_spike
  Launch event, first retail availability, PR/KOL burst, early adopters, preorder conversion.

early_ramp
  Reviews, word of mouth, marketplace ranking, retargeting, retail display, replenishment.

sustain
  Paid media optimization, promo calendar, channel expansion, creative fatigue management.

plateau_or_decay
  Demand normalizes, competitor response appears, promo dependence or stockout effects surface.
```

Map each phase to unit-sales range, not just demand:

```json
{
  "phase": "prelaunch_warmup | launch_spike | early_ramp | sustain | plateau_or_decay",
  "date_or_week_range": "",
  "baseline_unit_sales_range": {"min": 0, "max": 0},
  "marketing_incremental_unit_sales_range": {"min": 0, "max": 0},
  "total_unit_sales_range": {"min": 0, "max": 0},
  "main_drivers": [],
  "constraints": [],
  "confidence": "high | medium | low | hypothesis_only"
}
```

## Adoption Curve Options

Choose the simplest curve supported by evidence:

```text
phase_multiplier_curve
  Default when data is thin. Apply conservative/base/upside phase multipliers to total launch sales.

S_curve_logistic_or_gompertz
  Use when category adoption or comparable launch curves exist. Good for gradual adoption/ramp.

Bass_diffusion_proxy
  Use only when innovation/imitation assumptions or historical category adoption data exist. Useful for new-category consumer electronics.

cohort_retention_curve
  Use for preorder/waitlist/app-enabled products when cohorts move through signup -> purchase -> activation.
```

Do not fit a complex curve without data. If inputs are weak, keep it as `phase_multiplier_curve`.

## Marketing Investment Response

Separate baseline sales from incremental marketing-driven sales:

```text
total_sales_t =
  baseline_sales_t
+ marketing_incremental_sales_t
+ channel_promo_incremental_sales_t
- cannibalization_or_pull_forward_t
- stockout_lost_sales_t
```

Marketing spend must have diminishing returns:

```text
effective_spend_t = spend_t + adstock_rate * effective_spend_(t-1)

response_index_t =
  max_response * (effective_spend_t ^ shape)
  / (half_saturation ^ shape + effective_spend_t ^ shape)
```

If this is too much for the available data, use a simpler log response:

```text
response_index_t = response_scale * log(1 + effective_spend_t / spend_unit)
```

Never model sales as a linear function of spend unless the user supplies measured response evidence and requests a local linear approximation.

## Spend To Sales Bridge

Build the bridge by channel:

```text
marketing_spend
-> effective_reach_or_clicks
-> qualified_traffic_or_leads
-> conversion_action
-> unit_sales
```

Each bridge must state basis:

```text
measured_internal
platform_estimate
historical_proxy
S06_creator_estimate
S07_conversion_scenario
user_assumption
AI_heuristic
```

## Channel Effects

```text
brand_awareness_spend
  Usually affects awareness and later search/direct/retail demand. Higher lag, lower direct attribution.

performance_spend
  Usually affects traffic and near-term conversion. Faster effect, stronger saturation risk.

retail_media_or_marketplace_spend
  Affects PDP visibility, search rank, promo conversion, and channel sell-through.

creator_or_PR
  Can create launch spike, proof, and search lift. Must not be treated as guaranteed sales.

promo_discount
  Can pull demand forward and reduce later baseline. Record cannibalization or margin caveats, but do not model profit.
```

## Required Caveats

```text
1. Marketing incremental sales require spend, channel mix, response basis, and conversion/action basis.
2. If no response evidence exists, output a sensitivity curve and validation need, not a confident lift.
3. Apply adstock/carryover only when the forecast horizon spans multiple periods.
4. Apply saturation/diminishing returns whenever spend is modeled.
5. Separate incremental sales from shifted/cannibalized sales where promo timing may pull demand forward.
```
