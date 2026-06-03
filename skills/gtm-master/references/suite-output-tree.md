# GTM Master Suite Output Tree

This file is the top-level output map for the GTM Master skill suite. Use it
when reviewing the whole architecture, explaining the dashboard structure, or
checking what each sub-skill must produce.

The suite is report-language-required. Field names stay stable in
English so Codex, Claude Code, MCP tools, CLI tools, and HTML rendering can share
the same contracts.

## Reading Rules

- `visible`: may appear as a business section in the dashboard.
- `conditional`: appears only when triggered by product type, user input, or decision need.
- `hidden`: system output only; it supports planning, validation, or rendering but is not a business section.
- Every analysis skill still emits the standard envelope: `full_artifact`,
  `compressed_handoff_pack`, `html_section_draft`, `evidence_updates`,
  `decision_updates`, `data_gaps`, `context_escalations`,
  `recoverable_run_state_updates`, and `post_skill_isolation_record`.

## Execution Tree

```text
GTM Master Run
|-- S00 gtm-master [hidden orchestration]
|   |-- Project Brief
|   |-- Hardware current-state scorecard
|   |-- Run State / Resume Pointer
|   |-- Skill Execution Plan
|   +-- Report State
|-- S01 build-consumer-market-map [visible]
|   |-- Local market and evidence base
|   |-- Local source, access, TOP1 proof, price, voice, segment, channel, TAM/SAM/SOM seeds
|   +-- Handoff to S02, S04, S08, S14
|-- S02 mine-jtbd-scenarios [visible]
|   |-- JTBD scenarios and Four Forces switching dynamics
|   |-- Product-job fit, proof needs, anti-JTBD risks
|   +-- Handoff to S03, S04, S13, S14
|-- S03 match-messages-to-segments [visible]
|   |-- Message architecture
|   |-- Feature-benefit-proof, objections, claim risk, local-language, touchpoint, KOL/media seeds
|   +-- Handoff to S04, S05, S06, S07, S14
|-- S04 model-price-sensitivity [visible]
|   |-- Opening price strategy and price credibility
|   |-- WTP direct conclusion, rapid price prior, tests, private calculator spec
|   +-- Handoff to S07, S08, S13, S14
|-- Optional prelaunch branches
|   |-- S05 score-creative-assets [conditional]
|   |-- S06 score-kol-fit [conditional]
|   +-- S07 predict-dtc-conversion [conditional]
|-- S08 forecast-launch-demand [visible]
|   |-- Launch unit forecast, named channel priority, MKT response, budget posture, inventory risk
|   +-- Handoff to S09, S13, S14
|-- Conditional product-risk branches
|   |-- S09 predict-activation-risk [conditional]
|   |-- S10 generate-health-insights [conditional]
|   |-- S11 predict-subscription-and-churn [conditional]
|   +-- S12 mine-review-quality-feedback [conditional/post-launch]
|-- S13 plan-validation-experiments [hidden system capability]
|   |-- Assumption inventory, validation roadmap, test cards
|   +-- Hidden by default in the current dashboard
+-- S14 compose-html-gtm-dashboard [hidden composer]
    |-- Static HTML dashboard
    |-- Citations, data gaps, confidence badges, private calculators
    +-- Never appears as a business module
```

## Dashboard-Level Output Tree

```text
Final HTML Dashboard
|-- GTM judgment cover
|   |-- Enter / defend / cautious launch / validate-first / pause judgment
|   |-- Core recommendation
|   |-- Opening move
|   |-- Priority segment
|   |-- Must-win named channel
|   |-- Price or offer stance
|   |-- TOP1 competitor or internal ladder threat
|   +-- Decision-changing question
|-- GTM decision summary
|   |-- Expected weekly sales range
|   |-- MKT spend posture and budget caveats
|   |-- Named channel priority and channel capability
|   |-- Core competitor strengths, weaknesses, and response
|   +-- Top validation action
|-- Market and localization section from S01
|-- JTBD / scenario / consumer voice section from S02
|-- Message architecture section from S03
|-- Pricing and opening-price strategy section from S04
|-- Optional copy / creator / conversion sections from S05-S07
|-- Launch forecast section from S08
|-- Conditional risk or post-launch sections from S09-S12
|-- Questions that would change the conclusion, citations, and evidence index
|-- Source governance appendix only when requested or needed
+-- Local-only private calculator components when supplied
```

## S00 gtm-master Outputs

Role: hidden orchestration. S00 does not create market conclusions. It creates
the run contract and controls graph, context, state, and quality gates.

