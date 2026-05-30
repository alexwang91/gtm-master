# Suite Implementation Roadmap

Use this when planning, sequencing, or auditing the GTM skill suite buildout. The roadmap defines what to implement after S00 and S01, what each step needs from upstream skills, where the user can intervene, and what "done" means.

## Build Status

```text
S00.gtm-master
  Status: architecture scaffolded.
  Owns: orchestration, gates, handoff-only runtime, evidence/report state policy.

S01.build-consumer-market-map
  Status: active detailed buildout in progress.
  Owns: localized market context, source discovery, competitor/substitute map, consumer voice, TAM/SAM/SOM seed, segment/persona seed, channel/touchpoint seed, price seed, NSS/NPS seed.

S02.mine-jtbd-scenarios
  Status: detailed scaffold created.
  Owns: JTBD source mapping, scenario clustering, scenario priority, proof needs, anti-JTBD risks, validation seeds, HTML JTBD section.

S03.match-messages-to-segments
  Status: detailed scaffold created.
  Owns: segment message architecture, feature-benefit-proof, objection handling, claim/proof gates, local language message seeds, price message seeds, HTML message section.

S04.model-price-sensitivity
  Status: detailed scaffold created and expanded.
  Owns: local price credibility, segment WTP hypotheses, price sensitivity model, price-value proof, promo/subscription guidance, WTP test plans, private local pricing calculator, pricing test execution kit, pricing test result interpretation, pricing decision gate, pricing risk guardrails, HTML pricing section.

S05.score-creative-assets
  Status: detailed scaffold created.
  Owns: optional editable-copy scoring, proof/claim clarity, local language fit, channel copy fit, revision briefs, copy test backlog, HTML creative section.

S06.score-kol-fit
  Status: detailed scaffold created.
  Owns: optional creator/KOL discovery and scoring, review gates, recommendation rationale, budget/outcome ranges, brand-safety and sponsorship risk, HTML creator section.

S07.predict-dtc-conversion
  Status: detailed scaffold created and expanded for optional skip/prelaunch/live modes.
  Owns: DTC/PDP/preorder/waitlist conversion planning, competitor and previous-generation page benchmarks, prelaunch page requirements, tracking readiness, experiment backlog, HTML conversion section.

S08.forecast-launch-demand
  Status: detailed scaffold created and expanded for launch sales, lifecycle phase curves, and MKT investment response.
  Owns: launch unit-sales scenarios, sell-in/sell-through boundary, channel split, inventory risk, baseline vs marketing-incremental bridge, validation needs, HTML forecast section.

S09-S12
  Status: future conditional branch with trigger matrix; detailed skill specs not created yet.
  Trigger source: references/s09-s12-trigger-matrix.md

S13.plan-validation-experiments
  Status: detailed scaffold created.
  Owns: validation input coverage, cross-module assumption inventory, experiment priority scoring, survey/price/message/copy/channel/conversion/creator/forecast test plans, pass/fail rules, sample/data needs, validation decision gate, HTML validation section.

S14.compose-html-gtm-dashboard
  Status: thin renderer scaffold created.
  Owns: static HTML dashboard composition, section registry, executive summary shell, confidence badges, citations, data-gap panel, private-pricing-calculator render slot, render quality gates.

S15-S18
  Status: optional expansion slots, disabled by default.
```

## Implementation Order

Prioritize the chain that turns S01 evidence into the final HTML report with minimal rework.

```text
Phase 1: Finish S01 contracts
  S01 market context and handoff quality.

Phase 2: Demand and message core
  S02 JTBD scenarios
  S03 message architecture

Phase 3: Commercial decision branches
  S04 pricing model
  S05 creative text scoring
  S06 creator/KOL fit
  S07 DTC conversion
  S08 launch sales forecast

Phase 4: Product experience and retention branches
  S09 activation/return risk
  S10 insight/claim guardrails
  S11 subscription/churn
  S12 review and quality feedback loop

Phase 5: Validation and rendering
  S13 validation experiment roadmap
  S14 final HTML dashboard

Phase 6: Optional expansions
  S15 compliance claim risk
  S16 localize copy and creative
  S17 retail channel strategy
  S18 executive deck
```

## Current Next Build Sequence

