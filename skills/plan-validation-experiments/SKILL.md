---
name: plan-validation-experiments
description: Use when turning GTM report assumptions, data gaps, confidence caps, price/message/copy/channel/forecast test ideas, or prelaunch uncertainty into a prioritized validation experiment roadmap with sample needs, pass/fail rules, owner timing, and an S14-ready HTML validation section.
---

# Plan Validation Experiments

## Role

Use this skill as S13 in the GTM intelligence report suite. Its essence is validation planning: convert upstream assumptions, weak evidence, confidence caps, and test backlogs into the smallest practical set of experiments that can unlock the next GTM decision.

S13 is not a new research, pricing, KOL, conversion, or forecast skill. It does not rerun S01-S08 analysis. It ranks what must be validated, designs valid tests, defines pass/fail rules, and marks what remains hypothesis-only.

## Required Inputs

```json
{
  "project_brief": {},
  "all_major_handoff_packs": [],
  "data_gap_log": [],
  "decision_log": []
}
```

High-value upstream fields:

```json
{
  "market_sizing_data_gaps": [],
  "segment_priority_ranking": [],
  "competitor_candidate_review_list": [],
  "local_price_corridor": {},
  "opening_price_strategy": {},
  "launch_price_architecture": {},
  "rapid_price_prior": {},
  "private_profit_revenue_optimizer_spec": {},
  "price_path_30_60_90": [],
  "segment_price_sensitivity_seeds": [],
  "validation_question_seed": [],
  "message_test_backlog": [],
  "wtp_test_plan": {},
  "pricing_test_execution_kit": {},
  "copy_test_backlog": [],
  "creator_test_backlog": [],
  "page_experiment_plan": {},
  "tracking_readiness_audit": {},
  "forecast_confidence_caps": {},
  "sensitivity_driver_tornado": [],
  "validation_need_map": []
}
```

Optional user inputs:

```json
{
  "validation_input_scenario": "A_fast_gap_triage | B_prelaunch_validation_roadmap | C_price_message_validation | D_channel_conversion_forecast_validation | E_creator_copy_pilot_validation | F_private_internal_validation | G_post_launch_learning_plan",
  "validation_budget_range": "",
  "target_launch_date": "",
  "decision_deadlines": [],
  "available_testing_channels": [],
  "allowed_test_markets_or_countries": [],
  "sample_access": "",
  "survey_panel_access": "",
  "ad_account_or_media_test_access": "",
  "landing_page_or_pdp_test_access": "",
  "retailer_or_creator_pilot_access": "",
  "private_data_policy": "exclude_raw | aggregate | approved",
  "output_detail_level": "quick | standard | real_product_pilot | deep"
}
```

## Load Order

Read only what the current task needs:

1. Read `references/input-scenarios.md` before asking for validation inputs.
2. Read `references/upstream-input-map.md` before deciding whether S13 can run or should output a planning shell.
3. Read `references/output-contract.md` before producing artifacts, handoffs, or report sections.
4. Read `references/validation-methods.md` before selecting tests or writing pass/fail rules.
5. Read `references/scoring-rubrics.md` before scoring priority, validity, effort, or confidence.
6. Read `references/evidence-usage-policy.md` before using public benchmarks, private files, internal data, or synthetic personas.
7. Read `references/context-and-search-budget.md` before opening full artifacts, RAG collections, local files, or web/MCP lookup results.
8. Read `references/html-visual-block-generation.md` before producing S14-ready `visual_blocks`.
9. Read `references/html-section-contract.md` before producing the HTML validation section draft.

## Depth Modes

```text
quick
  Produce assumption inventory, top 5 validation questions, priority scorecard, and next-decision gate.

standard
  Produce core outputs: input coverage, assumption inventory, validation backlog, prioritized experiment roadmap, survey plan, price/message/copy/channel/forecast test plans, pass/fail rules, sample/data requirements, and HTML section.

deep
  Add method-specific briefs for Van Westendorp, Gabor-Granger, conjoint/DCE, landing-page A/B, creator pilots, retail/channel tests, private internal validation, and post-launch learning.
```

Default to `standard`.

## Output Tiers

Core outputs:

```text
validation_input_coverage_gate
assumption_inventory
validation_question_backlog
experiment_priority_scorecard
validation_experiment_roadmap
survey_test_plan
pricing_message_copy_test_plan
channel_conversion_forecast_test_plan
experiment_design_cards
pass_fail_decision_rules
sample_and_data_requirement_map
owner_timeline_effort_map
validation_decision_gate
html_validation_section
```

Conditional outputs:

```text
van_westendorp_execution_brief
gabor_granger_execution_brief
conjoint_dce_execution_brief
landing_page_ab_test_brief
creator_pilot_test_brief
retailer_channel_validation_brief
forecast_assumption_validation_brief
private_data_validation_path
post_launch_learning_plan
```

Audit outputs:

```text
assumption_source_trace
experiment_validity_audit
excluded_or_deferred_tests_log
private_data_exclusion_log
synthetic_persona_use_log
targeted_lookup_log
context_budget_report
```

## Conditional Triggers

