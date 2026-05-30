# S13 Input Scenarios

Use this before asking the user for more validation inputs. Ask only for the smallest template that matches the next decision.

## Scenario A: Fast Gap Triage

Use when the user wants a quick view of what is still weak before rendering the report.

Minimum inputs:

```json
{
  "project_brief": {},
  "data_gap_log": [],
  "decision_log": [],
  "available_handoff_packs": []
}
```

Outputs:

```text
top_validation_questions
priority_scorecard
decision_gate
html_validation_section
```

## Scenario B: Prelaunch Validation Roadmap

Use before launch when the team needs a practical research and experiment plan.

Ask for:

```json
{
  "target_launch_date": "",
  "decision_deadlines": [],
  "validation_budget_range": "",
  "available_testing_channels": [],
  "sample_access": "",
  "survey_panel_access": ""
}
```

## Scenario C: Price And Message Validation

Use when S04/S03 outputs carry high price, proof, or claim risk.

Ask for:

```json
{
  "opening_price_strategy": {},
  "launch_price_architecture": {},
  "rapid_price_prior": {},
  "private_profit_revenue_optimizer_spec": {},
  "candidate_price_points": [],
  "currency_and_tax_basis": "",
  "approved_claims_or_claim_constraints": [],
  "survey_panel_access": "",
  "landing_page_or_pdp_test_access": "",
  "channel_conflict_constraints": []
}
```

## Scenario D: Channel, Conversion, And Forecast Validation

Use when S07/S08 outputs depend on channel availability, traffic, CVR, inventory, or marketing response assumptions.

Ask for:

```json
{
  "planned_channels": [],
  "traffic_source_plan": [],
  "tracking_or_analytics_context": "",
  "inventory_or_supply_constraints": "",
  "marketing_budget_range": "",
  "historical_or_previous_generation_data_policy": "none | aggregate | approved"
}
```

## Scenario E: Creator And Copy Pilot Validation

Use when S05 or S06 ran and creator/copy decisions need validation before scale.

Ask for:

```json
{
  "copy_or_message_variants": [],
  "creator_candidates_or_archetypes": [],
  "pilot_budget_range": "",
  "target_platforms": [],
  "tracking_or_landing_page_context": ""
}
```

## Scenario F: Private Internal Validation

Use when the user can supply confidential COGS, margin, sales, channel, conversion, or inventory data.

Ask for:

```json
{
  "private_data_policy": "exclude_raw | aggregate | approved",
  "private_data_types_available": [],
  "allowed_public_summary_level": "none | aggregate | indexed | approved_detail"
}
```

Output only derived, approved, or aggregate public summaries.

## Scenario G: Post-Launch Learning Plan

Use after launch or for a future monitoring loop.

Ask for:

```json
{
  "launch_date": "",
  "available_live_metrics": [],
  "review_or_support_sources": [],
  "reporting_cadence": "",
  "owner_map": []
}
```
