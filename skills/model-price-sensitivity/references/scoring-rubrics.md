# S04 Scoring Rubrics

Scores are 0-100 unless stated otherwise. Clamp final scores to 0-100.

## Price Credibility Score

```text
Price Credibility =
  Local Anchor Fit * 0.18
+ Competitor Gap Acceptability * 0.16
+ Product-Job Fit * 0.14
+ Value Proof Readiness * 0.14
+ Segment WTP Support * 0.12
+ Channel Display Fit * 0.08
+ Promo/Financing Support * 0.06
+ Brand Trust Support * 0.06
+ Evidence Confidence * 0.06
```

Interpretation:

```text
75-100 = credible price posture
55-74  = credible with proof or testing
35-54  = risky; test before decision
0-34   = not credible with current evidence
```

## Opening Strategy Scores

Use these scores to decide whether S04 should recommend a high public anchor, parity/value opening, price attack, niche high-price opening, or test-before-scale path. These are strategy fit scores, not final price approvals.

```text
Premium Anchor Score =
  Product Differentiation * 0.18
+ Brand Trust * 0.14
+ Proof Readiness * 0.14
+ Competitor Scarcity / Weak Substitution * 0.13
+ Low Price Sensitivity * 0.13
+ Channel Premium Support * 0.10
+ Positioning Objective * 0.09
+ Promo Mechanism Readiness * 0.09
```

```text
Penetration Attack Score =
  Competitor Pressure * 0.18
+ Cost Advantage * 0.18
+ Price Sensitivity * 0.15
+ Market Volume Potential * 0.14
+ Channel Efficiency * 0.12
+ Product Parity Without Premium Proof Need * 0.10
+ Strategic Share Objective * 0.08
+ Promo / MKT Budget Support * 0.05
```

```text
Niche High Price Score =
  Low Volume Expectation * 0.16
+ Weak Direct Competition * 0.15
+ Differentiation Or Scarcity * 0.15
+ Manageable Proof Burden * 0.12
+ Positioning Protection Need * 0.12
+ Selective Channel Fit * 0.10
+ Low Elasticity Segment Presence * 0.10
+ Profit Over Volume Objective * 0.10
```

```text
Parity Value Score =
  Local Anchor Fit * 0.18
+ Product Parity Or Slight Advantage * 0.16
+ Medium Price Sensitivity * 0.14
+ Adequate Proof Readiness * 0.13
+ Channel Fit * 0.12
+ Promo Flexibility * 0.10
+ Conversion Objective * 0.09
+ Forecast Confidence * 0.08
```

Interpretation:

```text
75-100 = strong fit
60-74  = possible; test challenger strategy
40-59  = weak fit; use only with explicit objective
0-39   = avoid or block
```

Override rules:

```text
private floor above expected transaction price
  Price attack and heavy promo cannot proceed without finance review.

proof readiness low and price above local p75
  Premium proof-led cannot proceed; use premium anchor with controlled proof tests or test before scale.

cold demand and weak competition
  Do not open low unless there is evidence that lower price unlocks scale.

channel conflict unresolved
  Opening strategy cannot exceed channel_review.
```

## Price Sensitivity Score

```text
Price Sensitivity =
  Affordability Pressure * 0.16
+ Competitor Price Gap Pressure * 0.15
+ Price Objection Severity * 0.14
+ Price Ladder Pull * 0.12
+ Low Differentiation Risk * 0.10
+ Trust / Proof Gap * 0.10
+ Promo Dependence * 0.08
+ Subscription or Recurring Cost Resistance * 0.07
+ Channel Price Transparency * 0.05
+ Evidence Confidence * 0.03
```

Interpretation:

```text
0-30   = low sensitivity
31-55  = medium sensitivity
56-75  = high sensitivity
76-100 = very high sensitivity
```

## Rapid WTP Prior Score

Use this when real local WTP research, internal sales evidence, or immediate field testing is unavailable. The score is a quantified prior, not measured WTP.

```text
Rapid WTP Prior =
  Local Price Anchor Fit * 0.22
+ Purchasing Power Fit * 0.18
+ Product Competitiveness Fit * 0.17
+ Brand / Channel Trust Proxy * 0.13
+ Proof Readiness * 0.12
+ Demand Proxy Strength * 0.10
+ Sales / Review Velocity Proxy * 0.08
```

Interpretation:

```text
75-100 = price supported with caveats
55-74  = test before scale
35-54  = research first
0-34   = price not supported with current evidence
```

Evidence caps:

```text
direct WTP, sales, local anchors, and private constraints present
  Cap can be high.

public proxy only
  Cap at medium.

local price anchors missing
  Cap at low and do not output a precise WTP range.

synthetic persona only
  Cap at hypothesis_only and do not raise total confidence.

target price above local p75 without strong proof
  Cap at test_before_scale.
```

Each factor must retain `score_0_100`, `weight`, `weighted_score`, `evidence_level`, `source_refs`, `calculation_note`, and `confidence_cap`.

## WTP Confidence Score

```text
WTP Confidence =
  Direct WTP or Sales Evidence * 0.25
+ Segment Evidence Strength * 0.16
+ Price Anchor Quality * 0.14
+ Price Objection Clarity * 0.12
+ Message/Proof Support * 0.12
+ Channel Context Quality * 0.08
+ Recency * 0.06
+ Internal Constraint Support * 0.07
```

## Pricing Readiness Score

```text
Pricing Readiness =
  Price Credibility * 0.22
+ WTP Confidence * 0.18
+ Proof Readiness * 0.16
+ Channel/Margin Constraint Coverage * 0.14
+ Promo/Subscription Clarity * 0.10
+ Risk Guardrail Completeness * 0.10
+ Test Plan Quality * 0.10
```

Interpretation:

```text
75-100 = ready for pricing decision review
55-74  = ready for controlled test
35-54  = research first
0-34   = blocked by data gaps
```

## Decision Gate Override Rules

Readiness scores do not override hard blockers.

```text
missing_private_margin_constraints
  Cannot exceed finance_review or controlled_test_ready.

channel_conflict_unresolved
  Cannot exceed channel_review.

proof_gap_for_premium
  Cannot exceed controlled_test_ready for premium pricing.

synthetic_only_or_public_proxy_only
  Cannot exceed research_first unless the output is only a test plan.

test_results_low_quality_or_uncontrolled
  Cannot exceed controlled_test_ready.

margin_fail_after_private_calculation
  Cannot exceed finance_review unless a loss-leader strategy is explicitly approved.
```

## Promo Risk Score

```text
Promo Risk =
  Margin Risk * 0.20
+ Brand Dilution Risk * 0.15
+ Channel Conflict Risk * 0.15
+ Pull-Forward Risk * 0.12
+ Return/Support Risk * 0.10
+ Promo Dependency Risk * 0.10
+ Price Transparency Risk * 0.08
+ Evidence Confidence Inverse * 0.10
```
