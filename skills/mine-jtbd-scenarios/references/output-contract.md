# S02 Output Contract

S02 must produce a full artifact for humans, a compressed handoff pack for downstream skills, and an HTML section draft for the final dashboard.

## Output Envelope

```json
{
  "skill_id": "S02",
  "skill_name": "mine-jtbd-scenarios",
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

`html_section_draft` must follow `references/html-section-contract.md` and include S14-ready `visual_blocks` in standard and deep mode. The draft is incomplete if it only contains scenario prose or unprioritized tables.

Read `references/html-visual-block-generation.md` before deriving these blocks from S02 scenario scores, matrices, proof requirements, and risk fields.

Minimum S02 visual coverage:

```text
upstream input coverage gate when confidence is capped
scenario priority scorecard
scenario-to-segment matrix
product-job fit and proof readiness
```

If any minimum view is missing, add `missing_required_view` or `rendered_too_thin` to `html_section_draft.data_gaps` and to the top-level `data_gaps`.

## Full Artifact

```json
{
  "artifact_id": "A02.jtbd-scenarios-full-artifact",
  "title": "JTBD Scenarios: [Product] in [Country]",
  "format": "markdown_with_structured_json_blocks",
  "module_tier_summary": {},
  "core_sections": [
    "executive_summary",
    "upstream_input_coverage_gate",
    "jtbd_scenario_pack",
    "scenario_priority_scorecard",
    "scenario_to_segment_matrix",
    "four_forces_switching_map",
    "product_job_fit_matrix",
    "proof_requirement_seed",
    "anti_jtbd_risk_list",
    "local_language_trigger_phrase_map",
    "scenario_message_seed",
    "scenario_price_implication_seed",
    "evidence_assumptions_and_data_gaps"
  ],
  "conditional_sections": [
    "consumer_electronics_gtm_moment_map",
    "digital_shelf_and_retailer_decision_map",
    "behavioral_science_lever_map",
    "scenario_commercial_weight_map",
    "brand_claim_constraint_map",
    "validation_question_seed",
    "non_consumption_risk_map",
    "scenario_to_journey_matrix"
  ],
  "audit_sections": [
    "upstream_handoff_coverage",
    "upstream_input_map",
    "jtbd_source_map",
    "jtbd_candidate_pool",
    "jtbd_scenario_clusters",
    "scenario_distinctness_check"
  ]
}
```

## Output Tiers

Core fields are always produced. Conditional fields are produced only when their trigger is present. Audit fields are kept in the full artifact or by reference and should not appear in default HTML.

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

Default core modules:

```text
upstream_input_coverage_gate
jtbd_scenario_pack
scenario_priority_scorecard
scenario_to_segment_matrix
four_forces_switching_map
product_job_fit_matrix
proof_requirement_seed
anti_jtbd_risk_list
local_language_trigger_phrase_map
scenario_message_seed
scenario_price_implication_seed
```

Conditional module triggers:

```text
consumer_electronics_gtm_moment_map
  Produce as a separate module only when the journey stage changes message, channel, proof, activation, or support decisions. Otherwise embed moments in jtbd_scenario_pack.

digital_shelf_and_retailer_decision_map
  Produce when DTC, marketplace, retail, shopping search, store availability, delivery, return, warranty, payment, or channel conversion matters.

behavioral_science_lever_map
  Produce when downstream message, creative, funnel, proof, offer, or risk-reversal testing is planned.

scenario_commercial_weight_map
  Produce when launch sequencing, market sizing, inventory, channel priority, or commercial prioritization depends on scenario differences. Otherwise embed sub-scores in scenario_priority_scorecard.

brand_claim_constraint_map
  Produce when claims touch health, safety, privacy, accuracy, battery, children, elderly, certifications, warranty, sustainability, or regulated-adjacent issues.

validation_question_seed
  Produce when lead scenarios are weak, user-provided, confidence-capped, or commercially important enough to test.

non_consumption_risk_map
  Produce when doing nothing, delaying purchase, workaround use, or substitute sufficiency is a material risk.

scenario_to_journey_matrix
  Produce as a separate module only when journey-stage differences change downstream work. Otherwise embed journey refs in jtbd_scenario_pack.