Recommended next steps after S00-S08, S13, and S14 interface convergence:

```text
1. Dry-run the S00 -> S01/S02/S03/S04 -> optional S05/S06/S07 -> S08 -> S13 -> S14 handoff chain with a generic 2C hardware fixture.
2. Verify S13 can consolidate S01-S08 gaps without rerunning upstream analysis or inventing experiments from thin air.
3. Strengthen S14 rendering for the validation roadmap section and data-gap panel.
4. Add S09-S12 only when product/app/onboarding/retention/support/subscription risk is relevant or the user provides those materials.
5. Add S15-S18 optional expansions only after the core HTML report is runnable.
```

Active execution plan:

```text
docs/superpowers/plans/2026-05-25-gtm-suite-stabilization.md
```

Local work queue:

```text
.scratch/gtm-suite-stabilization/001-golden-dry-run.md
.scratch/gtm-suite-stabilization/002-s14-validation-rendering.md
.scratch/gtm-suite-stabilization/003-suite-contract-validator.md
.scratch/gtm-suite-stabilization/004-run-modes-context-budgets.md
.scratch/gtm-suite-stabilization/005-s09-s12-trigger-matrix.md
skills/gtm-master/references/s09-s12-trigger-matrix.md
```

Default execution order:

```text
1. Golden dry-run
2. Suite contract validator
3. S14 validation rendering
4. Run modes and context budgets
5. S09-S12 trigger matrix
```

Reasoning:

- S02 and S03 convert S01 evidence into the strategic middle of the report.
- S04 needs S01 and S03 to separate price facts from price messaging.
- S14 should exist early as a rendering contract, not only at the end.
- S08 should not forecast demand before price, segment, and channel assumptions are stable enough; conversion assumptions can remain explicit optional scenarios when S07 is skipped.
- S07 should not predict funnel conversion before S03 messages and S04 price guardrails exist, and should switch to prelaunch requirements when no owned page/funnel exists.
- S13 should consolidate validation after the major uncertainty map exists; otherwise it becomes a list of disconnected tests.
- S09-S12 should remain conditional because many 2C hardware launches need market, price, channel, creative, KOL, conversion, and forecast first; post-purchase modules are valuable only when the product category or supplied materials justify them.
- Use `references/s09-s12-trigger-matrix.md` before enabling any S09-S12 node. If the trigger is absent or required private/post-launch materials are missing, S14 should omit the section body unless the user requested a full-suite gap view.

## Stabilization Plan After S08

Use this sequence to stabilize the first runnable report before expanding product-experience branches.