```text
van_westendorp_execution_brief
  Trigger when acceptable price range is unknown and S04 or the user needs WTP evidence.

gabor_granger_execution_brief
  Trigger when specific candidate price points need purchase-intent comparison.

conjoint_dce_execution_brief
  Trigger when feature, bundle, warranty, service, or subscription tradeoffs materially affect price.

landing_page_ab_test_brief
  Trigger when landing page, PDP, waitlist, clickout, preorder, or traffic testing is available or required.

creator_pilot_test_brief
  Trigger when S06 ran or creator/KOL budget should be validated before scale.

retailer_channel_validation_brief
  Trigger when retail, marketplace, channel sell-in/sell-through, or price integrity risk drives the decision.

forecast_assumption_validation_brief
  Trigger when S08 validation_need_map, sensitivity_driver_tornado, or forecast_confidence_caps exist.

private_data_validation_path
  Trigger when private COGS, margin, sales, channel, inventory, conversion, or historical data can improve validation but must not appear in public HTML.

post_launch_learning_plan
  Trigger when the product is live or the user wants a learning loop after launch.
```

## Execution Workflow

```text
1. Select the smallest validation_input_scenario that matches the user's next decision.
2. Build input coverage by source skill, decision area, confidence cap, and data gap.
3. Extract assumptions from handoff packs, data gaps, test plans, and sensitivity drivers.
4. Link every assumption to the decision it affects: positioning, price, channel, budget, forecast, inventory, creative, creator, or launch readiness.
5. Score each assumption by impact, uncertainty, decision urgency, test feasibility, cost efficiency, and risk reduction.
6. Convert the highest-scoring assumptions into validation questions.
7. Select the smallest valid test portfolio; do not require every possible method.
8. For each experiment, define hypothesis, target population, sample/data need, stimulus, method, controlled variables, primary metrics, pass/fail rule, owner, timing, cost band, and failure action.
9. Separate survey intent, ad/landing behavior, retail sell-through, creator engagement, and internal historical evidence; do not merge them into one fake certainty score.
10. Label synthetic AI persona use as hypothesis generation only; never as WTP, demand, or conversion evidence.
11. Build a decision gate showing which decisions can proceed, which need validation, and which are blocked.
12. Produce compressed handoff pack for S14 and any later S09-S12/post-launch modules.
13. Produce HTML validation section draft with S14-ready visual blocks.
```

## Context And Search Control

Default to handoff-only execution:

```text
1. Read compressed handoff packs, data_gap_log, confidence caps, and referenced evidence IDs.
2. Do not reopen S01-S08 full artifacts unless a required field is missing, contradictory, or explicitly requested.
3. Do not run broad web search. S13 is not a market discovery module.
4. Use web/MCP/local lookup only for targeted validation feasibility checks with a named decision, query budget, and stop condition.
5. Summarize lookup results into short evidence records; never paste large pages, raw search result dumps, long forum threads, or full local files into the working context.
6. Keep the main assumption inventory decision-facing. Defer low-priority assumptions into `excluded_or_deferred_tests_log`.
7. Emit `context_budget_report` whenever full artifacts, RAG retrieval, local files, or targeted lookups are used.
```

Allowed targeted lookup examples:

```text
survey_panel_feasibility
  Check whether the target country/category can reasonably recruit respondents.

retailer_or_marketplace_test_feasibility
  Check whether a named channel can support offer, PDP, clickout, or sell-through tests.

ad_or_landing_test_feasibility
  Check platform or tracking constraints for a named experiment.

validation_method_freshness
  Confirm a method constraint or platform rule when it may have changed.
```

Forbidden lookup examples:

```text
new competitor discovery
new consumer forum mining
fresh market sizing
broad review scraping
creator discovery from scratch
price corridor rebuild
large local document ingestion without a field-level extraction goal
```

## Scope Boundary

S13 owns:

- Cross-module assumption inventory
- Data gap to validation question mapping
- Experiment priority scoring
- Survey, price, message, copy, channel, conversion, creator, and forecast validation plans
- Sample/data requirements and pass/fail rules
- Owner, timing, cost/effort bands, and decision linkage
- Experiment validity audit and deferred test log
- HTML validation section draft

S13 does not own:

- Broad market evidence collection from scratch
- Final price, budget, channel, inventory, creative, or KOL approval
- Real respondent recruitment or media buying
- Treating AI personas as real consumers
- Treating clicks, likes, or survey intent as sales
- Final HTML composition

## Required Output

Always return the S13 output envelope from `references/output-contract.md`:

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

- Rank tests by decision value; do not produce a long unprioritized research menu.
- Prefer the minimum valid test set that resolves the largest uncertainty.
- Stay within handoff-only context by default; use targeted lookup only when it changes a validation decision.
- Define pass/fail rules before recommending a test.
- Separate what a test can measure from what it cannot measure.
- Do not call survey purchase intent a sales forecast.
- Do not call CTR, likes, views, or comments proof of purchase demand.
- Do not call retailer sell-in proof of consumer sell-through.
- Do not run price tests without channel conflict, tax/shipping, warranty, and margin caveats.
- Mark private raw inputs as excluded, aggregated, or approved before public HTML use.
- Default dashboard-facing outputs to Simplified Chinese unless the user requests another report language.
