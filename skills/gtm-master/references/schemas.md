# GTM Master Schemas

Use these schemas as contracts. Keep fields stable across sub-skills.

## Project Brief

```json
{
  "project_id": "",
  "product_name_or_codename": "",
  "product_category": "",
  "product_features_and_specs": "",
  "launch_country_or_region": "",
  "target_price_range": "",
  "report_language": "BCP-47 tag or clear language name supplied by user",
  "report_language_source": "user_supplied | missing_needs_intake",
  "currency": "",
  "launch_timing": "",
  "target_price_or_msrp": "",
  "target_margin_or_floor_price": "",
  "cogs_or_bom": "",
  "channel_margin_terms": "",
  "retailer_or_marketplace_fee_rules": "",
  "promo_discount_policy": "",
  "inventory_or_forecast_constraints": "",
  "subscription_or_recurring_revenue_model": "",
  "finance_installment_constraints": "",
  "forecast_input_scenario": "A_directional_forecast | B_channel_allocation | C_inventory_decision | D_dtc_preorder_waitlist | E_previous_generation_calibration | F_media_creator_launch | G_lifecycle_marketing_investment",
  "structured_forecast_input_pack": {},
  "product_lifecycle_stage": "prelaunch | launch | early_growth | growth | maturity | decline | unknown",
  "launch_phase_calendar": [],
  "lifecycle_curve_assumption": "phase_multiplier_curve | S_curve | Bass_diffusion_proxy | cohort_curve | unknown",
  "marketing_investment_plan": [],
  "marketing_spend_by_phase": [],
  "marketing_response_assumptions": {},
  "historical_marketing_response_data": "",
  "baseline_calibration": {},
  "baseline_vs_incremental_sales_policy": "separate | aggregate_only",
  "constraints": {},
  "forecast_horizon": "launch_week | 30_days | 60_days | 90_days | custom",
  "target_sellout_window": "",
  "brand_positioning": "",
  "planned_channels": [],
  "known_competitors": [],
  "planned_channel_mix": [],
  "channel_capacity_constraints": [],
  "launch_inventory_available": "",
  "inventory_allocation_plan": [],
  "supply_lead_time_or_replenishment_constraints": "",
  "retail_sell_in_commitments_or_purchase_orders": "",
  "preorder_or_waitlist_counts": "",
  "marketing_budget_range": "",
  "media_plan_or_reach_assumptions": [],
  "historical_launch_sales_or_sellthrough": "",
  "seasonality_or_retail_calendar_notes": "",
  "target_revenue_or_unit_goal": "",
  "forecast_output_granularity": "total | segment | channel | segment_x_channel",
  "private_forecast_inputs_public_html_policy": "exclude_raw | aggregate | approved",
  "validation_input_scenario": "A_fast_gap_triage | B_prelaunch_validation_roadmap | C_price_message_validation | D_channel_conversion_forecast_validation | E_creator_copy_pilot_validation | F_private_internal_validation | G_post_launch_learning_plan",
  "validation_budget_range": "",
  "target_launch_date": "",
  "decision_deadlines": [],
  "available_testing_channels": [],
  "allowed_test_markets_or_countries": [],
  "sample_access": "",
  "survey_panel_access": "",
  "ad_account_or_media_test_access": "",
  "landing_page_or_pdp_test_access": "",
  "retailer_or_creator_pilot_access": "",
  "private_data_policy": "exclude_raw | aggregate | approved",
  "output_detail_level": "quick | standard | real_product_pilot | deep",
  "copy_assets_or_concepts": [],
  "historical_copy_landing_pages_kol_scripts_and_ads": "",
  "creator_budget_range": "",
  "creator_candidates": [],
  "known_creator_blacklist_or_risk_notes": [],
  "sponsorship_disclosure_policy": "",
  "target_platforms": [],
  "creator_rate_cards_or_media_kits": [],
  "campaign_budget_currency": "",
  "product_seeding_cost_or_sample_value": "",
  "historical_creator_performance_data": "",
  "creator_campaign_goal": "",
  "candidate_review_list_size": 8,
  "creator_candidate_review_decisions": [],
  "tracking_or_landing_page_context": "",
  "launch_page_planning_stage": "none | concept | draft | live | post_launch",
  "page_or_funnel_text": "",
  "landing_page_url_or_pdp_url": "",
  "page_structure_or_wireframe_text": "",
  "checkout_flow_description": "",
  "traffic_source_plan": [],
  "analytics_or_conversion_data": "",
  "historical_landing_page_results": "",
  "tracking_or_analytics_context": "",
  "offer_details": "",
  "return_warranty_shipping_payment_policy": "",
  "competitor_landing_pages_or_pdp_refs": [],
  "previous_generation_page_or_pdp_refs": [],
  "previous_generation_conversion_or_page_results": "",
  "competitor_offer_trust_policy_refs": [],
  "fixed_visual_or_layout_constraints": "",
  "target_language": "local evidence/search language; may differ from report_language",
  "output_language": "normalized copy of report_language",
  "claim_constraints": "",
  "compliance_constraints": "",
  "report_audience": "",
  "report_depth": "quick | standard | real_product_pilot | deep",
  "html_style_preference": "",
  "assumptions": [],
  "missing_optional_inputs": []
}
```

## Skill Runtime Input

