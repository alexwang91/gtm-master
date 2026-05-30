# S03 Output Contract

S03 must produce a full artifact for humans, a compressed handoff pack for downstream skills, and an HTML section draft for the final dashboard.

## Output Envelope

```json
{
  "skill_id": "S03",
  "skill_name": "match-messages-to-segments",
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

`html_section_draft` must follow `references/html-section-contract.md` and include S14-ready `visual_blocks` in standard and deep mode. The draft is incomplete if it only contains message seeds or copy-like prose.

Read `references/html-visual-block-generation.md` before deriving these blocks from S03 message-market fit, proof readiness, claim risk, and objection fields.

Minimum S03 visual coverage:

```text
message input coverage gate when confidence is capped
segment-message fit
feature-benefit-proof readiness
claim risk and proof gate
objection severity ranking
```

If any minimum view is missing, add `missing_required_view` or `rendered_too_thin` to `html_section_draft.data_gaps` and to the top-level `data_gaps`.

## Full Artifact

```json
{
  "artifact_id": "A03.message-architecture-full-artifact",
  "title": "Message Architecture: [Product] in [Country]",
  "format": "markdown_with_structured_json_blocks",
  "module_tier_summary": {},
  "core_sections": [
    "executive_summary",
    "message_input_coverage_gate",
    "segment_message_architecture",
    "feature_benefit_proof_matrix",
    "objection_matrix",
    "claim_risk_and_proof_gate",
    "local_language_message_seed",
    "price_message_seed",
    "message_market_fit_scorecard",
    "evidence_assumptions_and_data_gaps"
  ],
  "conditional_sections": [
    "competitive_contrast_matrix",
    "behavioral_lever_message_seed",
    "retail_sales_talk_track_seed",
    "landing_page_message_block_seed",
    "creator_brief_message_seed",
    "compliance_review_queue",
    "message_test_backlog"
  ],
  "audit_sections": [
    "message_source_trace",
    "message_variant_pool",
    "rejected_message_angles",
    "claim_evidence_audit"
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
  "handoff_id": "H03.message-architecture-pack",
  "from_skill": "S03.match-messages-to-segments",
  "to_skills": [
    "S04.model-price-sensitivity",
    "S05.score-creative-assets",
    "S06.score-kol-fit",
    "S07.predict-dtc-conversion",
    "S14.compose-html-gtm-dashboard"
  ],
  "summary": "",
  "canonical_fields": {
    "module_tier_summary": {},
    "message_input_coverage_gate": {},
    "segment_message_architecture": [],
    "feature_benefit_proof_matrix": [],
    "objection_matrix": [],
    "claim_risk_and_proof_gate": {},
    "local_language_message_seed": [],
    "price_message_seed": [],
    "message_market_fit_scorecard": [],
    "message_investment_allocation_seed": [],
    "conditional_outputs": {
      "competitive_contrast_matrix": [],
      "behavioral_lever_message_seed": [],
      "retail_sales_talk_track_seed": [],
      "landing_page_message_block_seed": [],
      "creator_brief_message_seed": [],
      "compliance_review_queue": [],
      "message_test_backlog": []
    },
    "audit_refs": {
      "message_source_trace_ref": "",
      "message_variant_pool_ref": "",
      "rejected_message_angles_ref": "",
      "claim_evidence_audit_ref": ""
    },
    "confidence_caps": {},
    "data_gaps": []
  },
  "key_findings": [],
  "required_downstream_use": [
    "S04 should use price_message_seed, price objections, proof requirements, and claim risk gates before pricing recommendations.",
    "S05 should use segment_message_architecture, feature_benefit_proof_matrix, objection_matrix, and behavioral lever seeds when scoring creative assets.",
    "S06 should use creator_brief_message_seed, recommended MKT carrier archetypes, message investment allocation seeds, and proof requirements when creator or expert content matters.",
    "S07 should use landing_page_message_block_seed, price message seeds, objection matrix, proof requirements, and claim risk gates for funnel analysis.",
    "S13 should use price message seeds and message investment allocation seeds to design message, price narrative, and proof validation tests.",
    "S14 should render html_section_draft, confidence badges, claim/proof status, and data gaps."
  ],
  "do_not_reopen": [
    "Do not rewrite S02 JTBD scenarios unless a blocking inconsistency is found.",
    "Do not treat message seeds as final copy.",
    "Do not present risky claims without proof and review status."
  ],
  "open_questions": [],
  "data_gaps": [],
  "full_artifact_ref": ""
}
```

## Core Schemas

### Segment Message Architecture

```json
{
  "segment_message_architecture": [
    {
      "segment_id": "",
      "scenario_refs": [],
      "message_role": "lead | support | proof | objection_handling | retention | avoid",
      "message_angle_seed": "",
      "primary_benefit": "",
      "supporting_benefits": [],
      "proof_requirements": [],
      "recommended_mkt_carrier_archetype": "brand_official | retailer_sales | expert_reviewer | lifestyle_creator | category_kol | community_advocate | paid_social | pr | owned_dtc | other",
      "investment_percent_seed": 0,
      "budget_note": "",
      "local_language_terms_to_preserve": [],
      "objections_to_address": [],
      "claims_to_avoid": [],
      "confidence": "high | medium | low",
      "evidence_refs": []
    }
  ]
}
```

### Message Investment Allocation Seed

This is an initial testing and attention split for message routes, not final media budget approval.

```json
{
  "message_investment_allocation_seed": [
    {
      "message_route_id": "",
      "message_angle_seed": "",
      "recommended_percent": 0,
      "budget_note": "",
      "recommended_mkt_carrier_archetype": "brand_official | retailer_sales | expert_reviewer | lifestyle_creator | category_kol | community_advocate | paid_social | pr | owned_dtc | other",
      "why_this_carrier": "",
      "channel_fit": "high | medium | low",
      "proof_dependency": [],
      "confidence": "high | medium | low",
      "evidence_refs": []
    }
  ]
}
```

### Feature Benefit Proof Matrix

```json
{
  "feature_benefit_proof_matrix": [
    {
      "feature_or_capability": "",
      "scenario_refs": [],
      "segment_refs": [],
      "benefit": "",
      "consumer_question_answered": "",
      "proof_type": "",
      "proof_status": "available | partial | missing | risky",
      "proof_asset_refs": [],
      "claim_risk": "high | medium | low",
      "evidence_refs": []
    }
  ]
}
```

### Objection Matrix

```json
{
  "objection_matrix": [
    {
      "objection_id": "",
      "scenario_refs": [],
      "segment_refs": [],
      "objection": "",
      "objection_type": "price | trust | proof | setup | compatibility | privacy | warranty | durability | accuracy | competitor | channel | subscription | other",
      "response_strategy_seed": "",
      "implicit_resolution": "proof_asset | third_party_review | comparison_education | onboarding_cue | warranty_or_return_reassurance | privacy_or_safety_reassurance | retailer_demo | offer_design | pr_guidance | other",
      "proof_needed": [],
      "do_not_say": [],
      "objection_severity_score": 0,
      "confidence": "high | medium | low",
      "evidence_refs": []
    }
  ]
}
```

### Price Message Seed

Price message seeds tell downstream modules what value narrative or offer framing should be tested.

```json
{
  "price_message_seed": [
    {
      "scenario_refs": [],
      "segment_refs": [],
      "price_message_angle": "",
      "price_posture": "premium_justification | parity_required | promo_dependency | affordability_pressure | value_uncertainty",
      "value_proof_needed": [],
      "recommended_execution_owner": "S04 | S05 | S06 | S07 | S13",
      "validation_method": "survey | landing_page_ab | retail_script_test | creator_brief_test | search_ad_test | channel_interview | other",
      "success_signal": "",
      "confidence": "high | medium | low",
      "evidence_refs": []
    }
  ]
}
```

## Recommended Next Skills

```json
[
  {
    "skill_id": "S04",
    "reason": "Pricing needs price message seeds, proof requirements, and objection handling before final price guidance.",
    "priority": "required | recommended | optional",
    "blocking_data_gaps": []
  }
]
```