- `project_brief`: normalized product, country/region, price range, optional private inputs, claim constraints, user-supplied report language, and audience.
- `skill_execution_plan`: selected run mode, active graph, optional branches, method crosswalk, tool slots, and execution order.
- `recoverable_run_state`: phase, current skill, resume pointer, skill status, artifacts, idempotency key, and interrupted/resumed status.
- `hardware_current_state_scorecard`: 17-section launch readiness score with gaps, blockers, and top validation priority.
- `private_data_policy_decision`: which private inputs are excluded, summarized, approved for internal artifact, approved for public HTML, or local-calculator-only.
- `evidence_ledger`: global index of evidence records, source refs, collection logs, confidence, and data permission labels.
- `report_state`: accumulated section drafts, executive takeaways, data gaps, decisions, citations, and render inputs.
- `quality_gate_results`: pass, pass-with-caveats, or fail results for inputs, methods, evidence, handoffs, context budget, tooling, and HTML readiness.
- `decision_log`: user decisions, include/exclude choices, skipped modules, private-data permissions, and approval state.
- `data_gap_log`: cross-suite list of missing, stale, blocked, weak, or unavailable evidence.

## S01 build-consumer-market-map Outputs

Role: visible. S01 builds the target-country market fact layer.

- `market_context_pack`: canonical compressed market context for downstream skills.
- `category_selling_point_map`: mainstream category selling points versus the product's features and proof.
- `feature_to_local_language_map`: product features mapped to local search phrases, consumer wording, and translated explanations.
- `localization_preflight`: local language, currency, tax, price display, retailer norms, payment, return, warranty, search, and compliance context.
- `local_source_map`: target-country source list for search, ecommerce, price comparison, specialist media, forums, and official data.
- `local_voice_source_map`: high-value places where consumers discuss, review, complain, compare, or ask questions.
- `source_accessibility_matrix`: access status, collection feasibility, expected record depth, restrictions, fallback, and tool slot for each key local source.
- `evidence_collection_summary`: what was collected, from where, by which tool slot, and with which limitations.
- `site_specific_comment_profiles`: source profiles for forums, specialist media comments, video comments, app reviews, Q&A, or deal communities.
- `comment_collection_coverage_reports`: bounded coverage status for comment/page/thread collection.
- `comment_export_refs`: references to stored comment exports or structured public comment records.
- `coverage_map`: coverage by source type, local language, competitor, price, voice, and channel.
- `competitor_substitute_map`: direct competitors, substitutes, premium anchors, budget anchors, previous generation, and ecosystem anchors.
- `competitor_candidate_review_list`: 5-10 candidate competitors/substitutes for user include/exclude/unsure review.
- `competitor_candidate_review_gate`: user or system review status before deep voice mining, with include/exclude/unsure decisions and unresolved gaps.
- `top1_competitor_proof_board`: weighted proof board explaining why the selected TOP1 competitor outranks alternatives, with previous-generation/internal risk split.
- `competitor_threat_scores`: scored competitor threat with overlap, price, channel, review, brand, feature, and switching-barrier factors.
- `substitute_taxonomy`: non-direct alternatives, workarounds, refurbished/used products, delayed purchase, and non-consumption choices.
- `price_ladder_scan`: local price tiers and jump-band risks across budget, mainstream, premium, flagship, used, and substitute options.
- `jump_decision_risks`: risks that consumers trade up/down or skip the target price band.
- `segment_competitor_threats`: competitor pressure by segment or use case.
- `consumer_voice_processing_summary`: counts and quality summary for source items, voice atoms, clusters, NSS/NPS proxy status, and Bain inputs.
- `consumer_opinion_map`: pain, praise, trigger, objection, comparison, trust, and price themes.
- `voice_atom_table`: deduped atomic consumer statements with source, journey, driver, sentiment, and confidence.
- `voice_theme_clusters`: grouped voice patterns with frequency, sentiment mix, local phrases, and confidence caps.
- `nss_nps_proxy_classification_table`: source-item-level promoter/passive/detractor-like classification when proxy thresholds are met.
- `nss_bain_input_refs`: references to NSS/NPS and Bain driver inputs used downstream.
- `bain_driver_inputs`: directional Bain-style driver impact records by driver, product, journey, and source mix.
- `journey_episode_inputs`: purchase, delivery, unboxing, setup, first use, app, support, return, and referral journey signals.
- `market_sizing_evidence_summary`: market sizing sources, proxy quality, and assumptions.
- `tam_sam_som_seed`: directional TAM/SAM/SOM ranges.
- `tam_sam_som_assumption_tree`: explicit market-sizing formulas, assumptions, caps, and sensitivity points.
- `comparable_market_proxies`: comparable category, country, product, or channel proxies.
- `market_sizing_confidence`: confidence score and caveats for sizing.
- `market_sizing_data_gaps`: missing official data, proxy weakness, or unresolved sizing assumptions.
- `segment_candidate_pool`: candidate consumer segments generated from evidence.
- `segment_evidence_strength_scores`: segment confidence based on voice, use case, price, channel, size, and cross-source support.
- `segment_seed_pack`: compact segment definitions for S02/S03/S08.
- `segment_priority_ranking`: ranked launch segments with product fit, WTP, reachability, size, and risk.
- `segment_distinctness_results`: merge/split/keep decision for segment overlap.
- `persona_cards`: evidence-backed persona cards, only as segment explanations, not unsupported demographics.
- `segment_level_tam_sam_som`: directional market size by segment.
- `segment_channel_touchpoint_map`: discovery, comparison, purchase, proof, support, retention, and advocacy touchpoints by segment.
- `retailer_marketplace_candidates`: named local ecommerce, marketplace, retail, operator, or own-store candidates.
- `content_proof_map`: proof assets needed by segment, claim, channel, and journey moment.
- `channel_fit_scores`: scored channel fit by reach, intent, trust, purchase path, local language, measurability, friction, and risk.
- `user_provided_channel_hypotheses`: user-supplied channel ideas preserved as hypotheses until evidence supports them.
- `local_price_corridor`: local price range and anchor bands.
- `price_anchor_panel`: competitor/substitute anchors with confidence, source, channel, and comparability.
- `competitor_price_gap_table`: target price versus competitor/substitute prices and price-gap risks.
- `segment_price_sensitivity_seeds`: early price sensitivity by segment.
- `value_proof_requirement_matrix`: proof required to support price and value by segment/scenario.
- `promotion_subscription_sensitivity_seed`: early signal of promo, installment, bundle, or recurring-cost sensitivity.
- `user_provided_price_hypotheses`: user price assumptions preserved with evidence status.
- `nss_nps_proxy_seed_panel`: surveyed/proxy status, source mix, confidence, and directional promoter/detractor view.
- `competitor_nss_nps_comparison_seed`: competitor comparison using surveyed or proxy voice evidence.
- `competitive_bain_voice_board`: lane-based NPS Proxy / Bain VOC comparison for our product, TOP1 competitor, and previous generation or internal benchmark.
- `nps_driver_tornado_seed`: ranked drivers that may move recommendation or detractor drag.
- `journey_episode_nss_seed`: NSS/NPS-like signals by hardware journey episode.
- `earned_growth_proxy_seed`: directional organic, referral, repeat, community, and detractor-drag readiness.
- `net_promoter_system_loop_seed`: closed-loop candidates for product, marketing, support, channel, or sales action.
- `hardware_experience_diagnosis_seed`: product/app/service/price/channel/root-cause diagnosis from voice evidence.
- `next_generation_marketing_sales_seed`: next-generation product, marketing, and sales recommendations seeded from voice drivers.
- `earned_growth_seed_notes`: caveats and limits on earned-growth attribution.
- `html_market_section`: S14-ready section draft in report_language with visual blocks, citations, confidence, and gaps.

