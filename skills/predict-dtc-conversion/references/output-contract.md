# S07 Output Contract

When S07 runs, it must produce a full artifact, compressed handoff pack, S14-ready HTML section draft, evidence updates, decisions, and gaps. When S07 is skipped, return the same envelope with `conversion_input_coverage_gate.status = "skipped"` and a skip reason.

## Output Envelope

```json
{
  "skill_id": "S07",
  "skill_name": "predict-dtc-conversion",
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
  "artifact_id": "A07.dtc-conversion-full-artifact",
  "title": "DTC Conversion Prediction: [Product] in [Country]",
  "format": "markdown_with_structured_json_blocks",
  "module_tier_summary": {},
  "core_sections": [
    "executive_summary",
    "conversion_input_coverage_gate",
    "prelaunch_conversion_planning_mode",
    "funnel_stage_inventory",
    "traffic_source_assumption_map",
    "segment_landing_page_fit_matrix",
    "offer_message_continuity_map",
    "proof_objection_friction_map",
    "price_trust_checkout_friction_map",
    "mobile_ux_friction_audit",
    "conversion_hypothesis_model",
    "dtc_conversion_model",
    "cvr_assumption_ladder",
    "funnel_friction_scorecard",
    "funnel_friction_map",
    "conversion_risk_guardrail",
    "tracking_readiness_audit",
    "page_experiment_plan",
    "evidence_assumptions_and_data_gaps"
  ],
  "conditional_sections": [
    "page_or_funnel_material_request_list",
    "competitor_landing_pdp_benchmark",
    "previous_generation_funnel_learnings",
    "category_page_requirement_brief",
    "prelaunch_page_recommendation_pack",
    "launch_tracking_requirement_brief",
    "landing_page_copy_fit_audit",
    "pdp_checkout_trust_audit",
    "retailer_clickout_conversion_fit",
    "campaign_landing_match_audit",
    "preorder_waitlist_flow_fit",
    "analytics_event_schema",
    "ab_test_plan",
    "conversion_performance_result_interpretation",
    "compliance_review_queue"
  ],
  "audit_sections": [
    "conversion_evidence_trace",
    "page_observation_log",
    "cvr_assumption_trace",
    "experiment_validity_audit",
    "tracking_data_audit"
  ]
}
```

## Compressed Handoff Pack

```json
{
  "handoff_id": "H07.dtc-conversion-pack",
  "from_skill": "S07.predict-dtc-conversion",
  "to_skills": [
    "S08.forecast-launch-demand",
    "S13.plan-validation-experiments",
    "S14.compose-html-gtm-dashboard"
  ],
  "summary": "",
  "canonical_fields": {
    "module_tier_summary": {},
    "conversion_input_coverage_gate": {},
    "prelaunch_conversion_planning_mode": {},
    "funnel_stage_inventory": [],
    "traffic_source_assumption_map": [],
    "segment_landing_page_fit_matrix": [],
    "offer_message_continuity_map": [],
    "proof_objection_friction_map": [],
    "price_trust_checkout_friction_map": [],
    "mobile_ux_friction_audit": [],
    "conversion_hypothesis_model": {},
    "dtc_conversion_model": {},
    "cvr_assumption_ladder": [],
    "funnel_friction_scorecard": [],
    "funnel_friction_map": [],
    "conversion_risk_guardrail": [],
    "tracking_readiness_audit": {},
    "page_experiment_plan": [],
    "conditional_outputs": {
      "page_or_funnel_material_request_list": [],
      "competitor_landing_pdp_benchmark": [],
      "previous_generation_funnel_learnings": [],
      "category_page_requirement_brief": [],
      "prelaunch_page_recommendation_pack": [],
      "launch_tracking_requirement_brief": {},
      "landing_page_copy_fit_audit": [],
      "pdp_checkout_trust_audit": [],
      "retailer_clickout_conversion_fit": {},
      "campaign_landing_match_audit": [],
      "preorder_waitlist_flow_fit": {},
      "analytics_event_schema": [],
      "ab_test_plan": [],
      "conversion_performance_result_interpretation": {},
      "compliance_review_queue": []
    },
    "audit_refs": {
      "conversion_evidence_trace_ref": "",
      "page_observation_log_ref": "",
      "cvr_assumption_trace_ref": "",
      "experiment_validity_audit_ref": "",
      "tracking_data_audit_ref": ""
    },
    "confidence_caps": {},
    "data_gaps": []
  },
  "key_findings": [],
  "required_downstream_use": [
    "S08 should use cvr_assumption_ladder only as scenario input with confidence caps, not proven demand.",
    "S13 should convert page_experiment_plan, tracking gaps, and validation blockers into experiments.",
    "S14 should render html_section_draft, friction scores, CVR caveats, tracking readiness, and data gaps."
  ],
  "do_not_reopen": [
    "Do not rewrite S03 messaging or S04 pricing unless a blocking inconsistency is found.",
    "Do not treat heuristic friction scores as measured CVR.",
    "Do not expose private analytics, raw page drafts, or confidential performance data in public HTML unless approved."
  ],
  "open_questions": [],
  "data_gaps": [],
  "full_artifact_ref": ""
}
```

