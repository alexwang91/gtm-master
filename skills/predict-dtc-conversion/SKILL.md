---
name: predict-dtc-conversion
description: Use when optionally planning or diagnosing DTC, landing-page, PDP, preorder, waitlist, checkout, or campaign-to-page conversion for 2C hardware GTM before or after launch using message fit, competitor/previous-generation page benchmarks, price/proof/trust friction, traffic assumptions, page/funnel text, analytics evidence, and experiment readiness without treating AI estimates as proven CVR.
---

# Predict DTC Conversion

## Role

Use this skill as optional S07 in the GTM intelligence report suite. It plans or diagnoses conversion friction across campaign entry, landing/PDP content, offer, proof, trust, CTA, checkout, and measurement readiness.

S07 has two valid paths:

- **Prelaunch planning mode:** use when the product is not live or the user's own page/PDP/checkout does not exist. Benchmark competitors, local retailer/PDP norms, previous-generation pages/results, and upstream S03/S04/S05/S06 handoffs to produce a page/PDP requirement brief, recommendation pack, tracking requirements, and validation plan.
- **Live/draft diagnosis mode:** use when page/funnel text, URLs, checkout descriptions, analytics, or historical conversion data exist. Diagnose the actual page/funnel and produce friction scores, CVR assumption caveats, and tests.

Skip S07 when DTC/PDP/landing-page/preorder/waitlist/clickout conversion planning is not relevant to the launch route.

S07 must not promise conversion rate, revenue, ROAS, sales lift, or demand. It produces ranges, friction scores, and validation plans.

## Required Inputs

```json
{
  "project_brief": {},
  "segment_message_architecture": [],
  "price_sensitivity_model": {},
  "price_risk_guardrail": []
}
```

High-value upstream fields:

```json
{
  "landing_page_message_block_seed": [],
  "objection_matrix": [],
  "claim_risk_and_proof_gate": {},
  "feature_benefit_proof_matrix": [],
  "price_message_seed": [],
  "promo_subscription_guidance": {},
  "digital_shelf_and_retailer_decision_map": [],
  "segment_channel_touchpoint_map": [],
  "channel_fit_scores": [],
  "copy_quality_scorecard": [],
  "landing_page_copy_fit": [],
  "marketplace_pdp_copy_fit": [],
  "copy_test_backlog": [],
  "creator_expected_outcome_estimate": [],
  "creator_budget_expectation_confidence": {}
}
```

Optional user inputs:

```json
{
  "page_or_funnel_text": "",
  "landing_page_url_or_pdp_url": "",
  "page_structure_or_wireframe_text": "",
  "checkout_flow_description": "",
  "traffic_source_plan": [],
  "campaign_assets_or_ad_copy": [],
  "analytics_or_conversion_data": "",
  "historical_landing_page_results": "",
  "launch_page_planning_stage": "none | concept | draft | live | post_launch",
  "competitor_landing_pages_or_pdp_refs": [],
  "previous_generation_page_or_pdp_refs": [],
  "previous_generation_conversion_or_page_results": "",
  "competitor_offer_trust_policy_refs": [],
  "target_conversion_action": "purchase | preorder | waitlist | lead | retailer_clickout | app_install | other",
  "tracking_or_analytics_context": "",
  "offer_details": "",
  "return_warranty_shipping_payment_policy": "",
  "retailer_or_marketplace_constraints": ""
}
```

## Load Order

Read only what the current task needs:

1. Read `references/output-contract.md` before producing artifacts, handoffs, or report sections.
2. Read `references/upstream-input-map.md` before deciding whether S07 can diagnose a real funnel or should request page/funnel materials.
3. Read `references/conversion-methods.md` before building conversion hypotheses, friction maps, traffic-source continuity, checkout trust review, or experiment plans.
4. Read `references/scoring-rubrics.md` before assigning friction, readiness, confidence, or experiment-priority scores.
5. Read `references/evidence-usage-policy.md` before using URLs, analytics, private funnel data, public pages, or historical performance.
6. Read `references/html-visual-block-generation.md` before producing S14-ready `visual_blocks`.
7. Read `references/html-section-contract.md` before producing the HTML conversion section draft.

## Depth Modes

```text
quick
  Decide skip vs prelaunch vs live/draft mode. Produce input coverage, top conversion or page-readiness risks, and next tests.

standard
  Produce core outputs plus funnel stage map, segment/page fit, price/proof/trust friction, tracking readiness, page experiment plan, and prelaunch benchmark outputs when the user's page is missing.

deep
  Add traffic-source continuity, checkout/payment/shipping/return audit, competitor/previous-generation page benchmark depth, analytics event schema, A/B test design, and performance result interpretation when data exists.
```

Default to `standard`.

## Output Tiers

Core outputs:

```text
conversion_input_coverage_gate
prelaunch_conversion_planning_mode
funnel_stage_inventory
traffic_source_assumption_map
segment_landing_page_fit_matrix
offer_message_continuity_map
proof_objection_friction_map
price_trust_checkout_friction_map
mobile_ux_friction_audit
conversion_hypothesis_model
dtc_conversion_model
cvr_assumption_ladder
funnel_friction_scorecard
funnel_friction_map
conversion_risk_guardrail
tracking_readiness_audit
page_experiment_plan
html_conversion_section
```

Conditional outputs:

