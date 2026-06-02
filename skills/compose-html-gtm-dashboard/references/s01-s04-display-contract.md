# S01-S04 Display Contract

Use this when rendering the first complete GTM dashboard from S01-S04. This file decides what must appear in the main report, what appears only when triggered, what belongs in appendices, and which display format best fits each output.

## Core Principle

S14 must turn analysis into an executive decision surface. Do not render every upstream table by default. Render the minimum set that answers:

```text
What did we learn?
How confident are we?
Why does it matter for GTM?
What decision or next action does it unlock?
What evidence or gap limits the conclusion?
```

Every core S01-S04 section should include:

```text
1. One executive takeaway
2. One confidence or coverage signal
3. One primary visual proof block
4. One risk/data-gap block
5. One downstream implication or next action block
```

If a section has only cards or generic text, mark it `rendered_too_thin` and request upstream section enrichment.

## Upstream Draft Alignment

S01-S04 should hand S14 an `html_section_draft.visual_blocks` array. S14 may render these block types directly:

```text
status_panel
ranked_bar
matrix_heatmap
range_chart
```

These are the only canonical values for `visual_blocks.type`. Method-level names such as `decision_status_panel`, `horizontal_range_chart`, `matrix_or_heatmap`, `scorecard_table`, `risk_table`, `action_table`, or `language_table` must be mapped to one of the four canonical types or rendered as `tables`, `metric_cards`, or `callouts` before S14 treats them as visual blocks.

If an upstream section has data for a required view but no `visual_blocks`, S14 may render a conservative table and add `missing_visual_block` to the render quality report. If the data itself is missing, S14 must add `missing_required_view` to the data-gap panel and must not invent chart values.

## Display Depth Rules

```text
executive_layer
  1-3 decisive findings per section. Use short text, scorecards, status panels, or a single priority chart.

analysis_layer
  The proof behind the executive finding. Use matrices, ranked tables, range charts, or risk tables.

detail_layer
  Supporting rows, source notes, caveats, and conditional modules. Use collapsible blocks or lower section placement.

appendix_layer
  Full source maps, candidate pools, raw comment refs, audit logs, assumption traces, and RAG refs.
```

Default dashboard depth:

```text
quick
  Show executive_layer only plus critical data gaps.

standard
  Show executive_layer and analysis_layer. Put detail_layer only where it changes decisions.

deep
  Show executive_layer, analysis_layer, triggered detail_layer, and appendices.
```

## Visual Selection Rules

```text
status_panel
  Use for decision gates, readiness states, blockers, and next owner.

metric_cards
  Use for 1-6 headline values. Never use as the only proof for a core section.

ranked_table
  Use for top competitors, segments, scenarios, objections, channels, actions, and tests.

matrix_heatmap
  Use when two dimensions matter: segment x scenario, feature x proof, price x segment, channel x segment.

scatter_or_2x2
  Use for prioritization: impact vs evidence, threat vs relevance, commercial weight vs confidence.

range_chart
  Use for price corridor, acceptable price bands, TAM/SAM/SOM ranges, or confidence intervals.

tornado_chart
  Use when driver contribution or sensitivity is the point. Use only with comparable numeric scores.

journey_matrix
  Use when stage changes GTM actions: discovery, comparison, purchase, setup, support, advocacy.

risk_table
  Use for blockers, anti-JTBD, claim risk, channel conflict, price risk, and data gaps.

action_table
  Use when the output is an instruction, experiment, proof requirement, or owner-linked next step.

card_grid
  Use for 3-5 scenarios, segment personas, or major options. Do not render more than 6 cards in the main body.

language_table
  Use for local trigger/search/message phrases with original language, translation/gloss, context, and source.

text_block
  Use only for interpretation, caveats, or narrative synthesis. Keep main text blocks short; tables carry detail.
```

Do not use charts when data is sparse, non-comparable, or confidence-capped. Render a table with caveats instead.

## S01 Display Plan: Localized Consumer Market Map

S01 answers: What is the local market reality, who matters, where demand lives, how reliable is the evidence, and which early GTM priorities follow?

### S01 Must Display

```text
1. Market confidence and evidence coverage with visible source identities
2. Product capability to local selling-point fit across enough adjacent/similar category drivers
3. Local language and search trigger map
4. Competitor/substitute threat, TOP1 proof board, and price landscape
5. Consumer voice themes, competitive Bain/NPS proxy board, and NSS/NPS proxy seed, large enough to guide marketing under fixed product constraints
6. TOP1 competitor and previous-generation voice deep dive with visible collection coverage, Bain/NSS/NPS seeds, and hardware journey scoring
7. Segment priority and segment evidence strength as an initial ranking, not a final segmentation decision
8. Channel/touchpoint and retailer/marketplace candidates
9. Initial GTM priorities and data gaps
```

### S01 Recommended Main Views

