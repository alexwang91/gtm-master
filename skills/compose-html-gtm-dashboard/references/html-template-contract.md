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

## Direct Report Wording

The main HTML body is a meeting-ready GTM report, not an agent workflow log. Standard and real-product reports must use business wording that a local GTM, sales, channel, or product team can present directly.

Use an upward-reporting tone: concise, evidence-scoped, cautious, and non-absolute. State recommendations as current judgment under known evidence, not as final truth. Prefer wording such as `基于当前证据，倾向判断`, `建议优先推进`, `仍需通过本地渠道或用户反馈确认`, and `若后续证据变化，结论需同步校准`.

Avoid contrastive sentence frames such as `而不是...` and `不是...而是...` in the visible report body. Use neutral decision structure instead: `当前重点`, `建议优先`, `需避免的误读`, `验证条件`, `后续校准信号`.

Forbidden in the main report body unless the user explicitly requests a method/audit appendix:

```text
S00, S01, S02, S03, S04, S05, S06, S07, S08, S09, S10, S11, S12, S13, S14
skill, sub-skill, module coverage, post-skill, handoff, report_state
隔离审计, 技能后隔离审计, 模块覆盖, 当前看板, 质量门
面向对象, 适用对象, 受众, report audience
methodology action direction, 方法论行动方向
```

Use these visible replacements:

```text
管理层看板 -> GTM 报告
管理层摘要 / 给管理层的摘要 -> 执行摘要
数据缺口 -> 关键待确认
方法论行动方向 -> 本地行动建议
用户输入 -> 已确认输入
S13 验证计划 -> 验证计划
S14 质量门 -> 报告质量检查
模块覆盖 -> 交付范围说明, appendix only
隔离审计 -> 来源与生成审计, appendix only
handoff -> 来源摘要, appendix only
```

Every main section should read in this order when the source data allows it:

```text
结论: what should the local team believe or decide?
证据: which local facts, competitor signals, consumer voices, price/channel data, or private inputs support it?
动作: what should the local team do next?
负责人/周期: which team should own it and when?
KPI/触发条件: what signal changes the recommendation?
风险/待确认: what could invalidate the conclusion?
```

Do not show how the suite passed data between skills in the main report. If auditability is needed, render it only in an appendix and title it as source governance rather than workflow state.

## First Screen Contract

The first screen must be a GTM judgment cover, not an input checklist.

Show:

```text
GTM判断
核心建议
首要打法
先打人群
Must-win渠道
价格/Offer
竞品威胁
会改变结论的问题
```

Do not use first-screen cards for:

```text
已确认输入
证据覆盖
私密数据边界
来源记录
报告阶段
产品/国家/价格 as standalone proof cards
```

Product, country, and price may appear in the report title, subtitle, or a
small note. Evidence coverage should appear beside the conclusion it supports.
Private-data boundaries should appear in pricing tools or appendix only, unless
they block the pricing recommendation.

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