```text
Step A: Build S14 thin renderer
  Status: implemented as scaffold.
  Goal: Produce a polished static HTML dashboard from existing section drafts.
  Inputs: report_state, html_section_drafts, evidence_ledger, data_gap_log.
  Must include: section registry, executive summary shell, confidence badges, citations, data-gap panel, private-pricing-calculator rendering slot, section ordering, static asset policy.
  Done when: S01-S04 section drafts can render into one navigable HTML file without inventing missing analysis.

Step B: Build S08 forecast-launch-demand
  Status: implemented as detailed scaffold.
  Goal: Turn segment, channel, pricing, and conversion assumptions into scenario-based launch unit-sales forecasts.
  Inputs: market_context_pack, segment sizes, channel seeds, pricing_decision_gate, price_sensitivity_model, elasticity_assumption_seed, optional conversion/KOL inputs, optional inventory/channel/private historical inputs.
  Must include: forecast boundary, base/upside/downside scenarios, assumption tree, confidence caps, inventory risk, channel split, sensitivity drivers, validation needs, no-false-precision rule.
  Done when: forecast output can clearly separate evidence-backed assumptions from user-provided or inferred assumptions and can state whether it is usable for direction, budget, channel allocation, or inventory planning.

Step C: Build S07 predict-dtc-conversion
  Status: implemented as detailed scaffold.
  Goal: Optionally plan prelaunch page/PDP conversion requirements or diagnose funnel friction for DTC/landing-page flows.
  Inputs: S03 message architecture, S04 price guardrails, optional editable copy/page text, competitor pages/PDPs, previous-generation pages/results, traffic and tracking context.
  Must include: skip/prelaunch/live mode gate, competitor and previous-generation benchmark path, page requirement brief, trust/proof requirements, tracking requirements, experiment backlog, handoff to S08 and S13.
  Done when: prelaunch recommendations or live conversion assumptions are explicit enough for S08 scenarios and S13 validation planning without pretending that missing pages have measured CVR.

Step D: Build S05/S06 optional branch skills
  Status: implemented as detailed scaffolds.
  Goal: Score editable copy and creator/KOL fit only when those materials exist or are strategically important.
  Inputs: message architecture, proof needs, editable copy, historical copy/performance data, creator candidates, local channel evidence.
  Must include: fit scores, risk checks, revision briefs, test backlog, branch-safe handoff.
  Done when: copy/KOL evidence can improve S07/S08 without blocking the main report; absence produces a skip note, not a failure.

Step E: Build S13 validation roadmap
  Status: implemented as detailed scaffold.
  Goal: Turn all major data gaps and risky assumptions into a prioritized experiment roadmap.
  Inputs: S01-S08 handoffs, pricing_test_execution_kit, data_gap_log, decision_log.
  Must include: experiment priority, cost/effort/impact, owner, required sample/data, pass/fail rules, next-decision linkage.
  Done when: users can see which tests to run first and what decision each test unlocks.

Step F: Build S09-S12 conditional product-experience loop
  Status: conditional future branch.
  Goal: Cover activation, return, insight, subscription/churn, review, and quality feedback only when relevant.
  Inputs: app/onboarding/support/review/subscription data or product category risk.
  Must include: activation risk, expectation gaps, retention/churn logic, review-quality feedback loop, next-generation GTM/product backlog.
  Done when: post-purchase risks can feed back into positioning, claims, forecast, and next-generation advice.
```

## Skill Build Template

For each new sub-skill:

```text
1. Define role and scope boundary.
2. Define required upstream handoff fields.
3. Define optional private inputs.
4. Define method modules and scoring rubrics.
5. Define output envelope:
   full_artifact
   compressed_handoff_pack
   html_section_draft
   evidence_updates
   decision_updates
   data_gaps
   recommended_next_skills
6. Define storage/RAG policy if the skill creates long evidence.
7. Define quality gates and human review points.
8. Update S00 codegraph.yaml.
9. Update S00 method-cards.yaml.
10. Validate skill and YAML.
```

## Planned Skill Details

### S02 Mine JTBD Scenarios

Purpose:
Convert S01 voice atoms, theme clusters, segment seeds, objections, purchase triggers, and competitor complaints into prioritized jobs-to-be-done and demand scenarios.

Must include:

- JTBD statement extraction
- Situation/motivation/outcome mapping
- Scenario clustering
- Anti-JTBD and non-consumption risks
- Proof requirement seeds
- Scenario priority score
- Local-language trigger phrases

Inputs:

- `market_context_pack`
- `voice_atom_refs`
- `voice_theme_clusters`
- `segment_seed_pack`
- `journey_episode_inputs`
- `bain_driver_inputs`
- `competitor_threat_scores`

Outputs:

- `jtbd_scenario_pack`
- `scenario_priority_scorecard`
- `proof_requirement_seed`
- `anti_jtbd_risk_list`
- `html_jtbd_section`

User review gate:
Show top scenarios and anti-scenarios when scenario priority materially affects positioning.

### S03 Match Messages To Segments

Purpose:
Turn JTBD scenarios into segment-level message architecture without writing final ads.

Must include:

- Feature-benefit-proof matrix
- Objection handling matrix
- Competitive contrast map
- Message-market fit scoring
- Claim risk and proof availability checks
- Local-language phrasing seed

Inputs:

- `jtbd_scenario_pack`
- `proof_requirement_seed`
- `segment_seed_pack`
- `value_proof_requirement_matrix`
- `content_proof_map`

Outputs:

- `segment_message_architecture`
- `feature_benefit_proof_matrix`
- `objection_matrix`
- `price_message_seed`
- `html_message_section`

User review gate:
Review message claims when claims are health, safety, child, elderly, privacy, accuracy, or regulated-adjacent.

### S04 Model Price Sensitivity

