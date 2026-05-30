# S04 HTML Section Contract

S04 contributes the pricing section of the final GTM dashboard.

## Default Section IDs

```text
pricing_overview
price_input_coverage
opening_price_strategy
launch_price_architecture
local_price_credibility
rapid_price_prior
segment_wtp_hypotheses
price_sensitivity_model
price_value_proof_matrix
price_risk_guardrails
wtp_test_plan
promo_subscription_guidance
private_profit_revenue_optimizer
price_path_30_60_90
pricing_decision_gate
pricing_handoff_summary
```

Conditional section IDs:

```text
van_westendorp_test_design
gabor_granger_test_design
conjoint_dce_test_plan
channel_margin_guardrail
retail_price_integrity_map
subscription_pricing_hypothesis
promo_test_plan
elasticity_assumption_seed
pricing_decision_options
private_pricing_calculator
pricing_test_execution_kit
```

## HTML Section Draft

```json
{
  "section_id": "s04_pricing",
  "source_skill": "S04.model-price-sensitivity",
  "section_title": "开盘价格策略与利润边界",
  "executive_takeaway": "",
  "narrative_blocks": [],
  "metric_cards": [],
  "visual_blocks": [],
  "tables": [],
  "charts": [],
  "callouts": [],
  "confidence_badges": [],
  "citations": [],
  "data_gaps": [],
  "next_actions": []
}
```

## S14 Visual Block Contract

S04 must produce `visual_blocks` that S14 can render directly. Pricing visuals must separate market evidence, hypotheses, private commercial constraints, and test readiness. Read `html-visual-block-generation.md` for block-level transformation rules, scoring fallbacks, private-data handling, and thin-output checks.

```json
{
  "visual_blocks": [
    {
      "type": "status_panel | ranked_bar | matrix_heatmap | range_chart",
      "title": "",
      "subtitle": "",
      "data_source": "",
      "items": [],
      "rows": [],
      "columns": [],
      "scale_min": 0,
      "scale_max": 100,
      "note": "",
      "evidence_refs": [],
      "confidence": "high | medium | low | hypothesis_only"
    }
  ]
}
```

Default S04 main-body `visual_blocks`:

```yaml
required_visual_blocks:
  - title: Pricing Decision Gate
    type: status_panel
    data_source: pricing_decision_gate
    core_question: Can pricing move forward, or is it blocked by evidence, finance, channel, or test gaps?

  - title: Opening Price Strategy
    type: status_panel
    data_source: opening_price_strategy
    core_question: Should the product open high, open at parity, attack with price, preserve niche premium, or test before scale?

  - title: Launch Price Architecture
    type: range_chart
    data_source: launch_price_architecture + local_price_corridor + private_profit_revenue_optimizer_spec
    core_question: What are the public anchor, expected transaction range, promo floor, channel floor, revenue-max point, and profit-max point?

  - title: Local Price Credibility Corridor
    type: range_chart
    data_source: local_price_credibility_model + local_price_corridor + price_anchor_panel
    core_question: Where does the target price sit against local anchors, substitutes, and tier jumps?

  - title: Rapid WTP Prior And Evidence Caps
    type: ranked_bar
    data_source: rapid_price_prior
    core_question: If real research is unavailable, which quantified factors support or weaken the price hypothesis?

  - title: Segment WTP And Sensitivity
    type: matrix_heatmap
    data_source: segment_wtp_hypothesis + price_sensitivity_model
    core_question: Which segments can tolerate premium, need promotion, or require stronger proof?

  - title: Price Value Proof Readiness
    type: matrix_heatmap
    data_source: price_value_proof_matrix + claim_risk_and_proof_gate
    core_question: Can the value story sustain the price?

  - title: Price Risk Guardrails
    type: ranked_bar
    data_source: price_risk_guardrail
    core_question: Which risks most threaten launch price credibility or margin safety?

  - title: 30/60/90 Price Path
    type: matrix_heatmap
    data_source: price_path_30_60_90
    core_question: How should price, offer, and guardrails evolve through the first three launch phases?
```

Use `tables` for strategy score traces, WTP test plan, promo/subscription guidance, pricing test execution kit, channel/margin guardrails, price path details, and decision options. These are action instructions and should preserve owners, assumptions, quality checks, and next-step conditions.

## Thin Output Gate

Mark the S04 HTML section as `rendered_too_thin` in `data_gaps` if it lacks any of:

```text
executive_takeaway
pricing decision gate
opening price strategy with score trace
launch price architecture separating public anchor, transaction price, promo floor, and channel floor
local price credibility signal or corridor
rapid WTP prior with factor weights when real WTP or sales evidence is missing
segment WTP/sensitivity view
price-value proof or price risk guardrails
WTP/pricing test plan when confidence is not high
private calculator note or explicit private-data exclusion when private constraints are relevant
profit/revenue optimizer spec or explicit private-data gap when revenue-max/profit-max price is requested
30/60/90 price path with guardrails and triggers
next_actions for S07/S08/S13/S14
```

