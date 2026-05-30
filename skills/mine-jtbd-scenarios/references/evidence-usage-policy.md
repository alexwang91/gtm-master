# S02 Evidence Usage Policy

Use this policy whenever S02 reads upstream evidence, retrieves from RAG, or writes derived JTBD artifacts.

## Core Rule

S02 should use S01 compressed handoff first. It should not recollect the market unless a required field is missing, a scenario materially affects strategy, or S00 has authorized a deeper evidence pass.

Default evidence order:

```text
direct upstream handoff
-> allowed evidence refs from S01
-> targeted RAG retrieval using evidence IDs
-> S01 full artifact escalation with reason
-> optional extra web/MCP collection only when approved or required by deep mode
```

Before using any evidence, run the input group checks in `upstream-input-map.md`. Segment, price, proof, and channel fields are not standalone user inputs by default; they are derived S01 handoff fields inside `market_context_pack.canonical_fields`.

## Retrieval Rules

- Retrieve only the evidence needed for the active scenario or proof question.
- Filter by country, language, product/category, allowed use, and source quality.
- Keep private and public evidence separated.
- Do not paste raw comment dumps into S02 artifacts.
- Do not use low-confidence evidence as primary proof unless the output is labeled as a hypothesis.

## Recommended Local Outputs

When a local run folder is available, use:

```text
runs/
  <project_id>/
    evidence/
      # core
      upstream_input_coverage_gate.json
      jtbd_scenario_pack.jsonl
      scenario_to_segment_matrix.jsonl
      product_job_fit_matrix.jsonl
      scenario_priority_scorecard.jsonl
      proof_requirement_seed.jsonl
      anti_jtbd_risk_list.jsonl
      local_language_trigger_phrase_map.jsonl
      scenario_message_seed.jsonl
      scenario_price_implication_seed.jsonl
      # conditional
      scenario_to_journey_matrix.jsonl
      consumer_electronics_gtm_moment_map.jsonl
      digital_shelf_and_retailer_decision_map.jsonl
      behavioral_science_lever_map.jsonl
      scenario_commercial_weight_map.jsonl
      brand_claim_constraint_map.jsonl
      non_consumption_risk_map.jsonl
      validation_question_seed.jsonl
      # audit / deep
      upstream_input_map.json
      jtbd_source_map.jsonl
      jtbd_candidate_pool.jsonl
      jtbd_scenario_clusters.jsonl
      scenario_distinctness_results.jsonl
    artifacts/
      s02_full_artifact.md
      s02_handoff_pack.json
      s02_html_section.json
```

If the runtime cannot write files, produce the same objects in the response or artifact bundle.

## Evidence Record

```json
{
  "derived_record_id": "",
  "record_type": "jtbd_source | jtbd_candidate | scenario | proof_requirement | anti_jtbd_risk | validation_question",
  "source_evidence_refs": [],
  "source_skill": "S01.build-consumer-market-map",
  "allowed_use": "public_context | internal_analysis_only | restricted",
  "claim_supported": "",
  "confidence": "high | medium | low",
  "limitations": []
}
```

## Context Escalation Triggers

Escalate beyond the compressed handoff when:

- A top scenario lacks source refs.
- Two scenarios are hard to merge/split and the decision changes downstream messaging.
- A proof requirement depends on local-language nuance not present in the handoff.
- A competitor complaint creates a major opportunity but product fit is uncertain.
- A weak user hypothesis is commercially important and needs targeted evidence.

Record the escalation reason in `decision_updates` or `data_gaps`.
