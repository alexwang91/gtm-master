# Opening Price Strategy

Use this reference when S04 must recommend how to open price for a launch, not just whether the target price is credible.

## Core Question

S04 should answer:

```text
What opening price posture should the product use, what transaction mechanism should convert demand, what floor protects economics, and which price path should be tested over the first 30/60/90 days?
```

This is not final price approval. It is a quantified launch price architecture that combines local anchors, product/brand proof, competitor pressure, cost capability, channel rules, and private economics when available.

## Strategy Types

```text
premium_anchor_promo
  Open with a high public anchor, then use controlled promo, bundle, trade-in, financing, or channel subsidy to improve conversion while preserving positioning.

premium_proof_led
  Open high only when product differentiation, proof, brand trust, and channel support can sustain the premium without heavy discounting.

parity_value
  Open near the strongest local anchor, compete on proof, message clarity, and channel execution rather than aggressive discounting.

penetration_attack
  Use price as an active market attack when cost advantage, channel efficiency, volume upside, and strategic share goals justify lower margin or lower ASP.

niche_high_price
  Keep price high when volume is likely limited, competition is weak, proof burden is manageable, and low pricing would damage positioning without unlocking real scale.

test_before_scale
  Use controlled tests before committing because evidence, private economics, or channel constraints are not strong enough.

blocked
  Do not recommend a launch price path until a hard blocker is resolved.
```

## Required Output Fields

```json
{
  "opening_price_strategy": {
    "recommended_strategy": "premium_anchor_promo | premium_proof_led | parity_value | penetration_attack | niche_high_price | test_before_scale | blocked",
    "strategic_objective": "profit | revenue | share | positioning | channel_entry | inventory_velocity | unknown",
    "strategy_scores": [],
    "recommended_public_anchor": "",
    "recommended_transaction_mechanism": "",
    "conditions_required": [],
    "why_this_strategy": "",
    "why_not_other_strategies": [],
    "do_not_do": [],
    "confidence": "high | medium | low | hypothesis_only",
    "evidence_refs": [],
    "data_gaps": []
  }
}
```

## Strategy Scores

Score each factor from 0 to 100. Keep factor-level evidence refs and confidence caps.

### Premium Anchor Score

```text
Premium Anchor Score =
  Product Differentiation * 0.18
+ Brand Trust * 0.14
+ Proof Readiness * 0.14
+ Competitor Scarcity / Weak Substitution * 0.13
+ Low Price Sensitivity * 0.13
+ Channel Premium Support * 0.10
+ Positioning Objective * 0.09
+ Promo Mechanism Readiness * 0.09
```

### Penetration Attack Score

```text
Penetration Attack Score =
  Competitor Pressure * 0.18
+ Cost Advantage * 0.18
+ Price Sensitivity * 0.15
+ Market Volume Potential * 0.14
+ Channel Efficiency * 0.12
+ Product Parity Without Premium Proof Need * 0.10
+ Strategic Share Objective * 0.08
+ Promo / MKT Budget Support * 0.05
```

### Niche High Price Score

```text
Niche High Price Score =
  Low Volume Expectation * 0.16
+ Weak Direct Competition * 0.15
+ Differentiation Or Scarcity * 0.15
+ Manageable Proof Burden * 0.12
+ Positioning Protection Need * 0.12
+ Selective Channel Fit * 0.10
+ Low Elasticity Segment Presence * 0.10
+ Profit Over Volume Objective * 0.10
```

### Parity Value Score

```text
Parity Value Score =
  Local Anchor Fit * 0.18
+ Product Parity Or Slight Advantage * 0.16
+ Medium Price Sensitivity * 0.14
+ Adequate Proof Readiness * 0.13
+ Channel Fit * 0.12
+ Promo Flexibility * 0.10
+ Conversion Objective * 0.09
+ Forecast Confidence * 0.08
```

Strategy score schema:

```json
{
  "strategy_id": "premium_anchor_promo",
  "score_0_100": 0,
  "score_formula": "",
  "factor_scores": [
    {
      "factor_id": "",
      "score_0_100": 0,
      "weight": 0,
      "weighted_score": 0,
      "evidence_level": "direct | strong_proxy | weak_proxy | synthetic_stress_test | missing",
      "source_refs": [],
      "calculation_note": "",
      "confidence_cap": "high | medium | low | hypothesis_only"
    }
  ],
  "classification": "strong_fit | possible | weak_fit | blocked",
  "confidence_cap": "high | medium | low | hypothesis_only",
  "data_gaps": []
}
```

Selection rules:

```text
highest_score_above_70_with_no_hard_blocker
  Recommend the highest scoring strategy if evidence cap supports at least medium confidence.

two_scores_within_5_points
  Recommend a primary strategy and a testable challenger.

premium_anchor_and_penetration_both_high
  Prefer premium_anchor_promo if proof and brand trust are strong. Prefer penetration_attack only when cost advantage and strategic share objective are explicit.

niche_high_price_high_and_volume_uncertain
  Do not recommend low opening price unless price elasticity or channel demand evidence shows scale will unlock.

private_floor_above_transaction_price
  Block penetration or promo-heavy strategy until finance review or derived private summary clears the gap.

proof_readiness_low_and_target_above_local_p75
  Do not recommend premium_proof_led; use premium_anchor_promo with proof tests or test_before_scale.
```

