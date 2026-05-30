# Consumer Electronics GTM Methods

Use this when S02 turns JTBD scenarios into consumer-electronics-ready GTM inputs. These methods do not create final copy or final channel strategy; they translate demand scenarios into proof, channel, retail, pricing, and post-purchase implications for downstream skills.

Reference concepts:

- Consumer decision journey: consumers actively evaluate, add/remove brands, and keep evaluating after purchase.
- Messy Middle: between trigger and purchase, consumers loop between exploration and evaluation rather than moving through a linear funnel.
- ZMOT/search moments: consumers ask online questions before purchase; winning requires showing up with relevant answers at the moment of need.
- Omnichannel electronics shopping: consumers compare products, retailers, prices, delivery, reviews, video proof, and in-store availability across online and offline touchpoints.
- Behavioral science levers: social proof, authority bias, category heuristics, power of free, delivery friction reduction, and price/promotion can reduce decision anxiety.

## Consumer Electronics Moment Map

Map every lead JTBD scenario to the consumer electronics buying and ownership journey.

```json
{
  "consumer_electronics_gtm_moment_map": [
    {
      "scenario_id": "",
      "moment": "trigger | exploration | evaluation | comparison | proof_trust | retailer_selection | purchase | delivery_unboxing | setup_activation | first_use | habit_formation | support_return | advocacy_repeat",
      "consumer_question": "",
      "dominant_anxiety": "",
      "needed_content_or_proof": [],
      "primary_touchpoints": [],
      "channel_or_retail_implication": "",
      "owner_hint": "product | marketing | sales | retail | ecommerce | support | channel | unknown",
      "evidence_refs": [],
      "confidence": "high | medium | low"
    }
  ]
}
```

Moment rules:

- `exploration` needs category education, use-case framing, search visibility, and plain-language capability explanation.
- `evaluation` needs specs, comparisons, reviews, expert proof, product demos, and price-value clarity.
- `retailer_selection` needs availability, delivery, return policy, warranty, retailer trust, payment, promo, and service confidence.
- `setup_activation` needs onboarding proof, app pairing clarity, compatibility, data/privacy explanation, and return-risk reduction.
- `advocacy_repeat` needs promoter drivers, referral reasons, earned growth signals, and post-purchase satisfaction loops.

## Product-Job Fit Matrix

Use S01 product capability fields to check whether the product can credibly satisfy a scenario.

Inputs from S01:

```text
product_capability_map
category_selling_point_map
selling_point_fit_scores
hardware_experience_diagnosis_seed
value_proof_requirement_matrix
```

Output:

```json
{
  "product_job_fit_matrix": [
    {
      "scenario_id": "",
      "job_need": "",
      "product_capability_refs": [],
      "mainstream_category_expectation": "",
      "differentiation_angle": "",
      "capability_gap": "",
      "proof_needed": [],
      "product_job_fit_score": 0,
      "confidence": "high | medium | low",
      "evidence_refs": []
    }
  ]
}
```

Rules:

- Do not recommend leading with a scenario where product-job fit is weak unless it is explicitly a validation hypothesis.
- If a feature is technically present but consumers cannot understand or trust it, mark proof or education gap.
- If the job depends on app, setup, firmware, compatibility, warranty, or service, include the operational dependency.

## Digital Shelf And Retailer Decision Map

Consumer electronics buyers often choose both product and seller. Map scenario needs to product visibility and retailer/channel confidence.

```json
{
  "digital_shelf_and_retailer_decision_map": [
    {
      "scenario_id": "",
      "product_visibility_need": "",
      "retailer_or_marketplace_decision_factors": [],
      "availability_delivery_return_factors": [],
      "price_promo_or_bundle_factors": [],
      "trust_signals_needed": [],
      "channel_refs": [],
      "risk_if_missing": "",
      "handoff_to": ["S03", "S04", "S07", "S14"],
      "confidence": "high | medium | low"
    }
  ]
}
```

Include search/shopping visibility, marketplace listing clarity, stock confidence, delivery speed, pickup, free returns, warranty, payment/installment options, retail sales objection handling, price comparison, and bundle framing.

## Behavioral Science Lever Map

Use behavioral science levers as proof and friction-reduction hypotheses, not manipulation or final creative.