```json
[
  {
    "module": "evidence_coverage",
    "display_tier": "executive_layer",
    "primary_visual": "coverage_heatmap_plus_source_quality_scorecards",
    "fallback_visual": "coverage_table",
    "core_point": "Can we trust the local market map, and where is evidence thin?",
    "show_fields": ["coverage_summary", "source_quality_summary", "confidence_caps", "market_sizing_confidence", "local_source_map", "source_name", "source_url", "source_logo_or_favicon", "access_status"],
    "do_not_show_by_default": ["raw_collection_logs", "full_comment_exports"]
  },
  {
    "module": "category_selling_points_and_local_language",
    "display_tier": "analysis_layer",
    "primary_visual": "selling_point_fit_matrix_plus_language_table",
    "fallback_visual": "ranked_table",
    "core_point": "Which fixed product features map to mainstream local and adjacent-category benefits, search language, and marketing proof needs?",
    "show_fields": ["category_selling_point_map", "adjacent_category_selling_point_map", "similar_product_driver_map", "selling_point_fit_scores", "feature_to_local_language_map", "local_search_term_map", "search_query_seed_pack", "trend_signal_status", "marketing_watchouts_for_fixed_product"],
    "do_not_show_by_default": ["all_query_expansion_variants"]
  },
  {
    "module": "competitor_landscape",
    "display_tier": "executive_layer",
    "primary_visual": "competitor_threat_2x2_or_ranked_table",
    "fallback_visual": "comparison_table",
    "core_point": "Who are the real local competitors and substitutes, and why do they threaten the launch?",
    "show_fields": ["top_competitors_and_substitutes", "competitor_candidate_scoring", "top1_competitor_proof_board", "competitor_threat_scores", "substitute_taxonomy", "competitor_candidate_review_list", "competitor_discovery_query_trace", "user_calibration_status"],
    "do_not_show_by_default": ["full_candidate_pool_if_not_selected"]
  },
  {
    "module": "price_landscape_seed",
    "display_tier": "analysis_layer",
    "primary_visual": "price_ladder_with_target_band_overlay_and_jump_callouts",
    "fallback_visual": "ranked_price_anchor_table",
    "core_point": "Where does the target price sit against local anchors, and where might consumers jump price tiers?",
    "show_fields": ["local_price_corridor", "price_anchor_panel", "competitor_price_gap_table", "price_ladder_scan", "jump_decision_risks", "target_price_overlay", "jump_down_options", "jump_up_options"],
    "do_not_show_by_default": ["price_assumption_trace"]
  },
  {
    "module": "consumer_voice",
    "display_tier": "executive_layer",
    "primary_visual": "voice_theme_panel_plus_selling_point_marketing_watchout_matrix",
    "fallback_visual": "theme_cluster_cards",
    "core_point": "Given that the product is fixed, what should marketing emphasize, prove, avoid, or localize based on local consumer praise, complaints, and buying proof?",
    "show_fields": ["local_voice_source_map", "voice_storage_compression_policy", "top1_previous_generation_voice_scope", "voice_collection_coverage_report", "bain_nss_journey_seed_panel", "competitive_bain_voice_board", "consumer_voice_processing_summary", "voice_theme_clusters", "pain_theme_clusters", "purchase_triggers", "objections", "nss_nps_proxy_source_mix", "nps_driver_tornado_seed", "bain_driver_inputs", "journey_episode_inputs", "selling_point_voice_alignment", "marketing_watchouts_for_fixed_product", "proof_required_before_claim"],
    "do_not_show_by_default": ["voice_atom_table_full", "full_comment_dump"]
  },
  {
    "module": "segment_priority",
    "display_tier": "executive_layer",
    "primary_visual": "segment_priority_2x2_or_ranked_table",
    "fallback_visual": "scorecard_table",
    "core_point": "Which segments should GTM investigate and prioritize first, and how strong is the evidence?",
    "show_fields": ["segment_priority_ranking", "segment_evidence_strength_scores", "segment_level_tam_sam_som", "persona_cards", "hypothesis_label", "validation_needed"],
    "do_not_show_by_default": ["demographic_only_persona_details", "low_priority_segment_pool"]
  },
  {
    "module": "channel_touchpoints",
    "display_tier": "analysis_layer",
    "primary_visual": "local_channel_priority_table_plus_segment_channel_touchpoint_matrix",
    "fallback_visual": "ranked_channel_table",
    "core_point": "Where can the brand reach, educate, and convert each priority segment?",
    "show_fields": ["local_channel_priority", "segment_channel_touchpoint_map", "channel_fit_scores", "retailer_marketplace_candidates", "content_proof_map", "channel_scoring_method"],
    "do_not_show_by_default": ["user_planned_channels_without_local_evidence"]
  },
  {
    "module": "initial_gtm_priorities",
    "display_tier": "executive_layer",
    "primary_visual": "action_table",
    "fallback_visual": "callout_list",
    "core_point": "What are the first GTM priorities implied by the market map?",
    "show_fields": ["initial_gtm_priorities", "next_generation_marketing_sales_seed", "hardware_experience_diagnosis_seed"],
    "do_not_show_by_default": ["final_budget_allocation", "final_kol_selection"]
  }
]
```

