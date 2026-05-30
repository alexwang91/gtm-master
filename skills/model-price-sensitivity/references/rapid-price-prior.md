# Rapid Price Prior

Use this reference when the user has no time, budget, or access to run a real price study before S04, but still needs a quantitative, reviewable pricing prior for a country launch.

## Principle

Rapid Price Prior is a hypothesis generator, not measured WTP. It creates an auditable prior from local price anchors, purchasing power, product competitiveness, brand/channel trust, proof readiness, demand proxies, and sales/review velocity proxies. S13 must then convert weak factors into calibration tests.

Never let synthetic personas, AI role-play, social buzz, search volume, or review counts raise confidence above the evidence cap they deserve. They can shape hypotheses and wording; they cannot prove willingness to pay.

## Two-Step Output

```text
1. Rapid WTP Prior
   Quantify where the target price appears supportable, risky, or unsupported before real research.

2. Calibration Plan
   Identify the smallest validation action that would upgrade or falsify the prior.
```

## Required Output Fields

```json
{
  "rapid_price_prior": {
    "status": "not_applicable | generated | generated_with_gaps | blocked",
    "target_price_or_band": "",
    "local_currency": "",
    "wtp_prior_range": {},
    "rapid_wtp_prior_score": 0,
    "pricing_classification": "price_supported_with_caveats | test_before_scale | research_first | price_not_supported_current_evidence | blocked",
    "factor_scores": [],
    "evidence_grade": "A | B | C | D | E",
    "confidence_cap": "high | medium | low | hypothesis_only",
    "calibration_plan": [],
    "limits": [],
    "evidence_refs": [],
    "data_gaps": []
  }
}
```

## Rapid WTP Prior Score

Score every factor from 0 to 100. Weights must sum to 1.00. Keep the factor-level trace so a human can challenge each input.

```text
Rapid WTP Prior Score =
  Local Price Anchor Fit * 0.22
+ Purchasing Power Fit * 0.18
+ Product Competitiveness Fit * 0.17
+ Brand / Channel Trust Proxy * 0.13
+ Proof Readiness * 0.12
+ Demand Proxy Strength * 0.10
+ Sales / Review Velocity Proxy * 0.08
```

Factor schema:

```json
{
  "factor_id": "local_price_anchor_fit",
  "definition": "",
  "score_0_100": 0,
  "weight": 0.22,
  "weighted_score": 0,
  "evidence_level": "direct | strong_proxy | weak_proxy | synthetic_stress_test | missing",
  "source_refs": [],
  "calculation_note": "",
  "confidence_cap": "high | medium | low | hypothesis_only",
  "data_gaps": []
}
```

Factor definitions:

```text
local_price_anchor_fit
  How normal the target price looks versus local competitor, substitute, and retailer anchors.

purchasing_power_fit
  Whether the price is plausible after country income, PPP, disposable consumption, tax, and financing context.

product_competitiveness_fit
  Whether product features, proof, design, compatibility, and service make the price gap defensible.

brand_channel_trust_proxy
  Whether brand trust and planned channels can reduce perceived purchase risk.

proof_readiness
  Whether claims needed to justify the price are substantiated by specs, reviews, demos, certifications, warranties, or credible third parties.

demand_proxy_strength
  Whether local search, trend, category interest, retailer rankings, forum/review volume, and adjacent demand point in the same direction.

sales_review_velocity_proxy
  Whether internal prior-generation data, public review velocity, sell-through proxy, or retailer rank suggests the category/brand can move at this price.
```

## Classification

```text
75-100 = price_supported_with_caveats
55-74  = test_before_scale
35-54  = research_first
0-34   = price_not_supported_current_evidence
```

Override rules:

```text
no_local_price_anchors
  Cannot exceed research_first.

synthetic_only
  Cannot exceed hypothesis_only confidence and cannot exceed research_first classification.

public_proxy_only
  Cannot exceed medium confidence.

missing_private_margin_or_channel_terms
  Cannot exceed finance_review or controlled_test_ready in pricing_decision_gate.

target_price_above_local_p75_without_strong_proof
  Cannot exceed test_before_scale.

no_demand_proxy_and_no_internal_sales_proxy
  Cannot exceed low confidence.
```

## WTP Prior Range

Use local anchors before abstract income math. If there are no local anchors, do not create a precise range; output a broad hypothesis and a data gap.

```text
low_prior =
  local_anchor_p25
* purchasing_power_multiplier
* proof_discount
* channel_risk_discount

base_prior =
  local_anchor_median
* product_value_multiplier
* brand_channel_multiplier
* purchasing_power_multiplier
* proof_discount

high_prior =
  local_anchor_p75
* product_value_multiplier
* brand_channel_multiplier
* proof_premium_multiplier
```