## S02 mine-jtbd-scenarios Outputs

Role: visible. S02 converts S01 evidence into demand scenarios.

- `upstream_input_map`: which S01 fields were used, missing, weak, or escalated.
- `upstream_input_coverage_gate`: pass/caveat/fail status for consumer voice, segment, price, proof, channel, competitor, and local language inputs.
- `jtbd_source_map`: evidence refs used for each job candidate.
- `jtbd_candidate_pool`: atomic situation-progress-outcome-alternative-barrier candidates.
- `jtbd_scenario_pack`: prioritized JTBD scenarios with situation, desired progress, current alternative, barrier, proof need, evidence, and confidence.
- `jtbd_scenario_clusters`: grouped demand scenarios by progress and trigger.
- `scenario_distinctness_results`: merge/split/keep decisions for similar scenarios.
- `scenario_to_segment_matrix`: relationship between scenarios and launch segments.
- `scenario_to_journey_matrix`: relationship between scenarios and purchase/use/advocacy journey stages.
- `four_forces_switching_map`: Push, Pull, Habit, and Anxiety scores by scenario with evidence, blocker, and downstream action hooks.
- `consumer_electronics_gtm_moment_map`: exploration, evaluation, proof, retailer selection, purchase, setup, and advocacy moments.
- `product_job_fit_matrix`: how credibly the product satisfies each job, including gaps and proof needs.
- `digital_shelf_and_retailer_decision_map`: product visibility and seller-confidence needs for marketplaces, retailers, own-store, or operators.
- `behavioral_science_lever_map`: social proof, authority, risk reversal, category heuristics, offer, delivery, and friction-reduction hypotheses.
- `scenario_commercial_weight_map`: commercial weight by segment value, market size, price, channel, advocacy, and strategic priority.
- `brand_claim_constraint_map`: brand, proof, compliance, privacy, health, safety, warranty, or retailer constraints.
- `scenario_priority_scorecard`: scored ranking of scenarios.
- `proof_requirement_seed`: proof requirements by scenario, segment, claim, price, and channel.
- `anti_jtbd_risk_list`: reasons consumers may not buy, switch, repeat, recommend, or may return.
- `non_consumption_risk_map`: do-nothing, delay, workaround, or substitute risks.
- `local_language_trigger_phrase_map`: local phrases for search, category framing, objection, and comparison.
- `scenario_message_seed`: message angle seeds for S03, not final copy.
- `scenario_price_implication_seed`: price sensitivity, premium justification, promo, or competitor-anchor implications for S04.
- `validation_question_seed`: weak but important scenario assumptions for S13.
- `html_jtbd_section`: S14-ready section draft in report_language.

