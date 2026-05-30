# S04 Upstream Input Map

Use this before S04 starts analysis. S04 receives price evidence from S01, scenario price implications from S02, and price message/proof context from S03.

## Input Timing

S04 should separate minimal public inputs, upstream evidence, and private commercial constraints.

```text
S00 project setup
  Required from user: product/category, key specs/features, launch country or region, and target price range if known.
  Optional from user: product spec sheets, previous-generation performance, brand positioning, internal benchmarks, channel plans, creative/material archives, and known competitor lists.

S01-S03 upstream work
  Collect public local market anchors, competitor/substitute prices, segment signals, JTBD scenarios, proof gaps, objections, and price-message seeds.
  Preserve source refs and confidence caps so S04 can distinguish evidence from inference.

S04 pricing start
  Request private pricing constraints if available: target MSRP, COGS/BOM, target gross margin or floor price, channel margin terms, marketplace fees, tax/VAT handling, promo policy, previous-generation price/sales/promo data, inventory constraints, and subscription/financing terms.

S04 pricing output
  If private constraints are missing, produce price hypotheses, risk guardrails, and WTP test designs only.
  If private constraints are present, add margin/channel guardrails and pricing decision options, still separating approved internal facts from market hypotheses.
```

## Required Input Groups

```json
{
  "required_input_groups": [
    "local_price_evidence",
    "competitor_anchor_evidence",
    "segment_price_sensitivity",
    "scenario_price_implications",
    "price_message_and_proof",
    "promo_subscription_channel_signals",
    "internal_pricing_constraints",
    "evidence_quality_signals"
  ]
}
```

## Field Map

### Local Price Evidence

From S01:

```text
local_price_corridor
price_anchor_panel
price_ladder_scan
jump_decision_risks
```

Use for local price credibility and price tier classification.

Missing behavior:

- If local price corridor and anchor panel are both missing, S04 cannot model local price credibility.
- If only target price exists, label outputs `hypothesis_only`.

### Competitor Anchor Evidence

From S01:

```text
competitor_price_gap_table
competitor_threat_scores
substitute_taxonomy
price_anchor_panel
```

Use for price gap, trade-up/trade-down, lateral switching, and substitute pressure.

Missing behavior:

- If competitor anchors are missing, do not claim price parity or premium justification.

### Segment Price Sensitivity

From S01/S02:

```text
segment_price_sensitivity_seeds
segment_priority_ranking
segment_level_tam_sam_som
scenario_commercial_weight_map
price_complaints
```

Use for WTP hypotheses and segment-specific sensitivity.

Missing behavior:

- If segment sensitivity is missing, produce market-level model only and cap confidence at medium.

### Scenario Price Implications

From S02:

```text
scenario_price_implication_seed
jtbd_scenario_pack
scenario_priority_scorecard
digital_shelf_and_retailer_decision_map
```

Use for scenario-level price risk and test design.

Missing behavior:

- If scenario implications are missing, S04 may still use S01 price seeds but should not produce scenario-level guidance.

### Price Message And Proof

From S03/S01:

```text
price_message_seed
segment_message_architecture
feature_benefit_proof_matrix
objection_matrix
claim_risk_and_proof_gate
value_proof_requirement_matrix
content_proof_map
```

Use for value proof, price message credibility, and premium justification.

Missing behavior:

- If proof and price messages are missing, do not recommend premium pricing; return proof gaps.

### Promo Subscription Channel Signals

From S01/S02/S03/private inputs:

```text
promotion_subscription_sensitivity_seed
digital_shelf_and_retailer_decision_map
channel_fit_scores
retailer_marketplace_candidates
promo_discount_policy
subscription_or_recurring_revenue_model
finance_installment_constraints
```

Use for promo/subscription guidance and retail price integrity.

Missing behavior:

- If recurring cost exists but subscription tolerance is missing, create data gap and test plan.

### Internal Pricing Constraints

From private inputs:

```text
target_margin_or_floor_price
cogs_or_bom
channel_margin_terms
retailer_or_marketplace_fee_rules
promo_discount_policy
inventory_or_forecast_constraints
previous_generation_sales_price_channel_performance
```

Use for decision options and margin/channel guardrails.

COGS/BOM interpretation:

```text
cogs_or_bom
  COGS means cost of goods sold: the per-unit direct cost required to make or acquire the product that is sold.
  For hardware, this usually starts with BOM/component cost plus assembly/manufacturing, packaging, quality-related direct cost, and inbound logistics/duties when that is the company's accounting policy.
  It normally excludes marketing, sales commissions, R&D, headquarters overhead, and general operating expenses unless the user's finance policy says otherwise.
```

Missing behavior:

- If these are missing, do not produce final approved price. Produce price hypotheses and tests.

### Evidence Quality Signals

From S01/S02/S03:

```text
coverage_summary
source_quality_summary
confidence_caps
rag_index_manifest_ref
message_input_coverage_gate
```

Use for confidence caps and escalation.

Missing behavior:

- If evidence quality is missing, cap S04 confidence at medium.

## Price Input Coverage Gate

Before price modeling, produce:

```json
{
  "price_input_coverage_gate": {
    "status": "pass | pass_with_gaps | fail",
    "input_groups": [
      {
        "group": "",
        "required_for": [],
        "available_fields": [],
        "missing_fields": [],
        "impact_if_missing": "",
        "confidence_cap": "high | medium | low | hypothesis_only",
        "action": "proceed | proceed_with_cap | retrieve_from_rag | ask_s01_s02_s03_rerun | request_private_constraints | stop_and_report_gap"
      }
    ],
    "blocking_gaps": [],
    "non_blocking_gaps": [],
    "private_constraints_missing": [],
    "rag_or_full_artifact_escalations": []
  }
}
```

Gate logic:

```text
pass
  Local price evidence, competitor anchors, segment sensitivity, scenario price implications, price message/proof, and evidence quality are usable.

pass_with_gaps
  Price evidence exists but one or more segment, proof, promo/channel, internal constraint, or evidence-quality groups are thin.

fail
  No local price corridor, no price anchor panel, and no target price hypothesis are available.
```