Multiplier guidance:

```text
purchasing_power_multiplier
  0.80-1.20 based on target country income, PPP, consumption context, and category affordability.

product_value_multiplier
  0.85-1.25 based on differentiated features, JTBD fit, design, durability, ecosystem, service, and warranty.

brand_channel_multiplier
  0.85-1.20 based on brand trust, local channel credibility, retailer trust, financing, and return support.

proof_discount
  0.80-1.00. Apply stronger discount when premium claims lack proof.

proof_premium_multiplier
  1.00-1.15. Use only when proof readiness is strong.

channel_risk_discount
  0.85-1.00. Apply when channel norms, shipping, returns, tax, or price transparency may hurt conversion.
```

Every multiplier must have a source ref, assumption note, and confidence cap. If the calculation uses a proxy instead of direct evidence, label the range as `hypothesis_prior_range`.

## Evidence Grade And Confidence Cap

```text
A
  Direct WTP or sales evidence plus local anchors and private constraints. Confidence cap can be high.

B
  Strong local anchors plus internal previous-generation data or reliable retailer/channel proxy. Confidence cap can be medium or high depending on quality.

C
  Public anchors plus several consistent proxies. Confidence cap is medium.

D
  Sparse public anchors or conflicting proxies. Confidence cap is low.

E
  Synthetic, generic, or missing evidence. Confidence cap is hypothesis_only.
```

Confidence cap rules:

```text
direct_survey_or_sales_missing
  Cap at medium unless other direct internal evidence exists.

local_anchor_missing
  Cap at low and mark no_precise_wtp_range.

synthetic_persona_used
  Cap synthetic factor at hypothesis_only; do not let it raise total confidence.

uncontrolled_ad_or_click_data
  Treat as weak_proxy unless randomized, matched, and quality-checked.

review_volume_without_sales_or_rank
  Treat as weak_proxy; useful for objections and proof, not price volume.

private_constraints_missing
  Pricing decision can move to testing or forecast caveat, not final approval.
```

## Calibration Plan

Each weak or high-impact factor must map to a calibration action for S13. Select the smallest test that can change the decision.

```json
{
  "calibration_plan": [
    {
      "calibration_id": "",
      "weak_factor": "",
      "decision_unlocked": "price_posture | price_band | promo_need | channel_priority | forecast_input | finance_review | launch_go_no_go",
      "recommended_method": "targeted_anchor_collection | van_westendorp | gabor_granger | conjoint_dce | landing_page_price_ab | retailer_pdp_or_offer_test | keyword_or_ad_smoke_test | internal_sales_analysis | channel_partner_interview",
      "minimum_sample_or_data": "",
      "pass_rule": "",
      "fail_rule": "",
      "update_rule": "",
      "owner_hint": "pricing | marketing | channel | finance | sales | product | research",
      "budget_or_effort_band": "low | medium | high",
      "evidence_upgrade_if_pass": "medium | high",
      "limits": []
    }
  ]
}
```

Calibration selection:

```text
weak local anchors
  Run targeted anchor collection across local ecommerce, retailer, marketplace, and price-comparison sources.

weak WTP
  Use Van Westendorp for acceptable range or Gabor-Granger for fixed candidate price points.

weak feature-price tradeoff
  Use conjoint/DCE only when feature, bundle, warranty, service, or subscription tradeoff matters enough.

weak proof readiness
  Run landing-page or PDP proof/price A/B with matched traffic if available.

weak channel confidence
  Run channel partner interview, retailer PDP pilot, or controlled offer test.

weak demand proxy
  Run keyword/ad smoke test with clear quality checks; do not call clicks sales.

weak internal comparability
  Analyze previous-generation sell-in, sell-through, promo, return, and channel data as private evidence.
```

## HTML Rendering Implication

S04 should render the prior as a compact scorecard plus factor bar/table, not as a final price decision. Show:

```text
1. Rapid WTP Prior Score and classification
2. Prior range with local anchor basis
3. Factor scores and weights
4. Evidence grade and confidence cap
5. Top 2-4 calibration actions for S13
6. Clear caveat when no real WTP, sales, or private economics are available
```

## Common Failure Modes

```text
fake_precision
  Do not output exact WTP when only proxies exist.

evidence_mixing
  Do not merge survey intent, clicks, reviews, and sales into one certainty score without evidence levels.

synthetic_inflation
  Do not let AI personas improve WTP confidence.

income_only_pricing
  Country income can adjust affordability, but local anchors should carry the price range.

unsupported_premium
  A high target price without proof readiness must trigger calibration, not a confident recommendation.
```
