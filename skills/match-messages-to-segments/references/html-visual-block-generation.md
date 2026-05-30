# S03 HTML Visual Block Generation

Use this when producing `html_section_draft.visual_blocks` for S14.

## Core Rule

`visual_blocks` are view models derived from S03 analysis outputs. They must not create final copy, new message claims, new proof status, new objections, or new compliance conclusions.

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

Use existing S03 scores from `scoring-rubrics.md`.

```text
80-100 -> high
60-79  -> medium
40-59  -> low
0-39   -> hypothesis_only or data_gap, depending on source quality
```

Message-market fit labels:

```text
75-100 = lead message candidate
55-74  = support or test message
35-54  = weak message hypothesis
0-34   = do not use
```

Claim risk labels:

```text
75-100 = high risk; do not use without review
55-74  = medium risk; use cautious wording and proof
35-54  = manageable with proof notes
0-34   = low risk
```

Proof readiness status mapping:

```text
available -> 90
partial   -> 60
missing   -> 25
risky     -> 10
```

Confidence caps:

```text
jtbd_scenario_pack missing
  S03 should fail and request S02 rerun; do not render normal message visuals.

proof_requirement_seed missing
  Do not create lead claims; cap proof and claim visuals at low and add `proof_gap`.

objection_and_risk_signals missing
  Use anti-JTBD risks as fallback if available; cap objection visuals at low.

local_language_signals missing
  Produce working-language seeds only; add localization gap and do not final-translate.

brand_claim_constraint_signals missing and sensitive claims appear
  Add compliance review queue and cap claim gate at low.

product_job_fit weak
  Message angle may remain support/test only, not lead.
```

If a sub-score is unavailable:

```text
Do not invent it from prose.
Use the closest approved score only if the source field explicitly maps to the same concept.
Otherwise render a table and add `missing_visual_block_score` to data_gaps.
```

## Block 1: Message Input Coverage Gate

Purpose: show which upstream gaps cap message confidence.

```json
{
  "type": "status_panel",
  "title": "Message Input Coverage Gate",
  "subtitle": "Shows whether S02/S01 inputs are enough to build message architecture",
  "data_source": "message_input_coverage_gate + confidence_caps"
}
```

Inputs:

```text
message_input_coverage_gate
confidence_caps
data_gaps
```

Build 5-8 items from required input groups:

```text
scenario_signals
segment_signals
proof_signals
objection_and_risk_signals
local_language_signals
price_message_signals
product_fit_signals
brand_claim_constraint_signals
```

Item mapping:

```json
{
  "label": "Proof signals",
  "value": "available | partial | missing | capped",
  "note": "proof_requirement_seed present; approved proof assets missing",
  "evidence_refs": [],
  "confidence": "medium"
}
```

Render this block in standard mode when any group is partial, missing, or confidence-capped. In deep mode, always render it.

## Block 2: Segment Message Fit

Purpose: show which message angles should lead, support, test, or be avoided for each priority segment.

```json
{
  "type": "matrix_heatmap",
  "title": "Segment Message Fit",
  "subtitle": "Maps message roles and message-market fit by segment and scenario",
  "data_source": "segment_message_architecture + message_market_fit_scorecard",
  "columns": ["Lead value", "Support proof", "Objection handling", "Price/value", "Avoid"]
}
```

Rows:

```text
Use priority segments from segment_message_architecture.
If segment mapping is missing, use scenario-level rows and add `segment_gap`.
Show 3-6 rows in the main body.
```

Cell score:

```text
Use message_market_fit_score for the segment + scenario + message role when available.
If only message_role exists:
  lead               -> 80
  support            -> 65
  proof              -> 60
  objection_handling -> 55
  retention          -> 50
  avoid              -> 0
Add note `role_based_score_only`.
```

If no score or role exists, render a grouped table and add `missing_message_market_fit_score`.

## Block 3: Feature Benefit Proof Readiness

Purpose: show whether each claim-like benefit is supported enough to use.

```json
{
  "type": "matrix_heatmap",
  "title": "Feature Benefit Proof Readiness",
  "subtitle": "Shows benefit, proof status, source confidence, and claim risk before copywriting",
  "data_source": "feature_benefit_proof_matrix",
  "columns": ["Benefit clarity", "Proof readiness", "Claim safety", "Local trust fit"]
}
```

Rows:

```text
Use top 5-8 feature-benefit rows that affect lead/support message architecture.
Prioritize rows with lead scenarios, high message-market fit, high proof urgency, missing proof, or high claim risk.
```

Cell mappings:

```text
Benefit clarity
  Use message-market fit benefit_clarity sub-score when available.
  If absent, show table and add `missing_benefit_clarity_score`.

Proof readiness
  available -> 90
  partial   -> 60
  missing   -> 25
  risky     -> 10

Claim safety
  inverse of claim_risk_score when numeric.
  If only claim_risk label exists:
    low    -> 85
    medium -> 55
    high   -> 20

Local trust fit
  Use proof readiness or local language/trust sub-score when available.
  If absent, leave as gap rather than assuming trust.
```