### S01 Display Notes

```text
evidence_coverage
  This is not only a status gate. Render it as a polished source coverage map with source names, URLs, favicons/logos when available, access status, collection role, evidence quality, and last checked date. It should look like a market-source board, not a plain checklist.

category_selling_points_and_local_language
  The matrix must include enough mainstream and adjacent-category drivers to make positioning clear. Do not compare only against the user's own 3-5 product claims. Mark strongest fit, proof gap, and "marketing watchout" for fixed product limitations.

local_search_and_competitor_discovery
  Show the bridge from local search terms to sources/channels to candidate competitors to user calibration. Search trends are only directional language signals; competitor candidates should remain preliminary until the user confirms include/exclude/add decisions. Render dense search/competitor tables as full-width blocks when they have more than six columns.

top1_competitor_proof_board
  The report must explain why the selected competitor is TOP1 using the weighted proof formula from S01: price pressure, feature substitution, local channel overlap, voice/review evidence, ecosystem lock-in, and decision-journey interception. Show the selected competitor, 5-10 alternative candidates when available, the factor scores, and exceptions where previous generation or internal price-ladder risk is more important for a segment.

local_voice_sources
  Show named local consumer-voice sources before showing themes: source name, URL when available, source type, access status, collection role, evidence quality, raw artifact ref, and downstream use. Raw comments stay in local artifacts; the dashboard shows source coverage, short permitted excerpts, compressed clusters, sample counts, and data gaps.

top1_previous_generation_voice_deep_dive
  Once competitor discovery is user-calibrated, show the two deep-dive objects: TOP1 competitor and previous-generation product or internal benchmark. Render the collection scope and coverage report so the reader can see which forums, local-language reviews, video comments, retailer reviews, pages, threads, and comments were fully enumerated. "All viewpoints" is bounded by confirmed source scope, access rights, page range, and platform policy; blocked or unavailable content must appear as a coverage gap.

consumer_voice_bain_hardware_journey
  Keep Bain/NSS/NPS method consistent: source-item-level promoter/passive/detractor classification, deduped voice atoms, Driver Impact Score, and journey episode inputs. Adapt journey labels to hardware decisions such as purchase, delivery, unboxing, setup/pairing, first use, first 7 days, app experience, support/return, and repurchase/referral. Show pain, praise, purchase triggers, objections, and marketing implications together.

competitive_bain_voice_board
  Render a lane-based comparison for our product, TOP1 competitor, and previous generation or internal benchmark when available. If our product has no pre-launch voice, show the proof agenda and expected objections instead of inferred sentiment. Label the board `NPS Proxy / Bain VOC` unless surveyed NPS/NSS exists.

price_landscape_seed
  Make the price view easy to read: show a horizontal ladder with low/mid/target/premium zones, target price overlay, top competitor anchors, jump-down options, jump-up options, and a short interpretation. Use a table below only for details.

consumer_voice
  This block should be large in standard/deep mode. Combine voice themes with the selling-point matrix to answer: since the product is fixed, which claims should marketing emphasize, which claims need proof, which objections need handling, and which promises should be avoided.

segment_priority
  Treat this as an initial segment ranking. It routes S02/S03/S04/S08/S13, but it is not final segmentation. Keep hypothesis/data-gap labels visible until validated by local voice, channel, conversion, or sales evidence.
```

### S01 Appendix By Default

```text
evidence_research_design
evidence_collection_runner
site_specific_comment_profiles
comment_collection_coverage_reports
voice_collection_coverage_report
comment_export_refs
voice_atom_table_full
tam_sam_som_assumption_tree_full
comparable_market_proxies_full
segment_candidate_pool
segment_distinctness_results
raw NSS/NPS proxy classification rows
RAG index and collection logs
```

## S02 Display Plan: JTBD Demand Scenarios

S02 answers: Which demand scenarios are worth serving, what proof is required, what risks could invalidate them, and what must downstream messaging/pricing test?

### S02 Must Display

```text
1. Upstream input coverage gate when confidence is capped
2. Lead JTBD scenarios
3. Scenario priority and evidence strength
4. Scenario-to-segment relationship
5. Product-job fit and proof requirements
6. Anti-JTBD and non-consumption risks
7. Local trigger phrases and price implications
8. Validation questions for weak-but-important hypotheses
```

### S02 Recommended Main Views

