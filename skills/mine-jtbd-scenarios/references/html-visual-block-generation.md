# S02 HTML Visual Block Generation

Use this when producing `html_section_draft.visual_blocks` for S14.

## Core Rule

`visual_blocks` are view models derived from S02 analysis outputs. They must not introduce new JTBD scenarios, new scores, new segments, new claims, or new willingness-to-pay conclusions.

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
  "note": "",
  "evidence_refs": [],
  "confidence": "high | medium | low | hypothesis_only"
}
```

## Shared Scoring Rules

Use existing S02 scores from `scoring-rubrics.md`.

```text
80-100 -> high
60-79  -> medium
40-59  -> low
0-39   -> hypothesis_only or data_gap, depending on source quality
```

Scenario priority labels:

```text
75-100 = lead launch scenario
55-74  = useful secondary scenario
35-54  = test or segment-specific scenario
0-34   = do not lead with this scenario
```

Product-job fit labels:

```text
75-100 = strong product-job fit
55-74  = usable fit with proof or education
35-54  = weak fit; validate before prioritizing
0-34   = do not lead with this job
```

Confidence caps:

```text
consumer_voice_signals missing
  Cap JTBD scenario confidence at low or hypothesis_only.

segment_signals missing
  Cap scenario-to-segment visuals at low and mark `segment_gap`.

proof_signals missing
  Cap product-job fit and proof readiness visuals at low; mark proof status as missing.

price_signals missing
  Cap scenario price implication outputs at hypothesis_only.

local_language_signals missing
  Keep scenarios, but cap local trigger phrase confidence at low.

mostly user-provided strategic scenario
  Preserve as hypothesis_only unless S01 evidence supports it.
```

If a sub-score is unavailable:

```text
Do not invent it from prose.
Use the closest approved score only if the source field explicitly maps to the same concept.
Otherwise render a table and add `missing_visual_block_score` to data_gaps.
```

## Block 1: Upstream Input Coverage Gate

Purpose: show whether S02 has enough S01 evidence to produce credible scenarios.

```json
{
  "type": "status_panel",
  "title": "Upstream Input Coverage Gate",
  "subtitle": "Shows which S01 signal groups cap JTBD confidence",
  "data_source": "upstream_input_coverage_gate + confidence_caps"
}
```

Inputs:

```text
upstream_input_coverage_gate
confidence_caps
data_gaps
```

Build 4-8 items from required input groups:

```text
consumer_voice_signals
segment_signals
proof_signals
price_signals
channel_signals
competitor_and_substitute_signals
local_language_signals
evidence_quality_signals
```

Item mapping:

```json
{
  "label": "Consumer voice",
  "value": "available | partial | missing | capped",
  "note": "voice atoms + theme clusters available; cap: none",
  "evidence_refs": [],
  "confidence": "medium"
}
```

Render this block in standard mode when any group is partial, missing, or confidence-capped. In deep mode, always render it.

## Block 2: Scenario Priority Scorecard

Purpose: show which jobs deserve GTM attention first.

```json
{
  "type": "ranked_bar",
  "title": "Scenario Priority Scorecard",
  "subtitle": "Ranks scenarios by priority, evidence strength, fit, and GTM relevance",
  "data_source": "scenario_priority_scorecard + jtbd_scenario_pack"
}
```

Rows:

```text
Use top 3-5 scenarios in main body.
Sort by scenario_priority_score descending.
Keep all low-priority or duplicate scenario candidates in full artifact or deep appendix.
```

Score:

```text
Use scenario_priority_score from scenario_priority_scorecard.
If absent but `jtbd_scenario_pack.scenario_priority_score` exists, use that.
If both are absent, render a scenario table and add `missing_scenario_priority_score`.
```

Item mapping:

```json
{
  "label": "[Scenario name]",
  "score": 86,
  "score_label": "Lead launch scenario",
  "note": "Evidence: strong; product-job fit: strong; proof: partial",
  "evidence_refs": []
}
```

Do not rank scenarios based on how persuasive the writing sounds.

## Block 3: Scenario To Segment Matrix

Purpose: show which priority segments map to which jobs.

```json
{
  "type": "matrix_heatmap",
  "title": "Scenario To Segment Matrix",
  "subtitle": "Shows whether each job is primary, secondary, hypothesis-only, or excluded for each segment",
  "data_source": "scenario_to_segment_matrix",
  "columns": ["[Priority segment 1]", "[Priority segment 2]", "[Priority segment 3]"]
}
```

Rows:

```text
Use the same top 3-5 scenarios as Scenario Priority Scorecard.
Use top 3-5 S01 segments by priority or S02 scenario relationship.
Do not create demographic segments inside this visual.
```

Relationship-to-score mapping:

```text
primary         -> 90
secondary       -> 65
hypothesis_only -> 40
excluded        -> 0
missing         -> data gap, not 0
```

Cell labels:

```text
primary
secondary
hypothesis
excluded
gap
```

If S02 lacks segment signals, render a grouped table and add `segment_gap` plus `missing_scenario_to_segment_matrix`.

## Block 4: Product Job Fit And Proof Readiness

Purpose: show whether the product can credibly satisfy each job and what proof is missing.

```json
{
  "type": "matrix_heatmap",
  "title": "Product Job Fit And Proof Readiness",
  "subtitle": "Checks capability fit, proof availability, price-value support, and risk before messaging",
  "data_source": "product_job_fit_matrix + proof_requirement_seed",
  "columns": ["Product-job fit", "Proof readiness", "Price-value support", "Setup/service risk"]
}
```

Rows:

```text
Use top 3-5 scenarios.
Use product_job_fit_matrix for fit.
Use proof_requirement_seed for proof readiness and urgency.
Use price implication seed or value proof signals for price-value support.
Use anti-JTBD risks or GTM moment dependencies for setup/service risk.
```

Cell mappings:

```text
Product-job fit
  product_job_fit_score.

