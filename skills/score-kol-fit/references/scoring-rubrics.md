# S06 Scoring Rubrics

Use 0-100 scores. Label weak evidence as hypothesis.

## Creator Archetype Fit Score

```text
Creator Archetype Fit =
  25% segment trust need fit
+ 20% proof requirement fit
+ 20% channel/platform role fit
+ 15% message architecture fit
+ 10% local language/category fit
+ 10% measurement/test feasibility
```

## Candidate Fit Score

```text
Candidate Fit =
  20% archetype-role fit
+ 20% audience/segment fit
+ 20% trust/proof fit
+ 15% platform relevance
+ 10% content quality proxy
+ 10% collaboration/test feasibility
- 15% brand_safety_or_claim_risk_penalty
```

Normalize to 0-100.

## Audience Segment Fit

```text
Audience Segment Fit =
  30% country/language relevance
+ 25% category/topic relevance
+ 20% segment/JTBD relevance
+ 15% engagement quality proxy
+ 10% channel reach relevance
```

Follower count alone contributes no more than 10 points unless first-party audience data is supplied.

## Candidate Discovery Priority

Use this before candidate fit scoring when a longlist is discovered.

```text
Candidate Discovery Priority =
  20% local country/language signal
+ 20% category authority signal
+ 15% competitor or anchor-product overlap
+ 15% proof/content sample relevance
+ 10% recent activity or evergreen authority
+ 10% accessible public evidence quality
+ 10% platform/channel relevance
```

Hard caps:

```text
no accessible public content sample -> max 59
no country/language signal -> max 64
only follower count found -> max 49
blocked source with no alternative evidence -> max 39
```

## Candidate Evidence Coverage

```text
Candidate Evidence Coverage =
  25% profile or author identity evidence
+ 25% relevant content samples
+ 20% country/language/category evidence
+ 15% public metric proxy availability
+ 15% risk/disclosure/brand-safety checkability
```

Use this as a confidence modifier, not as a fit score. A high-fit candidate with low evidence coverage must remain `needs_validation`.

## Trust Proof Fit

```text
Trust Proof Fit =
  30% proof type match
+ 25% credibility for the claim
+ 20% ability to demonstrate product context
+ 15% objection handling fit
+ 10% source/evidence quality
```

Hard caps:

```text
no relevant content samples -> max 59
unsupported sensitive claim role -> max 49
candidate known mainly for unrelated content -> max 64
```

## Brand Safety Risk Score

This is a risk score: higher means riskier.

```text
Brand Safety Risk =
  25% unsafe or controversial adjacency
+ 20% misleading claim/history risk
+ 20% category credibility mismatch
+ 15% sponsorship/disclosure risk
+ 10% competitor conflict
+ 10% suspicious audience or engagement proxy
```

## Test Priority Score

```text
Creator Test Priority =
  25% business impact
+ 20% uncertainty reduction
+ 20% proof/risk reduction
+ 15% audience/sample feasibility
+ 10% speed/cost feasibility
+ 10% downstream decision value
```

## Recommendation Rationale Completeness

```text
Rationale Completeness =
  20% segment/JTBD reason clarity
+ 20% proof and trust reason clarity
+ 15% platform/channel reason clarity
+ 15% budget reason clarity
+ 15% expected outcome reason clarity
+ 10% risk and counter-rationale clarity
+ 5% evidence refs and confidence label
```

Hard caps:

```text
no counter-rationale -> max 79
no budget basis -> max 69
no expected-outcome basis -> max 69
no evidence refs or hypothesis label -> max 59
```

## Budget Estimate Confidence

```text
Budget Estimate Confidence =
  30% user or first-party rate/spend data
+ 25% candidate rate card, media kit, or approved quote relevance
+ 20% local platform/category benchmark relevance
+ 15% campaign scope clarity
+ 10% currency, tax, logistics, and seeding cost clarity
```

Hard caps:

```text
no currency or country basis -> max 69
only public proxy data -> max 59
no rate, quote, benchmark, or historical basis -> max 39
```

## Expected Outcome Confidence

```text
Expected Outcome Confidence =
  30% historical first-party campaign performance
+ 25% candidate content sample performance relevance
+ 20% platform/category benchmark relevance
+ 15% audience/channel fit
+ 10% tracking and attribution plan clarity
```

Hard caps:

```text
no tracking or landing context for visits -> max 69
only follower counts available -> max 49
sales/conversion estimate without attribution evidence -> max 39
```
