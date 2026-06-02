# S06 Output Contract

S06 must produce a full artifact, compressed handoff pack, S14-ready HTML section draft, evidence updates, decisions, and gaps.

## Output Envelope

```json
{
  "skill_id": "S06",
  "skill_name": "score-kol-fit",
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
  "artifact_id": "A06.creator-kol-fit-full-artifact",
  "title": "Creator/KOL Fit: [Product] in [Country]",
  "format": "markdown_with_structured_json_blocks",
  "module_tier_summary": {},
  "core_sections": [
    "executive_summary",
    "creator_input_coverage_gate",
    "creator_archetype_fit_scorecard",
    "creator_trust_proof_fit_matrix",
    "platform_relevance_map",
    "creator_recommendation_rationale",
    "local_creator_execution_table",
    "content_seeding_wave_plan",
    "creator_budget_estimate",
    "creator_expected_outcome_estimate",
    "creator_budget_expectation_confidence",
    "brand_safety_risk_review",
    "sponsorship_disclosure_risk_review",
    "creator_brief_pack",
    "creator_test_backlog",
    "evidence_assumptions_and_data_gaps"
  ],
  "conditional_sections": [
    "creator_candidate_inventory",
    "creator_candidate_fit_scorecard",
    "candidate_segment_audience_fit",
    "candidate_content_proof_fit",
    "creator_candidate_request_list",
    "creator_sourcing_criteria",
    "public_creator_discovery_plan",
    "local_creator_discovery_query_bank",
    "creator_source_channel_map",
    "creator_candidate_longlist",
    "creator_discovery_coverage_report",
    "competitor_creator_overlap_map",
    "creator_candidate_review_gate",
    "creator_candidate_review_list",
    "creator_candidate_decision_log",
    "review_approved_candidate_set",
    "review_excluded_candidate_set",
    "category_creator_norm_scan",
    "affiliate_or_reviewer_program_fit",
    "retail_expert_or_media_fit",
    "creator_performance_result_interpretation",
    "compliance_review_queue"
  ],
  "audit_sections": [
    "creator_evidence_trace",
    "candidate_risk_audit",
    "audience_metric_quality_audit",
    "content_sample_audit",
    "performance_data_audit"
  ]
}
```

## Compressed Handoff Pack

```json
{
  "handoff_id": "H06.creator-kol-fit-pack",
  "from_skill": "S06.score-kol-fit",
  "to_skills": [
    "S08.forecast-launch-demand",
    "S13.plan-validation-experiments",
    "S14.compose-html-gtm-dashboard"
  ],
  "summary": "",
  "canonical_fields": {
    "module_tier_summary": {},
    "creator_input_coverage_gate": {},
    "creator_archetype_fit_scorecard": [],
    "creator_candidate_inventory": [],
    "creator_candidate_fit_scorecard": [],
    "creator_trust_proof_fit_matrix": [],
    "candidate_segment_audience_fit": [],
    "candidate_content_proof_fit": [],
    "platform_relevance_map": [],
    "creator_recommendation_rationale": [],
    "local_creator_execution_table": [],
    "content_seeding_wave_plan": [],
    "creator_budget_estimate": [],
    "creator_expected_outcome_estimate": [],
    "creator_budget_expectation_confidence": {},
    "brand_safety_risk_review": [],
    "sponsorship_disclosure_risk_review": [],
    "creator_brief_pack": [],
    "creator_test_backlog": [],
    "conditional_outputs": {
      "creator_candidate_request_list": [],
      "creator_sourcing_criteria": {},
      "public_creator_discovery_plan": {},
      "local_creator_discovery_query_bank": [],
      "creator_source_channel_map": [],
      "creator_candidate_longlist": [],
      "creator_discovery_coverage_report": {},
      "competitor_creator_overlap_map": [],
      "creator_candidate_review_gate": {},
      "creator_candidate_review_list": [],
      "creator_candidate_decision_log": [],
      "review_approved_candidate_set": [],
      "review_excluded_candidate_set": [],
      "category_creator_norm_scan": [],
      "affiliate_or_reviewer_program_fit": {},
      "retail_expert_or_media_fit": {},
      "creator_performance_result_interpretation": {},
      "compliance_review_queue": []
    },
    "audit_refs": {
      "creator_evidence_trace_ref": "",
      "candidate_risk_audit_ref": "",
      "audience_metric_quality_audit_ref": "",
      "content_sample_audit_ref": "",
      "performance_data_audit_ref": ""
    },
    "confidence_caps": {},
    "data_gaps": []
  },
  "key_findings": [],
  "required_downstream_use": [
    "S08 should use creator_archetype_fit_scorecard, creator_budget_estimate, and creator_expected_outcome_estimate only as assumptions, not guaranteed demand.",
    "S08 should use content_seeding_wave_plan and local_creator_execution_table to build the launch calendar, channel war room, and measurement assumptions.",
    "S13 should convert creator_test_backlog and data gaps into validation experiments.",
    "S14 should render html_section_draft, candidate review gate status, recommendation rationale, budget/outcome ranges, confidence badges, creator risks, and private-candidate exclusions."
  ],
  "do_not_reopen": [
    "Do not rewrite S03 message architecture unless a blocking inconsistency is found.",
    "Do not treat follower count as audience proof.",
    "Do not present budget or outcome ranges as approved spend or guaranteed results.",
    "Do not expose private creator contacts, rates, or campaign data in public HTML unless approved."
  ],
  "open_questions": [],
  "data_gaps": [],
  "full_artifact_ref": ""
}
```

