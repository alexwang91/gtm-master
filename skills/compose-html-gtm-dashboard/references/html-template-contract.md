# HTML Template Contract

Use `assets/dashboard-shell.html` as the default static template for S14. Use `assets/dashboard-shell-mat.html` when the user wants the Mat visual theme from Zara Zhang's beautiful-html-templates adapted into a report dashboard.

## Template Role

The template is a thin, offline-first shell. It can:

- Render report metadata.
- Render section drafts with metric cards, visual blocks, tables, callouts, citations, and data gaps.
- Render a private pricing calculator with local-only blank inputs.
- Render citation and data-gap appendices.

## Template Variants

```text
dashboard-shell.html
  Default executive dashboard theme.

dashboard-shell-mat.html
  Mat-inspired dashboard theme. Offline-safe adaptation of the Mat deck visual system; does not load Google Fonts or the original slide runtime.
```

It should not:

- Fetch data from the network.
- Load remote libraries.
- Store private values by default.
- Invent missing sections.

## Data Injection

Replace or define this object before rendering:

```javascript
window.GTM_REPORT_DATA = {
  project: {},
  language: "zh-CN",
  sections: [],
  dataGaps: [],
  citations: [],
  decisions: [],
  privatePricingCalculator: {}
};
```

If no data is supplied, the template renders preview data marked as `template_preview`.

Default output language is Simplified Chinese (`zh-CN`). The template shell uses Chinese UI labels by default; upstream section drafts should provide dashboard-facing prose in Chinese unless the user requests another language. Preserve original consumer/search language as evidence fields, with Chinese gloss or translation where useful.

## Language Contract

The current GTM Master version is Chinese-first. S14 must render the final dashboard in Simplified Chinese unless the user explicitly requests another report language.

Dashboard-facing text includes:

- navigation labels
- executive summary copy
- section titles and takeaways
- chart titles, labels, notes, and legends
- table headers and cell values intended for business readers
- skipped-section reasons
- data-gap descriptions and recommended resolutions
- citation, audit, and isolation explanations
- private-calculator labels and result labels

Allowed visible non-Chinese tokens:

- stable IDs and source refs such as `C-DRY-001`, `DG-001`, and `dryrun://...`
- URLs and source paths
- widely understood GTM acronyms such as `GTM`, `JTBD`, `HTML`, `NSS`, `NPS`, `WTP`, `COGS`, `MKT`, `DTC`, and `KOL`
- original local-language consumer/search phrases when they are evidence; add a Chinese explanation or gloss when useful
- product or brand names supplied by the user

Fail the language gate if English placeholder prose, method names, skipped-section reasons, data-gap explanations, or table values are visible to the business reader without Chinese rendering.

## Supported Section Fields

```json
{
  "section_id": "",
  "source_skill": "",
  "section_title": "",
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

Supported `visual_blocks.type` values:

```text
status_panel
ranked_bar
matrix_heatmap
range_chart
```

Canonical `visual_blocks` fields:

```json
{
  "visual_block_id": "",
  "source_skill": "S01 | S02 | S03 | S04",
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
  "citations": [],
  "confidence": "high | medium | low | hypothesis_only | blocked | unknown"
}
```

Use `visual_blocks` for S01-S08 required proof views. Use `tables` when the data is sparse, heterogeneous, non-numeric, pending user review, or better understood as audit detail.

Method-level display names such as `decision_status_panel`, `horizontal_range_chart`, `matrix_or_heatmap`, `scorecard_table`, or `risk_table` are not accepted as `visual_blocks.type`. Map them to a canonical type or render them as `tables`, `metric_cards`, or `callouts` before template injection.

## Template Checks

Before using the template as a final artifact:

- Confirm no external network calls exist.
- Confirm private calculator inputs are blank.
- Confirm all rendered text is escaped.
- Confirm section IDs are stable.
- Confirm print styles do not hide data gaps or confidence badges.
