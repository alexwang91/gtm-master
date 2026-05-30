# S13 Output Contract

S13 must produce a full artifact, compressed handoff pack, S14-ready HTML section draft, evidence updates, decisions, and gaps.

## Output Envelope

```json
{
  "skill_id": "S13",
  "skill_name": "plan-validation-experiments",
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
  "artifact_id": "A13.validation-roadmap-full-artifact",
  "title": "Validation Experiment Roadmap: [Product] in [Country]",
  "format": "markdown_with_structured_json_blocks",
  "module_tier_summary": {},
  "core_sections": [
    "executive_summary",
    "validation_input_coverage_gate",
    "assumption_inventory",
    "validation_question_backlog",
    "experiment_priority_scorecard",
    "validation_experiment_roadmap",
    "survey_test_plan",
    "opening_price_strategy_validation_plan",
    "rapid_price_prior_calibration_plan",
    "pricing_message_copy_test_plan",
    "channel_conversion_forecast_test_plan",
    "experiment_design_cards",
    "pass_fail_decision_rules",
    "sample_and_data_requirement_map",
    "owner_timeline_effort_map",
    "validation_decision_gate",
    "evidence_assumptions_and_data_gaps"
  ],
  "conditional_sections": [
    "van_westendorp_execution_brief",
    "gabor_granger_execution_brief",
    "conjoint_dce_execution_brief",
    "landing_page_ab_test_brief",
    "creator_pilot_test_brief",
    "retailer_channel_validation_brief",
    "forecast_assumption_validation_brief",
    "private_data_validation_path",
    "post_launch_learning_plan"
  ],
  "audit_sections": [
    "assumption_source_trace",
    "experiment_validity_audit",
    "excluded_or_deferred_tests_log",
    "private_data_exclusion_log",
    "synthetic_persona_use_log",
    "targeted_lookup_log",
    "context_budget_report"
  ]
}
```

## Compressed Handoff Pack

```json
{
  "handoff_id": "H13.validation-roadmap-pack",
  "from_skill": "S13.plan-validation-experiments",
  "to_skills": [
    "S14.compose-html-gtm-dashboard"
  ],
  "summary": "",
  "canonical_fields": {
    "module_tier_summary": {},
    "validation_input_coverage_gate": {},
    "assumption_inventory": [],
    "validation_question_backlog": [],
    "experiment_priority_scorecard": [],
    "validation_experiment_roadmap": [],
    "survey_test_plan": {},
    "opening_price_strategy_validation_plan": [],
    "rapid_price_prior_calibration_plan": [],
    "pricing_message_copy_test_plan": {},
    "channel_conversion_forecast_test_plan": {},
    "experiment_design_cards": [],
    "pass_fail_decision_rules": [],
    "sample_and_data_requirement_map": [],
    "owner_timeline_effort_map": [],
    "validation_decision_gate": {},
    "conditional_outputs": {
      "van_westendorp_execution_brief": {},
      "gabor_granger_execution_brief": {},
      "conjoint_dce_execution_brief": {},
      "landing_page_ab_test_brief": {},
      "creator_pilot_test_brief": {},
      "retailer_channel_validation_brief": {},
      "forecast_assumption_validation_brief": {},
      "private_data_validation_path": {},
      "post_launch_learning_plan": {}
    },
    "audit_refs": {
      "assumption_source_trace_ref": "",
      "experiment_validity_audit_ref": "",
      "excluded_or_deferred_tests_log_ref": "",
      "private_data_exclusion_log_ref": "",
      "synthetic_persona_use_log_ref": ""
    },
    "targeted_lookup_log": [],
    "context_budget_report": {},
    "data_gaps": []
  },
  "key_findings": [],
  "required_downstream_use": [
    "S14 should render validation status, priority tests, pass/fail rules, owners, timing, and gaps without creating new tests.",
    "Later live or post-launch modules should treat this roadmap as a plan, not completed evidence."
  ],
  "do_not_reopen": [
    "Do not rerun S01-S08 analysis.",
    "Do not treat synthetic personas as real validation evidence.",
    "Do not expose private raw inputs in public HTML."
  ],
  "open_questions": [],
  "data_gaps": [],
  "full_artifact_ref": ""
}
```

## Core Schemas

