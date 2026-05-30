# Price Anchor and Sensitivity Seed

Use this after price intelligence, competitor/substitute mapping, consumer voice processing, segment inference, and channel/touchpoint mapping. It creates the S01 price evidence layer for downstream pricing work.

S01 does not make the final pricing decision. It builds a structured price context: local price corridor, competitor price gaps, price ladder jump risks, affordability pressure, price objections, value proof requirements, promotion/subscription sensitivity, and segment-level price sensitivity seeds.

## Inputs

```json
{
  "target_price_range": "",
  "launch_country_or_region": "",
  "product_capability_map": {},
  "selling_point_fit_scores": [],
  "competitor_substitute_map": [],
  "competitor_threat_scores": [],
  "price_ladder_scan": [],
  "jump_decision_risks": [],
  "voice_theme_clusters": [],
  "price_complaints": [],
  "segment_seed_pack": [],
  "segment_channel_touchpoint_map": [],
  "retailer_marketplace_candidates": [],
  "localization_preflight": {},
  "previous_generation_sales_price_channel_performance": "",
  "user_provided_price_constraints": ""
}
```

## Core Rules

- Treat the user's target price as a hypothesis to test against local anchors.
- Do not infer exact willingness to pay from search interest or social buzz.
- Do not present S01 price sensitivity as a final pricing model.
- Separate local evidence from user-provided internal pricing assumptions.
- Keep price display context explicit: currency, VAT/sales tax, shipping, financing, installment, subscription, bundles, warranty, and promo norms.
- Include cross-price-tier alternatives because consumers may trade up, trade down, switch laterally, delay purchase, or buy nothing.
- Every price conclusion needs evidence refs or a data gap.

## Local Price Corridor

```json
{
  "local_price_corridor": {
    "currency": "",
    "price_display_context": {
      "vat_or_sales_tax_display": "included | excluded | mixed | unknown",
      "shipping_cost_visibility": "included | separate | mixed | unknown",
      "installment_or_financing_norms": [],
      "subscription_or_recurring_cost_norms": [],
      "bundle_or_promo_norms": []
    },
    "entry_price_band": "",
    "mainstream_price_band": "",
    "premium_price_band": "",
    "flagship_price_band": "",
    "previous_generation_or_refurbished_band": "",
    "promo_floor": "",
    "typical_discount_range": "",
    "our_target_price_classification": "budget | entry | mainstream | premium | flagship | price_abnormal | unknown",
    "confidence": "high | medium | low",
    "evidence_refs": [],
    "data_gaps": []
  }
}
```

## Price Anchor Panel

```json
{
  "price_anchor_panel": {
    "our_target_price_range": "",
    "anchors": [
      {
        "anchor_id": "",
        "brand": "",
        "product": "",
        "anchor_role": "direct_competitor | substitute | premium_anchor | budget_anchor | ecosystem_anchor | previous_generation | used_refurbished | non_consumption",
        "local_price": "",
        "sale_or_promo_price": "",
        "recurring_cost": "",
        "channel_or_retailer": "",
        "price_tier": "budget | entry | mainstream | premium | flagship | previous_generation | used_refurbished | non_consumption | unknown",
        "consumer_interpretation": "cheaper | comparable | slightly_premium | too_expensive | worth_premium | unclear",
        "evidence_refs": [],
        "confidence": "high | medium | low"
      }
    ],
    "anchor_summary": "",
    "confidence": "high | medium | low"
  }
}
```

## Competitor Price Gap Table

```text
Price Gap % = (Our Price - Competitor Price) / Competitor Price
```

```json
{
  "competitor_price_gap_table": [
    {
      "competitor_or_substitute_ref": "",
      "competitor_name": "",
      "anchor_role": "",
      "local_price": "",
      "our_price_assumption": "",
      "price_gap_pct": 0,
      "price_gap_interpretation": "discount | parity | slight_premium | major_premium | unclear",
      "consumer_risk": "low | medium | high",
      "required_value_proof": [],
      "evidence_refs": [],
      "confidence": "high | medium | low"
    }
  ]
}
```

Interpretation guide:

```text
10%+ below mainstream anchors
  Can test value-for-money, but watch quality/trust risk.

Within +/-10%
  Parity zone. Differentiation and trust proof must be clear.

10-30% above
  Premium justification required.

30%+ above
  Premium or flagship positioning only if proof, brand trust, and segment willingness support it.
```

## Segment Price Sensitivity Seed

```text
Price Sensitivity Seed Score =
  Affordability Pressure * 0.18
+ Competitor Price Gap Pressure * 0.16
+ Price Complaint Intensity * 0.15
+ Price Ladder Pull * 0.12
+ Promotion Dependence * 0.10
+ Subscription / Ongoing Cost Resistance * 0.10
+ Low Differentiation Risk * 0.08
+ Trust Deficit * 0.07
+ Channel Price Transparency * 0.04
```

```json
{
  "segment_price_sensitivity_seeds": [
    {
      "segment_id": "",
      "segment_name": "",
      "price_sensitivity_seed_score": 0,
      "price_sensitivity_level": "low | medium | high | very_high",
      "score_breakdown": {
        "affordability_pressure": 0,
        "competitor_price_gap_pressure": 0,
        "price_complaint_intensity": 0,
        "price_ladder_pull": 0,
        "promotion_dependence": 0,
        "subscription_or_ongoing_cost_resistance": 0,
        "low_differentiation_risk": 0,
        "trust_deficit": 0,
        "channel_price_transparency": 0
      },
      "acceptable_price_hypothesis": "",
      "premium_justification_needed": [],
      "discount_or_bundle_hypothesis": "",
      "confidence": "high | medium | low",
      "evidence_refs": [],
      "data_gaps": []
    }
  ]
}
```

Interpretation:

```text
0-30   = low sensitivity
31-55  = medium sensitivity
56-75  = high sensitivity
76-100 = very high sensitivity
```

## Value Proof Requirement Matrix

```json
{
  "value_proof_requirement_matrix": [
    {
      "segment_id": "",
      "price_position": "below_anchor | parity | slight_premium | major_premium | unclear",
      "proof_required": [],
      "proof_source_candidates": [],
      "claim_or_compliance_risks": [],
      "best_touchpoints_for_proof": [],
      "evidence_refs": [],
      "confidence": "high | medium | low"
    }
  ]
}
```

Proof types may include:

```text
feature proof
accuracy or performance proof
durability proof
comfort/design proof
app or AI insight proof
warranty/return proof
privacy/security proof
expert review proof
verified buyer proof
previous-generation proof
brand trust proof
local-language support proof
```

## Promotion And Subscription Sensitivity Seed

```json
{
  "promotion_subscription_sensitivity_seed": [
    {
      "segment_id": "",
      "promotion_dependence": "low | medium | high | unknown",
      "subscription_tolerance": "low | medium | high | not_applicable | unknown",
      "financing_or_installment_relevance": "low | medium | high | unknown",
      "bundle_relevance": "low | medium | high | unknown",
      "recommended_test_hypotheses": [],
      "risks": [],
      "evidence_refs": [],
      "confidence": "high | medium | low"
    }
  ]
}
```

## User-Provided Price Assumptions

If the user provides target price, margin constraints, channel price rules, previous-generation price results, discount history, or internal price beliefs:

- Store them as `user_provided_price_hypothesis` or `internal_private`.
- Compare against local price corridor and competitor anchors.
- Preserve unsupported but commercially required prices as test hypotheses with proof requirements.
- Do not present internal target price as locally validated unless local evidence supports it.
- Do not expose private margin or channel terms in public report sections unless approved.

## S04 Handoff

Downstream S04 should receive:

- `local_price_corridor`
- `price_anchor_panel`
- `competitor_price_gap_table`
- `segment_price_sensitivity_seeds`
- `value_proof_requirement_matrix`
- `promotion_subscription_sensitivity_seed`
- `price_ladder_scan`
- `jump_decision_risks`
- `price_complaints`
- `user_provided_price_hypotheses`
- confidence caps and data gaps

S04 owns final pricing strategy, willingness-to-pay research design, Van Westendorp/Gabor-Granger/conjoint planning, elasticity modeling, and final promotion guidance.
