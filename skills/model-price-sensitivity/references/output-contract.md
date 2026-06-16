# S04 Output Contract

S04 must produce a full artifact for humans, a compressed handoff pack for downstream skills, and an HTML section draft for the final dashboard.

## Output Envelope

```json
{
  "skill_id": "S04",
  "skill_name": "model-price-sensitivity",
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

## HTML Section Draft Requirement

`html_section_draft` must follow `references/html-section-contract.md` and include S14-ready `visual_blocks` in standard and deep mode. The draft is incomplete if it hides blockers, private-data limits, or price uncertainty behind generic pricing prose.

Read `references/html-visual-block-generation.md` before deriving these blocks from S04 pricing decision gates, credibility scores, WTP hypotheses, proof matrices, risk guardrails, and private calculator specs.

Minimum S04 visual coverage:

```text
pricing decision gate
opening price strategy
launch price architecture
local price credibility corridor
rapid WTP prior when real WTP or sales evidence is missing
WTP direct conclusion
segment WTP and sensitivity
price-value proof readiness
price risk guardrails
```

If any minimum view is missing, add `missing_required_view` or `rendered_too_thin` to `html_section_draft.data_gaps` and to the top-level `data_gaps`.

## Full Artifact

```json
{
  "artifact_id": "A04.price-sensitivity-full-artifact",
  "title": "Opening Price Strategy And Profit Boundary: [Product] in [Country]",
  "format": "markdown_with_structured_json_blocks",
  "module_tier_summary": {},
  "core_sections": [
    "executive_summary",
    "price_input_coverage_gate",
    "opening_price_strategy",
    "launch_price_architecture",
    "local_price_credibility_model",
    "rapid_price_prior",
    "wtp_direct_conclusion",
    "segment_wtp_hypothesis",
    "price_sensitivity_model",
    "price_value_proof_matrix",
    "price_risk_guardrail",
    "wtp_test_plan",
    "promo_subscription_guidance",
    "private_profit_revenue_optimizer_spec",
    "price_path_30_60_90",
    "pricing_decision_gate",
    "pricing_handoff_summary",
    "evidence_assumptions_and_data_gaps"
  ],
  "conditional_sections": [
    "van_westendorp_test_design",
    "gabor_granger_test_design",
    "maxdiff_feature_value_tradeoff_test_design",
    "conjoint_dce_test_plan",
    "channel_margin_guardrail",
    "retail_price_integrity_map",
    "accessory_bundle_attach_pricing",
    "subscription_pricing_hypothesis",
    "promo_test_plan",
    "elasticity_assumption_seed",
    "pricing_decision_options",
    "private_pricing_calculator_spec",
    "pricing_test_execution_kit",
    "pricing_test_result_interpretation"
  ],
  "audit_sections": [
    "price_anchor_audit",
    "competitor_price_gap_audit",
    "price_assumption_log",
    "sensitivity_calculation_trace",
    "private_pricing_input_register"
  ]
}
```

## Output Tiers

```json
{
  "module_tier_summary": {
    "core_modules_produced": [],
    "conditional_modules_produced": [],
    "conditional_modules_skipped": [
      {
        "module": "",
        "reason": "trigger_absent | insufficient_evidence | out_of_scope",
        "data_gap_or_followup": ""
      }
    ],
    "audit_modules_available": [],
    "default_html_modules": [],
    "deep_mode_only_modules": []
  }
}
```

## Compressed Handoff Pack

```json
{
  "handoff_id": "H04.price-sensitivity-pack",
  "from_skill": "S04.model-price-sensitivity",
  "to_skills": [
    "S05.score-creative-assets",
    "S07.predict-dtc-conversion",
    "S08.forecast-launch-demand",
    "S13.plan-validation-experiments",
    "S14.compose-html-gtm-dashboard"
  ],
  "summary": "",
  "canonical_fields": {
    "module_tier_summary": {},
    "price_input_coverage_gate": {},
    "opening_price_strategy": {},
    "launch_price_architecture": {},
    "local_price_credibility_model": {},
    "rapid_price_prior": {},
    "wtp_direct_conclusion": {},
    "segment_wtp_hypothesis": [],
    "price_sensitivity_model": {},
    "price_value_proof_matrix": [],
    "price_risk_guardrail": [],
    "wtp_test_plan": {},
    "promo_subscription_guidance": {},
    "private_profit_revenue_optimizer_spec": {},
    "price_path_30_60_90": [],
    "pricing_decision_gate": {},
    "pricing_handoff_summary": {},
    "conditional_outputs": {
      "van_westendorp_test_design": {},
      "gabor_granger_test_design": {},
      "maxdiff_feature_value_tradeoff_test_design": {},
      "conjoint_dce_test_plan": {},
      "channel_margin_guardrail": {},
      "retail_price_integrity_map": [],
      "accessory_bundle_attach_pricing": [],
      "subscription_pricing_hypothesis": {},
      "promo_test_plan": {},
      "elasticity_assumption_seed": {},
      "pricing_decision_options": [],
      "private_pricing_calculator_spec": {},
      "pricing_test_execution_kit": {},
      "pricing_test_result_interpretation": {}
    },
    "audit_refs": {
      "price_anchor_audit_ref": "",
      "competitor_price_gap_audit_ref": "",
      "price_assumption_log_ref": "",
      "sensitivity_calculation_trace_ref": "",
      "private_pricing_input_register_ref": ""
    },
    "confidence_caps": {},
    "data_gaps": []
  },
  "key_findings": [],
  "required_downstream_use": [
    "S05 should use price_message_seed, price risk guardrails, proof requirements, and promo guidance to evaluate editable copy price/value framing.",
    "S07 should use price_sensitivity_model, price risk guardrails, proof requirements, and promo guidance for funnel friction.",
    "S08 should use opening price strategy, launch price architecture, segment WTP hypotheses, price sensitivity model, elasticity assumptions, and pricing decision options for forecast scenarios.",
    "S13 should use opening strategy assumptions, rapid_price_prior calibration plans, WTP test plans, pricing data gaps, and confidence caps for validation planning.",
    "S14 should render html_section_draft, confidence badges, price caveats, and private-data exclusions."
  ],
  "do_not_reopen": [
    "Do not treat S01 price seed as final pricing.",
    "Do not treat price hypotheses as approved MSRP without internal constraints.",
    "Do not expose private margin, COGS, channel terms, or sales data in public sections unless approved."
  ],
  "open_questions": [],
  "data_gaps": [],
  "full_artifact_ref": ""
}
```

## Core Schemas

### Opening Price Strategy

```json
{
  "opening_price_strategy": {
    "recommended_strategy": "premium_anchor_promo | premium_proof_led | parity_value | penetration_attack | niche_high_price | test_before_scale | blocked",
    "strategic_objective": "profit | revenue | share | positioning | channel_entry | inventory_velocity | unknown",
    "strategy_scores": [
      {
        "strategy_id": "",
        "score_0_100": 0,
        "score_formula": "",
        "factor_scores": [
          {
            "factor_id": "",
            "score_0_100": 0,
            "weight": 0,
            "weighted_score": 0,
            "evidence_level": "direct | strong_proxy | weak_proxy | synthetic_stress_test | missing",
            "source_refs": [],
            "calculation_note": "",
            "confidence_cap": "high | medium | low | hypothesis_only"
          }
        ],
        "classification": "strong_fit | possible | weak_fit | blocked",
        "confidence_cap": "high | medium | low | hypothesis_only",
        "data_gaps": []
      }
    ],
    "recommended_public_anchor": "",
    "recommended_transaction_mechanism": "",
    "conditions_required": [],
    "why_this_strategy": "",
    "why_not_other_strategies": [],
    "do_not_do": [],
    "confidence": "high | medium | low | hypothesis_only",
    "evidence_refs": [],
    "data_gaps": []
  }
}
```

### Launch Price Architecture

```json
{
  "launch_price_architecture": {
    "currency": "",
    "public_anchor_price_or_msrp": "",
    "expected_transaction_price_range": "",
    "launch_offer_mechanism": "none | coupon | bundle | gift | trade_in | financing | installment | channel_subsidy | member_price | limited_time_discount | mixed | unknown",
    "promo_floor_price": "",
    "channel_floor_price": "",
    "revenue_max_price": "",
    "profit_max_price": "",
    "local_anchor_context": "",
    "price_ladder_position": "below_anchor | parity | slight_premium | major_premium | flagship | abnormal | unknown",
    "calculation_mode": "public_proxy_only | private_local_calculator | private_uploaded | derived_summary_only | blocked",
    "private_fields_required": [],
    "confidence": "high | medium | low | hypothesis_only",
    "evidence_refs": [],
    "data_gaps": []
  }
}
```

### Private Profit Revenue Optimizer Spec

```json
{
  "private_profit_revenue_optimizer_spec": {
    "mode": "client_side_blank_inputs | encrypted_local_snapshot | derived_summary_only | explicit_private_upload",
    "html_component_id": "private_profit_revenue_optimizer",
    "network_policy": "no_external_requests",
    "storage_policy": "memory_only_by_default",
    "private_input_fields": [],
    "candidate_price_grid": {
      "min_price": "",
      "max_price": "",
      "step_or_points": ""
    },
    "computed_fields": [
      "net_transaction_price",
      "estimated_units",
      "revenue",
      "unit_contribution",
      "contribution_profit",
      "revenue_max_price",
      "profit_max_price"
    ],
    "formula_notes": [],
    "public_rendering_policy": "do_not_render_raw_private_values",
    "downstream_handoff_policy": "formula_spec_and_user_approved_derived_summary_only",
    "security_warnings": [],
    "confidence_effect": ""
  }
}
```

### Price Path 30 60 90

```json
{
  "price_path_30_60_90": [
    {
      "phase": "day_0_30 | day_31_60 | day_61_90",
      "price_posture": "",
      "offer_mechanism": "",
      "decision_trigger": "",
      "watch_metrics": [],
      "guardrails": [],
      "allowed_moves": [],
      "forbidden_moves": [],
      "owner_hint": "pricing | marketing | channel | finance | sales | product",
      "confidence": "high | medium | low | hypothesis_only"
    }
  ]
}
```

### Local Price Credibility Model

```json
{
  "local_price_credibility_model": {
    "currency": "",
    "target_price_range": "",
    "price_display_context": {},
    "target_price_classification": "budget | entry | mainstream | premium | flagship | price_abnormal | unknown",
    "anchor_interpretation": "",
    "price_credibility_score": 0,
    "required_proof_to_sustain_price": [],
    "main_price_risks": [],
    "confidence": "high | medium | low",
    "evidence_refs": [],
    "data_gaps": []
  }
}
```

### Rapid Price Prior

Use this schema when real local WTP, internal sales evidence, or research access is missing. This is a quantitative prior, not measured willingness to pay.

```json
{
  "rapid_price_prior": {
    "status": "not_applicable | generated | generated_with_gaps | blocked",
    "target_price_or_band": "",
    "local_currency": "",
    "wtp_prior_range": {
      "range_type": "hypothesis_prior_range | measured_range_unavailable | blocked",
      "low": "",
      "base": "",
      "high": "",
      "anchor_basis": "",
      "multiplier_trace": []
    },
    "rapid_wtp_prior_score": 0,
    "pricing_classification": "price_supported_with_caveats | test_before_scale | research_first | price_not_supported_current_evidence | blocked",
    "factor_scores": [
      {
        "factor_id": "",
        "definition": "",
        "score_0_100": 0,
        "weight": 0,
        "weighted_score": 0,
        "evidence_level": "direct | strong_proxy | weak_proxy | synthetic_stress_test | missing",
        "source_refs": [],
        "calculation_note": "",
        "confidence_cap": "high | medium | low | hypothesis_only",
        "data_gaps": []
      }
    ],
    "evidence_grade": "A | B | C | D | E",
    "confidence_cap": "high | medium | low | hypothesis_only",
    "calibration_plan": [
      {
        "calibration_id": "",
        "weak_factor": "",
        "decision_unlocked": "price_posture | price_band | promo_need | channel_priority | forecast_input | finance_review | launch_go_no_go",
        "recommended_method": "targeted_anchor_collection | van_westendorp | gabor_granger | maxdiff | conjoint_dce | landing_page_price_ab | retailer_pdp_or_offer_test | keyword_or_ad_smoke_test | internal_sales_analysis | channel_partner_interview",
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
    "limits": [],
    "evidence_refs": [],
    "data_gaps": []
  }
}
```

### WTP Direct Conclusion

This object translates price evidence into the plain GTM answer. It must be
present whenever S04 emits a pricing section, even if the answer is
`research_first` or `blocked`.

```json
{
  "wtp_direct_conclusion": {
    "conclusion": "defend_target_price | defend_with_proof_or_offer | lower_effective_price | research_first | blocked",
    "plain_language_answer": "",
    "target_price_or_band": "",
    "target_price_defensibility": "strong | moderate | weak | unsupported | unknown",
    "segments_that_can_accept": [
      {
        "segment_id": "",
        "why_accepts": "",
        "required_proof_or_offer": [],
        "confidence": "high | medium | low | hypothesis_only"
      }
    ],
    "segments_that_resist": [
      {
        "segment_id": "",
        "why_resists": "",
        "likely_behavior": "trade_down | trade_up | wait_for_promo | choose_previous_generation | choose_competitor | delay_purchase | unknown",
        "mitigation": "",
        "confidence": "high | medium | low | hypothesis_only"
      }
    ],
    "minimum_proof_or_offer_required": [],
    "recommended_opening_posture": "premium_anchor_promo | premium_proof_led | parity_value | penetration_attack | niche_high_price | test_before_scale | blocked",
    "price_move_thresholds": [
      {
        "trigger": "",
        "move": "hold | bundle | finance | trade_in | coupon | channel_subsidy | lower_effective_price | raise_anchor | stop_scale",
        "watch_metric": "",
        "owner_hint": "pricing | marketing | channel | finance | sales | product | research"
      }
    ],
    "evidence_basis_summary": "",
    "confidence": "high | medium | low | hypothesis_only",
    "evidence_refs": [],
    "data_gaps": []
  }
}
```

### Segment WTP Hypothesis

```json
{
  "segment_wtp_hypothesis": [
    {
      "segment_id": "",
      "scenario_refs": [],
      "wtp_level": "low | medium | high | unknown",
      "acceptable_price_hypothesis": "",
      "premium_tolerance_hypothesis": "",
      "price_objections": [],
      "value_proof_needed": [],
      "recommended_test": "van_westendorp | gabor_granger | maxdiff | conjoint_dce | monadic_price | landing_page_price_test | no_test_needed | data_gap",
      "confidence": "high | medium | low",
      "evidence_refs": []
    }
  ]
}
```

### Price Sensitivity Model

```json
{
  "price_sensitivity_model": {
    "model_status": "evidence_backed | directional | hypothesis_only | blocked",
    "overall_price_sensitivity": "low | medium | high | very_high | unknown",
    "segment_sensitivity_summary": [],
    "price_ladder_risks": [],
    "price_gap_risks": [],
    "proof_dependency": [],
    "promo_dependency": "",
    "subscription_or_recurring_cost_risk": "",
    "confidence": "high | medium | low",
    "evidence_refs": [],
    "data_gaps": []
  }
}
```

### Price Risk Guardrail

```json
{
  "price_risk_guardrail": [
    {
      "risk_id": "",
      "risk_type": "affordability | premium_proof_gap | competitor_gap | channel_conflict | promo_dependency | margin_gap | subscription_resistance | claim_risk | return_support_risk | private_data_gap | other",
      "risk_summary": "",
      "affected_segments": [],
      "severity": "high | medium | low",
      "mitigation_or_test": "",
      "owner_hint": "pricing | finance | channel | marketing | sales | product | support | unknown",
      "evidence_refs": [],
      "confidence": "high | medium | low"
    }
  ]
}
```

### Accessory Bundle Attach Pricing

Use when an accessory/bundle catalog, attach-rate assumption, or accessory
price/margin basis exists. Hand the attach-rate seed to S08; do not present
attach revenue as device demand.

```json
{
  "accessory_bundle_attach_pricing": [
    {
      "accessory_or_bundle": "",
      "accessory_asp_band": "",
      "bundle_uplift_vs_standalone": "",
      "attach_rate_hypothesis": {"low": "", "base": "", "high": ""},
      "attach_margin_basis": "public_proxy | private_local_calculator | user_assumption | missing",
      "device_conversion_effect": "",
      "attach_rate_seed_for_s08": "",
      "confidence": "high | medium | low | hypothesis_only",
      "evidence_refs": [],
      "data_gaps": []
    }
  ]
}
```

### Private Pricing Calculator Spec

```json
{
  "private_pricing_calculator_spec": {
    "mode": "client_side_blank_inputs | encrypted_local_snapshot | derived_summary_only | explicit_private_upload",
    "html_component_id": "private_pricing_calculator",
    "network_policy": "no_external_requests",
    "storage_policy": "memory_only_by_default",
    "private_input_fields": [],
    "computed_fields": [],
    "formula_notes": [],
    "public_rendering_policy": "do_not_render_raw_private_values",
    "downstream_handoff_policy": "formula_spec_and_user_approved_derived_summary_only",
    "security_warnings": [],
    "confidence_effect": ""
  }
}
```

### Pricing Decision Gate

```json
{
  "pricing_decision_gate": {
    "status": "blocked | research_first | controlled_test_ready | finance_review | channel_review | forecast_ready | decision_review_ready",
    "status_reason": "",
    "readiness_scores": {
      "opening_strategy_score": 0,
      "price_credibility_score": 0,
      "rapid_wtp_prior_score": 0,
      "wtp_confidence_score": 0,
      "pricing_readiness_score": 0,
      "promo_risk_score": 0
    },
    "hard_blockers": [],
    "soft_risks": [],
    "candidate_options": [],
    "recommended_path": {},
    "downstream_readiness": {},
    "data_gaps": []
  }
}
```

### Pricing Test Execution Kit

```json
{
  "pricing_test_execution_kit": {
    "recommended_execution_level": "hypothesis_only | survey_panel | landing_page_test | marketplace_or_retail_test | internal_data_analysis | mixed",
    "respondent_screener": [],
    "stimulus_brief": [],
    "localized_question_blocks": [],
    "candidate_price_points": [],
    "ad_ab_price_test_plan": {},
    "retail_channel_price_test_plan": {},
    "survey_platform_notes": [],
    "panel_recruitment_brief": [],
    "csv_result_schema": [],
    "quality_checks": [],
    "analysis_plan": [],
    "decision_rules": [],
    "handoff_to_s13": [],
    "limits": []
  }
}
```

### Pricing Test Result Interpretation

```json
{
  "pricing_test_result_interpretation": {
    "result_source_type": "survey_panel | ad_ab | landing_page | marketplace | retail | channel_clickout | internal_sales | mixed",
    "data_quality_gate": {
      "status": "pass | pass_with_caveats | fail",
      "sample_or_traffic_size": "",
      "randomization_status": "randomized | matched_cells | observational | unknown",
      "control_quality": "strong | medium | weak | missing",
      "segment_match": "strong | medium | weak | unknown",
      "time_window_quality": "strong | medium | weak | unknown",
      "confounders": [],
      "missing_fields": [],
      "confidence_cap": "high | medium | low | hypothesis_only",
      "action": "interpret | interpret_with_caveats | request_cleaner_data | stop"
    },
    "method_specific_outputs": {},
    "price_variant_results": [],
    "decision_update": {},
    "handoff_updates": {},
    "data_gaps": []
  }
}
```