```json
{
  "behavioral_science_lever_map": [
    {
      "scenario_id": "",
      "lever": "social_proof | authority_bias | category_heuristic | power_of_free | delivery_friction_reduction | scarcity | price_promotion | risk_reversal | default_or_bundle | other",
      "why_this_lever_fits": "",
      "required_asset_or_offer": "",
      "risk_or_constraint": "",
      "evidence_refs": [],
      "confidence": "high | medium | low",
      "handoff_to": ["S03", "S04", "S05", "S07"]
    }
  ]
}
```

Lever rules:

- `social_proof`: use ratings, review themes, user stories, community comments, or NSS/NPS promoter drivers.
- `authority_bias`: use expert reviews, creator reviews, certifications, awards, retailer recommendations, or lab tests.
- `category_heuristic`: reduce complexity with clear key specs, "best for" use cases, comparison anchors, and simple compatibility notes.
- `power_of_free`: use accessories, extended service, trial, free shipping, setup help, or bundle extras only when commercially feasible.
- `delivery_friction_reduction`: use fast delivery, pickup, free returns, local warranty, payment options, and reliable seller information.
- `risk_reversal`: use warranty, return policy, trial period, support promise, privacy/security proof, or compatibility guarantee.

## Scenario Commercial Weight Map

Use market and business signals to avoid over-prioritizing interesting but small scenarios.

Inputs from S01:

```text
segment_priority_ranking
segment_level_tam_sam_som
market_sizing_confidence
initial_gtm_priorities
channel_fit_scores
price_anchor_panel
segment_price_sensitivity_seeds
earned_growth_proxy_seed
```

Output:

```json
{
  "scenario_commercial_weight_map": [
    {
      "scenario_id": "",
      "segment_value_signal": "",
      "market_size_or_reach_signal": "",
      "price_value_signal": "",
      "channel_reach_signal": "",
      "repeat_or_advocacy_signal": "",
      "strategic_priority_signal": "",
      "commercial_weight_score": 0,
      "confidence": "high | medium | low",
      "data_gaps": []
    }
  ]
}
```

Rules:

- A scenario can be emotionally intense but commercially secondary if reach, WTP, channel, or product fit is weak.
- A weak public signal can remain as a strategic hypothesis if the user provides internal commercial rationale.
- Do not convert market-size proxies into precise demand.

## Brand And Claim Constraint Map

Use project brief and optional private inputs to prevent downstream message claims that the product, brand, or legal context cannot support.

```json
{
  "brand_claim_constraint_map": [
    {
      "constraint_id": "",
      "scenario_refs": [],
      "constraint_type": "brand_tone | proof_gap | compliance | health_safety | privacy | accuracy | battery | sustainability | child_elderly | warranty_service | retailer_policy | other",
      "constraint": "",
      "impact_on_scenario": "",
      "claim_to_avoid": "",
      "safe_direction_seed": "",
      "owner_hint": "brand | legal | product | marketing | support | sales | unknown",
      "evidence_refs": [],
      "confidence": "high | medium | low"
    }
  ]
}
```

Rules:

- S02 may flag a message direction as risky but should not finalize compliant copy.
- Accuracy, health, privacy, battery, safety, children, elderly, and regulated-adjacent claims should be passed to S03/S15 with constraints.
- Brand tone can preserve or reject a scenario framing, but it should not override evidence without marking a decision update.

## GTM Theory To S02 Translation

Use this mapping:

```text
Consumer decision journey
  -> scenario_to_journey_matrix and post-purchase/advocacy signals.

Messy Middle exploration/evaluation
  -> consumer_electronics_gtm_moment_map, proof_requirement_seed, behavioral_science_lever_map.

ZMOT/search moments
  -> local_language_trigger_phrase_map and scenario_message_seed.

Digital shelf / omnichannel retail
  -> digital_shelf_and_retailer_decision_map and channel touchpoint handoff.

Behavioral science value levers
  -> proof requirements, risk reversal, authority/social proof/category heuristics, and S03/S04/S05/S07 handoffs.

Product-led post-purchase feedback
  -> anti-JTBD risks, setup/activation risks, earned-growth signals, and S12 feedback loop seeds.
```
