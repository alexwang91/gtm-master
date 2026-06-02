# Section Registry

Use this to order sections and decide what to show when sections are absent.

## Canonical Order

```json
{
  "canonical_section_order": [
    "input_boundary",
    "executive_summary",
    "market_context",
    "jtbd_scenarios",
    "message_architecture",
    "pricing",
    "copy_assets",
    "creator_kol",
    "dtc_conversion",
    "launch_forecast",
    "activation_return_risk",
    "insight_guardrails",
    "subscription_churn",
    "review_quality_feedback",
    "validation_roadmap",
    "appendix"
  ]
}
```

## Current Thin Renderer Core

The first runnable report should render these when available:

```text
executive_summary
input_boundary
market_context
jtbd_scenarios
message_architecture
pricing
copy_assets
creator_kol
dtc_conversion
launch_forecast
activation_return_risk
data_gap_panel
citation_index
```

Use `s01-s04-display-contract.md` to determine which subviews inside `market_context`, `jtbd_scenarios`, `message_architecture`, and `pricing` are mandatory in the main report. Use S05-S09 section contracts when `copy_assets`, `creator_kol`, `dtc_conversion`, `launch_forecast`, or `activation_return_risk` are present. S10-S13 remain mapped as conditional system capabilities, but they are not part of the current thin renderer body. A core section is not complete just because its top-level `html_section_draft` exists.

## Section Mapping

```json
{
  "section_map": [
    {
      "section_id": "input_boundary",
      "source_skill": "S00.gtm-master",
      "input_ref": "html_input_boundary",
      "importance": "core"
    },
    {
      "section_id": "market_context",
      "source_skill": "S01.build-consumer-market-map",
      "input_ref": "html_market_section",
      "importance": "core"
    },
    {
      "section_id": "jtbd_scenarios",
      "source_skill": "S02.mine-jtbd-scenarios",
      "input_ref": "html_jtbd_section",
      "importance": "core"
    },
    {
      "section_id": "message_architecture",
      "source_skill": "S03.match-messages-to-segments",
      "input_ref": "html_message_section",
      "importance": "core"
    },
    {
      "section_id": "pricing",
      "source_skill": "S04.model-price-sensitivity",
      "input_ref": "html_pricing_section",
      "importance": "core"
    },
    {
      "section_id": "copy_assets",
      "source_skill": "S05.score-creative-assets",
      "input_ref": "html_creative_section",
      "importance": "conditional"
    },
    {
      "section_id": "creator_kol",
      "source_skill": "S06.score-kol-fit",
      "input_ref": "html_creator_section",
      "importance": "conditional"
    },
    {
      "section_id": "dtc_conversion",
      "source_skill": "S07.predict-dtc-conversion",
      "input_ref": "html_conversion_section",
      "importance": "conditional"
    },
    {
      "section_id": "launch_forecast",
      "source_skill": "S08.forecast-launch-demand",
      "input_ref": "html_forecast_section",
      "importance": "conditional"
    },
    {
      "section_id": "activation_return_risk",
      "source_skill": "S09.predict-activation-risk",
      "input_ref": "html_activation_section",
      "importance": "conditional"
    },
    {
      "section_id": "insight_guardrails",
      "source_skill": "S10.generate-health-insights",
      "input_ref": "html_insight_section",
      "importance": "conditional"
    },
    {
      "section_id": "subscription_churn",
      "source_skill": "S11.predict-subscription-and-churn",
      "input_ref": "html_subscription_section",
      "importance": "conditional"
    },
    {
      "section_id": "review_quality_feedback",
      "source_skill": "S12.mine-review-quality-feedback",
      "input_ref": "html_feedback_section",
      "importance": "conditional"
    },
    {
      "section_id": "validation_roadmap",
      "source_skill": "S13.plan-validation-experiments",
      "input_ref": "html_validation_section",
      "importance": "conditional"
    }
  ]
}
```

## Missing Section Policy

```text
core section missing
  Show in the key-confirmation panel or source-governance appendix. Do not render a fake section or main-body module-coverage table.

core subview missing
  Mark `missing_required_view` in the section data gaps and request upstream enrichment. Do not replace it with generic text or decorative cards.

conditional section missing
  Omit from body unless it was triggered by report_state or requested by user.

future section missing
  Do not mention unless the roadmap or user explicitly asks for full-suite coverage.
```

## S13 Validation Roadmap Conditional Requirements

The validation roadmap is a hidden planning capability in the current dashboard. S14 must not render
`validation_roadmap` as a visible main-body section unless the user explicitly
asks for the validation body, a full gap review, or a future expanded suite
view. When that condition is met, render the section in Simplified Chinese by
default and preserve source refs. The required views are:

```text
Validation Input Coverage Gate -> status_panel
Experiment Priority Scorecard -> ranked_bar
Assumption Risk vs Test Feasibility -> matrix_heatmap
Timeline And Decision Unlock Map -> matrix_heatmap
Validation Decision Gate -> status_panel
Experiment Portfolio By Module -> ranked_bar
```

When present, render these as audit tables or appendix tables, not as hidden metadata:

```text
targeted_lookup_log
context_budget_report
post_skill_isolation_record
excluded_or_deferred_tests_log
```

If any required S13 view is absent, mark the section with `missing_required_view` and add the missing view to the data-gap panel. Do not invent a validation view from decorative text.