## Discovery Schemas

```json
{
  "content_seeding_wave_plan": [
    {
      "wave": "expert_review | comparison | lifestyle_creator | community_forum | retail_media | owner_review",
      "purpose": "",
      "recommended_candidates_or_archetypes": [],
      "budget_range": {"min": 0, "max": 0, "currency": ""},
      "expected_signal": "views | visits | likes | comments | saves | clickouts | search_lift | review_volume | retail_feedback | other",
      "expected_signal_range": "",
      "proof_needed": [],
      "timing": "",
      "owner_hint": "local_mkt | creator_manager | pr | ecommerce | retail_sales | mixed",
      "confidence": "high | medium | low | hypothesis_only",
      "evidence_refs": []
    }
  ],
  "local_creator_discovery_query_bank": [
    {
      "query_id": "",
      "query_text": "",
      "language": "",
      "country_or_region": "",
      "intent": "category_authority | competitor_overlap | proof_demo | community_voice | affiliate_deal | retailer_support | risk_check",
      "source_target": "search | youtube | tiktok | instagram | specialist_media | forum | retailer | affiliate | other",
      "upstream_refs": [],
      "expected_candidate_type": ""
    }
  ],
  "creator_source_channel_map": [
    {
      "source_stratum": "video_and_social | specialist_review_media | forums_and_communities | retail_and_pdp_support | affiliate_and_deal_sources | competitor_overlap_sources",
      "local_source_name": "",
      "source_url_or_search_target": "",
      "access_status": "accessible | partial | blocked | unknown",
      "candidate_role_likely": "",
      "limitations": [],
      "evidence_refs": []
    }
  ],
  "creator_candidate_longlist": [
    {
      "candidate_id": "",
      "name_or_handle": "",
      "candidate_type": "creator | reviewer | expert_media | forum_authority | affiliate_publisher | retailer_expert | community_admin | other",
      "platforms": [],
      "country_or_language_signal": "",
      "discovery_source": "",
      "matched_queries": [],
      "category_content_refs": [],
      "competitor_content_refs": [],
      "recent_activity_signal": "",
      "public_metric_proxies": {},
      "discovery_priority_score": 0,
      "evidence_coverage_score": 0,
      "promotion_status": "promote_to_scoring | keep_longlist | exclude | needs_user_review",
      "access_status": "accessible | partial | blocked | user_supplied | unknown",
      "privacy_status": "public | user_private | restricted",
      "evidence_refs": []
    }
  ],
  "creator_discovery_coverage_report": {
    "queries_attempted": 0,
    "source_strata_attempted": [],
    "accessible_sources": [],
    "blocked_or_partial_sources": [],
    "candidate_count_by_source": {},
    "promoted_candidate_count": 0,
    "coverage_gaps": [],
    "confidence": "high | medium | low | hypothesis_only"
  },
  "competitor_creator_overlap_map": [
    {
      "candidate_ref": "",
      "competitor_or_anchor_ref": "",
      "content_ref": "",
      "overlap_type": "reviewed | compared | ranked | sponsored | affiliate | mentioned | community_discussed",
      "proof_relevance": "",
      "recency": "",
      "risk_notes": [],
      "evidence_refs": []
    }
  ]
}
```

## Candidate Review Gate Schema

```json
{
  "creator_candidate_review_gate": {
    "status": "not_needed | pending_user_review | decisions_applied | skipped_no_candidates",
    "review_list_size": 8,
    "decision_options": ["include", "exclude", "unsure", "request_more_evidence"],
    "review_prompt": "",
    "provisional_policy": "candidate_scores_budget_and_outcomes_are_provisional_until_reviewed",
    "candidate_pool_refs": [],
    "data_gaps": []
  },
  "creator_candidate_review_list": [
    {
      "review_item_id": "",
      "candidate_ref": "",
      "display_name": "",
      "candidate_type": "",
      "primary_platform_or_source": "",
      "why_showing_this_option": [],
      "main_proof_role": "",
      "segment_or_scenario_fit": "",
      "known_risks_or_unknowns": [],
      "evidence_refs": [],
      "default_recommendation": "include | exclude | unsure | request_more_evidence",
      "user_decision": "include | exclude | unsure | request_more_evidence | not_reviewed",
      "user_reason": ""
    }
  ],
  "creator_candidate_decision_log": [
    {
      "candidate_ref": "",
      "decision": "include | exclude | unsure | request_more_evidence | not_reviewed",
      "decision_source": "user | system_default | prior_decision",
      "reason": "",
      "applied_to": ["candidate_fit_scorecard", "creator_budget_estimate", "creator_expected_outcome_estimate"],
      "timestamp_or_run_id": ""
    }
  ],
  "review_approved_candidate_set": [],
  "review_excluded_candidate_set": []
}
```