## Core Schemas

```json
{
  "conversion_input_coverage_gate": {
    "status": "skipped | ready | ready_with_gaps | prelaunch_planning | hypothesis_only | blocked",
    "run_mode": "skip | prelaunch_planning | live_or_draft_diagnosis",
    "launch_page_planning_stage": "none | concept | draft | live | post_launch | unknown",
    "has_page_or_funnel_materials": false,
    "has_competitor_page_benchmark": false,
    "has_previous_generation_materials_or_results": false,
    "has_offer_details": false,
    "has_tracking_context": false,
    "has_performance_data": false,
    "confidence": "high | medium | low | hypothesis_only",
    "gaps": []
  },
  "prelaunch_conversion_planning_mode": {
    "is_prelaunch_mode": true,
    "reason": "",
    "owned_page_status": "none | concept | draft | live | unknown",
    "allowed_basis": [
      "competitor_page_benchmark",
      "local_retailer_or_marketplace_norms",
      "previous_generation_learning",
      "upstream_message_price_proof_handoff",
      "explicit_user_hypothesis"
    ],
    "forbidden_claims": [
      "measured_cvr_without_data",
      "guaranteed_sales_or_revenue",
      "competitor_pattern_as_proven_best_practice"
    ],
    "confidence": "high | medium | low | hypothesis_only"
  },
  "funnel_stage_inventory": [
    {
      "stage_id": "",
      "stage": "traffic_source | entry_promise | landing_hero | proof | price_offer | trust_policy | CTA | checkout_or_clickout | confirmation",
      "available_evidence": "",
      "main_user_question": "",
      "risk_notes": [],
      "evidence_refs": []
    }
  ],
  "funnel_friction_scorecard": [
    {
      "stage_ref": "",
      "friction_type": "",
      "friction_score": 0,
      "impact": "high | medium | low",
      "fix_or_test": "",
      "confidence": "high | medium | low | hypothesis_only",
      "evidence_refs": []
    }
  ],
  "cvr_assumption_ladder": [
    {
      "scenario": "conservative | base | upside",
      "conversion_action": "",
      "cvr_range": {"min": 0, "max": 0},
      "basis": "measured_internal | valid_test_result | platform_or_category_benchmark | historical_proxy | heuristic_hypothesis",
      "confidence": "high | medium | low | hypothesis_only",
      "confounders": [],
      "evidence_refs": []
    }
  ],
  "page_experiment_plan": [
    {
      "experiment_id": "",
      "hypothesis": "",
      "funnel_stage": "",
      "variant_or_test": "",
      "primary_metric": "",
      "secondary_metrics": [],
      "minimum_traffic_or_sample_note": "",
      "decision_rule": "",
      "confounders": [],
      "owner": "",
      "priority_score": 0,
      "evidence_refs": []
    }
  ]
}
```

## Prelaunch Conditional Schemas

```json
{
  "competitor_landing_pdp_benchmark": [
    {
      "competitor_or_source": "",
      "source_type": "brand_site | marketplace_pdp | retailer_pdp | review_site | category_norm | other",
      "hero_promise_pattern": "",
      "proof_pattern": "",
      "price_offer_pattern": "",
      "trust_policy_pattern": "",
      "cta_or_clickout_pattern": "",
      "what_to_borrow_as_hypothesis": "",
      "what_to_avoid": "",
      "evidence_strength": "high | medium | low",
      "evidence_refs": []
    }
  ],
  "previous_generation_funnel_learnings": [
    {
      "source": "previous_page | previous_pdp | previous_campaign | previous_analytics | previous_reviews | previous_sales_channel_feedback",
      "observed_pattern": "",
      "likely_conversion_driver_or_blocker": "",
      "keep_change_or_test": "keep | change | test | avoid",
      "recommendation_for_next_generation": "",
      "confidence": "high | medium | low | hypothesis_only",
      "evidence_refs": []
    }
  ],
  "category_page_requirement_brief": [
    {
      "requirement_area": "hero | segment_use_case | proof | comparison | price_offer | trust_policy | CTA | tracking | compliance",
      "requirement": "",
      "why_it_matters": "",
      "source_basis": "competitor_benchmark | previous_generation_learning | upstream_handoff | category_norm | user_hypothesis",
      "priority": "high | medium | low",
      "evidence_refs": []
    }
  ],
  "prelaunch_page_recommendation_pack": [
    {
      "recommendation_id": "",
      "page_or_funnel_area": "",
      "recommendation": "",
      "expected_effect_direction": "",
      "validation_method": "",
      "risk_or_caveat": "",
      "confidence": "high | medium | low | hypothesis_only",
      "evidence_refs": []
    }
  ],
  "launch_tracking_requirement_brief": {
    "conversion_action": "",
    "required_events": [],
    "required_utm_or_source_dimensions": [],
    "experiment_split_requirements": [],
    "privacy_or_consent_notes": [],
    "minimum_reporting_views": []
  }
}
```
