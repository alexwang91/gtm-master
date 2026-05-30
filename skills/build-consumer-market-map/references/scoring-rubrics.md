# S01 Scoring Rubrics

Use these rubrics to make S01 quantifiable. Scores are 0-100 unless stated otherwise.

## Source Quality Score

```text
Source Quality Score =
  Country Relevance * 0.15
+ Category Relevance * 0.15
+ Consumer Intent Quality * 0.15
+ Review / Evidence Depth * 0.15
+ Freshness * 0.10
+ Sample Size * 0.10
+ Verified / High-Intent Signal * 0.10
+ Bias Risk Inverse * 0.07
+ Extraction Confidence * 0.03
```

Interpretation:

```text
80-100 = primary evidence
60-79  = secondary evidence
40-59  = context only
0-39   = avoid or use only as a data gap clue
```

## Coverage Score

```text
Coverage Score =
  Source Type Coverage * 0.30
+ Local Language Coverage * 0.20
+ Competitor Coverage * 0.20
+ Price Coverage * 0.15
+ Consumer Voice Coverage * 0.10
+ Local Voice Source Coverage * 0.05
```

Interpretation:

```text
80-100 = strong
60-79  = adequate
40-59  = thin
0-39   = missing
```

## Selling Point Fit Score

Use after product capability normalization and before broad evidence collection.

```text
Selling Point Fit Score =
  Category Mainstream Fit * 0.25
+ Local Search Language Match * 0.20
+ Product Feature Support * 0.20
+ Competitor Differentiation * 0.15
+ Trend / Rising Query Signal * 0.10
+ Proof Availability * 0.10
- Education Burden * 0.10
```

Interpretation:

```text
75-100 = strong GTM selling point candidate
55-74  = usable but needs proof or sharper wording
35-54  = weak or niche; validate before prioritizing
0-34   = do not lead with this claim
```

Trend signals are directional only. Do not treat Google Trends-style data as market size, exact demand, or purchase intent.

## Competitor Threat Score

```text
Competitor Threat Score =
  Positioning Overlap * 0.18
+ Price Anchor Strength * 0.16
+ Price Ladder Pull * 0.12
+ Channel Presence * 0.14
+ Review Strength * 0.14
+ Brand Trust * 0.13
+ Feature Overlap * 0.08
+ Switching Barrier * 0.05
```

Interpretation:

```text
75-100 = high threat
45-74  = medium threat
0-44   = low threat
```

Price Ladder Pull measures trade-up, trade-down, lateral-switch, delayed-purchase, and non-consumption risk.

## Consumer Pain Intensity Score

```text
Pain Intensity Score =
  Frequency * 0.30
+ Emotion Strength * 0.25
+ Purchase / Return Impact * 0.25
+ Current Solution Failure * 0.20
```

Use 1-5 sub-scores and normalize to 0-100.

## Voice Atom Evidence Strength Score

Use when turning reviews, comments, forum posts, surveys, and support notes into voice atoms.

```text
Voice Atom Evidence Strength Score =
  Source Item Quality * 0.20
+ Speaker Context Clarity * 0.15
+ Statement Specificity * 0.15
+ Local Language Preservation * 0.10
+ Product or Competitor Link Clarity * 0.10
+ Purchase or Journey Link * 0.10
+ Extraction Confidence * 0.10
+ Deduplication Confidence * 0.10
```

Interpretation:

```text
80-100 = high evidence strength
60-79  = medium evidence strength
0-59   = low evidence strength
```

## Theme Cluster Confidence Score

```text
Theme Cluster Confidence Score =
  Unique Source Item Count * 0.20
+ Distinct Source Count * 0.15
+ Cross-Source Agreement * 0.15
+ Local Language Consistency * 0.10
+ Driver Tag Consistency * 0.10
+ Source Quality * 0.10
+ Recency * 0.10
+ Deduplication Confidence * 0.10
```

Interpretation:

```text
80-100 = high confidence theme
60-79  = medium confidence theme
40-59  = low confidence theme
0-39   = weak signal or data gap
```

## Segment Evidence Strength Score

Use before promoting a segment candidate into the S01 segment seed pack.

```text
Segment Evidence Strength =
  Voice Theme Support * 0.20
+ Distinct Motivation Support * 0.15
+ Use Case or Journey Support * 0.15
+ Price Behavior Support * 0.12
+ Competitor/Substitute Support * 0.12
+ Channel Evidence Support * 0.10
+ Market Size Support * 0.08
+ Cross-Source Agreement * 0.08
```