## S03 match-messages-to-segments Outputs

Role: visible. S03 creates the message architecture, not final advertising copy.

- `message_input_coverage_gate`: whether S02/S01 inputs are sufficient for message architecture.
- `segment_message_architecture`: segment-by-scenario value proposition, proof, tone, and channel message structure.
- `feature_benefit_proof_matrix`: feature to benefit to proof chain.
- `objection_matrix`: consumer objections, hidden anxieties, response direction, and proof needs.
- `claim_risk_and_proof_gate`: available, partial, missing, or risky claims and required review.
- `local_language_message_seed`: local wording seeds and phrases to preserve.
- `price_message_seed`: price/value framing seeds for S04.
- `selling_point_segment_touchpoint_kol_seed`: ranked selling-point routes connecting feature, benefit, segment/JTBD, local phrase, touchpoint channel, MKT carrier, budget signal, and expected validation signal.
- `hero_message_proof_asset_pack`: direct report-ready hero claim, support claims, proof assets, proof gaps, and local language terms that should appear in PDP, retail, PR, and KOL briefs.
- `sales_enablement_pack`: retailer/operator/ecommerce/support talk tracks, objection cards, demo needs, competitor battlecard refs, and claims to avoid.
- `retail_pdp_ready_pack`: title/search terms, hero proof, comparison table needs, FAQ, warranty/return/payment messages, and review-generation plan.
- `message_market_fit_scorecard`: scored message fit by segment, proof, objection, channel, and risk.
- `competitive_contrast_matrix`: factual competitor contrast and response direction.
- `behavioral_lever_message_seed`: message applications of behavioral levers from S02.
- `retail_sales_talk_track_seed`: retailer or sales-associate talking points and objection handling.
- `landing_page_message_block_seed`: PDP/landing page message blocks for S07.
- `creator_brief_message_seed`: creator/KOL/expert briefing seeds for S06.
- `compliance_review_queue`: claims or wording requiring legal, regulatory, privacy, safety, or brand review.
- `message_test_backlog`: message assumptions and variants to validate.
- `html_message_section`: S14-ready section draft in report_language.

## S04 model-price-sensitivity Outputs

Role: visible. S04 creates pricing hypotheses, tests, and local/private calculator specs.

- `price_input_coverage_gate`: public, private, segment, message, channel, and proof input completeness.
- `opening_price_strategy`: recommended launch pricing posture and conditions.
- `launch_price_architecture`: public anchor, transaction range, offer mechanism, promo floor, channel floor, and calculation mode.
- `local_price_credibility_model`: target price credibility versus local anchors, proof, trust, affordability, and channel norms.
- `rapid_price_prior`: quantitative WTP prior when direct research is unavailable.
- `wtp_direct_conclusion`: plain GTM answer on whether the target price can be defended, for whom, with what proof/offer, and what validation signal changes the decision.
- `segment_wtp_hypothesis`: acceptable range, premium tolerance, proof need, objection, and test method by segment.
- `price_sensitivity_model`: directional sensitivity factors and confidence caps.
- `price_value_proof_matrix`: which value arguments and proof are required for each price position.
- `price_risk_guardrail`: affordability, premium, channel, promo, subscription, claim, return, and margin risks.
- `wtp_test_plan`: recommended WTP validation plan.
- `promo_subscription_guidance`: discount, bundle, freebie, financing, installment, subscription, and risk-reversal guidance.
- `private_profit_revenue_optimizer_spec`: local-only optimizer spec for revenue-max and profit-max calculations.
- `price_path_30_60_90`: launch price posture, allowed moves, forbidden moves, watch metrics, and decision triggers.
- `pricing_decision_gate`: research-first, controlled-test-ready, finance-review, channel-review, forecast-ready, or blocked status.
- `pricing_handoff_summary`: compact pricing posture and caveats for S07/S08/S14.
- `van_westendorp_test_design`: acceptable price range survey design.
- `gabor_granger_test_design`: candidate price-point purchase-intent design.
- `maxdiff_feature_value_tradeoff_test_design`: MaxDiff design for prioritizing feature, proof, bundle, service, color, or channel value drivers.
- `conjoint_dce_test_plan`: feature/price/bundle/warranty/service tradeoff design.
- `channel_margin_guardrail`: constraints from COGS, margin, retailer fees, marketplace fees, discounts, and channel rules.
- `retail_price_integrity_map`: channel conflict, MAP/MSRP, cross-border, promo, and retailer integrity risks.
- `subscription_pricing_hypothesis`: recurring service, app, warranty, consumable, or financing pricing hypothesis.
- `promo_test_plan`: launch offer, coupon, bundle, installment, free shipping, or gift test plan.
- `elasticity_assumption_seed`: elasticity assumptions for S08, explicitly labeled as assumptions unless measured.
- `pricing_decision_options`: candidate price options when evidence and private constraints are sufficient.
- `private_pricing_calculator_spec`: blank local HTML calculator spec for sensitive COGS/margin/channel inputs.
- `pricing_test_execution_kit`: survey/ad/landing/retail test kit and CSV/result schema.
- `pricing_test_result_interpretation`: interpretation of uploaded real test results.
- `html_pricing_section`: S14-ready section draft in report_language.