Purpose:
Convert S01 price seed and S03 price messaging into a fuller pricing model and test plan.

Must include:

- Local price credibility model
- Segment WTP hypothesis
- Van Westendorp test design
- Gabor-Granger test design
- Conjoint/DCE planning when useful
- Promo/subscription sensitivity
- Pricing risk and proof requirements

Inputs:

- `local_price_corridor`
- `price_anchor_panel`
- `competitor_price_gap_table`
- `segment_price_sensitivity_seeds`
- `value_proof_requirement_matrix`
- `price_message_seed`

Outputs:

- `price_sensitivity_model`
- `wtp_test_plan`
- `promo_subscription_guidance`
- `html_pricing_section`

User review gate:
Review target price, gross margin constraints, channel conflict, and discount policy before final recommendation.

### S05 Score Creative Text Assets

Purpose:
Score editable copy assets or concepts against message architecture, segment proof needs, local language, channel context, price/value guardrails, and claim risk. Do not require images, videos, packaging visuals, or design files; fixed visual/layout elements are constraints only.

Must include:

- Copy-message fit
- Proof and claim clarity
- Claim risk
- Local language fit
- Channel, PDP, retail, landing-page, script, and package-text fit
- Text attention hierarchy
- Copy priority scoring
- Revision brief generation
- Copy test backlog generation

Inputs:

- `segment_message_architecture`
- `content_proof_map`
- `feature_benefit_proof_matrix`
- `objection_matrix`
- `claim_risk_and_proof_gate`
- `local_language_message_seed`
- `channel_fit_scores`
- `digital_shelf_and_retailer_decision_map`
- `price_message_seed`
- `price_risk_guardrail`
- editable copy assets, scripts, PDP text, landing-page copy, package text, or claim lists
- historical copy and performance data if provided
- fixed visual/layout constraints if relevant

Outputs:

- `copy_quality_scorecard`
- `proof_and_claim_clarity_audit`
- `claim_risk_review`
- `channel_copy_fit_matrix`
- `copy_revision_briefs`
- `copy_test_backlog`
- `html_creative_section`

User review gate:
Required when copy contains regulated claims, before/after claims, children/elderly use, medical-adjacent language, or private brand materials.

### S06 Score KOL Fit

Purpose:
Score creator/expert types and candidate creators against segment trust needs and channel evidence.

Must include:

- Creator type fit
- Audience/segment fit
- Trust and proof fit
- Brand safety risk
- Sponsorship disclosure risk
- Local platform relevance
- Local-language creator discovery query bank
- Candidate longlist and source coverage audit
- Competitor-overlap creator map
- 5-10 candidate review gate with include/exclude/unsure decisions
- Recommendation rationale, including why to choose and why to hesitate
- Marketing budget range by scenario
- Expected visits/interactions range by scenario

Inputs:

- `segment_message_architecture`
- `trusted_expert_or_creator_types`
- `channel_fit_scores`
- creator candidates when provided
- local source map and competitor threat scores when available
- user candidate review decisions when available
- budget/rate cards/history when provided
- campaign goal and metric priority

Outputs:

- `creator_fit_scorecard`
- `creator_candidate_longlist`
- `creator_discovery_coverage_report`
- `competitor_creator_overlap_map`
- `creator_candidate_review_gate`
- `creator_candidate_review_list`
- `creator_candidate_decision_log`
- `creator_recommendation_rationale`
- `creator_budget_estimate`
- `creator_expected_outcome_estimate`
- `creator_brief_pack`
- `html_creator_section`

User review gate:
Review creator shortlists and budget assumptions before final use; S06 should not silently finalize KOL choices or promise campaign results. If candidate review is pending, candidate-level outputs are provisional.

### S07 Predict DTC Conversion

Purpose:
Optionally plan prelaunch DTC/PDP page requirements or estimate funnel friction and conversion assumptions for live/draft DTC or landing-page flows.

Must include:

- Landing page message fit
- Skip/prelaunch/live mode gate
- Competitor and local retailer/PDP benchmark
- Previous-generation page/result learnings when supplied
- Prelaunch page/PDP requirement brief and recommendation pack
- Price and proof friction
- Trust/return/warranty friction
- Checkout/payment friction
- Mobile UX and page evidence
- Traffic-source to landing-message continuity
- CVR assumption ladder with confidence caps
- Tracking readiness and analytics event schema
- Experiment backlog