Interpretation:

```text
80-100 = strong segment seed
60-79  = usable segment seed
40-59  = weak hypothesis; keep only if commercially important
0-39   = do not promote as a segment
```

## Market Sizing Confidence Score

Use for TAM/SAM/SOM seed outputs. S01 should report ranges, not false precision.

```text
Market Sizing Confidence =
  Official / Primary Data Quality * 0.20
+ Country and Category Match * 0.18
+ Assumption Transparency * 0.16
+ Price / Affordability Support * 0.12
+ Channel Reach Support * 0.10
+ Segment Evidence Support * 0.10
+ Internal Data Support * 0.08
+ Sensitivity Risk Inverse * 0.06
```

Interpretation:

```text
80-100 = high confidence seed
60-79  = medium confidence seed
40-59  = low confidence seed
0-39   = assumption-only seed
```

## Segment Priority Score

```text
Segment Priority Score =
  Pain Intensity * 0.18
+ Product Fit * 0.18
+ Willingness to Pay * 0.14
+ Reachability * 0.12
+ Local Market Size * 0.12
+ Competitor Gap * 0.10
+ Content Virality * 0.08
+ Retention / Repeat Potential * 0.08
- Trust Barrier * 0.10
- Return / Support Risk * 0.05
```

Interpretation:

```text
75-100 = P1 launch segment
55-74  = P2 secondary segment
35-54  = test or niche segment
0-34   = avoid or deprioritize
```

## Segment Distinctness Score

```text
Segment Distinctness Score =
  Motivation Difference * 0.30
+ Use Case Difference * 0.25
+ Price Behavior Difference * 0.15
+ Channel Difference * 0.15
+ Objection / Trust Barrier Difference * 0.15
```

Interpretation:

```text
75-100 = clearly distinct
55-74  = usable but watch overlap
35-54  = merge or split candidate
0-34   = not distinct
```

## Persona Confidence Score

Use after persona cards are generated from segment seeds.

```text
Persona Confidence Score =
  Segment Evidence Strength * 0.25
+ Local Language Support * 0.15
+ Buying Trigger Evidence * 0.15
+ Proof Need Clarity * 0.15
+ Channel Evidence * 0.10
+ Price Concern Evidence * 0.10
+ Objection Evidence * 0.10
```

Interpretation:

```text
80-100 = high confidence persona
60-79  = usable persona with caveats
40-59  = weak persona hypothesis
0-39   = do not use as launch persona
```

## Channel Fit Score

Use for segment-level discovery, comparison, purchase, proof/trust, complaint/support, and retention/advocacy touchpoints.

```text
Channel Fit Score =
  Segment Reach * 0.18
+ Touchpoint Intent Fit * 0.16
+ Source Trust * 0.14
+ Category Relevance * 0.12
+ Competitor Presence Signal * 0.10
+ Purchase Path Fit * 0.10
+ Content Format Fit * 0.08
+ Local Language Fit * 0.06
+ Measurability / Extractability * 0.04
+ Internal Plan Alignment * 0.02
- Friction / Access Risk * 0.10
- Brand Safety or Compliance Risk * 0.06
```

Interpretation:

```text
75-100 = strong channel candidate
55-74  = useful secondary channel candidate
35-54  = test or monitor
0-34   = weak fit or avoid
```

Internal plan alignment can preserve a user-provided channel as a test hypothesis, but it should not make it a locally proven channel.

## Price Sensitivity Seed Score

S01 produces a seed panel. Full pricing belongs to downstream pricing skill.

```text
Price Sensitivity Seed Score =
  Affordability Pressure * 0.18
+ Competitor Price Gap Pressure * 0.16
+ Price Complaint Intensity * 0.15
+ Price Ladder Pull * 0.12
+ Promotion Dependence * 0.10
+ Subscription or Ongoing Cost Resistance * 0.10
+ Low Differentiation Risk * 0.08
+ Trust Deficit * 0.07
+ Channel Price Transparency * 0.04
```

Interpretation:

```text
0-30   = low sensitivity
31-55  = medium sensitivity
56-75  = high sensitivity
76-100 = very high sensitivity
```

## Price Anchor Confidence Score

