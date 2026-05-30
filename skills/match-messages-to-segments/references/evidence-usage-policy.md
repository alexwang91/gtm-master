# S03 Evidence Usage Policy

S03 should use S02 compressed handoff first and avoid re-mining S01 unless message claims require proof detail missing from the handoff.

Default evidence order:

```text
S02 compressed handoff
-> allowed S02/S01 evidence refs
-> targeted RAG retrieval by evidence IDs
-> S02 or S01 full artifact escalation with reason
```

## Recommended Local Outputs

```text
runs/
  <project_id>/
    evidence/
      # core
      message_input_coverage_gate.json
      segment_message_architecture.jsonl
      feature_benefit_proof_matrix.jsonl
      objection_matrix.jsonl
      claim_risk_and_proof_gate.json
      local_language_message_seed.jsonl
      price_message_seed.jsonl
      message_market_fit_scorecard.jsonl
      # conditional
      competitive_contrast_matrix.jsonl
      behavioral_lever_message_seed.jsonl
      retail_sales_talk_track_seed.jsonl
      landing_page_message_block_seed.jsonl
      creator_brief_message_seed.jsonl
      compliance_review_queue.jsonl
      message_test_backlog.jsonl
      # audit / deep
      message_source_trace.jsonl
      message_variant_pool.jsonl
      rejected_message_angles.jsonl
      claim_evidence_audit.jsonl
    artifacts/
      s03_full_artifact.md
      s03_handoff_pack.json
      s03_html_section.json
```

## Rules

- Store message claims as seeds, not final public copy.
- Keep proof refs and claim risk with every claim.
- Keep private brand, sales, or legal notes separated from public report content unless approved.
- Do not store long customer quote dumps; use evidence IDs and short summaries.
- Record any RAG/full-artifact escalation in `decision_updates`.
