# S05 HTML Visual Block Generation

Use this when producing `html_section_draft.visual_blocks` for S14.

S05 may emit only canonical S14 visual block types:

```text
status_panel
ranked_bar
matrix_heatmap
range_chart
```

## Block 1: Copy Input Coverage Gate

```json
{
  "visual_block_id": "s05_coverage_gate",
  "source_skill": "S05.score-creative-assets",
  "type": "status_panel",
  "title": "文案输入覆盖度",
  "subtitle": "先说明是否真的有可编辑文本可评估",
  "data_source": "copy_input_coverage_gate",
  "items": [],
  "confidence": "medium",
  "evidence_refs": []
}
```

Items should cover: editable copy, message architecture, proof gate, local language, channel context, fixed visual/layout constraints, private copy policy.

## Block 2: Copy Priority Scorecard

Use `ranked_bar` when each copy item has `copy_priority_score`.

```json
{
  "visual_block_id": "s05_copy_priority",
  "source_skill": "S05.score-creative-assets",
  "type": "ranked_bar",
  "title": "文案优先级",
  "subtitle": "按信息匹配、证明清晰度、渠道适配、注意力层级与风险综合排序",
  "data_source": "copy_quality_scorecard",
  "items": [],
  "confidence": "medium",
  "evidence_refs": []
}
```

If comparable scores are missing, render a table and add `missing_visual_block_score`.

## Block 3: Segment Message Copy Fit

Use `matrix_heatmap` for segment x copy or segment x message-role fit.

Rows should be segments or copy items. Columns should be priority copy items, message roles, copy tasks, or placements.

## Block 4: Proof And Claim Risk Gate

Use `status_panel` to show:

```text
proof/claim clarity
unsupported lead claims
review-required claims
blocked copy
safe-to-test copy
private-copy restrictions
```

Do not hide claim risk because the wording is persuasive.

## Block 5: Channel Copy Fit Matrix

Use `matrix_heatmap` for copy item x placement fit when scores are comparable:

```text
paid social
search ad
short video script
marketplace/PDP
retailer/PDP
landing page
retail sales/package text
```

If target channels are not known, render a table and add `missing_channel_context`.

## Block 6: Revision And Test Priority

Use `ranked_bar` for revision or test items with priority scores.

Each item should include:

```text
copy_id or test_id
priority score
problem
change/test needed
owner
evidence refs
```

## Final Assembly Rules

```text
1. Order visual_blocks by decision flow:
   coverage -> copy priority -> segment/message fit -> proof/claim risk -> channel-copy fit -> revision/test priority.
2. Every block needs title, data_source, confidence, and evidence_refs/citations/source note.
3. If no editable text exists, show coverage gate plus request list/rubric tables; do not fabricate scorecards.
4. Fixed images, videos, layouts, and packaging visuals should appear only as constraints when supplied by text.
5. Private copy should appear as IDs, approved excerpts, and derived scores, not raw full text, unless explicitly approved.
6. Add `rendered_too_thin` if fewer than 4 required blocks can be produced in standard mode and no explicit missing-copy path exists.
```