```

## Compressed Handoff Pack

```json
{
  "handoff_id": "H02.jtbd-scenario-pack",
  "from_skill": "S02.mine-jtbd-scenarios",
  "to_skills": [
    "S03.match-messages-to-segments",
    "S04.model-price-sensitivity",
    "S13.plan-validation-experiments",
    "S14.compose-html-gtm-dashboard"
  ],
  "summary": "",
  "canonical_fields": {
    "module_tier_summary": {},
    "upstream_input_coverage_gate": {},
    "jtbd_scenario_pack": [],
    "scenario_to_segment_matrix": [],
    "four_forces_switching_map": [],
    "product_job_fit_matrix": [],
    "scenario_priority_scorecard": [],
    "proof_requirement_seed": [],
    "anti_jtbd_risk_list": [],
    "local_language_trigger_phrase_map": [],
    "scenario_message_seed": [],
    "scenario_price_implication_seed": [],
    "conditional_outputs": {
      "consumer_electronics_gtm_moment_map": [],
      "digital_shelf_and_retailer_decision_map": [],
      "behavioral_science_lever_map": [],
      "scenario_commercial_weight_map": [],
      "brand_claim_constraint_map": [],
      "validation_question_seed": [],
      "non_consumption_risk_map": [],
      "scenario_to_journey_matrix": []
    },
    "audit_refs": {
      "upstream_input_map_ref": "",
      "jtbd_source_map_ref": "",
      "jtbd_candidate_pool_ref": "",
      "jtbd_scenario_clusters_ref": "",
      "scenario_distinctness_results_ref": ""
    },
    "confidence_caps": {},
    "data_gaps": []
  },
  "key_findings": [],
  "required_downstream_use": [
    "S03 should use jtbd_scenario_pack, proof_requirement_seed, scenario_message_seed, local trigger phrases, anti-JTBD risks, and do-not-claim notes.",
    "S03 should use consumer_electronics_gtm_moment_map, product_job_fit_matrix, behavioral_science_lever_map, and brand_claim_constraint_map as input constraints, not final copy.",
    "S04 should use scenario_price_implication_seed, price-related objections, willingness-to-pay context, value proof requirements, commercial weight, and digital shelf price/promo factors.",
    "S07 should use digital_shelf_and_retailer_decision_map when DTC, marketplace, or retailer conversion matters.",
    "S13 should use validation_question_seed, weak-but-important scenario hypotheses, and data gaps.",
    "S14 should render html_section_draft, priority scores, evidence badges, citations, and scenario caveats."
  ],
  "do_not_reopen": [
    "Do not re-mine S01 evidence unless a required field is missing or a confidence gate fails.",
    "Do not treat JTBD scenarios as final copy.",
    "Do not treat weak scenario hypotheses as proven demand."
  ],
  "open_questions": [],
  "data_gaps": [],
  "full_artifact_ref": ""
}
```

## Canonical Schemas

### JTBD Source Map

```json
{
  "jtbd_source_map": [
    {
      "source_map_id": "",
      "source_signal_type": "voice_atom | theme_cluster | journey_episode | bain_driver | competitor_complaint | purchase_trigger | objection | segment_seed | price_signal | hardware_diagnosis | user_hypothesis",
      "source_ref": "",
      "signal_summary": "",
      "linked_segments": [],
      "linked_competitors_or_substitutes": [],
      "evidence_refs": [],
      "confidence": "high | medium | low"
    }
  ]
}
```

### JTBD Candidate

```json
{
  "jtbd_candidate_pool": [
    {
      "candidate_id": "",
      "raw_need_signal": "",
      "local_language_phrases": [],
      "situation": "",
      "motivation_or_progress": "",
      "desired_outcome": "",
      "current_alternative": "",
      "barriers_or_anxieties": [],
      "functional_job": "",
      "emotional_job": "",
      "social_job": "",
      "source_signal_refs": [],
      "evidence_refs": [],
      "confidence": "high | medium | low"
    }
  ]
}
```

### JTBD Scenario Pack

```json
{
  "jtbd_scenario_pack": [
    {
      "scenario_id": "",
      "scenario_name": "",
      "job_statement": "When [situation], I want to [motivation/progress], so I can [desired outcome], instead of [current alternative], while avoiding [barrier].",
      "trigger_context": "",
      "primary_segments": [],
      "secondary_segments": [],
      "local_language_trigger_phrases": [],
      "current_alternatives": [],
      "competitor_or_substitute_refs": [],
      "desired_outcomes": [],
      "success_metrics": [],
      "barriers_and_anxieties": [],
      "proof_requirements": [],
      "journey_episode_refs": [],
      "product_capability_fit": [],
      "price_sensitivity_signals": [],
      "channel_touchpoint_refs": [],
      "earned_growth_or_advocacy_signal": "",
      "scenario_priority_score": 0,
      "evidence_strength_score": 0,
      "confidence": "high | medium | low",
      "evidence_refs": [],
      "data_gaps": []
    }
  ]
}
```

### Consumer Electronics GTM Moment Map

```json
{
  "consumer_electronics_gtm_moment_map": []
}
```

See `consumer-electronics-gtm-methods.md` for schema and rules.

### Four Forces Switching Map

```json
{
  "four_forces_switching_map": [
    {
      "scenario_id": "",
      "push_score": 0,
      "push_reason": "",
      "pull_score": 0,
      "pull_reason": "",
      "habit_score": 0,
      "habit_reason": "",
      "anxiety_score": 0,
      "anxiety_reason": "",
      "net_switching_readiness": "high | medium | low | blocked",
      "marketing_action_hook": "",
      "pricing_or_proof_hook": "",
      "evidence_refs": [],
      "confidence": "high | medium | low | hypothesis_only"
    }
  ]
}
```

Use Push, Pull, Habit, and Anxiety to explain switching dynamics. Do not treat a high pain signal as purchase readiness when habit or anxiety is also high.

### Product-Job Fit Matrix

```json
{
  "product_job_fit_matrix": []
}
```

See `consumer-electronics-gtm-methods.md` for schema and rules.

### Scenario Commercial Weight Map

```json
{
  "scenario_commercial_weight_map": []
}
```

See `consumer-electronics-gtm-methods.md` for schema and rules.

## Evidence Update

```json
{
  "evidence_id": "",
  "evidence_type": "jtbd_source_map | jtbd_candidate | scenario_cluster | proof_requirement | anti_jtbd_risk | validation_question | other",
  "source_evidence_refs": [],
  "claim_supported": "",
  "confidence": "high | medium | low",
  "limitations": []
}
```

## Recommended Next Skills

```json
[
  {
    "skill_id": "S03",
    "reason": "Message architecture needs prioritized scenarios, proof requirements, objections, and local trigger phrases.",
    "priority": "required | recommended | optional",
    "blocking_data_gaps": []
  }
]
```
