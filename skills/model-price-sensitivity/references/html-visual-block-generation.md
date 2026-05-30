# S04 HTML Visual Block Generation

Use this when producing `html_section_draft.visual_blocks` for S14.

## Core Rule

`visual_blocks` are view models derived from S04 pricing outputs. They must not approve a final company price, invent willingness-to-pay evidence, expose private commercial inputs, or turn hypotheses into recommendations.

Each block must include:

```json
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
```

## Shared Scoring Rules

Use existing S04 scores from `scoring-rubrics.md`.

```text
80-100 -> high
60-79  -> medium
40-59  -> low
0-39   -> hypothesis_only or data_gap, depending on source quality
```

Price credibility labels:

```text
75-100 = credible price posture
55-74  = credible with proof or testing
35-54  = risky; test before decision
0-34   = not credible with current evidence
```

Price sensitivity labels:

```text
0-30   = low sensitivity
31-55  = medium sensitivity
56-75  = high sensitivity
76-100 = very high sensitivity
```

Pricing readiness labels:

```text
75-100 = ready for pricing decision review
55-74  = ready for controlled test
35-54  = research first
0-34   = blocked by data gaps
```

Rapid WTP prior labels:

```text
75-100 = price supported with caveats
55-74  = test before scale
35-54  = research first
0-34   = price not supported with current evidence
```

Opening strategy labels:

```text
75-100 = strong fit
60-74  = possible; test challenger strategy
40-59  = weak fit; use only with explicit objective
0-39   = avoid or block
```

Hard blocker rule:

```text
Never let a visual imply readiness above pricing_decision_gate.status.
Readiness scores do not override hard blockers.
```

Confidence caps:

```text
local_price_evidence missing
  Cap local price credibility and corridor visuals at hypothesis_only or blocked.

competitor_anchor_evidence missing
  Do not claim parity or premium justification.

segment_price_sensitivity missing
  Produce market-level model only; cap segment WTP visuals at medium or low.

price_message_and_proof missing
  Do not recommend premium pricing; mark proof gap.

internal_pricing_constraints missing
  Do not render final approved price or margin viability. Cap at finance_review, controlled_test_ready, or research_first.

private_optimizer_inputs_missing
  Do not render revenue-max or profit-max price values. Render optimizer readiness and blank local calculator instead.

synthetic_only_or_public_proxy_only
  Cap at research_first unless the section is only a test plan.

rapid_price_prior_without_factor_trace
  Do not render a score-only prior. Add `rapid_price_prior_missing_factor_trace`.
```

If a sub-score is unavailable:

```text
Do not invent it from prose.
Use the closest approved score only if the source field explicitly maps to the same concept.
Otherwise render a table and add `missing_visual_block_score` to data_gaps.
```

## Block 1: Pricing Decision Gate

Purpose: show what the pricing workflow is ready for next.

```json
{
  "type": "status_panel",
  "title": "Pricing Decision Gate",
  "subtitle": "Shows decision readiness, hard blockers, and next owner",
  "data_source": "pricing_decision_gate"
}
```

Inputs:

```text
pricing_decision_gate.status
pricing_decision_gate.status_reason
pricing_decision_gate.readiness_scores
pricing_decision_gate.hard_blockers
pricing_decision_gate.soft_risks
pricing_decision_gate.recommended_path
pricing_decision_gate.downstream_readiness
pricing_decision_gate.data_gaps
```

Build 4-7 items:

```text
Gate status
Recommended opening strategy
Public anchor / transaction mechanism
Price credibility
WTP confidence
Pricing readiness
Hard blockers
Next owner
Downstream readiness
```

Item mapping:

```json
{
  "label": "Gate status",
  "value": "research_first",
  "note": "WTP evidence is not strong enough for decision review",
  "evidence_refs": [],
  "confidence": "medium"
}
```

If no `pricing_decision_gate` exists, render a `blocked` status panel and add `missing_pricing_decision_gate`.

## Block 2: Opening Price Strategy

Purpose: show the launch pricing posture before detailed pricing evidence.

```json
{
  "type": "status_panel",
  "title": "Opening Price Strategy",
  "subtitle": "Public anchor, transaction mechanism, strategic objective, and confidence cap",
  "data_source": "opening_price_strategy"
}
```

Inputs:

```text
opening_price_strategy.recommended_strategy
opening_price_strategy.strategic_objective
opening_price_strategy.strategy_scores
opening_price_strategy.recommended_public_anchor
opening_price_strategy.recommended_transaction_mechanism
opening_price_strategy.conditions_required
opening_price_strategy.why_this_strategy
opening_price_strategy.do_not_do
opening_price_strategy.confidence
```

