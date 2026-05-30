# Pricing Test Result Interpretation

Use this when the user provides survey, advertising A/B, landing-page, marketplace, retail, channel, or internal sales results after S04 has designed pricing tests.

## Evidence Strength Ladder

Use the strongest valid evidence available, but keep method limitations visible.

```text
synthetic_or_ai_persona
  Hypothesis generation only. Never use as WTP or demand evidence.

public_market_proxy
  Useful for anchors, complaints, substitute pressure, and price corridor. Not exact WTP.

survey_stated_preference
  Useful for acceptable range, candidate price intent, and feature/price tradeoffs. Adjust confidence for sample quality and stated-intent inflation.

ad_or_landing_behavior
  Useful for attention, consideration, and funnel friction. Stronger than stated preference for click/add-to-cart behavior, but affected by targeting, creative, bidding, platform learning, and page quality.

marketplace_or_retail_sell_through
  Stronger purchase-proximity evidence when stock, placement, content, competitor prices, promo calendar, and channel conditions are controlled.

internal_sales_or_previous_generation
  Valuable for elasticity and guardrails when sell-through, price, promo, channel, seasonality, returns, and stockouts are separated.
```

## Result Ingestion Gate

Before interpreting results, classify the source and run a quality gate.

```json
{
  "pricing_test_result_interpretation": {
    "result_source_type": "survey_panel | ad_ab | landing_page | marketplace | retail | channel_clickout | internal_sales | mixed",
    "data_quality_gate": {
      "status": "pass | pass_with_caveats | fail",
      "sample_or_traffic_size": "",
      "randomization_status": "randomized | matched_cells | observational | unknown",
      "control_quality": "strong | medium | weak | missing",
      "segment_match": "strong | medium | weak | unknown",
      "time_window_quality": "strong | medium | weak | unknown",
      "confounders": [],
      "missing_fields": [],
      "confidence_cap": "high | medium | low | hypothesis_only",
      "action": "interpret | interpret_with_caveats | request_cleaner_data | stop"
    },
    "method_specific_outputs": {},
    "price_variant_results": [],
    "decision_update": {},
    "handoff_updates": {},
    "data_gaps": []
  }
}
```

## Quality Gate Checks

```text
survey_panel
  Check respondent country, language, segment fit, category relevance, budget band, purchase timing, straight-lining, speeders, duplicate responses, and sample size by segment.

ad_ab
  Check audience comparability, campaign learning phase, budget parity, bidding strategy, device mix, placement mix, frequency, creative equality, landing-page equality, attribution window, and traffic quality.

landing_page
  Check randomization, page speed, page parity, event tracking, bot filtering, device/browser mix, source mix, shipping/tax visibility, stock status, payment methods, and checkout availability.

marketplace_or_retail
  Check stock, delivery promise, search rank, PDP content, review count/rating, retailer merchandising, competitor prices/promos, promo calendar, return policy, and channel conflict.

internal_sales
  Check sell-in vs sell-through, stockouts, promo depth, seasonality, channel mix, return/cancellation rates, price changes, competitor events, and data granularity.
```

## Method-Specific Interpretation

### Survey Results

```text
van_westendorp
  Use for acceptable price range and segment differences. Do not treat the optimal price point as a final price without margin/channel checks and behavioral validation.

gabor_granger
  Use for candidate price intent, demand curve direction, and revenue curve hypothesis. Apply confidence caps when purchase intent is stated rather than paid behavior.

conjoint_or_dce
  Use for feature/price/bundle tradeoffs and scenario simulation. Check that attributes and levels are realistic and not overloaded.
```

### Ad / Landing Results

```text
ctr_lift
  Attention signal only. It can support message or offer interest but not final WTP.

qualified_click_or_page_engagement
  Consideration signal. Use with scroll depth, dwell time, spec clicks, comparison clicks, price-detail clicks, and FAQ engagement.

add_to_cart_or_checkout_start
  Stronger intent signal. Diagnose shipping, tax, financing, warranty, trust, and delivery drop-off before blaming price alone.

preorder_deposit_or_paid_commitment
  Strong behavioral evidence if legal, fulfilled/refundable as promised, and not distorted by scarcity or promo confusion.
```