```json
[
  {
    "module": "scenario_priority",
    "display_tier": "executive_layer",
    "primary_visual": "scatter_or_ranked_table",
    "fallback_visual": "ranked_table",
    "core_point": "Which jobs are commercially important and evidence-supported enough to lead GTM?",
    "show_fields": ["scenario_priority_scorecard", "scenario_commercial_weight_map", "evidence_strength_score", "confidence", "scoring_formula_note"],
    "do_not_show_by_default": ["jtbd_candidate_pool", "scenario_cluster_trace"]
  },
  {
    "module": "jtbd_scenario_cards",
    "display_tier": "executive_layer",
    "primary_visual": "card_grid",
    "fallback_visual": "ranked_table",
    "core_point": "What exact situation, motivation, desired outcome, current alternative, and barrier define each lead job?",
    "show_fields": ["jtbd_scenario_pack.top_3_to_5", "job_statement", "current_alternatives", "barriers_and_anxieties", "proof_requirements", "confidence", "data_gaps", "neutral_label_style"],
    "do_not_show_by_default": ["all_low_priority_scenarios"]
  },
  {
    "module": "scenario_to_segment_matrix",
    "display_tier": "analysis_layer",
    "primary_visual": "matrix_heatmap",
    "fallback_visual": "grouped_table",
    "core_point": "Which priority segments map to which jobs?",
    "show_fields": ["scenario_to_segment_matrix", "primary_segments", "secondary_segments"],
    "do_not_show_by_default": ["segment rows with no meaningful scenario relationship"]
  },
  {
    "module": "product_job_fit_matrix",
    "display_tier": "analysis_layer",
    "primary_visual": "scorecard_table_or_heatmap",
    "fallback_visual": "ranked_table",
    "core_point": "Where should the fixed product be lit up as high-fit, and where does it need proof, support, or softer marketing framing?",
    "show_fields": ["product_job_fit_matrix", "product_capability_fit", "proof_requirement_seed", "high_fit_highlight", "proof_gap_badge", "marketing_watchout"],
    "do_not_show_by_default": ["capability details that do not affect scenarios"]
  },
  {
    "module": "proof_and_risk",
    "display_tier": "executive_layer",
    "primary_visual": "proof_action_table_plus_risk_table",
    "fallback_visual": "callout_list",
    "core_point": "Which purchase risks must marketing solve indirectly through proof, reassurance, experience cues, social proof, onboarding, or offer design?",
    "show_fields": ["proof_requirement_seed", "anti_jtbd_risk_list", "non_consumption_risk_map", "implicit_risk_resolution", "do_not_say_directly"],
    "do_not_show_by_default": ["risk scoring trace"]
  },
  {
    "module": "local_trigger_and_price_implication",
    "display_tier": "analysis_layer",
    "primary_visual": "language_table_plus_price_implication_scorecard",
    "fallback_visual": "grouped_table",
    "core_point": "How do local consumers express the job, and what does that imply for price, offer, and proof?",
    "show_fields": ["local_language_trigger_phrase_map", "scenario_price_implication_seed", "price_implication_formula", "price_posture"],
    "do_not_show_by_default": ["raw translation variants"]
  },
  {
    "module": "downstream_constraints",
    "display_tier": "conditional_detail",
    "primary_visual": "journey_matrix_or_action_table",
    "fallback_visual": "grouped_table",
    "core_point": "Which downstream channel, retailer, behavior, or claim constraints change GTM execution?",
    "show_fields": ["consumer_electronics_gtm_moment_map", "digital_shelf_and_retailer_decision_map", "behavioral_science_lever_map", "brand_claim_constraint_map", "validation_question_seed"],
    "do_not_show_by_default": ["trigger_absent_conditional_modules"]
  }
]
```

### S02 Display Notes

```text
scenario_cards
  In Chinese dashboard text, avoid sentence frames such as "而不是..." or "不是...而是...". Use neutral labels instead: 触发情境, 想完成的进步, 当前替代方案, 主要阻力, 需要证明. This keeps the report constructive and easier to scan.

scenario_priority
  Show the scoring standard in small text near the visual: 场景优先级 = 任务频率 + 痛苦强度 + 切换意愿 + 产品适配 + 证明成熟度 + 渠道可达 + 商业价值 - 不购买风险. If exact weights are unavailable, label it as a scoring rubric rather than a measured formula.

product_job_fit_matrix
  Use a heatmap where high product-job fit is visually lit up. Recommended cell labels: 高适配可主打, 高适配但缺证明, 中适配需转译, 低适配不主打. Keep proof-readiness and marketing-watchout badges in the same row so a bright fit cell does not imply the claim is ready.

anti_jtbd
  Treat risks as marketing problems to resolve indirectly, not as literal ad copy. Convert each risk into proof assets, third-party/social proof, onboarding cues, comparison education, warranty/return reassurance, privacy/safety reassurance, or offer design. Do not write dashboard recommendations that tell marketers to say the consumer fear directly.

scenario_price_implication
  Calculate scenario price posture from value urgency, current alternative cost, competitor anchor pressure, proof readiness, brand trust, channel norms, and price sensitivity. Output categories should include premium_justification, parity_required, promo_dependency, affordability_pressure, or value_uncertainty, with confidence and evidence refs.
```