Use before treating a competitor or substitute as a price anchor.

```text
Price Anchor Confidence Score =
  Local Price Evidence Quality * 0.25
+ Channel Relevance * 0.15
+ Recency * 0.15
+ Product Comparability * 0.15
+ Consumer Comparison Evidence * 0.10
+ Price Display Clarity * 0.10
+ Cross-Source Agreement * 0.10
```

Interpretation:

```text
80-100 = strong price anchor
60-79  = usable price anchor
40-59  = weak/context price anchor
0-39   = do not use as anchor
```

## NSS/NPS Proxy Confidence Score

Use when direct NSS/NPS is unavailable.

```text
Proxy Confidence Score =
  Sample Size Adequacy * 0.20
+ Source Quality * 0.20
+ Recommendation Language Clarity * 0.15
+ Complaint Severity Clarity * 0.15
+ Verified Buyer / High Intent Share * 0.10
+ Country Match * 0.10
+ Recency * 0.05
+ Deduplication Confidence * 0.05
```

Interpretation:

```text
80-100 = high confidence proxy
60-79  = directional proxy
40-59  = weak proxy
0-39   = do not calculate; record data gap
```

Never label proxy NSS/NPS as surveyed NSS/NPS.

Calculate proxy from deduped source items, not raw voice atom counts. If the evidence fails the threshold in `consumer-voice-nss-bain-pipeline.md`, do not calculate the proxy; record the blocker.

## Earned Growth Readiness Score

Use for S01 earned growth seed. This is a directional readiness signal unless direct attribution data exists.

```text
Earned Growth Readiness Score =
  Recommendation / Referral Signal * 0.20
+ Repeat or Renewal Signal * 0.18
+ Organic / Direct Discovery Signal * 0.14
+ Community or Word-of-Mouth Signal * 0.14
+ Detractor Drag Inverse * 0.12
+ Product Experience Driver Strength * 0.12
+ Source Quality * 0.10
```

Interpretation:

```text
75-100 = strong earned-growth potential seed
55-74  = moderate seed
35-54  = weak or unproven seed
0-34   = do not claim earned-growth potential
```

## Bain Driver Impact Score

Use for directional Bain-style driver inputs, not causal claims.

```text
Bain Driver Impact Score =
  Normalized Frequency * 0.25
+ Mean Emotion Strength * 0.20
+ Purchase or Return Impact * 0.20
+ NSS/NPS Class Weight * 0.15
+ Recency * 0.10
+ Cross-Source Agreement * 0.10
```

Interpretation:

```text
75-100 = major driver candidate
55-74  = meaningful driver candidate
35-54  = weak or segment-specific driver
0-34   = context only
```

Driver impact is a prioritization signal. It is not proof that changing the driver will cause NSS/NPS or earned growth improvement.

## Bain Outer Loop Opportunity Score

Use when turning NSS/NPS drivers into systemic hardware, GTM, service, or channel actions.

```text
Bain Outer Loop Opportunity Score =
  Customer Impact * 0.22
+ Frequency * 0.18
+ Detractor Drag * 0.16
+ Revenue or Conversion Relevance * 0.14
+ Next-Generation Strategic Fit * 0.12
+ Fix or Proof Feasibility * 0.10
+ Evidence Confidence * 0.08
```

Interpretation:

```text
75-100 = top outer-loop action candidate
55-74  = meaningful action candidate
35-54  = monitor or test
0-34   = keep as context or data gap
```

This score ranks action candidates. It is not evidence that the action will improve NSS/NPS until tested or measured.

## GTM Priority Score

```text
GTM Priority Score =
  Segment Priority * 0.25
+ Market Opportunity * 0.15
+ Price Credibility * 0.15
+ Competitive Gap * 0.15
+ Channel Reachability * 0.10
+ Proof Availability * 0.10
+ Earned Growth Potential * 0.05
- Claim / Compliance Risk * 0.05
```

Use this score to support recommendations, not to replace reasoning.

## Data Confidence Score

```text
Data Confidence Score =
  Evidence Coverage * 0.25
+ Source Quality * 0.25
+ Cross-Source Agreement * 0.20
+ Freshness * 0.15
+ Internal Data Support * 0.10
+ Extraction Reliability * 0.05
```

Interpretation:

```text
80-100 = high confidence
60-79  = medium confidence
40-59  = low confidence
0-39   = assumption only
```