```text
page_or_funnel_material_request_list
competitor_landing_pdp_benchmark
previous_generation_funnel_learnings
category_page_requirement_brief
prelaunch_page_recommendation_pack
launch_tracking_requirement_brief
landing_page_copy_fit_audit
pdp_checkout_trust_audit
retailer_clickout_conversion_fit
campaign_landing_match_audit
preorder_waitlist_flow_fit
analytics_event_schema
ab_test_plan
conversion_performance_result_interpretation
compliance_review_queue
```

Audit outputs:

```text
conversion_evidence_trace
page_observation_log
cvr_assumption_trace
experiment_validity_audit
tracking_data_audit
```

## Conditional Triggers

```text
page_or_funnel_material_request_list
  Trigger when DTC/PDP conversion matters but page text, URL, checkout description, or offer details are missing.

prelaunch_conversion_planning_mode
  Trigger when launch_page_planning_stage is none, concept, or draft, or when the user's own page/PDP/checkout is not available.

competitor_landing_pdp_benchmark
  Trigger in prelaunch mode when public competitor, marketplace, retailer, or category PDP/landing pages can be collected or supplied.

previous_generation_funnel_learnings
  Trigger when previous-generation page refs, launch pages, PDPs, sales/channel performance, analytics, reviews, or user feedback are supplied.

category_page_requirement_brief
  Trigger in prelaunch mode to define what the launch page/PDP must prove, say, collect, and avoid before launch.

prelaunch_page_recommendation_pack
  Trigger in prelaunch mode to produce actionable page/PDP, offer, proof, trust, CTA, and measurement recommendations.

launch_tracking_requirement_brief
  Trigger when the page/funnel is not live or tracking context is missing.

campaign_landing_match_audit
  Trigger when paid ads, creator traffic, search ads, email, affiliate, or retail media drive traffic.

pdp_checkout_trust_audit
  Trigger when retailer/PDP, delivery, warranty, return, payment, reviews, Q&A, or marketplace trust affects conversion.

preorder_waitlist_flow_fit
  Trigger when the target action is preorder, waitlist, reservation, lead, or launch notification.

analytics_event_schema
  Trigger when tracking context is missing or S08 needs traffic-to-demand assumptions.

conversion_performance_result_interpretation
  Trigger when analytics, A/B test, heatmap, session recording, ad, or landing-page performance data is supplied.
```

## Execution Workflow

```text
1. Validate whether S07 should run. Skip with a clear reason when no DTC/PDP/preorder/waitlist/clickout conversion planning need exists.
2. Validate upstream message, price, proof, channel, page/funnel, competitor, previous-generation, and tracking coverage.
3. Classify launch_page_planning_stage as none, concept, draft, live, or post_launch.
4. Define target conversion action and funnel stages.
5. If no owned page/funnel exists, enter prelaunch mode: benchmark competitor/local retailer/PDP patterns, extract previous-generation learnings, produce page/PDP requirements, recommendation pack, and tracking requirements.
6. If owned page/funnel materials exist, inventory them and score segment x landing/PDP fit and campaign-to-page message continuity.
7. Diagnose friction: proof, objection, price/value, trust, warranty/return, shipping, payment, CTA, mobile UX, and checkout/clickout.
8. Build conversion hypothesis model and CVR assumption ladder only when a measured, benchmark, historical, or explicitly heuristic basis exists. Otherwise record `missing_cvr_basis`.
9. Build conversion risk guardrails: claims, price shock, trust gaps, attribution gaps, and page readiness blockers.
10. Build tracking readiness audit and analytics event schema when needed.
11. Build page experiment plan with hypothesis, variant, metric, sample/traffic note, decision rule, and confounders.
12. Interpret performance data only after checking traffic quality, attribution, sample size, timing, novelty, seasonality, and selection bias.
13. Produce compressed handoff pack.
14. Produce HTML conversion section draft with S14-ready visual blocks.
```

## Scope Boundary

S07 owns:

- DTC, landing-page, PDP, preorder, waitlist, and checkout conversion friction
- Prelaunch landing/PDP requirement planning from competitor, category, previous-generation, and channel evidence
- Traffic-source to landing-message continuity
- Price/proof/trust/return/warranty/payment friction diagnosis
- CVR assumption ranges with confidence caps
- Tracking readiness and page experiment plan

S07 does not own:

- Final demand forecast or inventory planning
- Final media budget approval
- Final price approval
- Final legal/compliance approval
- Redesigning visual creative assets
- Treating heuristic scores as measured conversion lift
- Final page design, visual layout, copywriting approval, or implementation
- Final HTML composition

## Required Output

Always return the S07 output envelope from `references/output-contract.md`:

```json
{
  "full_artifact": {},
  "compressed_handoff_pack": {},
  "html_section_draft": {},
  "evidence_updates": [],
  "decision_updates": [],
  "data_gaps": [],
  "post_skill_isolation_record": {},
  "recommended_next_skills": []
}
```

## Quality Rules

- Do not invent page content, checkout steps, analytics, traffic source quality, or CVR benchmarks.
- If page/funnel materials are missing, enter prelaunch mode, label recommendations as `hypothesis_only` or `planning_recommendation`, and request the missing materials.
- In prelaunch mode, use competitor/local retailer/PDP patterns and previous-generation learnings as benchmark evidence; do not claim they prove this product's future CVR.
- Separate measured conversion data, public benchmark proxy, historical internal data, and AI heuristic judgment.
- Every CVR range must include basis, scenario, confidence, and confounders.
- Omit CVR ranges or mark `missing_cvr_basis` when no measured, benchmark, historical, or explicit heuristic basis exists.
- Do not estimate sales or revenue without S08 demand model and explicit price/channel assumptions.
- Default dashboard-facing outputs to Simplified Chinese unless the user requests another report language.