### S02 Appendix By Default

```text
upstream_input_map
jtbd_source_map
jtbd_candidate_pool
jtbd_scenario_clusters
scenario_distinctness_results
full scenario-to-journey matrix when it does not change downstream work
```

## S03 Display Plan: Segment Message Architecture

S03 answers: What should the product say to each segment, what proof is required, what objections must be handled, and which claims are unsafe or unready?

### S03 Must Display

```text
1. Message-market fit scorecard
2. Message investment allocation seed with percent split, budget note, and recommended MKT carrier/persona archetype
3. Segment message architecture
4. Feature-benefit-proof system
5. Objection handling matrix
6. Claim risk and proof gate as a local PR guide
7. Local language message seeds
8. Selling-point ranking with target segment, touchpoint channel, creator/media carrier, and budget signal
9. Price message seeds for S04/S05/S07/S13 execution
10. Message test backlog when confidence is weak
```

### S03 Recommended Main Views

```json
[
  {
    "module": "message_market_fit",
    "display_tier": "executive_layer",
    "primary_visual": "scorecard_table",
    "fallback_visual": "metric_cards_plus_table",
    "core_point": "Which segment-message pairs are strong enough to guide GTM, and which are still weak?",
    "show_fields": ["message_market_fit_scorecard", "confidence_caps", "data_gaps", "message_investment_allocation_seed", "budget_note", "recommended_mkt_carrier_archetype"],
    "do_not_show_by_default": ["message scoring trace"]
  },
  {
    "module": "message_investment_allocation",
    "display_tier": "executive_layer",
    "primary_visual": "allocation_bar_plus_role_cards",
    "fallback_visual": "ranked_table",
    "core_point": "How should initial message testing and MKT attention be split across lead message routes, and who should carry each route?",
    "show_fields": ["message_route", "recommended_percent", "budget_note", "mkt_carrier_archetype", "channel_fit", "proof_dependency", "confidence"],
    "do_not_show_by_default": ["final_media_plan", "final_kol_selection", "final_budget_approval"]
  },
  {
    "module": "segment_message_architecture",
    "display_tier": "executive_layer",
    "primary_visual": "message_route_swimlane_or_message_house",
    "fallback_visual": "card_grid",
    "core_point": "What value angle, benefit, proof, objection, and avoid-language belong to each priority segment?",
    "show_fields": ["segment_message_architecture", "message_role", "message_angle_seed", "primary_benefit", "proof_requirements", "objections_to_address", "claims_to_avoid", "channel_or_mkt_carrier", "investment_percent"],
    "do_not_show_by_default": ["final_ad_copy"]
  },
  {
    "module": "feature_benefit_proof_matrix",
    "display_tier": "analysis_layer",
    "primary_visual": "proof_stack_or_claim_readiness_ladder",
    "fallback_visual": "proof_status_table",
    "core_point": "Which features can credibly support which benefits, and where is proof missing?",
    "show_fields": ["feature_benefit_proof_matrix", "proof_status", "proof_asset_refs", "claim_risk", "proof_gap", "recommended_proof_asset", "s13_validation_task"],
    "do_not_show_by_default": ["unsupported claim variants"]
  },
  {
    "module": "selling_point_segment_touchpoint_kol_seed",
    "display_tier": "executive_layer",
    "primary_visual": "ranked_route_table_or_swimlane",
    "fallback_visual": "ranked_table",
    "core_point": "Which selling points should lead, which segment they serve, which touchpoints carry them, and which KOL/media archetype or candidate source should prove them?",
    "show_fields": ["selling_point_rank", "feature_or_capability", "benefit", "target_segment", "jtbd_scenario", "local_language_terms", "touchpoint_channels", "recommended_mkt_carrier_archetype", "candidate_or_source_hint", "budget_signal", "expected_signal", "proof_dependency", "confidence"],
    "do_not_show_by_default": ["final_kol_contracting", "unverified_creator_rates", "final_media_plan"]
  },
  {
    "module": "objection_and_do_not_claim",
    "display_tier": "executive_layer",
    "primary_visual": "risk_action_table",
    "fallback_visual": "ranked_table",
    "core_point": "What objections can block conversion, and what must the brand not say?",
    "show_fields": ["objection_matrix", "response_strategy_seed", "proof_needed", "do_not_say", "objection_severity_score"],
    "do_not_show_by_default": ["low_severity_objections_when_space_limited"]
  },
  {
    "module": "claim_risk_and_proof_gate",
    "display_tier": "executive_layer",
    "primary_visual": "risk_table",
    "fallback_visual": "callout_list",
    "core_point": "Which claims are available, partial, missing, risky, or require local PR/legal review?",
    "show_fields": ["claim_risk_and_proof_gate", "compliance_review_queue", "local_pr_guidance", "approved_claim_boundary", "do_not_say", "review_owner"],
    "do_not_show_by_default": ["legal approval language unless provided"]
  },
  {
    "module": "local_language_and_price_message_seed",
    "display_tier": "analysis_layer",
    "primary_visual": "language_table_plus_price_message_table",
    "fallback_visual": "grouped_table",
    "core_point": "Which local words and price messages should downstream creative, pricing, landing page, creator, retail, and validation teams preserve or test?",
    "show_fields": ["local_language_message_seed", "price_message_seed", "testable_hypothesis", "recommended_execution_owner", "validation_method", "success_signal"],
    "do_not_show_by_default": ["final translation", "final copy"]
  },
  {
    "module": "conditional_execution_seeds",
    "display_tier": "conditional_detail",
    "primary_visual": "action_table",
    "fallback_visual": "grouped_table",
    "core_point": "What should retail, landing page, creator, and testing teams do with the message architecture?",
    "show_fields": ["competitive_contrast_matrix", "behavioral_lever_message_seed", "retail_sales_talk_track_seed", "landing_page_message_block_seed", "creator_brief_message_seed", "message_test_backlog"],
    "do_not_show_by_default": ["trigger_absent_conditional_modules"]
  }
]
```