## Default Visuals

```yaml
visuals:
  - name: Opening Price Strategy
    type: status_panel
    data_source: opening_price_strategy

  - name: Launch Price Architecture
    type: range_chart
    data_source: launch_price_architecture

  - name: Local Price Credibility
    type: scorecard
    data_source: local_price_credibility_model

  - name: Rapid WTP Prior
    type: ranked_bar
    data_source: rapid_price_prior

  - name: Segment WTP Hypotheses
    type: scorecard_table
    data_source: segment_wtp_hypothesis

  - name: Price Sensitivity Model
    type: matrix_heatmap
    data_source: price_sensitivity_model

  - name: Price-Value Proof Matrix
    type: matrix
    data_source: price_value_proof_matrix

  - name: Price Risk Guardrails
    type: risk_table
    data_source: price_risk_guardrail

  - name: WTP Test Plan
    type: action_table
    data_source: wtp_test_plan

  - name: Promo And Subscription Guidance
    type: action_table
    data_source: promo_subscription_guidance

  - name: Pricing Decision Gate
    type: status_panel
    data_source: pricing_decision_gate

  - name: Private Pricing Calculator
    type: client_side_calculator
    data_source: private_pricing_calculator_spec

  - name: Private Profit Revenue Optimizer
    type: client_side_calculator
    data_source: private_profit_revenue_optimizer_spec

  - name: 30/60/90 Price Path
    type: action_table
    data_source: price_path_30_60_90

  - name: Pricing Test Execution Kit
    type: action_table
    data_source: pricing_test_execution_kit
```

## Rendering Rules

- Mark price outputs as hypotheses unless direct WTP/sales evidence and private constraints support them.
- Render opening price strategy before detailed WTP views. Show recommended posture, strategic objective, public anchor, transaction mechanism, why it fits, do-not-do rules, and confidence cap.
- Keep public anchor price, expected transaction price, promo floor, channel floor, revenue-max price, and profit-max price visually separate.
- Render revenue-max and profit-max values only when they come from private local calculator output, explicit private upload, or user-approved derived summary. Otherwise show the local optimizer as blank-input readiness.
- Show target price, price corridor, and anchor interpretation with confidence.
- If using `rapid_price_prior`, show factor weights, factor scores, evidence grade, confidence cap, prior range basis, and S13 calibration actions. Do not render it as measured WTP.
- Show proof requirements next to any premium or parity price posture.
- Do not render private COGS, margin, channel terms, or internal sales details unless approved.
- Render conditional research designs only when triggered.
- Do not hide pricing blockers; price data gaps are executive-relevant.
- If rendering `private_pricing_calculator`, use blank fields and local browser calculations only; do not prefill or expose raw COGS, margin, channel, promo, or internal sales values.
- The private calculator must not use external scripts, remote assets, analytics, telemetry, network requests, cookies, or unencrypted local storage.
- If encrypted local snapshot export is offered, use browser Web Crypto and make clear that encrypted data is for local storage/transport, not AI reasoning.

## Private Calculator Component

```json
{
  "component_id": "private_pricing_calculator",
  "title": "Private Price And Margin Calculator",
  "privacy_notice": "Values entered here are calculated locally in the browser and are not part of the AI-generated report unless you choose to share a derived summary.",
  "input_fields": [],
  "computed_outputs": [
    "estimated_net_selling_price",
    "gross_margin",
    "minimum_net_selling_price",
    "margin_gap",
    "promo_margin_after_discount",
    "estimated_units",
    "revenue",
    "unit_contribution",
    "contribution_profit",
    "revenue_max_price",
    "profit_max_price"
  ],
  "controls": [
    "reset_local_values",
    "export_encrypted_snapshot_optional",
    "import_encrypted_snapshot_optional",
    "copy_derived_summary_optional"
  ],
  "forbidden_behaviors": [
    "external_network_requests",
    "remote_scripts_or_fonts",
    "analytics_or_telemetry",
    "prefilled_private_values",
    "plain_local_storage"
  ]
}
```

## Private Profit Revenue Optimizer Component

```json
{
  "component_id": "private_profit_revenue_optimizer",
  "title": "Private Profit And Revenue Optimizer",
  "privacy_notice": "Demand, elasticity, COGS, channel, and MKT values are calculated locally in the browser and are not part of the AI-generated report unless you choose to share a derived summary.",
  "input_fields": [],
  "computed_outputs": [
    "revenue_curve",
    "profit_curve",
    "revenue_max_price",
    "profit_max_price",
    "floor_price_warnings"
  ],
  "controls": [
    "reset_local_values",
    "export_encrypted_snapshot_optional",
    "import_encrypted_snapshot_optional",
    "copy_derived_summary_optional"
  ],
  "forbidden_behaviors": [
    "external_network_requests",
    "remote_scripts_or_fonts",
    "analytics_or_telemetry",
    "prefilled_private_values",
    "plain_local_storage"
  ]
}
```
