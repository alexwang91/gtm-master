# S04 Evidence Usage Policy

S04 should use S01/S02/S03 compressed handoffs first. It should not recollect prices unless the price decision depends on missing or stale anchor evidence.

Default evidence order:

```text
S01/S02/S03 compressed handoffs
-> allowed evidence refs
-> targeted RAG retrieval by evidence IDs
-> S01/S02/S03 full artifact escalation with reason
-> additional web/MCP price collection only when authorized or required by deep mode
```

## Private Evidence Rules

Private pricing inputs are high value but sensitive:

- COGS/BOM
- margin floor
- channel margin terms
- marketplace fees
- retailer contracts
- inventory constraints
- historical sales by price/promo/channel

Store them separately and do not render raw values in public HTML unless approved.

## Recommended Local Outputs

```text
runs/
  <project_id>/
    evidence/
      # core
      price_input_coverage_gate.json
      local_price_credibility_model.json
      segment_wtp_hypothesis.jsonl
      price_sensitivity_model.json
      price_value_proof_matrix.jsonl
      price_risk_guardrail.jsonl
      wtp_test_plan.json
      promo_subscription_guidance.json
      pricing_handoff_summary.json
      # conditional
      van_westendorp_test_design.json
      gabor_granger_test_design.json
      conjoint_dce_test_plan.json
      channel_margin_guardrail.json
      retail_price_integrity_map.jsonl
      subscription_pricing_hypothesis.json
      promo_test_plan.json
      elasticity_assumption_seed.json
      pricing_decision_options.jsonl
      # audit / deep
      price_anchor_audit.jsonl
      competitor_price_gap_audit.jsonl
      price_assumption_log.jsonl
      sensitivity_calculation_trace.jsonl
      private_pricing_input_register.jsonl
    artifacts/
      s04_full_artifact.md
      s04_handoff_pack.json
      s04_html_section.json
```

## Rules

- Store public price evidence separately from private commercial constraints.
- Preserve currency, tax/VAT, shipping, financing, promo, warranty, and channel context.
- Record collection dates for prices because price evidence decays quickly.
- If price data is stale, mark confidence and recommend refresh before final pricing.
- Record every formula or assumption used in `price_assumption_log` or `sensitivity_calculation_trace`.