### S03 Display Notes

```text
message_investment_allocation
  S03 may recommend initial percentage split for message testing/MKT attention, not final media budget approval. Show percent allocation across message routes, a simple budget note, confidence, and the recommended carrier archetype: brand official, retailer sales, expert reviewer, lifestyle creator, category KOL, community advocate, paid social, PR, or owned DTC. Actual creator/KOL selection belongs to S06, and final budget allocation belongs to S08/S13 after validation.

segment_message_architecture
  Avoid a heavy grouped table as the default. Prefer a Message Route Swimlane: rows are priority segment/scenario, columns are lead promise, support proof, objection to resolve, channel/carrier, investment percent, and do-not-say. For a more strategic first view, use a Message House: roof = positioning idea, pillars = 3-4 value pillars, foundation = proof points and claims to avoid. Keep details in a table below.

feature_benefit_proof_matrix
  Avoid making every proof view another heatmap. Use a Proof Stack or Claim Readiness Ladder when possible: feature -> benefit -> proof asset -> readiness -> claim boundary -> validation task. This gives stronger viewpoint than a generic matrix and makes missing proof feel actionable.

selling_point_segment_touchpoint_kol_seed
  This is the bridge the local MKT team can execute. Each row should connect a product selling point to a priority segment/JTBD, local phrase, touchpoint channel, recommended carrier archetype, provisional candidate/source hint, rough budget signal, and expected validation signal. Candidate names are allowed only as provisional evidence-backed hints until S06 or user review approves them.

claim_risk_and_proof_gate
  Keep this as local PR guidance. It should say which claims are safe, which need cautious wording, which require proof/review, and which should be avoided in PR, retail scripts, creator briefs, landing pages, and paid ads.

price_message_seed
  Price message seeds are not decorative. They tell S04 what value proof or offer framing affects WTP, tell S05 what copy variants to test, tell S07 how to structure the price/value block, tell S06 what creators or reviewers should demonstrate, and tell S13 which price narrative tests to run. Each seed should include what it can validate, who should use it, how to execute it, and what success signal to watch.
```

### S03 Appendix By Default

```text
message_source_trace
message_variant_pool
rejected_message_angles
claim_evidence_audit
full conditional seeds when they are not triggered
```

## S04 Display Plan: Opening Price Strategy And Profit Boundary

S04 answers: What price should the product open with, whether it should use high-anchor promo, parity/value, penetration attack, niche high-price, or test-before-scale posture, how MSRP differs from transaction price, what private economics are needed to find revenue-max and profit-max points, and what price path should run through the first 30/60/90 days.

### S04 Must Display

```text
1. Pricing decision gate
2. Opening price strategy and strategic objective
3. Launch price architecture: public anchor, transaction range, promo floor, channel floor, revenue-max, profit-max
4. Local price credibility and target price context
5. Rapid WTP prior with factor weights when real WTP or sales evidence is unavailable
6. WTP direct conclusion: whether the target price can be defended, for whom, and with which proof or offer
7. Segment WTP hypotheses and price sensitivity
8. Price-value proof matrix
9. Price risk guardrails
10. WTP/pricing test plan
11. Promo/subscription/channel guidance
12. Private profit/revenue optimizer and pricing calculator when specified
13. 30/60/90 price path
14. Handoff summary to S07/S08/S13
```

### S04 Recommended Main Views