### Marketplace / Retail Results

```text
sell_through_velocity
  Stronger demand signal when stock, traffic, placement, and competitor conditions are controlled.

average_selling_price
  Use with promo depth and coupon redemption to distinguish list-price acceptance from discount dependence.

return_or_cancellation_rate
  High returns after price-led demand can signal expectation mismatch, poor fit, quality concern, or buyer remorse.

retailer_feedback
  Useful context but not consumer demand by itself. Separate retailer sell-in from consumer sell-through.
```

## Commercial Metrics

When private financial values are not shared, output formulas and let the HTML private calculator or user-provided derived summaries complete the calculation.

```text
variant_lift = (variant_metric - control_metric) / control_metric

revenue_per_visitor = conversion_rate * average_selling_price

contribution_per_visitor =
  conversion_rate * (net_selling_price - cogs - variable_fulfillment_or_support_cost)
  - acquisition_cost_per_visitor

margin_pass =
  gross_margin >= target_gross_margin
```

Do not expose raw COGS, margin, or channel terms unless explicitly approved.

## Decision Update Rules

```text
price_confirmed
  Behavioral or strong survey evidence supports the candidate price, proof is adequate, and margin/channel constraints pass. Increase confidence and hand off to S08/S13.

price_needs_proof
  Price is plausible, but conversion depends on trust, demo, comparison, warranty, reviews, certification, influencer proof, or retail sales explanation. Hand back to S03/S05/S07.

price_too_high_for_priority_segment
  Priority segment shows high objection, low conversion, or unfavorable tradeoff at candidate price. Recommend lower band, bundle, financing, launch offer, or segment narrowing.

price_can_move_up
  Lower price performs similarly to higher price, premium proof holds, and margin/channel constraints pass. Recommend testing higher tier or reducing promo depth.

promo_drives_low_quality_demand
  Promo lifts volume but hurts margin, return rate, cancellation, support burden, brand perception, or channel health. Flag promo dependency and redesign offer.

channel_or_margin_blocked
  Consumer response is positive but economics, MAP/MSRP, retailer terms, fees, tax, inventory, or channel conflict block decision. Route to finance/channel review.

test_inconclusive
  Results are underpowered, uncontrolled, noisy, or confounded. Keep hypothesis status and recommend cleaner test.
```

## Output Schema

```json
{
  "pricing_test_result_interpretation": {
    "result_source_type": "",
    "data_quality_gate": {},
    "method_specific_outputs": {
      "survey_outputs": {},
      "ad_landing_outputs": {},
      "retail_marketplace_outputs": {},
      "internal_sales_outputs": {}
    },
    "price_variant_results": [
      {
        "variant_id": "",
        "price_or_offer": "",
        "primary_metric_result": "",
        "commercial_metric_result": "",
        "segment_or_channel": "",
        "evidence_strength": "high | medium | low | hypothesis_only",
        "main_caveats": [],
        "interpretation": ""
      }
    ],
    "decision_update": {
      "status": "price_confirmed | price_needs_proof | price_too_high_for_priority_segment | price_can_move_up | promo_drives_low_quality_demand | channel_or_margin_blocked | test_inconclusive",
      "recommended_price_posture": "value | parity | slight_premium | premium_with_proof | promo_led | bundle_led | finance_or_installment_led | blocked | retest",
      "confidence_change": "increase | hold | decrease",
      "pricing_readiness_change": "",
      "next_action": "handoff_to_s08 | handoff_to_s13 | rerun_test | finance_review | channel_review | message_or_proof_revision | avoid"
    },
    "handoff_updates": {
      "to_s07": [],
      "to_s08": [],
      "to_s13": [],
      "to_s14": []
    },
    "data_gaps": []
  }
}
```
