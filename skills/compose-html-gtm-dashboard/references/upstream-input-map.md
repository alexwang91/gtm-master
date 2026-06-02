# S14 Upstream Input Map

Use this before S14 renders a dashboard.

## Required Input Groups

```json
{
  "required_input_groups": [
    "report_state",
    "html_section_drafts",
    "evidence_ledger",
    "data_gap_log"
  ]
}
```

## Field Map

### Report State

From S00 and accumulated skills:

```text
project_brief
report_state
decision_log
quality_gate_results
report_depth
report_audience
```

Use for title, scope, execution-summary shell, decision notes, render depth, and appendix-only source governance. Do not display `report_audience` or module coverage in the main report body.

Missing behavior:

- If `project_brief` is missing, render only a generic title and flag a blocking data gap.
- If `report_state` is missing but section drafts are available, render with gap notes.

### HTML Section Drafts

From implemented S01-S08 and S13, plus optional future S09-S12:

```text
html_market_section
html_jtbd_section
html_message_section
html_pricing_section
html_creative_section
html_creator_section
html_conversion_section
html_forecast_section
html_activation_section
html_insight_section
html_subscription_section
html_feedback_section
html_validation_section
```

Use for dashboard body. Each draft should follow the section draft schema in `render-architecture.md`.

Missing behavior:

- Render available sections.
- Show important missing sections in the coverage/data-gap panel.
- Do not create substitute analysis for missing sections.

### Evidence Ledger

From S00/S01 and downstream evidence updates:

```text
evidence_ledger
citation_index
rag_index_manifest
collection_logs
source_quality_summary
```

Use for citations, source badges, appendices, and audit refs.

Missing behavior:

- If a section has claims but no evidence refs, flag citation caveat.
- Do not invent URLs, titles, or source metadata.

### Data Gap Log

From all upstream skills:

```text
data_gap_log
confidence_caps
quality_gate_results
blocking_gaps
non_blocking_gaps
```

Use for the data gap panel and confidence badges.

Missing behavior:

- If no data gap log exists, render a caveat that gap coverage is unknown.

### Private Calculator Specs

From S04:

```text
private_pricing_calculator_spec
pricing_decision_gate
pricing_test_execution_kit
```

Use for local-only private calculator and pricing caveats.

Missing behavior:

- If no calculator spec exists, do not render calculator controls.
- If a calculator spec exists, render blank inputs only.
