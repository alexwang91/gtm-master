# S05 HTML Section Contract

S05 contributes the editable creative text scoring section of the final GTM dashboard.

## Section Role

The S05 section should answer:

```text
Which copy assets are usable, which need revision, which are risky, and what should be tested next?
```

Dashboard-facing text must use the user-supplied report_language.

## Required Section Shape

```json
{
  "section_id": "copy_assets",
  "source_skill": "S05.score-creative-assets",
  "section_title": "文案资产评分",
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
  - name: Copy Input Coverage Gate
    type: status_panel
    data_source: copy_input_coverage_gate

  - name: Copy Priority Scorecard
    type: ranked_bar
    data_source: copy_quality_scorecard

  - name: Segment Message Copy Fit
    type: matrix_heatmap
    data_source: copy_message_fit_scorecard

  - name: Proof And Claim Risk Gate
    type: status_panel
    data_source: proof_and_claim_clarity_audit + claim_risk_review

  - name: Channel Copy Fit Matrix
    type: matrix_heatmap
    data_source: channel_copy_fit_matrix

  - name: Revision And Test Priority
    type: ranked_bar
    data_source: copy_revision_briefs + copy_test_backlog
```

Use `tables` for copy inventory, detailed revision briefs, claim-copy maps, public copy norm scans, and performance data audits.

## Thin Output Rules

Mark the S05 HTML section as `rendered_too_thin` if it lacks any of:

```text
editable copy availability or explicit missing_editable_copy gap
copy scorecard or request rubric
proof/claim risk status
channel-copy fit or explicit missing_channel_context gap
revision briefs or copy test backlog
private-copy handling note when copy is private
```

## Data Gap Codes

```text
missing_editable_copy
missing_message_architecture
missing_proof_gate
missing_local_language
missing_channel_context
fixed_visual_only
missing_visual_block
missing_visual_block_score
private_copy_restricted
performance_data_confounders
claim_review_required
rendered_too_thin
```
