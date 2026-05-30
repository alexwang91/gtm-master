# Pricing Test Design

Use this when S04 needs to design research rather than pretend public evidence can produce exact willingness to pay.

## AI Persona Simulation Policy

Do not use AI personas, synthetic respondents, or simulated local consumers as evidence of willingness to pay. A 100-person AI simulation can help draft hypotheses, identify possible objections, localize language, pressure-test survey wording, and check whether a concept stimulus is confusing. It cannot estimate real demand, real WTP, or final price.

When AI simulation is used, label it:

```json
{
  "source_type": "synthetic_hypothesis_generation",
  "allowed_use": [
    "hypothesis_generation",
    "survey_pretest",
    "local_wording_variants",
    "objection_discovery"
  ],
  "prohibited_use": [
    "wtp_evidence",
    "demand_forecast",
    "final_price_decision"
  ],
  "confidence_cap": "hypothesis_only"
}
```

## Real Test Modes

Use one or more of these when the pricing decision needs stronger evidence:

```text
survey_panel
  Recruit screened respondents in the target country and target segments. Use Van Westendorp for acceptable price range, Gabor-Granger for candidate price points, and conjoint/DCE for feature/price/bundle tradeoffs.

landing_page_or_ad_test
  Show real users localized product stimuli and candidate prices. Measure click, add-to-cart, checkout start, conversion, email signup, and price objection signals. Use carefully when legal, brand, channel, or price-discrimination risk exists.

marketplace_or_retail_test
  Test controlled offers, bundles, coupons, or retail/channel placements where the company can avoid channel conflict and preserve price integrity.

previous_generation_or_internal_sales_analysis
  Use historical sell-through, promo depth, returns, channel mix, and price changes to seed elasticity assumptions and guardrails.

qualitative_interview_or_sales_objection_test
  Use to understand why a price feels acceptable or unacceptable. Do not treat small qualitative samples as a numeric demand curve.
```

## What The Skill Can Do

S04 can create a practical pricing test kit. It cannot recruit real respondents, force marketplaces to run tests, or convert synthetic personas into real WTP evidence.

```json
{
  "pricing_test_execution_kit": {
    "recommended_execution_level": "hypothesis_only | survey_panel | landing_page_test | marketplace_or_retail_test | internal_data_analysis | mixed",
    "respondent_screener": [],
    "stimulus_brief": [],
    "localized_question_blocks": [],
    "candidate_price_points": [],
    "ad_ab_price_test_plan": {},
    "retail_channel_price_test_plan": {},
    "survey_platform_notes": [],
    "panel_recruitment_brief": [],
    "csv_result_schema": [],
    "quality_checks": [],
    "analysis_plan": [],
    "decision_rules": [],
    "handoff_to_s13": [],
    "limits": []
  }
}
```

Use these execution levels:

```text
hypothesis_only
  Use when there is no budget, no panel, and no traffic. Output objections, local wording, and survey drafts only. Confidence remains hypothesis_only.

survey_panel
  Output screener, localized concept stimulus, Van Westendorp/Gabor-Granger/conjoint blocks, sample guidance, CSV schema, and analysis plan. The user or a research platform collects real responses.

landing_page_test
  Output price variants, landing-page blocks, event schema, success metrics, and guardrails. S07/S13 should own funnel execution and experiment design.

marketplace_or_retail_test
  Output offer variants, channel conflict guardrails, promo integrity checks, and sell-through/return metric schema. The user or channel partner executes.

internal_data_analysis
  Output upload schema for previous-generation sales, price, promo, returns, and channel data. Analyze only after the user supplies data or derived summaries.

mixed
  Combine survey evidence with live or internal data when pricing risk is high.
```

## Advertising A/B Price Test Logic

Use advertising A/B tests to measure real user response to price, offer framing, and value proof. Treat it as behavioral evidence for acquisition and funnel friction, not as a complete market demand curve.

### Test Levels

```text
level_1_message_interest
  Test value propositions with the same price or no visible price. Use this to identify which segment/message earns qualified attention before testing price.

level_2_price_framing
  Hold product, audience, creative quality, landing page, and price economics mostly constant while varying price framing: full price, launch offer, bundle, installment, warranty, free shipping, or savings claim.

level_3_landing_page_price
  Randomize traffic to pages with different candidate prices or offer structures. Measure deeper intent: product-detail engagement, email signup, add-to-cart, checkout start, preorder/deposit where allowed.

level_4_paid_commitment
  Use only when legal, brand-safe, and operationally approved. Measure deposit, preorder, reservation, or paid waitlist behavior. This is stronger evidence than clicks but needs fulfillment and refund guardrails.
```

