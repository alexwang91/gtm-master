# S10 Output Contract

S10 must produce a claim-guardrail artifact, compressed handoff pack, S14-ready HTML section draft, evidence updates, decisions, gaps, and `post_skill_isolation_record`.

## Output Envelope

```json
{
  "skill_id": "S10",
  "skill_name": "generate-health-insights",
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
  "handoff_id": "H10.claim-guardrails-pack",
  "from_skill": "S10.generate-health-insights",
  "to_skills": [
    "S11.predict-subscription-and-churn",
    "S13.plan-validation-experiments",
    "S14.compose-html-gtm-dashboard"
  ],
  "canonical_fields": {
    "insight_claim_trigger_check": {},
    "insight_system_boundaries": {},
    "claim_guardrail_matrix": [],
    "privacy_safety_proof_need": [],
    "human_review_queue": [],
    "retention_insight_opportunities": [],
    "data_gaps": []
  },
  "do_not_reopen": [
    "Do not treat this artifact as legal approval.",
    "Do not expose legal notes, sensitive evidence, or private claim drafts in public HTML.",
    "Do not convert unverified insights into medical or safety promises."
  ],
  "full_artifact_ref": ""
}
```

## HTML Section Draft

```json
{
  "section_id": "insight_guardrails",
  "source_skill": "S10.generate-health-insights",
  "section_title": "Insight, Health, Safety, And Sensitive Claim Guardrails",
  "status": "rendered_with_gaps",
  "executive_takeaway": "",
  "visual_blocks": [
    {
      "visual_block_id": "s10-trigger-check",
      "type": "status_panel",
      "title": "Claim Trigger Check",
      "data_source": "insight_claim_trigger_check",
      "items": []
    },
    {
      "visual_block_id": "s10-claim-guardrail",
      "type": "matrix_heatmap",
      "title": "Claim Guardrail Matrix",
      "data_source": "claim_guardrail_matrix",
      "rows": []
    },
    {
      "visual_block_id": "s10-proof-need",
      "type": "ranked_bar",
      "title": "Privacy And Safety Proof Need",
      "data_source": "privacy_safety_proof_need",
      "items": []
    }
  ],
  "data_gaps": [],
  "citations": [],
  "handoff_ref": ""
}
```