```json
{
  "project_brief": {},
  "active_skill": "",
  "active_modules": [],
  "task_goal": "",
  "upstream_handoff_pack": {},
  "allowed_evidence_refs": [],
  "skill_method_card": {},
  "allowed_inputs": [],
  "allowed_outputs": [],
  "out_of_scope": [],
  "quality_gate": []
}
```

## GTM Run State

```json
{
  "run_id": "",
  "project_id": "",
  "report_version": "v1",
  "phase": "intake | evidence | skill_run | review | finalize | finalized",
  "current_skill": "",
  "current_gate": "",
  "resume_pointer": {
    "next_skill": "",
    "next_action": "",
    "required_refs": []
  },
  "selected_run_mode": "quick | standard | real_product_pilot | deep",
  "skill_status": {},
  "approved_sections": [],
  "pending_review_items": [],
  "state_artifacts": {
    "project_brief_ref": "",
    "evidence_ledger_ref": "",
    "decision_log_ref": "",
    "data_gap_log_ref": "",
    "report_state_ref": ""
  },
  "idempotency_key": "",
  "last_updated": ""
}
```

## Skill Output Envelope

```json
{
  "skill_id": "",
  "skill_name": "",
  "full_artifact": {
    "artifact_id": "",
    "title": "",
    "format": "markdown | json | html | mixed",
    "content_or_path": ""
  },
  "compressed_handoff_pack": {},
  "html_section_draft": {},
  "evidence_updates": [],
  "decision_updates": [],
  "risk_updates": [],
  "data_gaps": [],
  "context_escalations": [],
  "recoverable_run_state_updates": [],
  "post_skill_isolation_record": {},
  "quality_gate_result": {
    "status": "pass | pass_with_caveats | fail",
    "failed_checks": [],
    "notes": ""
  },
  "recommended_next_skills": []
}
```

## Post Skill Isolation Record

```json
{
  "isolation_id": "",
  "skill_id": "",
  "status": "isolated | isolated_with_gaps | blocked",
  "full_artifact_ref": "",
  "compressed_handoff_ref": "",
  "html_section_ref": "",
  "evidence_update_refs": [],
  "decision_update_refs": [],
  "data_gap_refs": [],
  "allowed_downstream_refs": [],
  "withheld_context": [],
  "reopen_conditions": [],
  "privacy_notes": [],
  "quality_gate_status": "pass | pass_with_caveats | fail"
}
```

## Compressed Handoff Pack

```json
{
  "handoff_id": "",
  "from_skill": "",
  "to_skills": [],
  "summary": "",
  "canonical_fields": {},
  "key_findings": [
    {
      "finding": "",
      "evidence_level": "direct_evidence | cross_source_evidence | internal_evidence | model_inference | weak_hypothesis | needs_validation | avoid_or_risk",
      "evidence_refs": [],
      "confidence": "high | medium | low"
    }
  ],
  "required_downstream_use": [],
  "do_not_reopen": [],
  "open_questions": [],
  "data_gaps": [],
  "full_artifact_ref": ""
}
```

## Evidence Record

```json
{
  "evidence_id": "",
  "evidence_type": "competitor | price | review | social_discussion | expert_review | internal_sales | internal_review | internal_support | internal_app_analytics | survey | market_size | other",
  "country_or_region": "",
  "language": "source language of the evidence",
  "source_name": "",
  "source_url_or_path": "",
  "source_type": "",
  "collected_at": "",
  "freshness_window": "",
  "connector_slot": "",
  "tool_or_connector_used": "",
  "raw_excerpt_or_value": "",
  "translated_excerpt": "",
  "claim_supported": "",
  "confidence": "high | medium | low",
  "limitations": [],
  "pii_status": "none | redacted | restricted",
  "usage_permission": "approved | public_context_only | restricted | unavailable"
}
```

## RAG Index Manifest

```json
{
  "project_id": "",
  "indexed_collections": [],
  "embedding_policy": {
    "index_short_excerpts_only": true,
    "index_private_evidence_separately": true,
    "do_not_index_raw_html": true,
    "do_not_mix_private_and_public_collections": true
  },
  "retrieval_policy": {
    "prefer_evidence_ids_from_handoff": true,
    "filter_by_country_or_region": true,
    "filter_by_allowed_use": true,
    "rerank_by_source_quality": true
  }
}
```

## Context Escalation

```json
{
  "context_escalation_id": "",
  "active_skill": "",
  "opened_artifact_ref": "",
  "reason": "missing_required_field | contradiction | low_confidence | raw_quote_needed | user_requested_audit | other",
  "fields_needed": [],
  "decision": "",
  "new_evidence_refs": []
}
```

## HTML Section Draft

```json
{
  "section_id": "",
  "section_title": "",
  "narrative_summary": "",
  "key_cards": [],
  "visual_blocks": [],
  "tables": [],
  "charts": [],
  "confidence_badges": [],
  "citations": [],
  "data_gap_notes": [],
  "recommended_visual_style": "executive | consulting | dashboard | investor_deck"
}
```

Use `visual_blocks` for the standard S14 components: `status_panel`, `ranked_bar`, `matrix_heatmap`, and `range_chart`. S01-S08 should include these blocks for required proof views; missing required blocks should appear as data gaps. See `report-data-contract.md` and `visual-block-acceptance-matrix.md` for the full block schema.

## Decision Record

```json
{
  "decision_id": "",
  "decision": "",
  "applies_to_nodes": [],
  "rationale": "",
  "evidence_refs": [],
  "supersedes": [],
  "reopen_conditions": [],
  "decided_at": ""
}
```