Build 5-8 items:

```text
Recommended strategy
Strategic objective
Public anchor
Transaction mechanism
Top supporting score
Required condition
Do-not-do rule
Confidence cap
```

If strategy scores are missing, render the recommendation as `test_before_scale` or add `opening_strategy_missing_score_trace`.

## Block 3: Launch Price Architecture

Purpose: separate visible price, real transaction price, floors, and optimizer outputs.

```json
{
  "type": "range_chart",
  "title": "Launch Price Architecture",
  "subtitle": "MSRP, transaction range, promo floor, channel floor, and optimizer points when available",
  "data_source": "launch_price_architecture + private_profit_revenue_optimizer_spec"
}
```

Items:

```text
Public anchor / MSRP
Expected transaction range
Promo floor
Channel floor
Revenue-max price when available
Profit-max price when available
```

If private optimizer values are missing, show `revenue_max_price` and `profit_max_price` as local-calculator pending, not blank approval. If range values are non-comparable or missing, render a table and add `launch_price_architecture_not_comparable`.

## Block 4: Local Price Credibility Corridor

Purpose: show where target price sits versus local anchors, substitutes, and tier jumps.

```json
{
  "type": "range_chart",
  "title": "Local Price Credibility Corridor",
  "subtitle": "Target price versus local anchors, substitutes, and premium bands",
  "data_source": "local_price_credibility_model + local_price_corridor + price_anchor_panel"
}
```

Numeric requirement:

```text
Only render `range_chart` when prices are normalized to one currency and comparable unit.
If anchors are mixed across bundles, subscription, financing, tax treatment, or channel formats, render a table and add `price_range_chart_not_comparable`.
```

Scale:

```text
scale_min = min(entry/substitute anchor, target_min, competitor_min) rounded down
scale_max = max(premium/flagship anchor, target_max, competitor_max) rounded up
```

Items:

```text
Entry/substitute band
Main competitor band
Target price range
Premium/flagship band
```

Item mapping:

```json
{
  "label": "Target price range",
  "min": 450,
  "max": 520,
  "marker": 499,
  "value_label": "450-520 | target 499",
  "note": "Classification: premium; credibility score: 62",
  "evidence_refs": []
}
```

Never show this as final price approval.

## Block 5: Rapid WTP Prior And Evidence Caps

Purpose: show the quantified prior when real WTP or sales evidence is missing.

```json
{
  "type": "ranked_bar",
  "title": "Rapid WTP Prior And Evidence Caps",
  "subtitle": "Factor-weighted price prior, not measured WTP",
  "data_source": "rapid_price_prior"
}
```

Inputs:

```text
rapid_price_prior.rapid_wtp_prior_score
rapid_price_prior.pricing_classification
rapid_price_prior.wtp_prior_range
rapid_price_prior.factor_scores
rapid_price_prior.evidence_grade
rapid_price_prior.confidence_cap
rapid_price_prior.calibration_plan
rapid_price_prior.data_gaps
```

Rows:

```text
Use factor_scores sorted by weighted_score or business impact.
Show all seven canonical factors when available.
If factor_scores are missing, render a data-gap callout and add `rapid_price_prior_missing_factor_trace`.
```

Item mapping:

```json
{
  "label": "Local price anchor fit",
  "score": 68,
  "score_label": "0.22 weight | strong_proxy",
  "note": "Anchor median supports parity, but target is above local p75; cap: medium",
  "evidence_refs": []
}
```

The block note must include score, classification, evidence grade, confidence cap, and prior range basis. Do not call the prior measured WTP.

## Block 6: Segment WTP And Sensitivity

Purpose: show which segments can tolerate premium, need promotion, or require stronger proof.

```json
{
  "type": "matrix_heatmap",
  "title": "Segment WTP And Sensitivity",
  "subtitle": "Separates WTP hypotheses from measured WTP evidence",
  "data_source": "segment_wtp_hypothesis + price_sensitivity_model",
  "columns": ["Premium tolerance", "Price sensitivity", "Promo sensitivity", "Proof dependence", "WTP confidence"]
}
```

Rows:

```text
Use priority segments from segment_wtp_hypothesis.
Show 3-6 rows in main body.
If only market-level sensitivity exists, render market-level status panel and add `missing_segment_wtp_hypothesis`.
```

Cell mappings:

```text
Premium tolerance
  high -> 85
  medium -> 60
  low -> 30
  unknown -> gap

Price sensitivity
  Use price_sensitivity_score if segment-level score exists.
  If only labels exist:
    low -> 20
    medium -> 45
    high -> 70
    very_high -> 90

Promo sensitivity
  Use promo_dependency or promotion dependence when available.

Proof dependence
  Use value_proof_needed count/severity or price_value_proof_matrix proof status.

WTP confidence
  Use WTP Confidence score or confidence label. Direct sales/survey evidence should be visible in notes.
```

Do not use AI personas or synthetic respondents as WTP evidence.

## Block 7: Price Value Proof Readiness

Purpose: show whether the value story can support the target price or premium posture.

```json
{
  "type": "matrix_heatmap",
  "title": "Price Value Proof Readiness",
  "subtitle": "Shows proof status, claim risk, and message support for price posture",
  "data_source": "price_value_proof_matrix + price_message_seed + claim_risk_and_proof_gate",
  "columns": ["Price position", "Proof readiness", "Claim safety", "Message support"]
}
```

Rows:

```text
Use segment/scenario combinations that affect price posture.
Prioritize premium, slight premium, high objection, or high sensitivity rows.
Show 5-8 rows in standard mode.
```

Cell mappings:

```text
Price position
  below_anchor -> 85
  parity -> 75
  slight_premium -> 60
  major_premium -> 35 unless proof readiness is high
  unclear -> gap

Proof readiness
  available -> 90
  partial -> 60
  missing -> 25
  risky -> 10

Claim safety
  low claim risk -> 85
  medium claim risk -> 55
  high claim risk -> 20

Message support
  Use price_message_seed confidence and message-market fit support when available.
```

If proof status is missing, do not infer premium support; add `missing_price_value_proof_status`.

## Block 8: Price Risk Guardrails

Purpose: show the biggest pricing risks before forecast or launch planning.

```json
{
  "type": "ranked_bar",
  "title": "Price Risk Guardrails",
  "subtitle": "Ranks affordability, premium proof, channel, promo, margin, subscription, and support risks",
  "data_source": "price_risk_guardrail"
}
```

Rows:

```text
Sort by severity and available risk score.
Show all high severity risks and top medium risks in main body.
Always include private_data_gap, margin_gap, channel_conflict, and proof_gap_for_premium when present.
```

Score mapping when no numeric score exists:

```text
high severity -> 85
medium severity -> 60
low severity -> 35
```

Item mapping:

```json
{
  "label": "Premium proof gap",
  "score": 85,
  "score_label": "High risk",
  "note": "Affected: performance seeker; mitigation: expert review + comparison demo",
  "evidence_refs": []
}
```

Never hide risk guardrails because they weaken the pricing story.

## Block 9: WTP Test And Evidence Plan

Purpose: show the smallest real-world test needed to reduce pricing uncertainty.

```json
{
  "type": "status_panel",
  "title": "WTP Test And Evidence Plan",
  "subtitle": "Shows recommended test level, evidence limits, and next handoff",
  "data_source": "wtp_test_plan + pricing_test_execution_kit + pricing_test_result_interpretation"
}
```

Items:

```text
Recommended execution level
Best method
Candidate price points
Quality checks
Decision rule
Handoff to S13
```

Item mapping:

```json
{
  "label": "Recommended execution",
  "value": "survey_panel",
  "note": "Use Gabor-Granger for 3 candidate prices; screen target segment in launch country",
  "evidence_refs": [],
  "confidence": "medium"
}
```

If only hypothesis generation is possible, label `hypothesis_only` and do not imply measured WTP.

## Block 10: Private Pricing Calculator Readiness

Purpose: show how private COGS, margin, channel, and promo constraints are handled without exposing raw values.

```json
{
  "type": "status_panel",
  "title": "Private Pricing Calculator Readiness",
  "subtitle": "Blank local calculator only; raw private values stay out of public HTML by default",
  "data_source": "private_pricing_calculator_spec + price_input_coverage_gate"
}
```

Render when:

```text
private_pricing_calculator_spec exists
internal_pricing_constraints are missing but relevant
COGS, margin, channel terms, promo policy, retailer fees, or previous-generation sales are private
```

Items:

```text
Mode
Storage policy
Network policy
Private fields
Computed fields
Allowed downstream handoff
```

Item mapping:

```json
{
  "label": "Mode",
  "value": "client_side_blank_inputs",
  "note": "No raw COGS, margin, or channel values embedded in public report",
  "confidence": "high"
}
```

Do not render raw private values. If explicit private upload is used, mark the section as private and keep it out of public-facing dashboard unless approved.

## Block 11: Private Profit And Revenue Optimizer Readiness

