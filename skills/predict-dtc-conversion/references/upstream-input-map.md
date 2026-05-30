# S07 Upstream Input Map

Use this before deciding whether S07 should be skipped, run in prelaunch planning mode, or diagnose a concrete owned funnel.

## Run Mode Gate

```text
skip
  Use when the launch route has no DTC/PDP/landing page, preorder, waitlist, retailer clickout, or funnel-planning decision.

prelaunch_planning
  Use when launch_page_planning_stage is none, concept, or draft, or when owned page/funnel materials do not exist yet.
  Output competitor/previous-generation benchmark, page requirement brief, recommendation pack, tracking requirements, and validation plan.

live_or_draft_diagnosis
  Use when owned page/PDP/funnel text, URL, checkout flow, offer details, analytics, or historical conversion data exists.
  Diagnose the actual materials and only then produce page-specific friction scores.
```

## Minimum Proceed Gate

S07 can produce a hypothesis-level conversion model when these groups exist:

```text
message_system
  segment_message_architecture, landing_page_message_block_seed, objection_matrix, proof requirements

price_and_offer_context
  price_sensitivity_model, price_risk_guardrail, price_message_seed, promo_subscription_guidance if available

channel_or_traffic_context
  segment_channel_touchpoint_map, channel_fit_scores, traffic_source_plan, creator_expected_outcome_estimate, or campaign source assumptions
```

S07 can produce page-level diagnosis when:

```text
page_or_funnel_materials
  page_or_funnel_text, landing/PDP URL, page structure text, checkout description, offer details, or PDP copy.
```

S07 can produce prelaunch page/PDP planning when:

```text
prelaunch_benchmark_materials
  competitor_landing_pages_or_pdp_refs, previous_generation_page_or_pdp_refs,
  previous_generation_conversion_or_page_results, competitor_offer_trust_policy_refs,
  digital_shelf_and_retailer_decision_map, landing_page_message_block_seed,
  price_risk_guardrail, or local retailer/PDP norms from S01/S02.
```

S07 can produce measured performance interpretation only when:

```text
performance_data
  Analytics, A/B test results, landing-page results, ad data, retailer clickout data, heatmap/session evidence, or event data.
```

## Missing Input Handling

```text
missing_page_or_funnel_text
  If S07 is relevant, enter prelaunch planning mode instead of pretending to diagnose a real page.
  Produce material request list, competitor/previous-generation benchmark needs, page requirement brief, and hypothesis-only recommendation pack.

missing_competitor_page_benchmark
  Do not produce confident category page recommendations. Request competitor, local marketplace, retailer, or category PDP refs.

missing_previous_generation_funnel_data
  Produce competitor/category recommendations only. Mark previous-generation learning as unavailable.

missing_offer_details
  Cap price/value and CTA confidence at low.

missing_checkout_or_policy_context
  Cap checkout, payment, return, warranty, and shipping trust confidence at low.

missing_tracking_context
  Do not produce confident visit-to-conversion assumptions. Produce analytics_event_schema.

missing_traffic_source_context
  Can diagnose generic page friction but cap traffic-message continuity confidence at low.
```

## High-Value Inputs

```text
landing_page_message_block_seed
  Use as expected page narrative and message hierarchy.

copy_quality_scorecard, landing_page_copy_fit, marketplace_pdp_copy_fit
  Use only if S05 ran; S07 should not require S05.

creator_expected_outcome_estimate
  Use only as traffic-source assumption for creator-driven landing paths. Do not treat it as demand.

price_risk_guardrail
  Use to identify price shock, discount dependence, financing need, and proof-before-price requirements.

digital_shelf_and_retailer_decision_map
  Use when retailer/PDP conversion, reviews, Q&A, delivery, warranty, and marketplace trust matter.

competitor_landing_pages_or_pdp_refs
  Use to benchmark hero promise, proof order, comparison strategy, review/trust surface, CTA pattern, offer framing, and local policy visibility.

previous_generation_page_or_pdp_refs, previous_generation_conversion_or_page_results
  Use to extract what worked, where trust/price/proof objections appeared, and what must change for next-generation launch materials.
```
