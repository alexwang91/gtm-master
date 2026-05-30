# S13 Validation Methods

Use this to choose a valid test, define what it can measure, and avoid false certainty.

## Method Portfolio

```text
desk_research_refresh
  Use to close source freshness or competitor/price gaps. Measures public evidence, not real demand.

local_search_trend_check
  Use to compare local language category terms, feature language, and competitor interest. Measures search interest, not purchase intent.

qualitative_interview
  Use to understand objections, proof gaps, use cases, and wording. Good for why, weak for sizing.

survey_panel
  Use for screened local respondents. Measures stated perception and intent, with confidence capped below behavioral evidence.

van_westendorp
  Use for acceptable price range. Needs clear local stimulus and local currency.

gabor_granger
  Use for candidate price-point purchase intent. Do not treat as exact demand curve.

conjoint_or_dce
  Use when feature, bundle, warranty, service, subscription, or price tradeoffs matter enough to justify complexity.

message_or_copy_test
  Use for claim clarity, proof belief, objection reduction, and local language preference.

landing_page_ab_test
  Use for behavioral interest and funnel friction. Needs controlled traffic, stable variants, tracking, and runtime rules.

waitlist_or_preorder_smoke_test
  Use when legal and operationally approved to measure stronger intent. Needs refund, fulfillment, and brand-safety guardrails.

creator_pilot
  Use to validate creator/audience fit and content proof before scale. Measures reach, engagement quality, traffic, and downstream intent when tracking exists.

retail_or_marketplace_test
  Use for sell-through, offer, channel, price integrity, or PDP proof when channel rules allow.

internal_historical_analysis
  Use previous-generation or comparable internal sales, promo, traffic, conversion, returns, and channel data when supplied.

post_launch_cohort_read
  Use after launch to learn actual sell-through, activation, support, returns, repeat use, and review drivers.
```

## Experiment Card Fields

Each experiment must define:

```text
experiment_id
decision_unlocked
assumption_tested
hypothesis
method
target_population_or_data_source
sample_or_data_requirement
stimulus_or_materials_needed
controlled_variables
primary_metric
secondary_metrics
pass_rule
fail_rule
runtime_or_collection_window
owner
timing
budget_or_effort_band
privacy_or_compliance_notes
failure_action
confidence_after_pass
confidence_after_fail
```

## Validity Checks

Fail or downgrade the experiment when:

```text
no hypothesis
no decision link
no pass/fail rule
sample is not target-country or target-segment relevant
variant changes multiple major variables without labeling it exploratory
claims lift without control or baseline
landing test has no tracking plan
price test ignores tax, shipping, warranty, promo, or channel conflict
creator test has no traffic or engagement quality metric
retail test confuses sell-in with sell-through
survey result is treated as measured sales
AI personas are treated as respondents
```

## AI Persona Simulation Policy

AI personas may support:

```text
hypothesis_generation
survey_wording_pretest
local_language_variant_generation
objection_brainstorming
stimulus_clarity_check
```

AI personas may not support:

```text
WTP evidence
demand forecast evidence
conversion evidence
market share evidence
final price decision
final channel decision
```

Always label synthetic outputs as `hypothesis_only`.
