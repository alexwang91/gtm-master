# S08 Output Contract

S08 must produce a full artifact, compressed handoff pack, S14-ready HTML section draft, evidence updates, decisions, and gaps.

## Output Envelope

```json
{
  "skill_id": "S08",
  "skill_name": "forecast-launch-demand",
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
  "artifact_id": "A08.launch-sales-full-artifact",
  "title": "Launch Sales Forecast: [Product] in [Country]",
  "format": "markdown_with_structured_json_blocks",
  "module_tier_summary": {},
  "core_sections": [
    "executive_summary",
    "forecast_input_coverage_gate",
    "forecast_scope_boundary",
    "forecast_assumption_tree",
    "scenario_sales_forecast",
    "segment_sales_split",
    "launch_sales_forecast",
    "lifecycle_phase_sales_curve",
    "marketing_investment_response_model",
    "baseline_incremental_sales_bridge",
    "channel_split_forecast",
    "price_conversion_assumption_bridge",
    "sensitivity_driver_tornado",
    "inventory_risk_map",
    "forecast_confidence_caps",
    "forecast_decision_gate",
    "validation_need_map",
    "evidence_assumptions_and_data_gaps"
  ],
  "conditional_sections": [
    "launch_calendar_seasonality_adjustment",
    "retail_sell_in_sell_through_split",
    "media_reach_to_demand_bridge",
    "marketing_spend_sensitivity_curve",
    "creator_traffic_demand_bridge",
    "dtc_conversion_scenario_bridge",
    "previous_generation_calibration",
    "supply_constraint_scenario",
    "preorder_waitlist_projection",
    "gross_revenue_range_estimate",
    "regional_channel_allocation",
    "forecast_review_gate"
  ],
  "audit_sections": [
    "forecast_evidence_trace",
    "forecast_assumption_log",
    "source_basis_matrix",
    "formula_trace",
    "excluded_private_data_log",
    "scenario_change_log"
  ]
}
```

## Compressed Handoff Pack

```json
{
  "handoff_id": "H08.launch-demand-pack",
  "from_skill": "S08.forecast-launch-demand",
  "to_skills": [
    "S09.predict-activation-risk",
    "S13.plan-validation-experiments",
    "S14.compose-html-gtm-dashboard"
  ],
  "summary": "",
  "canonical_fields": {
    "module_tier_summary": {},
    "forecast_input_coverage_gate": {},
    "forecast_scope_boundary": {},
    "forecast_assumption_tree": [],
    "scenario_sales_forecast": [],
    "segment_sales_split": [],
    "launch_sales_forecast": {},
    "lifecycle_phase_sales_curve": [],
    "marketing_investment_response_model": {},
    "baseline_incremental_sales_bridge": [],
    "channel_split_forecast": [],
    "price_conversion_assumption_bridge": {},
    "sensitivity_driver_tornado": [],
    "inventory_risk_map": [],
    "forecast_confidence_caps": {},
    "forecast_decision_gate": {},
    "validation_need_map": [],
    "conditional_outputs": {
      "launch_calendar_seasonality_adjustment": {},
      "retail_sell_in_sell_through_split": [],
      "media_reach_to_demand_bridge": {},
      "marketing_spend_sensitivity_curve": [],
      "creator_traffic_demand_bridge": {},
      "dtc_conversion_scenario_bridge": {},
      "previous_generation_calibration": {},
      "supply_constraint_scenario": [],
      "preorder_waitlist_projection": {},
      "gross_revenue_range_estimate": [],
      "regional_channel_allocation": [],
      "forecast_review_gate": {}
    },
    "audit_refs": {
      "forecast_evidence_trace_ref": "",
      "forecast_assumption_log_ref": "",
      "source_basis_matrix_ref": "",
      "formula_trace_ref": "",
      "excluded_private_data_log_ref": ""
    },
    "data_gaps": []
  },
  "key_findings": [],
  "required_downstream_use": [
    "S09 should use sales and channel scenarios as exposure context, not as guaranteed user volume.",
    "S13 should convert sensitivity drivers, confidence caps, and validation_need_map into prioritized validation experiments.",
    "S14 should render scenario ranges, confidence caveats, inventory risk, and data gaps without hiding assumptions."
  ],
  "do_not_reopen": [
    "Do not treat TAM/SAM/SOM seeds as forecasted launch units.",
    "Do not treat S06 creator estimates or S07 CVR ranges as measured sales.",
    "Do not expose private sales, inventory, PO, or channel data in public HTML unless approved."
  ],
  "open_questions": [],
  "data_gaps": [],
  "full_artifact_ref": ""
}
```