Purpose: show whether revenue-max and profit-max price can be calculated locally.

```json
{
  "type": "status_panel",
  "title": "Private Profit And Revenue Optimizer Readiness",
  "subtitle": "Local-only model for revenue-max and profit-max price",
  "data_source": "private_profit_revenue_optimizer_spec + launch_price_architecture"
}
```

Items:

```text
Mode
Candidate price grid
Required private inputs
Computed outputs
Network/storage policy
Derived summary handoff
```

Never render revenue or profit curves from invented values. If the user has not entered local private inputs, render only formulas, empty fields, and pending output labels.

## Block 12: 30/60/90 Price Path

Purpose: show how price and offer mechanics should evolve after launch.

```json
{
  "type": "matrix_heatmap",
  "title": "30/60/90 Price Path",
  "subtitle": "Phase-specific offer mechanics, triggers, metrics, and guardrails",
  "data_source": "price_path_30_60_90",
  "columns": ["Price posture", "Offer mechanism", "Decision trigger", "Guardrail", "Allowed move"]
}
```

Rows:

```text
day_0_30
day_31_60
day_61_90
```

Use labels rather than fake scores when the values are procedural. If S14 needs a numeric cell, map high-risk guardrails to 80, medium to 55, low to 30, and note that the matrix is a planning view.

## Optional Main-Body Blocks

Add these only when triggered and decision-relevant:

```text
Pricing Decision Options
  type: ranked_bar or status_panel
  source: pricing_decision_options
  trigger: enough evidence and constraints exist to compare 2-5 options.

Channel Margin Guardrail
  type: status_panel
  source: channel_margin_guardrail
  trigger: COGS, margin, retailer, marketplace, distributor, promo, or MAP/MSRP constraints are provided or required.

Retail Price Integrity Map
  type: matrix_heatmap
  source: retail_price_integrity_map
  trigger: multiple retailers/marketplaces, promo conflict, cross-border pricing, or channel conflict matters.

Promo And Subscription Risk
  type: ranked_bar or status_panel
  source: promo_subscription_guidance + subscription_pricing_hypothesis + promo_test_plan
  trigger: discounting, bundles, financing, subscription, consumables, warranty extension, or recurring costs matter.
```

## Companion Tables Required In Standard Mode

Visual blocks are not enough. S04 should also include compact tables for:

```text
opening_price_strategy score trace and do-not-do rules
launch_price_architecture anchor, transaction, floor, and optimizer status
local_price_credibility_model assumptions and caveats
rapid_price_prior factor scores, evidence caps, and calibration plan when produced
segment_wtp_hypothesis
price_value_proof_matrix
price_risk_guardrail
wtp_test_plan
promo_subscription_guidance
private_profit_revenue_optimizer_spec
price_path_30_60_90
pricing_handoff_summary
pricing_decision_options when produced
```

## Thin Output Gate

Mark the S04 HTML section as `rendered_too_thin` if it lacks any of:

```text
executive_takeaway
pricing decision gate
opening price strategy
launch price architecture
local price credibility or explicit local anchor gap
rapid WTP prior or explicit real-WTP/sales evidence when pricing confidence is below high
segment WTP/sensitivity view or explicit segment gap
price-value proof or risk guardrail view
WTP/pricing test plan when confidence is not high
private-data exclusion or private calculator note when internal constraints are relevant
private profit/revenue optimizer readiness when revenue-max or profit-max price is requested
30/60/90 price path with guardrails
next_actions for S07/S08/S13/S14
```

## Final Assembly Checklist

Before returning `html_section_draft`:

```text
1. Order visual_blocks by decision flow:
   decision gate -> opening strategy -> launch price architecture -> price corridor -> rapid WTP prior when needed -> segment WTP/sensitivity -> price-value proof -> risk guardrails -> WTP test plan -> private calculator readiness -> profit/revenue optimizer readiness -> 30/60/90 price path.

2. Every price claim traces to S04 outputs and evidence refs.

3. Target price remains a hypothesis unless direct WTP/sales evidence and approved private constraints support review readiness.

4. Readiness visuals never exceed pricing_decision_gate.status.

5. Raw COGS, BOM, margin, channel terms, promo policy, retailer fees, internal sales, and private constraints are not embedded in public HTML unless explicitly approved.

5a. Revenue-max and profit-max price values are not rendered unless they come from private local calculator output, explicit private upload, or user-approved derived summary.

6. Missing scores become tables + data gaps, not fabricated chart values.

7. Add `rendered_too_thin` if fewer than 4 required visual_blocks can be produced in standard mode.
```