Proof readiness
  available -> 90
  partial   -> 60
  missing   -> 25
  risky     -> 10
  If multiple proof requirements exist, use the lowest status for launch-critical proof and show urgency in note.

Price-value support
  Use WTP/price credibility component when available.
  If absent, use scenario_price_implication_seed confidence as a label only and add `missing_price_value_score`.

Setup/service risk
  Use inverse of relevant anti_jtbd_risk_score when risk type is setup_friction, support_return, expectation_gap, privacy, compatibility, or service.
  If no risk evidence exists, leave as gap rather than assuming low risk.
```

If product-job fit is below 55, the scenario can remain visible only as validation hypothesis unless the user explicitly keeps it for strategic reasons.

## Block 5: Proof Requirement Urgency Ranking

Purpose: make proof blockers visible before S03 writes message architecture.

```json
{
  "type": "ranked_bar",
  "title": "Proof Requirement Urgency Ranking",
  "subtitle": "Ranks what must be proven before launch messaging or pricing can rely on a scenario",
  "data_source": "proof_requirement_seed"
}
```

Rows:

```text
Sort proof requirements by proof_requirement_urgency_score descending.
Show top 5-8 proof needs in standard mode.
Group by scenario when multiple proof needs share the same owner.
```

Item mapping:

```json
{
  "label": "[Proof question or claim]",
  "score": 78,
  "score_label": "Must prove before launch",
  "note": "Scenario: X; status: partial; owner: product/marketing",
  "evidence_refs": []
}
```

If urgency scores are missing, render an action table and add `missing_proof_urgency_score`.

## Block 6: Anti-JTBD And Non-Consumption Risk Ranking

Purpose: show why consumers might not buy, not switch, not repeat, or not recommend.

```json
{
  "type": "ranked_bar",
  "title": "Anti-JTBD And Non-Consumption Risk Ranking",
  "subtitle": "Ranks barriers that could invalidate or weaken lead scenarios",
  "data_source": "anti_jtbd_risk_list + non_consumption_risk_map"
}
```

Rows:

```text
Sort anti_jtbd_risk_list by anti_jtbd_risk_score descending.
Show major and important blockers in the main body.
Include non-consumption reasons when doing nothing or delaying purchase is a material risk.
```

Item mapping:

```json
{
  "label": "[Risk name]",
  "score": 74,
  "score_label": "Important blocker",
  "note": "Mechanism: substitute suffices; affected segments: value optimizer",
  "evidence_refs": []
}
```

Never hide anti-JTBD risks because they weaken the product story.

## Optional Main-Body Blocks

Add these only when their trigger is present and the view changes downstream work:

```text
Scenario Commercial Weight
  type: ranked_bar
  source: scenario_commercial_weight_map
  trigger: launch sequencing, market sizing, inventory, or channel priority depends on scenario differences.

Consumer Electronics GTM Moment Matrix
  type: matrix_heatmap
  source: consumer_electronics_gtm_moment_map
  trigger: journey stage changes message, proof, channel, activation, or support decisions.

Digital Shelf And Retailer Decision Readiness
  type: status_panel
  source: digital_shelf_and_retailer_decision_map
  trigger: DTC, marketplace, retail, delivery, returns, warranty, or channel conversion matters.

Behavioral Lever Fit
  type: ranked_bar
  source: behavioral_science_lever_map
  trigger: downstream message, creative, funnel, proof, offer, or risk-reversal testing is planned.
```

## Companion Tables Required In Standard Mode

Visual blocks are not enough. S02 should also include compact tables for:

```text
jtbd_scenario_cards
local_language_trigger_phrase_map
scenario_message_seed
scenario_price_implication_seed
validation_question_seed when triggered
brand_claim_constraint_map when triggered
```

## Thin Output Gate

Mark the S02 HTML section as `rendered_too_thin` if it lacks any of:

```text
executive_takeaway
lead 3-5 JTBD scenarios with evidence refs
scenario priority visual block
scenario-to-segment visual block or explicit segment_gap
product-job fit/proof readiness visual block
anti-JTBD risk table or visual block
next_actions for S03/S04/S13
```

## Final Assembly Checklist

Before returning `html_section_draft`:

```text
1. Order visual_blocks by decision flow:
   input gate -> scenario priority -> scenario-to-segment -> product-job fit/proof -> proof urgency -> anti-JTBD risk.

2. Every ranked item and matrix cell traces to S02 output fields or approved S01 handoff fields.

3. Weak but commercially important scenarios remain visible as hypotheses with validation questions.

4. Scenario cards preserve job statement, current alternative, proof need, and barrier.

5. Local trigger phrases remain exact seeds with language/context; do not final-translate or transcreate them.

6. Missing scores become tables + data gaps, not fabricated chart values.

7. Add `rendered_too_thin` if fewer than 4 required visual_blocks can be produced in standard mode.
```