## Core Schemas

```json
{
  "forecast_input_coverage_gate": {
    "status": "ready | ready_with_gaps | directional_only | blocked",
    "selected_input_scenario": "A_directional_forecast | B_channel_allocation | C_inventory_decision | D_dtc_preorder_waitlist | E_previous_generation_calibration | F_media_creator_launch | G_lifecycle_marketing_investment | inferred",
    "forecast_horizon": "",
    "forecast_boundary": "demand_potential | reachable_launch_demand | launch_unit_sales | sell_in | sell_through | supply_constrained_shipments",
    "has_market_size_seed": false,
    "has_segment_split": false,
    "has_channel_context": false,
    "has_price_context": false,
    "has_conversion_basis": false,
    "has_inventory_context": false,
    "has_historical_calibration": false,
    "has_lifecycle_phase_calendar": false,
    "has_marketing_investment_plan": false,
    "has_marketing_response_basis": false,
    "has_baseline_calibration": false,
    "private_forecast_inputs_public_html_policy": "exclude_raw | aggregate | approved",
    "missing_fields_by_scenario": [],
    "confidence": "high | medium | low | hypothesis_only",
    "gaps": []
  },
  "scenario_sales_forecast": [
    {
      "scenario": "conservative | base | upside",
      "forecast_boundary": "demand_potential | reachable_launch_demand | launch_unit_sales | sell_in | sell_through | supply_constrained_shipments",
      "forecast_horizon": "",
      "unit_range": {"min": 0, "max": 0},
      "gross_revenue_range": {"min": 0, "max": 0, "currency": ""},
      "basis": [],
      "main_assumptions": [],
      "confidence": "high | medium | low | hypothesis_only",
      "caps_and_confounders": [],
      "evidence_refs": []
    }
  ],
  "channel_split_forecast": [
    {
      "channel": "",
      "unit_range": {"min": 0, "max": 0},
      "share_range": {"min": 0, "max": 0},
      "basis": "",
      "risk_notes": [],
      "confidence": "high | medium | low | hypothesis_only",
      "evidence_refs": []
    }
  ],
  "lifecycle_phase_sales_curve": [
    {
      "phase": "prelaunch_warmup | launch_spike | early_ramp | sustain | plateau_or_decay",
      "date_or_week_range": "",
      "baseline_unit_sales_range": {"min": 0, "max": 0},
      "marketing_incremental_unit_sales_range": {"min": 0, "max": 0},
      "total_unit_sales_range": {"min": 0, "max": 0},
      "main_drivers": [],
      "constraints": [],
      "confidence": "high | medium | low | hypothesis_only",
      "evidence_refs": []
    }
  ],
  "marketing_investment_response_model": {
    "response_model_type": "none | log_response | hill_saturation | adstock_saturation | measured_model",
    "adstock_or_lag_assumption": "",
    "saturation_or_diminishing_return_assumption": "",
    "spend_to_sales_bridge_basis": "measured_internal | platform_estimate | historical_proxy | S06_creator_estimate | S07_conversion_scenario | user_assumption | AI_heuristic | missing",
    "confidence": "high | medium | low | hypothesis_only",
    "caveats": []
  },
  "baseline_incremental_sales_bridge": [
    {
      "phase_or_channel": "",
      "baseline_unit_sales_range": {"min": 0, "max": 0},
      "marketing_incremental_unit_sales_range": {"min": 0, "max": 0},
      "pull_forward_or_cannibalization_note": "",
      "basis": "",
      "confidence": "high | medium | low | hypothesis_only",
      "evidence_refs": []
    }
  ],
  "inventory_risk_map": [
    {
      "scenario": "",
      "channel": "",
      "risk_type": "stockout | overstock | replenishment | allocation_mismatch | unknown",
      "risk_score": 0,
      "trigger": "",
      "recommended_action_or_test": "",
      "confidence": "high | medium | low | hypothesis_only",
      "evidence_refs": []
    }
  ],
  "validation_need_map": [
    {
      "assumption": "",
      "why_it_moves_forecast": "",
      "validation_method": "",
      "owner": "",
      "priority_score": 0,
      "decision_unlocked": "",
      "evidence_refs": []
    }
  ]
}
```
