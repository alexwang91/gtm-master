# S13 Scoring Rubrics

Use 0-100 scores. Label weak evidence as hypothesis.

## Experiment Priority

```text
Experiment Priority =
  30% impact_on_decision
+ 20% uncertainty_level
+ 15% decision_urgency
+ 15% test_feasibility
+ 10% cost_efficiency
+ 10% risk_reduction
```

Score interpretation:

```text
80-100  run before decision
60-79   run if budget or timing allows
40-59   keep as monitored hypothesis
0-39    defer unless a decision owner requests it
```

## Assumption Risk

```text
Assumption Risk =
  30% decision_impact
+ 25% evidence_weakness
+ 15% downside_severity
+ 15% reversibility_difficulty
+ 15% cross_module_dependency
```

Hard caps:

```text
no source skill or evidence ref -> max confidence hypothesis_only
private data not approved for use -> public confidence capped at source_limited
AI persona only -> confidence hypothesis_only
survey intent only -> cannot validate sales or inventory decisions above medium
CTR or engagement only -> cannot validate sales above low without downstream behavior
retailer sell-in only -> cannot validate consumer sell-through above low
```

## Test Feasibility

```text
Test Feasibility =
  25% access_to_audience_or_data
+ 20% stimulus_readiness
+ 20% tracking_or_measurement_readiness
+ 15% time_available
+ 10% budget_fit
+ 10% legal_brand_channel_safety
```

## Evidence Strength After Test

```text
measured_purchase_or_sell_through_with_controls -> high
preorder_or_deposit_with_refund_guardrails -> medium_to_high
landing_page_behavior_with_tracking_and_control -> medium
screened_survey_with_local_stimulus -> medium
qualitative_interviews -> low_to_medium
public benchmark proxy -> low
synthetic persona -> hypothesis_only
```

## Decision Gate

```text
ready_to_decide
  Critical assumptions have medium or better evidence, pass rules are met, and private constraints are cleared.

decide_with_caveats
  The decision can move forward, but caveats must be explicit and confidence capped.

needs_validation
  One or more high-priority assumptions are untested and reversible enough to test.

blocked
  Missing private constraint, legal/channel approval, tracking, sample access, or core upstream handoff prevents useful validation.
```