## S05 score-creative-assets Outputs

Role: conditional. Run only when editable text, concepts, or copy testing is relevant.

- `copy_input_coverage_gate`: whether editable copy and required upstream message/proof inputs exist.
- `copy_asset_inventory`: inventory of provided copy assets or concepts.
- `copy_asset_request_list`: missing copy/materials that would improve scoring.
- `copy_scoring_rubric`: scoring dimensions and weights.
- `copy_message_fit_scorecard`: fit against segment message architecture.
- `proof_and_claim_clarity_audit`: whether proof and claims are clear, specific, and supported.
- `claim_risk_review`: risky or unsupported copy claims.
- `local_language_fit_audit`: local wording, translation, or cultural fit issues.
- `channel_copy_fit_matrix`: copy fit by channel or placement.
- `copy_quality_scorecard`: overall copy quality and priority.
- `copy_revision_briefs`: rewrite briefs, not final copy unless explicitly requested.
- `copy_test_backlog`: copy tests to validate.
- `competitor_copy_norm_scan`: competitor copy conventions and category norms.
- `marketplace_pdp_copy_fit`: PDP copy fit.
- `landing_page_copy_fit`: landing page copy fit.
- `retail_sales_copy_fit`: retail or sales copy fit.
- `short_video_script_hook_audit`: short-video hook assessment.
- `package_text_claim_audit`: packaging or visible text claim audit.
- `copy_performance_result_interpretation`: interpretation of provided copy performance data.
- `compliance_review_queue`: copy claims needing review.
- `html_creative_section`: S14-ready section draft in report_language when triggered.

## S06 score-kol-fit Outputs

Role: conditional. Run when creator/KOL/expert/reviewer decisions matter.

- `creator_input_coverage_gate`: whether creator, proof, segment, channel, budget, and rate inputs are sufficient.
- `creator_archetype_fit_scorecard`: best creator/reviewer/expert archetypes before candidate scoring.
- `creator_candidate_inventory`: user-provided or discovered candidate inventory.
- `creator_fit_scorecard`: creator fit summary.
- `creator_candidate_fit_scorecard`: scored candidates after user review gate.
- `creator_trust_proof_fit_matrix`: fit between creator role, trust barrier, proof need, and audience.
- `candidate_segment_audience_fit`: segment/audience fit per candidate.
- `candidate_content_proof_fit`: candidate ability to communicate required proof.
- `platform_relevance_map`: local platform relevance and format fit.
- `creator_recommendation_rationale`: detailed reasons, counter-reasons, risks, and confidence.
- `local_creator_execution_table`: local candidate or archetype action rows with rationale, budget range, expected signal, timing, owner, disclosure risk, and evidence basis.
- `content_seeding_wave_plan`: expert-review, comparison, lifestyle creator, community/forum, retail-media, and owner-review waves tied to proof needs and first-sale timing.
- `creator_budget_estimate`: conservative/base/upside marketing budget ranges.
- `creator_expected_outcome_estimate`: expected visits, interactions, engagement quality, traffic, or tracked intent ranges.
- `creator_budget_expectation_confidence`: confidence and basis for budget/outcome estimates.
- `brand_safety_risk_review`: brand, content, history, audience, and controversy risk.
- `sponsorship_disclosure_risk_review`: disclosure and platform policy risk.
- `creator_brief_pack`: briefing structure for creator outreach.
- `creator_test_backlog`: creator pilot validation tests.
- `creator_candidate_request_list`: candidates or data to request from user.
- `creator_sourcing_criteria`: search and selection criteria.
- `public_creator_discovery_plan`: bounded public discovery plan.
- `local_creator_discovery_query_bank`: local-language creator discovery queries.
- `creator_source_channel_map`: owned/rented/borrowed or local source-channel mapping.
- `creator_candidate_longlist`: public longlist before review.
- `creator_discovery_coverage_report`: coverage and limitations.
- `competitor_creator_overlap_map`: overlap with competitor creator/media activity.
- `creator_candidate_review_gate`: include/exclude/unsure gate.
- `creator_candidate_review_list`: reviewable candidate list.
- `creator_candidate_decision_log`: user decisions on candidates.
- `review_approved_candidate_set`: candidates approved for scoring/recommendation.
- `review_excluded_candidate_set`: excluded candidates and reasons.
- `category_creator_norm_scan`: category creator norms.
- `affiliate_or_reviewer_program_fit`: affiliate/reviewer program fit.
- `retail_expert_or_media_fit`: retailer expert, media, or specialist reviewer fit.
- `creator_performance_result_interpretation`: interpretation of provided creator results.
- `compliance_review_queue`: creator claim/disclosure review items.
- `html_creator_section`: S14-ready section draft in report_language when triggered.

