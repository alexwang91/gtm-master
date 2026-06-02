# S08 Forecast Methods

Use these methods after input coverage and before scoring. S08's final object is launch sales forecast; demand potential is only one upstream input.

## Forecast Boundary

Declare which forecast is being produced:

```text
demand_potential
  Local demand that could exist if awareness, supply, and channel access were sufficient.

reachable_launch_demand
  Demand S08 believes the launch plan can reach in the selected horizon.

sell_in
  Units committed or shipped into retail/distribution. Not the same as consumer demand.

sell_through
  Units expected to be purchased by end consumers.

supply_constrained_shipments
  Units capped by launch inventory, allocation, or replenishment limits.
```

Do not mix these in the same KPI.

## Sales Scenario Formula

Use formulas as an assumption scaffold, not as fake precision:

```text
Reachable Launch Unit Sales =
  addressable_segment_pool
* launch_reach_or_channel_availability
* segment_priority_weight
* price_acceptance_factor
* proof_and_trust_readiness_factor
* conversion_or_action_rate_factor
* lifecycle_phase_multiplier
* marketing_response_factor
* timing_and_competition_factor
* supply_or_inventory_cap
```

All factors must be ranges, basis-labeled, and confidence-capped.

When marketing investment is supplied, split sales into:

```text
total_unit_sales =
  baseline_unit_sales
+ marketing_incremental_unit_sales
- pull_forward_or_cannibalization
- stockout_lost_sales
```

Use `lifecycle-marketing-models.md` for phase curves, adstock, saturation, and spend-to-sales bridges.

## Scenario Set

Produce three scenarios:

```json
{
  "scenario": "conservative | base | upside",
  "forecast_horizon": "",
  "unit_range": {"min": 0, "max": 0},
  "basis": [],
  "main_assumptions": [],
  "confidence": "high | medium | low | hypothesis_only",
  "caps_and_confounders": []
}
```

Conservative should reflect proof, price, channel, conversion, supply, or timing friction. Upside must still respect market-size and supply ceilings unless explicitly marked as an alternative assumption.

## Channel Split

Build channel split from:

```text
segment_channel_touchpoint_map
channel_fit_scores
retailer_marketplace_candidates
planned_channel_mix
sell-in commitments or PO signals
DTC conversion bridge if S07 ran
creator traffic bridge if S06 ran
```

Use separate rows for:

```text
DTC / brand site
marketplace
retailer ecommerce
offline retail
distributor / operator / partner
creator affiliate / referral
other local channels
```

Only include channels that exist in the launch plan or local evidence.

## Local Channel Action Priority

When local channel evidence or user channel hypotheses exist, S08 must turn the
forecast channel view into named execution priorities. Do not stop at generic
labels such as `local ecommerce > retail > DTC` when local channel names are
available.

For each named channel, output:

```text
channel name
channel type
priority rank
role in GTM
why priority
segment fit
budget percent or amount seed when marketing budget exists
expected signal range
required asset or proof
owner
tracking or validation method
confidence and data gaps
```

Use S01 retailer/marketplace candidates, S03 message carrier seeds, S04 price
guardrails, S06 creator estimates when available, and the user-provided channel
plan. Treat budget and outcome ranges as planning assumptions, not approved
spend or guaranteed sales.

## Price And Conversion Bridge

Do not double count price risk. Use S04 to adjust price acceptance and S07 to adjust action-rate readiness:

```text
S04 price sensitivity -> price_acceptance_factor
S04 price risk guardrail -> downside cap and proof-before-price requirement
S07 CVR ladder -> conversion_or_action_rate_factor only when basis is explicit
S07 funnel friction -> confidence cap and validation need, not a direct unit multiplier unless user approves
```

## Inventory Risk

Inventory risk should compare scenario sales ranges with inventory or channel allocation:

```text
stockout_risk = demand_range_high > allocated_inventory
overstock_risk = demand_range_low < allocated_inventory * sellthrough_threshold
replenishment_risk = lead_time longer than expected stockout window
```

If inventory data is missing, describe what cannot be known.

## Sensitivity Analysis

Rank drivers by expected forecast movement and uncertainty:

```text
segment size uncertainty
channel availability
price acceptance
conversion/action rate
creator or media reach
proof/trust readiness
competitive pressure
seasonality/timing
inventory cap
retail sell-in vs sell-through ambiguity
```

Use a tornado-style ranked score rather than precise elasticity unless measured data supports elasticity.

## Calibration Hierarchy

Prefer evidence in this order:

```text
1. Approved internal historical launch/sell-through data
2. Retail PO, preorder, waitlist, or channel commitment data
3. Previous-generation same-country performance
4. Comparable product/category benchmark from target country
5. S01/S04/S06/S07 modeled upstream handoffs
6. User-provided hypothesis
7. AI heuristic assumption
```

Record basis for every material number.