### Controls

Keep these stable unless the test explicitly varies them:

```text
audience
  Country, language, segment, budget band, platform targeting, exclusion rules.

stimulus
  Product images, claim strength, proof, landing page layout, shipping/tax visibility, warranty, and trust signals.

traffic
  Budget, bidding strategy, time window, device mix, placement, frequency cap, campaign learning phase, and attribution window.

offer
  Price, discount, bundle, installment, freebie, delivery promise, return policy, and stock availability.
```

### Metrics

```text
attention
  Impressions, CTR, CPC, qualified click rate.

consideration
  Product page dwell time, scroll depth, comparison clicks, FAQ clicks, price-detail expansion.

purchase_intent
  Add-to-cart, checkout start, preorder/deposit, email capture, retailer clickout.

commercial_quality
  CPA, margin after promo, expected net selling price, refund/cancellation risk, projected payback.

diagnostic_signals
  Price objection clicks, shipping/tax drop-off, financing clicks, warranty clicks, trust badge clicks.
```

### Decision Logic

Do not choose the winning price from CTR alone.

```text
high_ctr_low_add_to_cart
  The message attracts curiosity, but price, trust, product fit, or landing page proof may be weak.

low_ctr_high_conversion
  The audience may be smaller but more qualified. Consider premium niche positioning or tighter targeting.

high_add_to_cart_low_checkout
  Price, shipping, tax, payment, trust, delivery time, or return policy is likely creating late-stage friction.

high_conversion_margin_fail
  Consumer response is not enough. The offer needs margin review, bundle redesign, channel review, or avoid.

small_lift_low_confidence
  Keep as directional evidence only. Use survey or longer live test before pricing decision.
```

### Output Schema

```json
{
  "ad_ab_price_test_plan": {
    "test_level": "level_1_message_interest | level_2_price_framing | level_3_landing_page_price | level_4_paid_commitment",
    "hypothesis": "",
    "audiences": [],
    "variants": [
      {
        "variant_id": "",
        "price_or_offer": "",
        "message_angle": "",
        "proof_assets": [],
        "landing_page_ref": ""
      }
    ],
    "controlled_variables": [],
    "primary_metrics": [],
    "secondary_metrics": [],
    "minimum_runtime_or_sample_note": "",
    "decision_rules": [],
    "risks": [],
    "handoff_to_s07_or_s13": []
  }
}
```

## Marketplace And Retail Price Test Logic

Use marketplace or retail tests when the company can safely observe behavior closer to purchase: product detail views, conversion, sell-through, returns, and retailer feedback. This evidence is stronger than ad clicks but harder to control.

### Test Modes

```text
marketplace_pdp_test
  Test price, bundle, coupon, installment, title, hero image, proof assets, and A+ content on a product detail page when platform rules allow.

retailer_offer_test
  Test MSRP, launch offer, gift-with-purchase, warranty extension, free shipping, or bundle through one or more retailers.

geo_or_store_cell_test
  Compare matched stores, regions, cities, or retailer cells with controlled price/offer differences.

time_block_test
  Compare matched time windows only when seasonality, payday, campaign spend, competitor promo, and inventory are controlled.

channel_clickout_test
  When direct sale is not possible, measure retailer clickouts from a brand page or campaign page by price/offer variant.
```

### Required Controls

```text
availability
  Stock level, delivery promise, out-of-stock risk, fulfillment speed, and return policy.

traffic_and_placement
  Search rank, category placement, retailer merchandising, PDP traffic source, paid media support.

competitive_context
  Competitor prices, coupons, bundles, stockouts, review ratings, and promo calendar during the test.

channel_policy
  MAP/MSRP rules, retailer contracts, cross-border price leakage, and channel conflict risk.

content_quality
  PDP title, imagery, specs, proof, reviews, Q&A, comparison table, warranty and support promises.
```

### Metrics

```text
demand
  PDP sessions, conversion rate, units sold, sell-through velocity, add-to-cart, buy-box share when applicable.

price_response
  Conversion lift vs control, revenue per visitor, average selling price, discount redemption, installment usage.

commercial_quality
  Gross margin after fees and promo, return/cancellation rate, refund reason, warranty/support contact rate.

channel_health
  Retailer feedback, price matching pressure, cross-channel complaints, inventory imbalance, review impact.
```

### Decision Logic

