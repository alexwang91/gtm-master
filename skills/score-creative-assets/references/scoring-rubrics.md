# S05 Scoring Rubrics

Use 0-100 scores. Label weak evidence as hypothesis. Scores evaluate editable text only.

## Copy Message Fit Score

```text
Copy Message Fit =
  25% segment-message match
+ 20% JTBD/situation match
+ 20% benefit clarity
+ 15% objection handling
+ 10% local language alignment
+ 10% CTA/channel alignment
```

Interpretation:

```text
80-100 strong fit; can test or scale if proof/claim risk is acceptable
65-79  usable with targeted revision
45-64  weak; revise before paid, PDP, retail, or landing-page use
0-44   misaligned or unusable for the intended segment/placement
```

## Proof And Claim Clarity Score

```text
Proof And Claim Clarity =
  30% proof statement exists and is readable
+ 25% proof matches lead claim
+ 20% proof is credible/local enough
+ 15% proof is understandable for the channel
+ 10% proof addresses the main objection
```

Hard caps:

```text
unsupported lead claim -> max 49
proof line vague or hidden -> max 64
proof not local or not source-backed -> max 74
```

## Claim Risk Score

This is a risk score: higher means riskier.

```text
Claim Risk =
  30% regulated/sensitive topic exposure
+ 25% evidence gap severity
+ 20% absoluteness or ambiguity
+ 15% competitor/comparison risk
+ 10% local compliance or platform policy uncertainty
```

Interpretation:

```text
0-24   low risk
25-49  manageable with proof/source notes
50-74  needs review before use
75-100 block or rewrite before use
```

## Channel Copy Fit Score

```text
Channel Copy Fit =
  25% placement norm fit
+ 20% segment reach/channel fit
+ 20% copy density and readability
+ 15% proof/CTA clarity
+ 10% price/value context
+ 10% technical text readiness
```

Use channel context from S01/S02. If channel context is missing, cap at `low` confidence.

## Text Attention Hierarchy Score

```text
Text Attention Hierarchy =
  30% primary hook clarity
+ 25% main claim specificity
+ 20% proof line proximity
+ 15% objection reversal clarity
+ 10% CTA clarity
```

Use this as a component of copy quality, not as proof of conversion.

## Copy Priority Score

```text
Copy Priority =
  0.30 copy_message_fit
+ 0.20 proof_and_claim_clarity
+ 0.15 channel_copy_fit
+ 0.15 text_attention_hierarchy
+ 0.10 commercial/segment priority
+ 0.10 revision feasibility
- 0.15 claim_risk_penalty
```

Normalize to 0-100. Do not rank copy items if comparable scores are missing; use tables and add `missing_visual_block_score`.

## Test Priority Score

```text
Test Priority =
  25% business impact
+ 20% uncertainty reduction
+ 20% risk reduction
+ 15% traffic/sample feasibility
+ 10% speed/cost feasibility
+ 10% downstream decision value
```

High-scoring tests should name hypothesis, audience, channel, metric, minimum evidence, and confounders.