## S07 predict-dtc-conversion Outputs

Role: conditional. Run when DTC, PDP, marketplace clickout, preorder, waitlist, or landing-page conversion matters.

- `conversion_input_coverage_gate`: whether page, offer, traffic, tracking, message, pricing, proof, and channel inputs exist.
- `prelaunch_conversion_planning_mode`: planning mode for prelaunch/no-live-data situations.
- `funnel_stage_inventory`: acquisition, page/PDP, cart, checkout, preorder, waitlist, clickout, and purchase stages.
- `traffic_source_assumption_map`: traffic source assumptions and basis.
- `segment_landing_page_fit_matrix`: segment fit to page/PDP structure and content.
- `offer_message_continuity_map`: continuity from message/offer to page/PDP/checkout.
- `proof_objection_friction_map`: proof gaps and objections that hurt conversion.
- `price_trust_checkout_friction_map`: price, trust, payment, delivery, return, and checkout frictions.
- `mobile_ux_friction_audit`: mobile readability and UX friction.
- `conversion_hypothesis_model`: hypotheses for conversion risk and opportunity.
- `cvr_assumption_ladder`: CVR assumptions by evidence level.
- `funnel_friction_scorecard`: scored funnel friction.
- `conversion_risk_guardrail`: limits on interpreting conversion proxies.
- `tracking_readiness_audit`: analytics, UTM, event, attribution, and reporting readiness.
- `page_or_funnel_material_request_list`: missing page/funnel assets.
- `competitor_landing_pdp_benchmark`: competitor PDP/landing benchmark.
- `previous_generation_funnel_learnings`: prior product funnel learnings when supplied.
- `category_page_requirement_brief`: category page/PDP requirements.
- `prelaunch_page_recommendation_pack`: planning recommendations before live traffic.
- `launch_tracking_requirement_brief`: event and measurement requirements.
- `landing_page_copy_fit_audit`: landing page copy fit.
- `pdp_checkout_trust_audit`: PDP/checkout trust audit.
- `retailer_clickout_conversion_fit`: retailer clickout path fit.
- `campaign_landing_match_audit`: campaign-message to landing-page match.
- `preorder_waitlist_flow_fit`: preorder or waitlist flow fit.
- `analytics_event_schema`: recommended event schema.
- `ab_test_plan`: page/offer/message/conversion A/B test plan.
- `conversion_performance_result_interpretation`: interpretation of uploaded performance results.
- `compliance_review_queue`: conversion-page claim review items.
- `dtc_conversion_model`: directional conversion model for S08.
- `funnel_friction_map`: visual/structured map of conversion friction.
- `page_experiment_plan`: experiments for S13.
- `html_conversion_section`: S14-ready section draft in report_language when triggered.

## S08 forecast-launch-demand Outputs

Role: visible. S08 forecasts launch unit sales and decision ranges.

