# S12 Output Contract

S12 must produce a review and quality-feedback artifact, compressed handoff pack, S14-ready HTML section draft, evidence updates, decisions, gaps, and `post_skill_isolation_record`.

## Output Envelope

```json
{
  "skill_id": "S12",
  "skill_name": "mine-review-quality-feedback",
  "full_artifact": {},
  "compressed_handoff_pack": {},
  "html_section_draft": {},
  "evidence_updates": [],
  "decision_updates": [],
  "data_gaps": [],
  "post_skill_isolation_record": {},
  "recommended_next_skills": []
}
```

## Compressed Handoff Pack

```json
{
  "handoff_id": "H12.review-quality-pack",
  "from_skill": "S12.mine-review-quality-feedback",
  "to_skills": [
    "S01.build-consumer-market-map",
    "S02.mine-jtbd-scenarios",
    "S03.match-messages-to-segments",
    "S09.predict-activation-risk",
    "S13.plan-validation-experiments",
    "S14.compose-html-gtm-dashboard"
  ],
  "canonical_fields": {
    "feedback_loop_trigger_check": {},
    "review_support_source_map": [],
    "feedback_theme_cluster": [],
    "quality_feedback_priority": [],
    "product_quality_backlog": [],
    "gtm_feedback_backlog": [],
    "feedback_loop_action_map": [],
    "evidence_graph_updates": [],
    "data_gaps": []
  },
  "do_not_reopen": [
    "Do not expose raw private customer records in public HTML.",
    "Do not drop dissenting viewpoints from scoped source coverage.",
    "Do not treat a convenience corpus as statistically representative."
  ],
  "full_artifact_ref": ""
}
```

## HTML Section Draft

```json
{
  "section_id": "review_quality_feedback",
  "source_skill": "S12.mine-review-quality-feedback",
  "section_title": "Review, Support, And Quality Feedback Loop",
  "status": "rendered_with_gaps",
  "executive_takeaway": "",
  "visual_blocks": [
    {
      "visual_block_id": "s12-trigger-check",
      "type": "status_panel",
      "title": "Feedback Loop Trigger Check",
      "data_source": "feedback_loop_trigger_check",
      "items": []
    },
    {
      "visual_block_id": "s12-source-map",
      "type": "matrix_heatmap",
      "title": "Review And Support Source Map",
      "data_source": "review_support_source_map",
      "rows": []
    },
    {
      "visual_block_id": "s12-quality-priority",
      "type": "ranked_bar",
      "title": "Quality Feedback Priority",
      "data_source": "quality_feedback_priority",
      "items": []
    },
    {
      "visual_block_id": "s12-action-map",
      "type": "matrix_heatmap",
      "title": "Feedback Loop Action Map",
      "data_source": "feedback_loop_action_map",
      "rows": []
    }
  ],
  "data_gaps": [],
  "citations": [],
  "handoff_ref": ""
}
```