## Recommendation Rationale Schema

```json
{
  "creator_recommendation_rationale": [
    {
      "recommendation_id": "",
      "target_type": "archetype | candidate",
      "target_ref": "",
      "recommended_role": "",
      "why_recommended": [],
      "why_not_recommended": [],
      "segment_fit_reason": "",
      "proof_fit_reason": "",
      "platform_reason": "",
      "budget_reason": "",
      "expected_outcome_reason": "",
      "risk_reason": "",
      "evidence_refs": [],
      "confidence": "high | medium | low | hypothesis_only"
    }
  ]
}
```

## Local Creator Execution Table Schema

Use this table when candidate-level creator, KOL, reviewer, media, affiliate,
or community options are shown in the dashboard. It is the local execution view,
not contract approval.

```json
{
  "local_creator_execution_table": [
    {
      "candidate_ref": "",
      "display_name": "",
      "candidate_type": "creator | reviewer | expert_media | forum_authority | affiliate_publisher | retailer_expert | community_admin | other",
      "primary_platform_or_source": "",
      "public_url_or_source_ref": "",
      "recommended_role": "",
      "target_segment_or_scenario": "",
      "why_this_candidate_or_source": [],
      "proof_task": "",
      "budget_range_ref": "",
      "expected_outcome_range_ref": "",
      "budget_summary": "",
      "expected_signal_summary": "",
      "review_status": "approved_by_user | provisional_pending_user_review | request_more_evidence | excluded",
      "main_risks": [],
      "confidence": "high | medium | low | hypothesis_only",
      "evidence_refs": [],
      "data_gaps": []
    }
  ]
}
```

If candidate names are not reliable yet, use archetype rows or source rows and
set `review_status` to `provisional_pending_user_review` or
`request_more_evidence`.

## Budget Estimate Schema

```json
{
  "creator_budget_estimate": [
    {
      "target_ref": "",
      "currency": "",
      "budget_scenario": "conservative | base | upside",
      "creator_fee_range": {"min": 0, "max": 0},
      "product_seeding_cost_range": {"min": 0, "max": 0},
      "shipping_or_local_logistics_range": {"min": 0, "max": 0},
      "production_or_editing_cost_range": {"min": 0, "max": 0},
      "paid_boosting_range": {"min": 0, "max": 0},
      "agency_or_platform_fee_range": {"min": 0, "max": 0},
      "affiliate_or_commission_assumption": "",
      "tracking_or_landing_setup_cost_range": {"min": 0, "max": 0},
      "contingency_range": {"min": 0, "max": 0},
      "total_marketing_budget_range": {"min": 0, "max": 0},
      "assumptions": [],
      "evidence_refs": [],
      "confidence": "high | medium | low | hypothesis_only"
    }
  ]
}
```

## Expected Outcome Schema

```json
{
  "creator_expected_outcome_estimate": [
    {
      "target_ref": "",
      "budget_scenario": "conservative | base | upside",
      "expected_reach_range": {"min": 0, "max": 0},
      "expected_views_or_impressions_range": {"min": 0, "max": 0},
      "expected_likes_range": {"min": 0, "max": 0},
      "expected_comments_range": {"min": 0, "max": 0},
      "expected_shares_or_saves_range": {"min": 0, "max": 0},
      "expected_clicks_or_visits_range": {"min": 0, "max": 0},
      "expected_ctr_range": {"min": 0, "max": 0},
      "expected_engagement_rate_range": {"min": 0, "max": 0},
      "expected_conversions_or_sales_range": {"min": 0, "max": 0},
      "metric_basis": "historical_first_party | creator_public_proxy | platform_benchmark | category_proxy | hypothesis",
      "confounders": [],
      "evidence_refs": [],
      "confidence": "high | medium | low | hypothesis_only"
    }
  ]
}
```

## Budget And Outcome Confidence Schema

```json
{
  "creator_budget_expectation_confidence": {
    "budget_confidence": "high | medium | low | hypothesis_only",
    "expected_outcome_confidence": "high | medium | low | hypothesis_only",
    "confidence_caps": [],
    "missing_basis": [],
    "private_data_excluded": true,
    "public_html_note": ""
  }
}
```