- `forecast_input_coverage_gate`: whether sizing, segment, channel, price, conversion, creator, marketing, inventory, and private inputs are sufficient.
- `forecast_scope_boundary`: whether the forecast is demand potential, reachable demand, sell-in, sell-through, or supply-constrained shipment.
- `forecast_assumption_tree`: formulas, assumptions, ranges, basis labels, and confidence caps.
- `scenario_sales_forecast`: conservative/base/upside unit ranges.
- `segment_sales_split`: unit split by segment when supported.
- `launch_sales_forecast`: main launch forecast summary.
- `lifecycle_phase_sales_curve`: phase curve across warmup, launch spike, ramp, sustain, plateau/decay.
- `marketing_investment_response_model`: MKT spend response, adstock/saturation, and spend-to-sales bridge.
- `budget_posture_model`: conservative, standard, or aggressive launch budget posture with revenue-based, goal-based, and blended CAC checks.
- `aarrr_orb_channel_architecture`: hardware AARRR stage map joined to Owned/Rented/Borrowed channel roles and named local channel responsibilities.
- `local_channel_action_priority`: named local channel priority with role, capability score, budget seed, expected signal, required proof asset, owner, and tracking method.
- `gtm_judgment_cover`: first-screen commercial judgment with launch posture, core recommendation, opening move, priority segment, must-win channel, price/offer stance, competitor threat, budget posture, and decision-changing question.
- `gtm_command_center`: compact launch decision board with objective, hero claim, expected weekly sales, MKT posture, must-win channel, top competitor threat, and main risk.
- `channel_war_room`: named channel action table with readiness, owner, budget seed, first-week KPI, and required proof/asset.
- `launch_calendar`: T-30/T-14/T-7/T0/T+7/T+30 launch workstream plan for PR, KOL, retail, ecommerce, DTC, operator, service, supply, and measurement.
- `measurement_war_room`: daily or weekly KPI plan covering traffic, conversion, price integrity, stock, review volume, sentiment, competitor moves, and channel feedback.
- `competitive_response_playbook`: pre-agreed responses to competitor price drops, bundles, review pushes, retailer promos, claim attacks, stock advantage, or ecosystem pushes.
- `baseline_incremental_sales_bridge`: baseline versus incremental sales separation.
- `channel_split_forecast`: unit split by named channels when supported.
- `price_conversion_assumption_bridge`: how S04 price assumptions affect acceptance and conversion without double counting.
- `sensitivity_driver_tornado`: ranked assumptions that move the forecast most.
- `inventory_risk_map`: stockout, overstock, replenishment, allocation, or PO risk.
- `forecast_confidence_caps`: where forecast confidence is capped and why.
- `forecast_decision_gate`: usable for direction, budget, inventory, or not ready.
- `validation_need_map`: forecast assumptions to validate in S13.
- `launch_calendar_seasonality_adjustment`: calendar, seasonality, promo, or retail timing adjustment.
- `retail_sell_in_sell_through_split`: retail sell-in versus consumer sell-through split.
- `media_reach_to_demand_bridge`: media reach/click/lead/action bridge to units.
- `marketing_spend_sensitivity_curve`: spend range versus unit range.
- `creator_traffic_demand_bridge`: S06 creator traffic/outcome bridge to demand.
- `dtc_conversion_scenario_bridge`: S07 conversion bridge to forecast.
- `previous_generation_calibration`: calibration from previous-generation performance.
- `supply_constraint_scenario`: supply, allocation, lead-time, and replenishment constraints.
- `preorder_waitlist_projection`: preorder/waitlist projection.
- `gross_revenue_range_estimate`: revenue range only when price, currency, and display permission are explicit.
- `regional_channel_allocation`: region/channel allocation assumptions.
- `forecast_review_gate`: review status for private assumptions, inventory, budget, or channel decisions.
- `html_forecast_section`: S14-ready section draft in report_language.

## S09 predict-activation-risk Outputs

Role: conditional. Run for setup, onboarding, sizing, compatibility, app pairing, support, warranty, or return risk.

- `activation_return_trigger_check`: whether S09 should run and why.
- `activation_journey_risk_map`: setup/onboarding/compatibility/support journey risks.
- `expectation_gap_map`: mismatch between promised value and likely first experience.
- `return_prevention_priority`: ranked preventable return or dissatisfaction risks.
- `support_education_plan`: support, FAQ, onboarding, retail training, or education plan.
- `channel_expectation_guardrails`: PDP/retail/channel guardrails to reduce expectation mismatch.
- `html_activation_section`: S14-ready section when triggered.
- `post_skill_isolation_record`: isolation and reopen conditions.

## S10 generate-health-insights Outputs

Role: conditional. Run for wellness, health-adjacent, AI insight, safety, children, elderly, privacy, or regulated-adjacent claims.

- `insight_claim_trigger_check`: whether S10 should run and why.
- `insight_system_boundaries`: what the product can and cannot claim.
- `claim_guardrail_matrix`: allowed, needs-proof, avoid, or human-review claim boundaries.
- `privacy_safety_proof_need`: proof needed for privacy, safety, data, or vulnerable-user claims.
- `human_review_queue`: claims requiring legal, compliance, product, or safety review.
- `retention_insight_opportunities`: safe insight/retention opportunities without overclaiming.
- `html_insight_section`: S14-ready section when triggered.
- `post_skill_isolation_record`: isolation and reopen conditions.

## S11 predict-subscription-and-churn Outputs

Role: conditional. Run when the product has subscription, paid app, warranty plan, consumable, service, renewal, or recurring value loop.

- `subscription_retention_trigger_check`: whether S11 should run and why.
- `subscription_value_driver_map`: recurring value drivers and entitlement fit.
- `retention_value_driver_map`: retention drivers across activation, value realization, renewal, and service.
- `churn_risk_model`: qualitative churn risks with confidence caps.
- `retention_trigger_plan`: triggers and actions to improve retention.
- `pricing_retention_linkage`: link between price, recurring value, and churn risk.
- `html_subscription_section`: S14-ready section when triggered.
- `post_skill_isolation_record`: isolation and reopen conditions.

## S12 mine-review-quality-feedback Outputs

Role: conditional/post-launch. Run when reviews, support, returns, NSS/NPS, RMA, app reviews, warranty claims, or post-launch feedback exist.