Never convert `missing` or `risky` proof into a polished claim.

## Block 4: Claim Risk And Proof Gate

Purpose: show what can be said now, what needs proof/review, and what must not be said.

```json
{
  "type": "status_panel",
  "title": "Claim Risk And Proof Gate",
  "subtitle": "Prevents unsupported claims from flowing into creative, pricing, and funnel work",
  "data_source": "claim_risk_and_proof_gate"
}
```

Items:

```text
Gate status
Usable now
Needs proof
Needs owner review
Blocked / do not say
```

Item mapping:

```json
{
  "label": "Needs proof",
  "value": "4 claims",
  "note": "Partial/missing proof; owners: product, marketing, support",
  "evidence_refs": [],
  "confidence": "medium"
}
```

Gate status:

```text
pass -> no lead claims blocked; partial proof is manageable.
pass_with_cautions -> some claims need cautious wording or review.
fail -> lead message depends on missing/risky proof or sensitive claim without constraints.
```

If `blocking_claims` exists, show them in a companion table even if the status panel is concise.

## Block 5: Objection Severity Ranking

Purpose: show which objections most threaten conversion or trust.

```json
{
  "type": "ranked_bar",
  "title": "Objection Severity Ranking",
  "subtitle": "Ranks objections by purchase impact, trust barrier, price/risk sensitivity, and evidence confidence",
  "data_source": "objection_matrix"
}
```

Rows:

```text
Sort by objection_severity_score descending.
Show top 5-8 objections in standard mode.
Preserve do_not_say and proof_needed in a companion table.
```

Item mapping:

```json
{
  "label": "[Objection]",
  "score": 78,
  "score_label": "High severity",
  "note": "Type: price/trust; proof needed: benchmark + warranty; do not say: guaranteed",
  "evidence_refs": []
}
```

If severity scores are missing, render an action table and add `missing_objection_severity_score`.

## Block 6: Price Message Readiness

Purpose: show whether value framing can support S04 pricing work.

```json
{
  "type": "status_panel",
  "title": "Price Message Readiness",
  "subtitle": "Shows whether S03 can support premium, value, promo, subscription, or risk-reversal framing",
  "data_source": "price_message_seed + objection_matrix + feature_benefit_proof_matrix"
}
```

Items:

```text
Premium justification
Value-for-money framing
Promo/bundle framing
Risk reversal
Avoid price lead
```

Item mapping:

```json
{
  "label": "Premium justification",
  "value": "partial",
  "note": "Proof needed: comparison chart; price objections: high",
  "evidence_refs": [],
  "confidence": "low"
}
```

Render this block when price message seeds exist or S04 is the next required skill. If price signals are missing, show a warning item and hand off the gap to S04.

## Optional Main-Body Blocks

Add these only when their trigger is present and the view changes downstream work:

```text
Competitive Contrast Readiness
  type: matrix_heatmap
  source: competitive_contrast_matrix
  trigger: competitor/substitute comparison materially affects the message.

Behavioral Lever Message Fit
  type: ranked_bar
  source: behavioral_lever_message_seed
  trigger: S02 produced behavioral levers or S05/S07 testing is planned.

Landing Page Message Block Readiness
  type: status_panel
  source: landing_page_message_block_seed
  trigger: DTC, landing page, product page, or funnel conversion matters.

Creator Brief Message Readiness
  type: status_panel
  source: creator_brief_message_seed
  trigger: creator/KOL/expert content is planned.
```

## Companion Tables Required In Standard Mode

Visual blocks are not enough. S03 should also include compact tables for:

```text
segment_message_architecture
feature_benefit_proof_matrix
objection_matrix with do_not_say
local_language_message_seed
price_message_seed
compliance_review_queue when triggered
message_test_backlog when triggered
```

## Thin Output Gate

Mark the S03 HTML section as `rendered_too_thin` if it lacks any of:

```text
executive_takeaway
message input coverage signal
segment-message fit visual block or explicit segment_gap
feature-benefit-proof readiness visual block
claim risk/proof gate
objection severity table or visual block
next_actions for S04/S05/S06/S07/S13
```

## Final Assembly Checklist

Before returning `html_section_draft`:

```text
1. Order visual_blocks by decision flow:
   input gate -> segment message fit -> feature-benefit-proof -> claim gate -> objection severity -> price message readiness.

2. Every message angle traces to a scenario, segment, benefit, proof requirement, and evidence refs.

3. Message seeds remain architecture, not final ad copy.

4. Local-language phrases remain seeds with language/context; do not final-translate or transcreate.

5. Missing proof, risky proof, and do-not-say notes are visible in the main body.

6. Missing scores become tables + data gaps, not fabricated chart values.

7. Add `rendered_too_thin` if fewer than 4 required visual_blocks can be produced in standard mode.
```