```json
[
  {
    "module": "pricing_decision_gate",
    "display_tier": "executive_layer",
    "primary_visual": "status_panel",
    "fallback_visual": "callout_plus_option_table",
    "core_point": "What is pricing ready for now: research, controlled test, finance review, channel review, forecast, or decision review?",
    "show_fields": ["pricing_decision_gate.status", "status_reason", "hard_blockers", "candidate_options", "recommended_path", "downstream_readiness"],
    "do_not_show_by_default": ["raw_private_values"]
  },
  {
    "module": "opening_price_strategy",
    "display_tier": "executive_layer",
    "primary_visual": "status_panel_plus_strategy_scorecards",
    "fallback_visual": "ranked_table",
    "core_point": "Which opening price posture should be used, and why should the product open high, attack with price, stay at parity, preserve niche premium, or test first?",
    "show_fields": ["opening_price_strategy", "recommended_strategy", "strategic_objective", "strategy_scores", "recommended_public_anchor", "recommended_transaction_mechanism", "conditions_required", "do_not_do", "confidence"],
    "do_not_show_by_default": ["raw_private_values", "unscored_strategy_opinions"]
  },
  {
    "module": "launch_price_architecture",
    "display_tier": "executive_layer",
    "primary_visual": "price_architecture_ladder",
    "fallback_visual": "price_point_table",
    "core_point": "What are the separate price points for positioning, conversion, floor protection, revenue maximization, and profit maximization?",
    "show_fields": ["launch_price_architecture", "public_anchor_price_or_msrp", "expected_transaction_price_range", "promo_floor_price", "channel_floor_price", "revenue_max_price", "profit_max_price", "calculation_mode", "private_fields_required"],
    "do_not_show_by_default": ["raw COGS", "raw margin", "raw elasticity", "raw channel terms"]
  },
  {
    "module": "local_price_credibility",
    "display_tier": "executive_layer",
    "primary_visual": "range_chart_plus_scorecard",
    "fallback_visual": "price_anchor_table",
    "core_point": "Does the target price feel normal, premium, risky, or abnormal in the local category?",
    "show_fields": ["local_price_credibility_model", "local_price_corridor", "price_anchor_panel", "competitor_price_gap_table"],
    "do_not_show_by_default": ["price_anchor_audit_full"]
  },
  {
    "module": "rapid_price_prior",
    "display_tier": "executive_layer",
    "primary_visual": "ranked_bar_plus_evidence_cap_badges",
    "fallback_visual": "factor_score_table",
    "core_point": "When there is no real WTP study, what quantified prior can we defend, and which weak factors must S13 calibrate?",
    "show_fields": ["rapid_price_prior", "rapid_wtp_prior_score", "wtp_prior_range", "factor_scores", "evidence_grade", "confidence_cap", "calibration_plan"],
    "do_not_show_by_default": ["synthetic_persona_votes", "fake_precision_wtp"]
  },
  {
    "module": "wtp_direct_conclusion",
    "display_tier": "executive_layer",
    "primary_visual": "verdict_card_plus_segment_table",
    "fallback_visual": "callout_plus_ranked_table",
    "core_point": "What is the direct WTP answer: defend the price, defend with proof/offer, reduce effective price, research first, or block the decision?",
    "show_fields": ["wtp_direct_conclusion", "plain_language_answer", "target_price_defensibility", "segments_that_can_accept", "segments_that_resist", "minimum_proof_or_offer_required", "recommended_opening_posture", "price_move_thresholds", "confidence"],
    "do_not_show_by_default": ["synthetic_persona_votes", "raw_private_values", "fake_precision_wtp"]
  },
  {
    "module": "segment_wtp_and_sensitivity",
    "display_tier": "analysis_layer",
    "primary_visual": "segment_price_heatmap_or_scorecard_table",
    "fallback_visual": "ranked_table",
    "core_point": "Which segments are likely to tolerate, resist, or require proof for the target price?",
    "show_fields": ["segment_wtp_hypothesis", "price_sensitivity_model", "segment_price_sensitivity_seeds"],
    "do_not_show_by_default": ["synthetic_persona_votes"]
  },
  {
    "module": "price_value_proof",
    "display_tier": "analysis_layer",
    "primary_visual": "price_value_proof_matrix",
    "fallback_visual": "proof_action_table",
    "core_point": "What proof is required to sustain parity, premium, financing, bundle, or launch offer posture?",
    "show_fields": ["price_value_proof_matrix", "value_proof_requirement_matrix", "claim_risk_and_proof_gate"],
    "do_not_show_by_default": ["unapproved claims"]
  },
  {
    "module": "price_risk_guardrails",
    "display_tier": "executive_layer",
    "primary_visual": "risk_table",
    "fallback_visual": "callout_list",
    "core_point": "What pricing risks could damage conversion, margin, channel, trust, or support outcomes?",
    "show_fields": ["price_risk_guardrail", "promo_subscription_guidance", "retail_price_integrity_map"],
    "do_not_show_by_default": ["final discount budget"]
  },
  {
    "module": "pricing_tests",
    "display_tier": "executive_layer",
    "primary_visual": "test_action_table",
    "fallback_visual": "experiment_seed_cards",
    "core_point": "What test is required to turn price hypotheses into usable evidence?",
    "show_fields": ["wtp_test_plan", "pricing_test_execution_kit", "van_westendorp_test_design", "gabor_granger_test_design", "conjoint_dce_test_plan", "pricing_test_result_interpretation"],
    "do_not_show_by_default": ["full survey questionnaire unless deep mode"]
  },
  {
    "module": "private_pricing_calculator",
    "display_tier": "conditional_detail",
    "primary_visual": "client_side_calculator",
    "fallback_visual": "formula_spec_callout",
    "core_point": "Let users test COGS, margin, channel fee, and promo economics locally without exposing private inputs to the model.",
    "show_fields": ["private_pricing_calculator_spec"],
    "do_not_show_by_default": ["prefilled COGS", "raw margin", "channel terms", "internal sales data"]
  },
  {
    "module": "private_profit_revenue_optimizer",
    "display_tier": "conditional_detail",
    "primary_visual": "client_side_calculator_plus_curve_placeholders",
    "fallback_visual": "formula_spec_callout",
    "core_point": "Let users find revenue-max and profit-max price locally without exposing private demand, COGS, channel, MKT, or elasticity inputs.",
    "show_fields": ["private_profit_revenue_optimizer_spec", "candidate_price_grid", "computed_fields", "formula_notes", "downstream_handoff_policy"],
    "do_not_show_by_default": ["prefilled private values", "raw sales data", "raw elasticity", "raw COGS"]
  },
  {
    "module": "price_path_30_60_90",
    "display_tier": "executive_layer",
    "primary_visual": "phase_plan_matrix",
    "fallback_visual": "action_table",
    "core_point": "How should price, offer, and guardrails evolve in day 0-30, 31-60, and 61-90?",
    "show_fields": ["price_path_30_60_90", "phase", "price_posture", "offer_mechanism", "decision_trigger", "watch_metrics", "guardrails", "allowed_moves", "forbidden_moves", "owner_hint"],
    "do_not_show_by_default": ["final discount calendar"]
  },
  {
    "module": "pricing_handoff_summary",
    "display_tier": "analysis_layer",
    "primary_visual": "handoff_action_table",
    "fallback_visual": "callout_list",
    "core_point": "What should S07, S08, S13, and the human pricing owner use next?",
    "show_fields": ["pricing_handoff_summary", "data_gaps", "recommended_next_skills"],
    "do_not_show_by_default": ["final approved price without internal constraints"]
  }
]
```

