# Pricing Decision Gate

Use this after S04 has built opening price strategy, launch price architecture, price credibility, WTP hypotheses, sensitivity, proof requirements, test plans or test results, and private calculator/optimizer specs or user-approved derived summaries.

The gate does not approve a final company price. It tells the GTM workflow what the pricing decision is ready for next.

## Gate Inputs

```text
market_evidence
  local_price_credibility_model, price_anchor_panel, competitor_price_gap_table, price_ladder_scan

opening_strategy
  opening_price_strategy, launch_price_architecture, price_path_30_60_90

consumer_evidence
  segment_wtp_hypothesis, price_sensitivity_model, price complaints, survey/test results when available

proof_and_message
  price_value_proof_matrix, price_message_seed, objection_matrix, claim_risk_and_proof_gate

commercial_constraints
  private_pricing_calculator_spec, private_profit_revenue_optimizer_spec, user-approved derived summaries, COGS/margin/channel/promo/demand/elasticity constraints when explicitly provided

channel_and_promo
  promo_subscription_guidance, channel_margin_guardrail, retail_price_integrity_map, promo_test_plan

validation
  wtp_test_plan, pricing_test_execution_kit, pricing_test_result_interpretation
```

## Gate Status

```text
blocked
  Missing local anchors, target price, product/category basics, or severe contradictions make pricing analysis unusable.

research_first
  Price hypotheses exist but WTP, proof, channel, or local anchor evidence is too weak for a live test.

controlled_test_ready
  Evidence is sufficient to run survey, landing-page, marketplace, retail, or internal-data tests, but not enough for forecast or decision review.

finance_review
  Market and consumer evidence are plausible, but COGS, margin, fees, promo, tax, or channel economics are missing or unresolved.

channel_review
  Price may work economically, but retailer terms, MAP/MSRP, cross-channel conflict, regional leakage, stock, or promo integrity needs review.

forecast_ready
  Price posture has enough evidence and guardrails for S08 to model demand scenarios, but still may not be final approved price.

decision_review_ready
  Strong evidence, proof, commercial constraints, and channel guardrails exist. Route to human pricing decision review.
```

## Hard Blockers

Any hard blocker should cap status at the named level.

```text
no_local_price_anchors
  Cap at blocked or research_first.

no_target_price_or_band
  Cap at research_first unless S04 is only designing a research test.

no_segment_or_jtbd_context
  Cap at research_first.

proof_gap_for_premium
  Cap at controlled_test_ready for premium pricing until proof is added or tested.

missing_private_margin_constraints
  Cap at finance_review or controlled_test_ready; never decision_review_ready.

missing_private_optimizer_inputs_for_profit_or_revenue_max
  Revenue-max and profit-max claims cannot exceed finance_review, forecast_ready with caveats, or controlled_test_ready.

channel_conflict_unresolved
  Cap at channel_review.

test_results_low_quality
  Cap at controlled_test_ready or research_first.

margin_fail_after_private_calculation
  Cap at finance_review or blocked unless user requests loss-leader strategy.

legal_or_policy_risk
  Cap at blocked until reviewed.
```

## Option Taxonomy

Every gate should produce 2-5 candidate options when enough evidence exists. Options may be price bands instead of exact prices.

```text
hold_target_price
  Keep current target price or band. Requires local credibility, proof, and no major margin/channel blocker.

lower_to_parity
  Move toward category parity or mainstream anchor. Use when premium proof or WTP support is weak.

premium_with_proof
  Keep or raise premium posture only with specific proof, bundle, warranty, demo, review, creator, certification, or retail education support.

launch_offer
  Use temporary launch discount, coupon, gift, bundle, free shipping, warranty extension, or trade-in while protecting reference price.

premium_anchor_promo
  Use high public anchor plus controlled transaction mechanism. Requires proof plan, promo floor, channel floor, and do-not-discount guardrails.

penetration_attack
  Use lower transaction price to attack market. Requires cost advantage, channel support, and explicit share or revenue objective.

niche_high_price
  Preserve high price when demand is cold, competition is weak, and discounting would damage positioning without unlocking volume.

installment_or_financing
  Reduce affordability friction without lowering MSRP when local financing behavior supports it.

bundle_or_tier
  Change value architecture instead of simple price cut: bundle, accessory, warranty, service, good/better/best tiers.

test_before_decision
  Do not choose price yet; run specified survey, landing-page, ad, retail, or internal data test.

avoid_or_rework
  Current price/offer is not credible, not profitable, or creates unacceptable channel/brand risk.
```

## Decision Rules

```text
if price_credibility >= 75 and wtp_confidence >= 65 and pricing_readiness >= 75 and no hard blockers:
  status = decision_review_ready

if price_credibility >= 60 and pricing_readiness >= 55 and test plan is clear:
  status = controlled_test_ready

if market/consumer evidence is plausible but private economics are missing:
  status = finance_review

if channel conflict, retailer terms, MAP/MSRP, regional leakage, or promo integrity is unresolved:
  status = channel_review

if price sensitivity is high and proof readiness is weak:
  status = research_first or controlled_test_ready depending on evidence quality

if test results are strong but margin or channel fails:
  status = finance_review or channel_review, not decision_review_ready

if evidence is weak, noisy, or synthetic-only:
  status = research_first
```

## Output Schema

```json
{
  "pricing_decision_gate": {
    "status": "blocked | research_first | controlled_test_ready | finance_review | channel_review | forecast_ready | decision_review_ready",
    "status_reason": "",
    "readiness_scores": {
      "price_credibility_score": 0,
      "price_sensitivity_score": 0,
      "wtp_confidence_score": 0,
      "opening_strategy_score": 0,
      "pricing_readiness_score": 0,
      "promo_risk_score": 0
    },
    "hard_blockers": [],
    "soft_risks": [],
    "candidate_options": [
      {
        "option_id": "",
        "option_type": "hold_target_price | lower_to_parity | premium_with_proof | premium_anchor_promo | penetration_attack | niche_high_price | launch_offer | installment_or_financing | bundle_or_tier | test_before_decision | avoid_or_rework",
        "price_or_band": "",
        "conditions_required": [],
        "evidence_support": [],
        "main_risks": [],
        "next_step": "research_first | controlled_test | finance_review | channel_review | forecast_scenario | human_decision_review | avoid",
        "confidence": "high | medium | low"
      }
    ],
    "recommended_path": {
      "primary_option_id": "",
      "why": "",
      "must_not_do": [],
      "next_owner": "pricing | finance | channel | marketing | sales | product | research | unknown"
    },
    "downstream_readiness": {
      "s07_conversion": "ready | ready_with_caveats | not_ready",
      "s08_forecast": "ready | ready_with_caveats | not_ready",
      "s13_validation": "ready | ready_with_caveats | not_ready",
      "s14_html": "ready | ready_with_caveats | not_ready"
    },
    "data_gaps": []
  }
}
```
