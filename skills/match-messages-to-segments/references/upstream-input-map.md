# S03 Upstream Input Map

Use this before S03 starts analysis. S03 normally receives S02 compressed handoff fields plus project brief and selected S01 evidence carried forward.

## Required Input Groups

```json
{
  "required_input_groups": [
    "scenario_signals",
    "segment_signals",
    "proof_signals",
    "objection_and_risk_signals",
    "local_language_signals",
    "price_message_signals",
    "product_fit_signals",
    "brand_claim_constraint_signals"
  ]
}
```

## Field Map

### Scenario Signals

From S02:

```text
jtbd_scenario_pack
scenario_priority_scorecard
scenario_message_seed
```

Use for lead message roles, segment relevance, and prioritization.

Missing behavior:

- If `jtbd_scenario_pack` is missing, S03 fails and should request S02 rerun.
- If priority is missing, produce message architecture but cap confidence at medium.

### Segment Signals

From S02/S01:

```text
scenario_to_segment_matrix
segment_seed_pack
segment_priority_ranking
```

Use for segment-specific message architecture.

Missing behavior:

- If segment mapping is missing, build scenario-level architecture only and mark `segment_gap`.

### Proof Signals

From S02/S01:

```text
proof_requirement_seed
product_job_fit_matrix
feature_to_local_language_map
content_proof_map
value_proof_requirement_matrix
approved_claims_or_proof_assets
```

Use for feature-benefit-proof matrix and proof readiness.

Missing behavior:

- If proof requirements are missing, do not create lead claims; return proof data gaps.

### Objection And Risk Signals

From S02:

```text
anti_jtbd_risk_list
objection_matrix_seed
brand_claim_constraint_map
non_consumption_risk_map
```

Use for objection handling and claims to avoid.

Missing behavior:

- If objections are missing, use anti-JTBD risks as fallback and mark confidence cap.

### Local Language Signals

From S02/S01:

```text
local_language_trigger_phrase_map
feature_to_local_language_map
localization_preflight
```

Use for local-language message seeds and terms to preserve.

Missing behavior:

- If local language is missing, produce working-language seeds and add localization gap. Do not final-translate.

### Price Message Signals

From S02/S01:

```text
scenario_price_implication_seed
segment_price_sensitivity_seeds
price_anchor_panel
value_proof_requirement_matrix
```

Use for price message seed.

Missing behavior:

- If price signals are missing, do not imply price credibility; hand off gap to S04.

### Product Fit Signals

From S02/S01:

```text
product_job_fit_matrix
product_capability_map
hardware_experience_diagnosis_seed
```

Use for whether a message angle is credible.

Missing behavior:

- If product fit is weak, mark message angle as support/test only, not lead.

### Brand And Claim Constraint Signals

From project brief/S02/private inputs:

```text
brand_claim_constraint_map
brand_positioning_self_perception_and_tone
claim_constraints
compliance_constraints
forbidden_claims_or_words
```

Use for claim risk gate and compliance review queue.

Missing behavior:

- If sensitive claims appear and constraints are missing, create `compliance_review_queue` and cap confidence.

## Message Input Coverage Gate

Before message architecture, produce:

```json
{
  "message_input_coverage_gate": {
    "status": "pass | pass_with_gaps | fail",
    "input_groups": [
      {
        "group": "",
        "required_for": [],
        "available_fields": [],
        "missing_fields": [],
        "impact_if_missing": "",
        "confidence_cap": "high | medium | low | assumption_only",
        "action": "proceed | proceed_with_cap | ask_s02_rerun | retrieve_from_rag | stop_and_report_gap"
      }
    ],
    "blocking_gaps": [],
    "non_blocking_gaps": [],
    "rag_or_full_artifact_escalations": []
  }
}
```

Gate logic:

```text
pass
  Scenario, proof, objection/risk, local language, product fit, and brand/claim constraint groups are usable.

pass_with_gaps
  Scenario exists but one or more proof, segment, price, local language, or claim groups are thin.

fail
  No JTBD scenario pack, no proof requirements, or no evidence refs for lead message claims.
```