Inputs:

- `segment_message_architecture`
- `price_sensitivity_model`
- `launch_page_planning_stage`
- competitor page/PDP refs when available
- previous-generation page/results when available
- `copy_quality_scorecard`
- `creator_expected_outcome_estimate`
- traffic source plan when available
- page/funnel text when provided

Outputs:

- `conversion_input_coverage_gate`
- `prelaunch_conversion_planning_mode`
- `competitor_landing_pdp_benchmark`
- `previous_generation_funnel_learnings`
- `category_page_requirement_brief`
- `prelaunch_page_recommendation_pack`
- `launch_tracking_requirement_brief`
- `cvr_assumption_ladder`
- `funnel_friction_scorecard`
- `tracking_readiness_audit`
- `dtc_conversion_model`
- `funnel_friction_map`
- `page_experiment_plan`
- `html_conversion_section`

User review gate:
Ask whether S07 should run at all. If the user's page/funnel is unavailable but conversion planning matters, ask for competitor references, previous-generation materials/results, and channel constraints; otherwise run prelaunch mode with explicit gaps.

### S08 Forecast Launch Sales

Purpose:
Convert market sizing seed, segment priorities, pricing, channel, conversion, and creator assumptions into launch sales scenarios.

Must include:

- Forecast boundary: demand potential, reachable demand, sell-in, sell-through, or supply-constrained shipment
- Scenario sales forecast: conservative/base/upside
- Segment sales split
- Channel split forecast
- Inventory and stockout risk
- Sensitivity analysis
- Assumption audit
- Decision gate and validation need map

Inputs:

- `tam_sam_som_seed`
- `tam_sam_som_assumption_tree`
- `segment_priority_ranking`
- `segment_channel_touchpoint_map`
- `price_sensitivity_model`
- `dtc_conversion_model`
- `creator_fit_scorecard`
- `creator_budget_estimate`
- `creator_expected_outcome_estimate`
- optional inventory, sell-in, PO, media, previous-generation, or historical launch data

Outputs:

- `forecast_input_coverage_gate`
- `forecast_scope_boundary`
- `forecast_assumption_tree`
- `scenario_sales_forecast`
- `segment_sales_split`
- `launch_sales_forecast`
- `channel_split_forecast`
- `sensitivity_driver_tornado`
- `inventory_risk_map`
- `forecast_decision_gate`
- `validation_need_map`
- `html_forecast_section`

User review gate:
Ask for forecast horizon and whether private inventory, historical sales, PO, or channel data may be used. If the forecast will influence inventory, require inventory allocation and replenishment constraints or mark inventory risk as hypothesis-only.

User review gate:
Required for inventory, forecast horizon, channel capacity, margin constraints, and internal sales targets.

### S09 Predict Activation Risk

Purpose:
Identify onboarding, setup, expectation, return, and early-use risks.

Must include:

- Expectation gap map
- Setup and first-use friction
- Return reason risk
- Support load hypotheses
- Early journey recovery actions

Inputs:

- `segment_message_architecture`
- `launch_sales_forecast`
- app/onboarding docs if provided
- previous-generation reviews/support if provided

Outputs:

- `activation_risk_map`
- `expectation_gap_map`
- `return_prevention_plan`
- `html_activation_section`

### S10 Generate Health Insights

Purpose:
For health, safety, elderly, child, wellness, AI-insight, or regulated-adjacent products, define insight and claim guardrails.

Must include:

- Claim boundary map
- Risky insight patterns
- Human review triggers
- Retention insight opportunities
- Regulatory/compliance notes

Inputs:

- `activation_risk_map`
- device signal context
- claim constraints

Outputs:

- `insight_system_boundaries`
- `health_claim_risk_rules`
- `retention_insight_opportunities`
- `html_insight_section`

User review gate:
Always required for health/medical-adjacent claims.

### S11 Predict Subscription And Churn

Purpose:
Evaluate subscription value, churn risk, renewal friction, and retention loops.

Must include:

- Subscription value driver map
- Paywall resistance
- Churn risk model
- Retention trigger plan
- Renewal proof requirements

