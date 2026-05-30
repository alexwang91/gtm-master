# S11 Output Contract

S11 must produce a subscription and churn artifact, compressed handoff pack, S14-ready HTML section draft, evidence updates, decisions, gaps, and `post_skill_isolation_record`.

## Output Envelope

```json
{
  "skill_id": "S11",
  "skill_name": "predict-subscription-and-churn",
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
  "handoff_id": "H11.subscription-churn-pack",
  "from_skill": "S11.predict-subscription-and-churn",
  "to_skills": [
    "S12.mine-review-quality-feedback",
    "S13.plan-validation-experiments",
    "S14.compose-html-gtm-dashboard"
  ],
  "canonical_fields": {
    "subscription_retention_trigger_check": {},
    "subscription_value_driver_map": [],
    "retention_value_driver_map": [],
    "churn_risk_model": [],
    "retention_trigger_plan": [],
    "pricing_retention_linkage": {},
    "data_gaps": []
  },
  "do_not_reopen": [
    "Do not expose raw billing, cohort, or customer-level usage data in public HTML.",
    "Do not treat qualitative retention risk as measured churn.",
    "Do not recommend paid service pricing without S04 linkage and validation needs."
  ],
  "full_artifact_ref": ""
}
```

## HTML Section Draft

```json
{
  "section_id": "subscription_churn",
  "source_skill": "S11.predict-subscription-and-churn",
  "section_title": "Subscription, Retention, And Churn",
  "status": "rendered_with_gaps",
  "executive_takeaway": "",
  "visual_blocks": [
    {
      "visual_block_id": "s11-trigger-check",
      "type": "status_panel",
      "title": "Subscription Retention Trigger Check",
      "data_source": "subscription_retention_trigger_check",
      "items": []
    },
    {
      "visual_block_id": "s11-retention-driver",
      "type": "matrix_heatmap",
      "title": "Retention Value Driver Map",
      "data_source": "retention_value_driver_map",
      "rows": []
    },
    {
      "visual_block_id": "s11-churn-risk",
      "type": "ranked_bar",
      "title": "Churn Risk Priority",
      "data_source": "churn_risk_priority",
      "items": []
    }
  ],
  "data_gaps": [],
  "citations": [],
  "handoff_ref": ""
}
```