```json
{
  "validation_input_coverage_gate": {
    "status": "ready | ready_with_gaps | planning_only | blocked",
    "selected_input_scenario": "A_fast_gap_triage | B_prelaunch_validation_roadmap | C_price_message_validation | D_channel_conversion_forecast_validation | E_creator_copy_pilot_validation | F_private_internal_validation | G_post_launch_learning_plan | inferred",
    "source_skills_available": [],
    "source_skills_skipped": [],
    "has_data_gap_log": false,
    "has_confidence_caps": false,
    "has_test_backlogs": false,
    "has_decision_deadlines": false,
    "has_budget_or_effort_context": false,
    "private_data_policy": "exclude_raw | aggregate | approved | unknown",
    "missing_fields_by_scenario": [],
    "confidence": "high | medium | low | hypothesis_only",
    "gaps": []
  },
  "assumption_inventory": [
    {
      "assumption_id": "",
      "source_skill": "",
      "decision_area": "market | segment | message | pricing | copy | creator | conversion | forecast | channel | inventory | post_launch",
      "assumption": "",
      "current_basis": "measured_internal | public_source | upstream_model_output | survey_or_research_plan | live_experiment_plan | retailer_or_creator_partner_input | user_hypothesis | AI_heuristic | synthetic_hypothesis_generation | missing",
      "confidence": "high | medium | low | hypothesis_only",
      "impact_score": 0,
      "uncertainty_score": 0,
      "decision_urgency_score": 0,
      "evidence_refs": [],
      "data_gaps": []
    }
  ],
  "validation_experiment_roadmap": [
    {
      "experiment_id": "",
      "priority_score": 0,
      "decision_unlocked": "",
      "assumptions_tested": [],
      "recommended_method": "",
      "target_population_or_data_source": "",
      "sample_or_data_requirement": "",
      "owner": "",
      "timing": "",
      "budget_or_effort_band": "low | medium | high | unknown",
      "pass_rule": "",
      "fail_rule": "",
      "failure_action": "",
      "confidence_after_pass": "high | medium | low | hypothesis_only",
      "confidence_after_fail": "high | medium | low | hypothesis_only",
      "evidence_refs": []
    }
  ],
  "experiment_design_cards": [
    {
      "experiment_id": "",
      "hypothesis": "",
      "method": "",
      "stimulus_or_materials_needed": [],
      "controlled_variables": [],
      "primary_metric": "",
      "secondary_metrics": [],
      "runtime_or_collection_window": "",
      "privacy_or_compliance_notes": [],
      "validity_risks": []
    }
  ],
  "rapid_price_prior_calibration_plan": [
    {
      "source_prior_ref": "",
      "weak_factor": "",
      "current_score_0_100": 0,
      "current_evidence_level": "direct | strong_proxy | weak_proxy | synthetic_stress_test | missing",
      "current_confidence_cap": "high | medium | low | hypothesis_only",
      "recommended_method": "targeted_anchor_collection | van_westendorp | gabor_granger | conjoint_dce | landing_page_price_ab | retailer_pdp_or_offer_test | keyword_or_ad_smoke_test | internal_sales_analysis | channel_partner_interview",
      "decision_unlocked": "price_posture | price_band | promo_need | channel_priority | forecast_input | finance_review | launch_go_no_go",
      "minimum_sample_or_data": "",
      "pass_rule": "",
      "fail_rule": "",
      "update_rule": "",
      "owner_hint": "pricing | marketing | channel | finance | sales | product | research",
      "budget_or_effort_band": "low | medium | high",
      "evidence_upgrade_if_pass": "medium | high",
      "limits": []
    }
  ],
  "opening_price_strategy_validation_plan": [
    {
      "source_strategy_ref": "",
      "strategy_assumption": "",
      "decision_unlocked": "opening_strategy | public_anchor | transaction_mechanism | promo_floor | channel_floor | revenue_max_price | profit_max_price | price_path",
      "current_confidence": "high | medium | low | hypothesis_only",
      "recommended_method": "private_optimizer_run | derived_private_summary | channel_partner_interview | retailer_pdp_or_offer_test | landing_page_price_ab | gabor_granger | internal_sales_analysis | forecast_sensitivity_review",
      "minimum_sample_or_data": "",
      "pass_rule": "",
      "fail_rule": "",
      "update_rule": "",
      "owner_hint": "pricing | marketing | channel | finance | sales | product | research",
      "budget_or_effort_band": "low | medium | high",
      "limits": []
    }
  ],
  "validation_decision_gate": {
    "status": "ready_to_decide | decide_with_caveats | needs_validation | blocked",
    "decisions_ready": [],
    "decisions_requiring_validation": [],
    "blocked_decisions": [],
    "top_tests_to_run_first": [],
    "confidence": "high | medium | low | hypothesis_only",
    "gaps": []
  },
  "targeted_lookup_log": [
    {
      "lookup_id": "",
      "reason": "",
      "source_type": "",
      "queries_or_refs_used": [],
      "fields_extracted": [],
      "decision_impact": "",
      "result": "used | partial | unavailable | deferred",
      "created_evidence_refs": [],
      "limitations": []
    }
  ],
  "context_budget_report": {
    "context_policy": "handoff_only | targeted_escalation",
    "handoff_packs_used": [],
    "full_artifacts_opened": [],
    "local_files_opened": [],
    "rag_refs_retrieved": [],
    "web_or_mcp_lookups": [],
    "assumptions_in_main_view": 0,
    "assumptions_deferred": 0,
    "reason_if_budget_exceeded": ""
  }
}
```
