# Report Data Contract

The final HTML dashboard is composed from accumulated report state, not from a last-minute free-form summary.

Report state is also the isolation boundary. After each sub-skill finishes, S14 should render from `html_section_draft`, citation refs, confidence badges, and data gaps. It must not require upstream full artifacts for normal rendering.

## Report State

```json
{
  "report_id": "",
  "project_brief": {},
  "generated_at": "",
  "report_audience": "",
  "style": "executive | consulting | dashboard | investor_deck",
  "sections": [],
  "global_kpis": [],
  "charts": [],
  "tables": [],
  "evidence_ledger_refs": [],
  "citation_index": [],
  "data_gap_log": [],
  "decision_log": [],
  "quality_gate_summary": {}
}
```

## Section Object

```json
{
  "section_id": "",
  "source_skill": "",
  "title": "",
  "status": "draft | reviewed | final | blocked | rendered | rendered_with_gaps | skipped | skipped_missing | skipped_not_triggered",
  "executive_takeaway": "",
  "narrative_blocks": [],
  "metric_cards": [],
  "visual_blocks": [],
  "tables": [],
  "charts": [],
  "callouts": [],
  "confidence_badges": [],
  "citations": [],
  "data_gaps": [],
  "next_actions": []
}
```

## Visual Block Contract

Use `visual_blocks` for S14-ready proof views that should render directly in the final dashboard.

```json
{
  "visual_block_id": "",
  "source_skill": "",
  "type": "status_panel | ranked_bar | matrix_heatmap | range_chart",
  "title": "",
  "subtitle": "",
  "data_source": "",
  "items": [],
  "rows": [],
  "columns": [],
  "scale_min": 0,
  "scale_max": 100,
  "note": "",
  "evidence_refs": [],
  "confidence": "high | medium | low | hypothesis_only",
  "citations": []
}
```

S01-S08 and S13 core or triggered conditional sections should provide `visual_blocks` for their required proof views. Use `charts` only for richer or custom visualizations that exceed the default S14 components. See `visual-block-acceptance-matrix.md` for canonical block types, legacy visual type mapping, and required gap codes.

## Default HTML Sections

Current runnable suite sections are produced by implemented S00-S08 plus S13 and S14. Future conditional sections remain in the canonical registry but should not be shown as missing body sections unless the user requested them or their trigger fired.

```yaml
implemented_first_report_sections:
  - executive_summary
  - product_capability_summary
  - data_sources_and_collection_log
  - local_competitor_and_substitute_map
  - consumer_opinion_map
  - tam_sam_som_summary
  - segment_priority_table
  - persona_cards
  - jtbd_scenario_map
  - message_architecture
  - local_price_sensitivity
  - copy_asset_scorecard
  - creator_kol_fit
  - dtc_conversion_prediction
  - launch_sales_forecast
  - validation_experiment_roadmap
  - evidence_assumptions_and_data_gaps

future_conditional_sections:
  - activation_and_return_risk
  - insight_guardrails
  - subscription_and_churn
  - review_quality_feedback
```

## Chart Contract

```json
{
  "chart_id": "",
  "source_skill": "",
  "chart_type": "bar | stacked_bar | horizontal_bar | line | journey_curve | tornado | scatter | matrix | sankey | radar | scorecard",
  "title": "",
  "data": [],
  "encoding": {},
  "notes": "",
  "confidence": "high | medium | low",
  "citations": []
}
```

## Confidence Badge Contract

```json
{
  "badge_id": "",
  "label": "Evidence | Strong Inference | Weak Inference | Assumption | Needs Validation | Risk",
  "applies_to": "",
  "reason": "",
  "evidence_refs": []
}
```

## Rendering Rules

- Preserve uncertainty visibly; do not hide data gaps in footnotes only.
- Render from isolated section drafts and report state; do not reopen full artifacts unless a recorded context escalation is required.
- Keep raw consumer quotes short and cite their source.
- Separate measured data from modeled estimates and assumptions.
- Use charts only when the underlying data is structured enough.
- Show "needs validation" as a first-class report state, not a failure.
- Include a final evidence and data-gap appendix.