Inputs:

- `price_sensitivity_model`
- `activation_risk_map`
- `insight_system_boundaries`
- app/subscription data when provided

Outputs:

- `subscription_value_driver_map`
- `churn_risk_model`
- `retention_trigger_plan`
- `html_subscription_section`

### S12 Mine Review Quality Feedback

Purpose:
Turn post-launch reviews, support, returns, and app feedback into product and GTM feedback loops.

Must include:

- Review quality mining
- Product quality backlog
- GTM promise mismatch
- Evidence graph updates
- Feedback loop into S01/S02/S03

Inputs:

- `activation_risk_map`
- `subscription_churn_model`
- review/support/return data

Outputs:

- `product_quality_backlog`
- `gtm_feedback_backlog`
- `evidence_graph_updates`
- `html_feedback_section`

### S13 Plan Validation Experiments

Purpose:
Turn weak assumptions and data gaps into practical validation tests.

Must include:

- Cross-module assumption inventory
- Data gap to validation question mapping
- Experiment Priority Score
- Survey, price, message, copy, channel, conversion, creator, and forecast validation plans
- Sample/data requirements
- Owner, timeline, budget/effort bands
- Pass/fail decision rules
- Experiment validity audit
- Private-data and synthetic-persona limits
- Validation decision gate
- Prioritized experiment roadmap

Inputs:

- `all_major_handoff_packs`
- `data_gap_log`
- `decision_log`
- `confidence_caps`
- `validation_need_map`
- `sensitivity_driver_tornado`
- `pricing_test_execution_kit`
- optional budget, timeline, sample, tracking, channel, creator, survey-panel, and private-data policy inputs

Outputs:

- `assumption_inventory`
- `experiment_priority_scorecard`
- `validation_experiment_roadmap`
- `survey_test_plan`
- `pricing_message_copy_test_plan`
- `channel_conversion_forecast_test_plan`
- `experiment_design_cards`
- `pass_fail_decision_rules`
- `sample_and_data_requirement_map`
- `validation_decision_gate`
- `html_validation_section`

### S14 Compose HTML GTM Dashboard

Purpose:
Render report state into a polished HTML dashboard without inventing analysis.

Must include:

- Section assembly
- Citation index
- Confidence badges
- Data gap rendering
- Chart data validation
- Executive narrative synthesis
- Static assets and responsive layout

Inputs:

- report_state
- html_section_drafts
- evidence_ledger
- data_gap_log

Outputs:

- `full_html_dashboard`
- `citation_index`
- `confidence_badge_map`
- `static_assets`

User review gate:
Review public/private evidence display, quote usage, and executive summary claims before final external sharing.

## Optional Expansion Slots

```text
S15 compliance-claim-risk
  Build when product involves regulated, health, safety, child, elderly, privacy, wireless, battery, or certification claims.

S16 localize-copy-and-creative
  Build when user wants final local-language copy, creative variants, or transcreation.

S17 plan-retail-channel-strategy
  Build when retail, marketplace, offline channel, distributor, or channel conflict is a major launch concern.

S18 build-executive-deck
  Build when user needs PPT/deck in addition to HTML.
```

## Human Interruption Points

Do not make these blockers by default, but explicitly offer them:

```text
Gate 0: Optional private file upload before S01.
Gate 1: Web/MCP/crawling plan before broad collection.
Gate 2: Competitor/substitute candidate calibration.
Gate 3: Segment/persona hypothesis review.
Gate 4: JTBD scenario and anti-scenario review.
Gate 5: Message claim and proof review.
Gate 6: Price/margin/channel assumption review.
Gate 7: Forecast/inventory/channel capacity review.
Gate 8: Validation experiment roadmap review.
Gate 9: Public HTML evidence, quote, and private-data review.
```

## Completion Definition

The suite architecture is complete when:

- S00 can create a skill execution plan from minimal inputs.
- Each implemented sub-skill has a SKILL.md, output contract, quality rules, and method card.
- Every sub-skill writes full artifact, compressed handoff, HTML section draft, evidence updates, decision updates, and data gaps.
- S14 can render a dashboard from available section drafts without inventing missing analysis.
- Quality gates pass and no required handoff field is silently missing.