### S04 Display Notes

```text
wtp_direct_conclusion
  This is the first thing a commercial reader needs from pricing. It must state whether the target price is defendable, defendable only with proof or offer design, too high for the lead segment, or blocked by evidence gaps. It should name the accepting and resisting segments, the minimum proof/offer required, and the next validation signal. Do not let a detailed WTP model appear without this direct conclusion.

segment_wtp_and_sensitivity
  Segment WTP rows should explain why a segment tolerates or resists the price: income and affordability context, competitor anchors, previous-generation anchor, product-job urgency, proof readiness, channel norms, and offer availability. Keep public proxy estimates separate from measured WTP.
```

### S04 Appendix By Default

```text
opening_strategy_score_trace
launch_price_architecture_assumption_trace
price_anchor_audit
competitor_price_gap_audit
price_assumption_log
sensitivity_calculation_trace
private_pricing_input_register
private_profit_revenue_optimizer_formula_trace
full Van Westendorp/Gabor-Granger/Conjoint questionnaires unless requested
```

## Cross-Section Narrative Order

The first complete S01-S04 dashboard should tell this story:

```text
1. Market truth
  What local evidence says, how reliable it is, and where the category language/competitors/segments are.

2. Demand logic
  Which jobs/scenarios explain why people would care and what they are currently using instead.

3. Message logic
  What must be said, proven, avoided, and localized for each priority segment.

4. Price logic
  What opening price posture to use, how public anchor differs from transaction price, what proof/economics/tests are needed, and what decision gate is unlocked.
```

## Minimum S01-S04 Dashboard Checklist

Before S14 marks an S01-S04 dashboard as complete, verify:

```text
S01
  Evidence coverage, TOP1 proof board, competitor landscape, competitive Bain/NPS proxy board, consumer voice, segment priority, channel map, and price corridor are visible.

S02
  Top scenarios, priority/evidence scores, product-job fit, proof needs, anti-JTBD risks, and local trigger phrases are visible.

S03
  Segment message architecture, proof matrix, selling-point/segment/touchpoint/KOL seed, objection matrix, claim risk/proof gate, and local/price message seeds are visible.

S04
  Pricing decision gate, opening price strategy, launch price architecture, price credibility, rapid WTP prior when needed, WTP direct conclusion, segment WTP/sensitivity, proof matrix, risk guardrails, test plan, private optimizer/calculator policy, and 30/60/90 price path are visible.

All sections
  Each core conclusion has confidence, evidence refs or citation caveat, data gaps, and downstream implication.
```

If any required view is missing, do not pad the UI. Add a visible `missing_required_view` gap and request upstream enrichment.
