# S05 Output Contract

S05 must produce a full artifact, compressed handoff pack, S14-ready HTML section draft, evidence updates, decisions, and gaps.

## Output Envelope

```json
{
  "skill_id": "S05",
  "skill_name": "score-creative-assets",
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

## Full Artifact

```json
{
  "artifact_id": "A05.copy-assets-full-artifact",
  "title": "Creative Text Asset Scoring: [Product] in [Country]",
  "format": "markdown_with_structured_json_blocks",
  "module_tier_summary": {},
  "core_sections": [
    "executive_summary",
    "copy_input_coverage_gate",
    "copy_asset_inventory",
    "copy_message_fit_scorecard",
    "proof_and_claim_clarity_audit",
    "claim_risk_review",
    "local_language_fit_audit",
    "channel_copy_fit_matrix",
    "copy_quality_scorecard",
    "copy_revision_briefs",
    "copy_test_backlog",
    "evidence_assumptions_and_data_gaps"
  ],
  "conditional_sections": [
    "copy_asset_request_list",
    "copy_scoring_rubric",
    "competitor_copy_norm_scan",
    "marketplace_pdp_copy_fit",
    "landing_page_copy_fit",
    "retail_sales_copy_fit",
    "short_video_script_hook_audit",
    "package_text_claim_audit",
    "copy_performance_result_interpretation",
    "compliance_review_queue"
  ],
  "audit_sections": [
    "copy_evidence_trace",
    "copy_observation_log",
    "claim_copy_map",
    "revision_rationale_trace",
    "performance_data_audit"
  ]
}
```

## Compressed Handoff Pack

```json
{
  "handoff_id": "H05.copy-assets-pack",
  "from_skill": "S05.score-creative-assets",
  "to_skills": [
    "S06.score-kol-fit",
    "S07.predict-dtc-conversion",
    "S13.plan-validation-experiments",
    "S14.compose-html-gtm-dashboard"
  ],
  "summary": "",
  "canonical_fields": {
    "module_tier_summary": {},
    "copy_input_coverage_gate": {},
    "copy_asset_inventory": [],
    "copy_message_fit_scorecard": [],
    "proof_and_claim_clarity_audit": [],
    "claim_risk_review": [],
    "local_language_fit_audit": [],
    "channel_copy_fit_matrix": [],
    "copy_quality_scorecard": [],
    "copy_revision_briefs": [],
    "copy_test_backlog": [],
    "conditional_outputs": {
      "copy_asset_request_list": [],
      "copy_scoring_rubric": {},
      "competitor_copy_norm_scan": [],
      "marketplace_pdp_copy_fit": [],
      "landing_page_copy_fit": [],
      "retail_sales_copy_fit": [],
      "short_video_script_hook_audit": [],
      "package_text_claim_audit": [],
      "copy_performance_result_interpretation": {},
      "compliance_review_queue": []
    },
    "audit_refs": {
      "copy_evidence_trace_ref": "",
      "copy_observation_log_ref": "",
      "claim_copy_map_ref": "",
      "revision_rationale_trace_ref": "",
      "performance_data_audit_ref": ""
    },
    "confidence_caps": {},
    "data_gaps": []
  },
  "key_findings": [],
  "required_downstream_use": [
    "S06 should use claim/proof and script fit notes when creator scripts or briefs are evaluated.",
    "S07 should use copy_message_fit_scorecard, proof_and_claim_clarity_audit, objection gaps, and landing/PDP copy fit for funnel friction.",
    "S13 should convert copy_test_backlog into validation experiments.",
    "S14 should render html_section_draft, confidence badges, copy risk notes, and private-copy exclusions."
  ],
  "do_not_reopen": [
    "Do not rewrite S03 message architecture unless a blocking inconsistency is found.",
    "Do not treat copy scores as proven conversion lift.",
    "Do not expose private copy, scripts, or raw performance data in public HTML unless approved."
  ],
  "open_questions": [],
  "data_gaps": [],
  "full_artifact_ref": ""
}
```

## Core Schemas

### Copy Asset Inventory

```json
{
  "copy_asset_inventory": [
    {
      "copy_id": "",
      "copy_name": "",
      "copy_type": "headline | subheadline | body_copy | PDP_title | PDP_bullets | landing_page_copy | FAQ | ad_caption | script | transcript | retail_talk_track | package_text | claim_list | email_push | concept",
      "placement_context": "paid_social | search_ad | short_video_script | landing_page | marketplace_pdp | retailer_pdp | retail_sales | package_text | creator_brief | email_push | other",
      "target_segment_refs": [],
      "language": "",
      "privacy_status": "public | uploaded_private | restricted",
      "copy_ref": "",
      "fixed_constraints": [],
      "evidence_refs": []
    }
  ]
}
```

### Copy Quality Scorecard

```json
{
  "copy_quality_scorecard": [
    {
      "copy_id": "",
      "target_segment_ref": "",
      "placement_context": "",
      "copy_task": "awareness | comparison | conversion | proof | objection_handling | retail_or_pdp_trust",
      "copy_message_fit_score": 0,
      "proof_and_claim_clarity_score": 0,
      "claim_risk_score": 0,
      "local_language_fit_score": 0,
      "channel_copy_fit_score": 0,
      "text_attention_hierarchy_score": 0,
      "copy_priority_score": 0,
      "recommendation_status": "test_ready | revise_before_test | review_required | blocked | request_copy",
      "confidence": "high | medium | low | hypothesis_only",
      "evidence_refs": [],
      "data_gaps": []
    }
  ]
}
```

### Revision Brief

```json
{
  "copy_revision_briefs": [
    {
      "copy_id": "",
      "priority": "high | medium | low",
      "target_segment_ref": "",
      "copy_task": "",
      "problem": "",
      "change_needed": "",
      "proof_or_claim_guardrail": "",
      "fixed_constraints": [],
      "expected_effect": "",
      "owner_hint": "copy | brand | product | legal | retail | ecommerce | performance | unknown",
      "test_recommendation": "",
      "evidence_refs": []
    }
  ]
}
```
