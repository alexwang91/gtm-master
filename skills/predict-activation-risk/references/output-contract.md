# S09 Output Contract

S09 must produce an activation and return-risk artifact, compressed handoff pack, S14-ready HTML section draft, evidence updates, decisions, gaps, and `post_skill_isolation_record`.

## Output Envelope

```json
{
  "skill_id": "S09",
  "skill_name": "predict-activation-risk",
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
  "handoff_id": "H09.activation-risk-pack",
  "from_skill": "S09.predict-activation-risk",
  "to_skills": [
    "S10.generate-health-insights",
    "S12.mine-review-quality-feedback",
    "S13.plan-validation-experiments",
    "S14.compose-html-gtm-dashboard"
  ],
  "canonical_fields": {
    "activation_return_trigger_check": {},
    "activation_journey_risk_map": [],
    "expectation_gap_map": [],
    "return_prevention_priority": [],
    "support_education_plan": [],
    "channel_expectation_guardrails": [],
    "data_gaps": []
  },
  "do_not_reopen": [
    "Do not reopen raw support or return data without context escalation.",
    "Do not treat synthetic risk scores as measured return rate.",
    "Do not expose private support, warranty, or return records in public HTML."
  ],
  "full_artifact_ref": ""
}
```

## HTML Section Draft

```json
{
  "section_id": "activation_return_risk",
  "source_skill": "S09.predict-activation-risk",
  "section_title": "Activation, Return, And Onboarding Risk",
  "status": "rendered_with_gaps",
  "executive_takeaway": "",
  "visual_blocks": [
    {
      "visual_block_id": "s09-trigger-check",
      "type": "status_panel",
      "title": "Activation And Return Trigger Check",
      "data_source": "activation_return_trigger_check",
      "items": []
    },
    {
      "visual_block_id": "s09-journey-risk",
      "type": "matrix_heatmap",
      "title": "Activation Journey Risk Map",
      "data_source": "activation_journey_risk_map",
      "rows": []
    },
    {
      "visual_block_id": "s09-return-prevention",
      "type": "ranked_bar",
      "title": "Return Prevention Priority",
      "data_source": "return_prevention_priority",
      "items": []
    }
  ],
  "data_gaps": [],
  "citations": [],
  "handoff_ref": ""
}
```