```text
conversion_lift_margin_pass
  Candidate offer can move forward, subject to channel and brand review.

conversion_lift_margin_fail
  Demand exists but economics fail. Test bundle, financing, cost-down, or proof-led premium instead.

no_lift_high_traffic
  Price/offer may not solve the issue. Recheck product-market fit, content, reviews, trust, or competitor gap.

sell_through_lift_return_spike
  Price can create low-quality demand. Flag support, quality, expectation-setting, or segment mismatch risk.

retailer_sell_in_without_sell_through
  Do not treat retailer purchase order as consumer demand. Separate sell-in from sell-through.
```

### Output Schema

```json
{
  "retail_channel_price_test_plan": {
    "test_mode": "marketplace_pdp_test | retailer_offer_test | geo_or_store_cell_test | time_block_test | channel_clickout_test",
    "hypothesis": "",
    "channels_or_retailers": [],
    "variants": [
      {
        "variant_id": "",
        "price_or_offer": "",
        "bundle_or_promo": "",
        "content_changes": [],
        "channel_constraints": []
      }
    ],
    "control_cells": [],
    "required_controls": [],
    "primary_metrics": [],
    "secondary_metrics": [],
    "data_collection_schema": [],
    "decision_rules": [],
    "risks": [],
    "handoff_to_s13": []
  }
}
```

## Respondent And Sample Guidance

Prefer real respondents from the launch country, screened by category relevance, budget band, purchase intent/timing, channel behavior, and target segment. Use local-language stimuli and local currency with tax, shipping, financing, warranty, and subscription framing that match the buying context.

```text
qualitative_pretest
  8-15 respondents per priority segment can expose confusing value claims, missing proof, and major price objections.

directional_survey
  About 100-300+ usable respondents per priority country or key segment is a common directional starting point; larger samples are needed for stable subgroup reads.

conjoint_or_dce
  Usually needs larger, carefully designed samples and controlled attributes/levels. Use when feature, bundle, warranty, service, or subscription tradeoffs materially affect price.

live_experiment
  Requires traffic, conversion baselines, and power analysis. Run long enough to avoid reading noise as signal.
```

## WTP Test Plan

```json
{
  "wtp_test_plan": {
    "status": "required | recommended | optional | not_needed | blocked",
    "recommended_methods": [],
    "test_objectives": [],
    "target_segments": [],
    "candidate_price_points": [],
    "sample_requirements": "",
    "questions_or_tasks": [],
    "success_metrics": [],
    "failure_signals": [],
    "data_gaps_addressed": [],
    "priority": "high | medium | low"
  }
}
```

## Van Westendorp Test Design

Use when price acceptability range is unknown and the product/category can be evaluated in survey.

```json
{
  "van_westendorp_test_design": {
    "trigger_reason": "",
    "target_segments": [],
    "question_set": [
      "At what price would you consider this too cheap to trust?",
      "At what price would you consider this a bargain?",
      "At what price would you consider this expensive but still worth considering?",
      "At what price would you consider this too expensive?"
    ],
    "stimulus_requirements": [],
    "analysis_outputs": [
      "acceptable_price_range",
      "indifference_price_point",
      "optimal_price_point",
      "segment_differences"
    ],
    "limitations": []
  }
}
```

## Gabor-Granger Test Design

Use when there are specific candidate price points and purchase-intent testing is needed.

```json
{
  "gabor_granger_test_design": {
    "trigger_reason": "",
    "target_segments": [],
    "candidate_price_points": [],
    "purchase_intent_scale": "",
    "analysis_outputs": [
      "demand_curve",
      "revenue_curve",
      "conversion_thresholds",
      "segment_price_response"
    ],
    "limitations": []
  }
}
```

## Conjoint/DCE Test Plan

Use only when feature, bundle, warranty, subscription, or service tradeoffs matter enough to justify the complexity.

```json
{
  "conjoint_dce_test_plan": {
    "trigger_reason": "",
    "attributes": [],
    "levels": {},
    "target_segments": [],
    "sample_requirements": "",
    "analysis_outputs": [
      "part_worth_utilities",
      "price_tradeoff",
      "bundle_preference",
      "scenario_simulation"
    ],
    "limitations": []
  }
}
```

## Promo Test Plan

```json
{
  "promo_test_plan": {
    "testable_offers": [],
    "test_channels": [],
    "metrics": [
      "conversion_rate",
      "average_order_value",
      "return_rate",
      "margin_after_promo",
      "incremental_revenue"
    ],
    "risks": [],
    "confidence": "high | medium | low"
  }
}
```