- `feedback_loop_trigger_check`: whether S12 should run and why.
- `review_support_source_map`: source layers and permissions for public/private feedback.
- `voice_atom_collection_scope`: declared scope for collecting and deduplicating feedback.
- `feedback_theme_cluster`: feedback themes with frequency, sentiment, recency, consistency, and source separation.
- `quality_feedback_priority`: ranked quality/product/experience issues.
- `product_quality_backlog`: product or engineering action candidates.
- `gtm_feedback_backlog`: GTM, channel, support, messaging, and sales action candidates.
- `feedback_loop_action_map`: action owner, loop type, and downstream use.
- `evidence_graph_updates`: new evidence refs and graph updates.
- `html_feedback_section`: S14-ready section when triggered.
- `post_skill_isolation_record`: isolation and reopen conditions.

## S13 plan-validation-experiments Outputs

Role: hidden system capability. S13 should not appear as a visible business module
in the current dashboard unless explicitly requested.

- `validation_input_coverage_gate`: whether S13 has enough handoff, gap, deadline, budget, and access context.
- `assumption_inventory`: cross-module assumptions with source, decision linkage, impact, uncertainty, and confidence cap.
- `validation_question_backlog`: questions that would reduce decision risk.
- `experiment_priority_scorecard`: ICE-style prioritization with hardware feasibility, budget, risk, sample, and deadline constraints.
- `validation_experiment_roadmap`: smallest useful validation portfolio.
- `survey_test_plan`: survey or panel plan.
- `pricing_message_copy_test_plan`: price, message, copy, and proof validation plan.
- `channel_conversion_forecast_test_plan`: channel, conversion, forecast, and sell-through validation plan.
- `experiment_design_cards`: experiment cards with hypothesis, method, population, sample, metrics, pass/fail rules, owner, timing, cost, and failure action.
- `pass_fail_decision_rules`: decision thresholds before tests run.
- `sample_and_data_requirement_map`: respondent, traffic, retailer, creator, internal-data, or measurement requirements.
- `owner_timeline_effort_map`: owner, timeline, effort, and budget bands.
- `validation_decision_gate`: ready, decide-with-caveats, needs-validation, or blocked.
- `van_westendorp_execution_brief`: execution brief for acceptable price range.
- `gabor_granger_execution_brief`: execution brief for fixed price-point testing.
- `conjoint_dce_execution_brief`: execution brief for feature/price/bundle tradeoff testing.
- `landing_page_ab_test_brief`: landing/PDP/waitlist/preorder A/B test brief.
- `creator_pilot_test_brief`: creator/KOL pilot validation brief.
- `retailer_channel_validation_brief`: retail, marketplace, sell-in/sell-through, or channel test brief.
- `forecast_assumption_validation_brief`: S08 forecast assumption validation brief.
- `private_data_validation_path`: how private data can validate assumptions without public exposure.
- `post_launch_learning_plan`: learning loop after launch.
- `targeted_lookup_log`: any targeted lookup used by S13, with query budget and stop condition.
- `context_budget_report`: context use, escalations, and budget status.
- `html_validation_section`: generated but hidden by default in current dashboard policy.

## S14 compose-html-gtm-dashboard Outputs

Role: hidden composer. S14 renders; it does not invent or change conclusions.

- `render_input_gate`: whether report state, section drafts, evidence, gaps, decisions, and private calculator specs are sufficient.
- `section_registry_instance`: final ordered section map and skipped-section states.
- `executive_summary_panel`: management summary synthesized only from upstream decision updates and takeaways.
- `dashboard_navigation`: stable anchors and section navigation.
- `full_html_dashboard`: final offline static HTML file.
- `static_assets`: embedded or local static assets when used.
- `citation_index`: source refs, evidence IDs, titles, URLs, dates, and usage notes.
- `confidence_badge_map`: confidence labels and reasons by section and conclusion.
- `data_gap_panel`: visible gap list, priority, impact, and next validation action.
- `render_quality_report`: HTML quality, language, privacy, offline, citation, chart, and layout checks.
- `static_asset_manifest`: local asset manifest.

## Optional Expansion Slots

These are not active by default.

- `S15 compliance-claim-risk`: expands S10 into a dedicated compliance and claim-risk skill.
- `S16 localize-copy-and-creative`: expands S03/S05 into full local-language copy and creative localization.
- `S17 plan-retail-channel-strategy`: expands S01/S03/S07/S08 into a dedicated retail/channel strategy module.
- `S18 build-executive-deck`: converts report state into a presentation artifact in addition to HTML.

## Output Integrity Rules

- Business conclusions must come from S01-S12, not S14.
- S13 is a validation planner and context-control layer, not a market research rerun.
- `real_product_pilot` must keep deep voice collection bounded to reviewed competitors and must keep S13 hidden unless explicitly requested.
- Every visible section needs evidence refs, confidence, and data gaps.
- Optional modules should be skipped visibly when not triggered.
- Private COGS, margin, internal sales, channel terms, and raw private customer data must not enter public HTML unless explicitly approved.
- Downstream skills consume compressed handoffs by default, not full upstream artifacts.

