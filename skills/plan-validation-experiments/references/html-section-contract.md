# S13 HTML Section Contract

S13 contributes the validation roadmap section of the final GTM dashboard.

## Section Role

The S13 section should answer:

```text
Which assumptions are most dangerous, which experiments should run first, what data/sample is needed, what pass/fail rule decides the next move, and which GTM decisions can proceed now versus after validation?
```

Dashboard-facing text must use the user-supplied report_language.

## Required Section Shape

```json
{
  "section_id": "validation_roadmap",
  "source_skill": "S13.plan-validation-experiments",
  "section_title": "S13 Validation Roadmap",
  "status": "rendered | rendered_with_gaps | skipped",
  "confidence": "high | medium | low | hypothesis_only | blocked | unknown",
  "executive_takeaway": "",
  "narrative_blocks": [],
  "metric_cards": [],
  "visual_blocks": [],
  "tables": [],
  "callouts": [],
  "citations": [],
  "data_gaps": [],
  "next_actions": []
}
```

## Default Visual Blocks

```yaml
required_visual_blocks:
  - name: Validation Input Coverage Gate
    type: status_panel
    data_source: validation_input_coverage_gate

  - name: Experiment Priority Scorecard
    type: ranked_bar
    data_source: experiment_priority_scorecard

  - name: Assumption Risk vs Test Feasibility
    type: matrix_heatmap
    data_source: assumption_inventory + experiment_priority_scorecard

  - name: Timeline And Decision Unlock Map
    type: matrix_heatmap
    data_source: owner_timeline_effort_map + validation_experiment_roadmap

  - name: Test Cost Effort vs Impact
    type: matrix_heatmap
    data_source: experiment_priority_scorecard

  - name: Validation Decision Gate
    type: status_panel
    data_source: validation_decision_gate

  - name: Experiment Portfolio By Module
    type: ranked_bar
    data_source: validation_experiment_roadmap
```

Use `tables` for detailed experiment cards, sample requirements, pass/fail rules, private-data exclusion logs, targeted lookup logs, context budget reports, and deferred tests.

## Thin Output Rules

Mark the S13 HTML section as `rendered_too_thin` if it lacks any of:

```text
input coverage or explicit blocked status
assumption inventory
priority scorecard
at least 3 experiment cards or explicit not_enough_testable_assumptions gap
pass/fail rules
decision gate
private/synthetic data caveat when relevant
```

## Data Gap Codes

```text
missing_handoff_packs
missing_data_gap_log
missing_confidence_caps
missing_decision_deadlines
missing_budget_or_effort_context
missing_sample_access
missing_tracking_readiness
missing_private_data_policy
not_enough_testable_assumptions
synthetic_persona_limited_to_hypothesis
survey_intent_not_sales_evidence
clicks_not_sales_evidence
private_data_excluded
targeted_lookup_used
context_budget_exceeded
full_artifact_escalation_used
rapid_price_prior_needs_calibration
rapid_price_prior_missing_factor_trace
opening_price_strategy_needs_validation
private_optimizer_inputs_missing
price_path_guardrail_missing
missing_visual_block
missing_visual_block_score
rendered_too_thin
```

## Rapid Price Prior Rendering

When S04 provides `rapid_price_prior`, S13 should render its calibration path as validation work, not as a completed price conclusion. Show the weak factor, current score, evidence level, confidence cap, recommended method, minimum sample/data, pass/fail rule, update rule, owner, and budget/effort band.

Add `rapid_price_prior_needs_calibration` when a price decision depends on proxy-only, weak, missing, or synthetic factors. Add `rapid_price_prior_missing_factor_trace` when S04 provides a prior score without factor weights, evidence levels, or source refs.

## Opening Price Strategy Rendering

When S04 provides `opening_price_strategy`, `launch_price_architecture`, `private_profit_revenue_optimizer_spec`, or `price_path_30_60_90`, S13 should turn weak strategy assumptions into validation work. Show the strategy assumption, decision unlocked, method, sample/data need, pass/fail rule, update rule, owner, and budget/effort band.

Add `opening_price_strategy_needs_validation` when the opening strategy depends on weak proof, uncertain elasticity, channel conflict, missing private floors, or unresolved MKT response. Add `private_optimizer_inputs_missing` when revenue-max or profit-max price is requested but COGS, elasticity, demand, MKT spend, channel, or variable cost inputs are not available. Add `price_path_guardrail_missing` when the 30/60/90 plan lacks triggers, metrics, or forbidden moves.
