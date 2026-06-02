# HTML Dashboard Design

The final report should feel like a decision dashboard, not a generated essay.

The final report should also read like a direct GTM report, not an internal
workflow artifact. Main sections should use business words: execution summary,
channel priority, price conclusion, competitor response, content/KOL plan,
retail readiness, launch calendar, measurement war room, and key confirmations.
Do not show skill IDs, handoff mechanics, module coverage, isolation audit,
report audience labels, or method names as the visible point of a section.

## Layout

- Start with a GTM judgment cover, not an input-boundary strip. The first screen must answer whether the product should enter, defend, pause, or validate first; which opening move is recommended; which segment and channel should be prioritized; what budget posture is implied; which competitor threat matters most; and what single uncertainty could change the answer.
- Show assumptions only when they affect the judgment. Inputs, evidence coverage, and private-data boundaries are routing/governance material by default; move them to appendix or show them inline only when they materially cap confidence, change price/channel advice, or block an action.
- After the judgment cover, show a GTM decision summary band containing expected weekly sales range, sales-driver decomposition, simple MKT budget posture, channel priority and channel capability, competitor advantage/weakness and response, confidence cap, and top next validation action.
- Add a compact GTM command center when S08 supplies it: objective, hero claim, expected weekly sales range, MKT budget posture, must-win channel, top competitor threat, and top risk.
- Add launch execution views when supplied: channel war room, content seeding wave plan, retail/PDP readiness, launch calendar, service trust loop, measurement war room, and competitive response playbook.
- Use clear report sections with dense but readable cards, tables, and charts.
- Keep data gaps visible in context, not only at the end.
- Separate measured evidence, modeled estimates, and assumptions with badges.
- Use a final appendix for evidence ledger, assumptions, methods, and source limitations.

## Report Naming

Default Chinese report title:

```text
[Product] [Country/Region] GTM 报告
```

Do not use `管理层看板` in the default title unless the user explicitly asks for
that audience label. The top band can still serve executives, but the artifact
name should stay neutral and reusable for local GTM, channel, sales, and product
teams.

## Visual Components

Use these components consistently:

```text
verdict_card
metric_card
status_panel
ranked_bar
matrix_heatmap
range_chart
confidence_badge
evidence_badge
data_gap_callout
segment_priority_table
competitor_matrix
price_corridor_chart
nps_composition_chart
journey_curve
driver_tornado
handoff_summary_card
validation_roadmap_table
```

## Evidence Badges

```text
Evidence
Strong Inference
Weak Inference
Assumption
Needs Validation
Risk
```

Badges must appear near the claim they qualify.

## Chart Rules

- Use a chart only when the underlying data is structured enough.
- Do not imply precision for assumption-based TAM, NPS proxy, or earned growth proxy.
- Label proxy metrics clearly.
- Show sample size and source type when available.
- Include citation refs in chart notes.

## Narrative Rules

- Lead each section with the decision implication.
- Follow with evidence, not general explanation.
- Then state the local action, owner hint, timing/cadence, KPI or decision trigger, and confidence.
- Keep section summaries concise enough for executive scanning.
- Preserve local consumer language where it matters for messaging or JTBD.
- Do not hide uncertainty to make the report look cleaner.
- Do not use labels such as `方法论行动方向`, `受众`, `面向对象`, `模块覆盖`, or `隔离审计` in the main report body.

## Direct Report Section Order

Use this order for a full meeting-ready report when the data exists:

```text
GTM 判断封面
GTM 执行摘要
GTM 作战总览
市场与本地化判断
竞品证明与消费者声音
卖点、人群、触媒与KOL路线
价格结论与促销护栏
渠道优先级与首销战情室
内容种草、零售/PDP与服务信任准备
上市需求预测与投入产出假设
会改变结论的关键问题
引用与证据索引
来源治理附录, only when requested
```

## Executive Summary Content

Before the executive summary, show a judgment cover. It should be short and business-first:

- GTM judgment: enter, defend, cautious launch, validate first, or pause.
- Core recommendation: one sentence on who to target, which benefit to lead with, which channel to prioritize, how to defend price, and what to avoid.
- Opening move: price/offer/channel/content action for the first launch window.
- Must-win route: named local channel or touchpoint, not a generic category.
- Main competitor threat: TOP1 competitor or internal ladder risk and the response.
- Budget posture: minimum/base/stretch or user-supplied budget interpretation.
- Decision-changing question: the one uncertainty that would change the recommendation.

The top summary should not describe the skill chain. It should synthesize the report into business decisions:

- Expected weekly sales range, derived from S08 launch forecast and labeled by confidence.
- Why the sales range is plausible: market space, brand strength, price competitiveness, and product competitiveness.
- MKT spend posture: minimum test, base launch, and stretch/upside budget when supported by inputs.
- Channel priority: rank channels by reach, conversion readiness, commercial access, proof fit, margin/price constraints, and validation need.
- Competitor response: show top competitor/substitute strengths, weaknesses, price pressure, proof gaps, and response strategy.
- Evidence risks: show only the top questions that could change the recommendation.

If market size, brand strength, conversion, or channel readiness is not supported by evidence, keep the summary but mark the affected driver as hypothesis or data gap.

## HTML Composition Guardrails

- Do not invent missing analysis during rendering.
- Do not rewrite upstream conclusions unless a decision record says so.
- Do not merge conflicting conclusions silently; show the conflict and data gap.
- Do not use raw consumer quotes in public-facing materials unless usage is allowed.
- Keep the dashboard self-contained: charts, citations, and notes should render without external dependencies unless explicitly approved.
