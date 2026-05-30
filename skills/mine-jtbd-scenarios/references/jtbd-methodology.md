# JTBD Methodology

Use this when extracting, normalizing, clustering, and interpreting jobs-to-be-done from S01 evidence.

## Core Principle

A JTBD scenario describes the progress a consumer seeks in a specific situation. It is not a demographic persona, feature request, marketing slogan, or category benefit.

Canonical statement:

```text
When [situation],
I want to [motivation or progress],
so I can [desired outcome],
instead of [current alternative],
while avoiding [barrier or anxiety].
```

For Chinese dashboard rendering, do not force this into a single sentence with "而不是" or "不是...而是..." phrasing. Render it as labeled fields instead:

```text
触发情境
想完成的进步
理想结果
当前替代方案
主要阻力/焦虑
需要证明
```

## Input Signal Priority

Use the strongest available evidence first:

1. Local-language voice atoms with clear purchase/use context
2. Theme clusters with cross-source support
3. Journey episodes with promoter/detractor class mix
4. Bain driver inputs and hardware experience diagnosis
5. Competitor complaints and substitute workarounds
6. Purchase triggers and objections
7. Segment seed packs and persona cards
8. User-provided commercial hypotheses

User hypotheses may preserve weak but important scenarios, but they must remain labeled as hypotheses until evidence supports them.

## Extraction Lenses

For each source signal, ask:

```text
Situation
  What was happening when the need appeared?

Progress
  What better state was the consumer trying to reach?

Alternative
  What did the consumer use, avoid, delay, or compare against?

Barrier
  What blocked purchase, satisfaction, repeat use, or recommendation?

Proof
  What would make the consumer believe the product can solve it?
```

## Candidate Generation Rules

Create one candidate per distinct progress signal. A long review can generate multiple candidates, but each candidate must point back to source refs and should not inflate NSS/NPS sample counts.

Keep local-language phrases when they reveal:

- Search wording
- Category framing
- Competitor comparison language
- Objection language
- Trust or proof language
- Use-case naming

## Scenario Clustering

Cluster candidates by:

```text
primary key: progress sought
secondary key: trigger situation
tie-breakers: current alternative, proof need, barrier, journey episode
```

Do not cluster by demographics alone. Demographics may explain reachability or channel choices, but they should not define the job unless the situation or constraints are materially different.

## Scenario Distinctness

Two scenarios should stay separate when at least two of these differ materially:

- Trigger situation
- Desired outcome
- Current alternative
- Proof requirement
- Price sensitivity
- Main barrier
- Channel/touchpoint behavior
- Activation or return risk

Merge scenarios when they differ only by wording, minor feature preference, or demographic label.

## Scenario-To-Segment Matrix

Each scenario should map to segments as:

```json
{
  "scenario_to_segment_matrix": [
    {
      "scenario_id": "",
      "segment_id": "",
      "relationship": "primary | secondary | hypothesis_only | excluded",
      "reason": "",
      "evidence_refs": [],
      "confidence": "high | medium | low"
    }
  ]
}
```

## Scenario Message Seed

S02 can create message seeds, but not final messages.

```json
{
  "scenario_message_seed": [
    {
      "scenario_id": "",
      "message_angle_seed": "",
      "proof_needed": [],
      "objection_to_address": [],
      "local_language_terms_to_preserve": [],
      "claims_to_avoid": [],
      "handoff_to_s03": true
    }
  ]
}
```

## Price Implication Seed

```json
{
  "scenario_price_implication_seed": [
    {
      "scenario_id": "",
      "price_issue_type": "premium_justification | affordability_pressure | promo_dependency | subscription_resistance | value_uncertainty | competitor_anchor | none",
      "price_sensitivity_refs": [],
      "value_proof_needed": [],
      "handoff_to_s04": true,
      "confidence": "high | medium | low"
    }
  ]
}
```