## Launch Price Architecture

S04 should separate public anchor, transaction price, and economic floors.

```json
{
  "launch_price_architecture": {
    "currency": "",
    "public_anchor_price_or_msrp": "",
    "expected_transaction_price_range": "",
    "launch_offer_mechanism": "none | coupon | bundle | gift | trade_in | financing | installment | channel_subsidy | member_price | limited_time_discount | mixed | unknown",
    "promo_floor_price": "",
    "channel_floor_price": "",
    "revenue_max_price": "",
    "profit_max_price": "",
    "local_anchor_context": "",
    "price_ladder_position": "below_anchor | parity | slight_premium | major_premium | flagship | abnormal | unknown",
    "calculation_mode": "public_proxy_only | private_local_calculator | private_uploaded | derived_summary_only | blocked",
    "private_fields_required": [],
    "confidence": "high | medium | low | hypothesis_only",
    "evidence_refs": [],
    "data_gaps": []
  }
}
```

Interpretation:

```text
public_anchor_price_or_msrp
  The visible price that sets positioning and channel reference.

expected_transaction_price_range
  The realistic launch selling range after allowed offer mechanics.

promo_floor_price
  Lowest recommended transaction price before margin, channel, brand, or reference-price damage becomes unacceptable.

channel_floor_price
  Lowest channel-safe price after retailer, marketplace, distributor, tax, financing, or cross-channel constraints.

revenue_max_price
  Price that maximizes modeled revenue under demand assumptions.

profit_max_price
  Price that maximizes modeled contribution profit under private cost and channel assumptions.
```

If private economics are unavailable, output `private_local_calculator` or `derived_summary_only` and leave `revenue_max_price` / `profit_max_price` as not calculated. Do not invent them from public data.

## Profit And Revenue Optimizer

The optimizer belongs in the private local HTML calculator unless the user explicitly shares approved private inputs.

Required local inputs:

```text
cogs_or_bom
msrp_or_candidate_price
discount_or_offer_cost
channel_margin_or_fee
shipping_financing_payment_subsidy
tax_or_vat_treatment
variable_support_warranty_return_cost
base_demand_units
reference_price
own_price_elasticity
mkt_spend
mkt_response_multiplier
channel_availability_multiplier
proof_maturity_multiplier
stock_availability_multiplier
```

Local formulas:

```text
net_transaction_price =
  msrp_or_candidate_price
  - discount_or_offer_cost
  - channel_margin_or_fee
  - shipping_financing_payment_subsidy
  - tax_or_vat_amount_when_accounted_from_price

price_index =
  net_transaction_price / reference_price

estimated_units =
  base_demand_units
* POWER(price_index, own_price_elasticity)
* mkt_response_multiplier
* channel_availability_multiplier
* proof_maturity_multiplier
* stock_availability_multiplier

revenue =
  net_transaction_price * estimated_units

unit_contribution =
  net_transaction_price
  - cogs_or_bom
  - variable_support_warranty_return_cost

contribution_profit =
  unit_contribution * estimated_units - mkt_spend
```

Optimization:

```text
candidate_price_grid
  Evaluate 20-50 candidate prices between floor price and premium anchor.

revenue_max_price
  Candidate price with highest revenue.

profit_max_price
  Candidate price with highest contribution_profit.

guardrail
  Never show optimizer output as finance-approved unless private constraints were provided, checked, and approved.
```

## 30/60/90 Price Path

```json
{
  "price_path_30_60_90": [
    {
      "phase": "day_0_30 | day_31_60 | day_61_90",
      "price_posture": "",
      "offer_mechanism": "",
      "decision_trigger": "",
      "watch_metrics": [],
      "guardrails": [],
      "allowed_moves": [],
      "forbidden_moves": [],
      "owner_hint": "pricing | marketing | channel | finance | sales | product",
      "confidence": "high | medium | low | hypothesis_only"
    }
  ]
}
```

Path rules:

```text
premium_anchor_promo
  Start with high public anchor and controlled offer. Do not use naked price cuts early.

penetration_attack
  Start with clear lower transaction price only if private floor and channel rules support it.

niche_high_price
  Preserve high price, focus proof and selective channels, and avoid broad discounting unless demand evidence changes.

test_before_scale
  Use controlled cells or limited channel tests before national rollout.
```

## Common Mistakes

```text
confusing MSRP with transaction price
  Always separate public anchor and expected transaction price.

using public evidence for profit optimum
  Profit maximum requires private or user-approved derived cost/channel inputs.

over-discounting scarce or cold products
  Low price does not create demand if awareness, proof, or channel access is the blocker.

choosing premium without proof
  High anchor needs proof, risk reversal, channel confidence, and a controlled offer path.

ignoring channel conflict
  A price path that breaks retailer, DTC, or marketplace rules is not executable.
```
