# Competitor and Substitute Mapping

Use this after Coverage and Source Quality, before consumer opinion mapping and segmentation.

## Purpose

Build a local competitive context that explains which products, brands, substitutes, and non-consumption alternatives shape consumer expectations, price anchors, and trust.

## Key Rule

Do not decide the biggest competitor from AI memory alone. Top competitors need local evidence.

## Candidate Review List

In standard and deep mode, present 5-10 potential competitors or substitutes for user calibration when review mode allows it.

```json
{
  "competitor_candidate_review_list": [
    {
      "candidate_id": "",
      "brand": "",
      "product": "",
      "candidate_type": "competitor | substitute | anchor | unknown",
      "competitor_roles": ["direct", "premium_anchor", "budget_anchor", "substitute", "ecosystem_anchor", "previous_generation", "channel_threat", "trust_anchor"],
      "why_candidate": "",
      "local_evidence_refs": [],
      "initial_threat_hypothesis": "high | medium | low",
      "evidence_signal_count": 0,
      "user_action": "include | exclude | unsure | add_note",
      "user_note": ""
    }
  ]
}
```

Emit `competitor_candidate_review_gate` before deep voice collection:

```json
{
  "competitor_candidate_review_gate": {
    "status": "pending_user_review | auto_selected_with_caveats | reviewed | skipped_with_gap",
    "candidate_count": 0,
    "included_candidate_ids": [],
    "excluded_candidate_ids": [],
    "unsure_candidate_ids": [],
    "top1_deep_voice_candidate_id": "",
    "previous_generation_candidate_id": "",
    "deep_collection_allowed": false,
    "reason": "",
    "data_gaps": []
  }
}
```

In `real_product_pilot`, do not run deep voice mining across the whole category. Use the reviewed TOP1 competitor plus previous generation when available, then preserve the rest as candidate context.

## Competitor / Substitute Record

```json
{
  "brand": "",
  "product": "",
  "product_type": "",
  "competitor_roles": [],
  "local_price": "",
  "price_tier": "budget | entry | mainstream | premium | flagship | previous_generation | used_refurbished | non_consumption | unknown",
  "subscription_or_recurring_cost": "",
  "channel_presence": [],
  "positioning": "",
  "key_claims": [],
  "feature_overlap": [],
  "strengths": [],
  "weaknesses": [],
  "consumer_praise": [],
  "consumer_complaints": [],
  "opportunity_gaps": [],
  "segment_threat_fit": [],
  "evidence": {
    "price_evidence_refs": [],
    "review_evidence_refs": [],
    "channel_evidence_refs": [],
    "positioning_evidence_refs": [],
    "consumer_comparison_evidence_refs": []
  },
  "evidence_level": "direct_evidence | cross_source_evidence | model_inference | weak_hypothesis | needs_validation",
  "confidence": "high | medium | low"
}
```

## Role Taxonomy

```text
direct
  Same product type and same core job.

substitute
  Different product or behavior solving the same job.

premium_anchor
  Higher-priced product that defines premium expectations.

budget_anchor
  Lower-priced product that compresses willingness to pay.

ecosystem_anchor
  Product tied to a platform, app, device ecosystem, or brand lock-in.

previous_generation
  Older version or prior generation acting as lower-price reference.

channel_threat
  Strong local retail, marketplace, or availability advantage.

trust_anchor
  Strong brand, certification, review base, or expert endorsement.
```

Roles are arrays. Do not force a single role when multiple apply.

## Substitute Taxonomy

```json
{
  "substitute_taxonomy": [
    {
      "substitute_type": "adjacent_device | lower_cost_device | app_or_software | manual_behavior | service | ecosystem_product | non_consumption",
      "examples": [],
      "job_solved": "",
      "why_consumers_choose_it": "",
      "price_or_friction_advantage": "",
      "weakness_vs_our_product": "",
      "evidence_refs": []
    }
  ]
}
```

## Segment-Level Threats

The biggest competitor may differ by segment.

```json
{
  "segment_competitor_threats": [
    {
      "segment_name": "",
      "top_threats": [
        {
          "brand_or_substitute": "",
          "threat_reason": "",
          "threat_score_for_segment": 0,
          "evidence_refs": []
        }
      ],
      "implication": ""
    }
  ]
}
```

Examples:

```text
price-sensitive segment -> budget anchor may be biggest threat
performance segment -> pro sports ecosystem may be biggest threat
sleep recovery segment -> sleep-specialist product may be biggest threat
style-led segment -> jewelry or fashion-adjacent substitute may matter
```

## Price Ladder and Jump Decision Map

Consumers may compare across price tiers instead of staying inside the target price band.

```json
{
  "price_ladder_scan": [
    {
      "price_tier": "budget | entry | mainstream | premium | flagship | previous_generation | used_refurbished | non_consumption",
      "local_price_range": "",
      "representative_products": [],
      "consumer_jump_logic": "trade_up | trade_down | lateral_switch | delay_purchase | no_purchase",
      "why_consumers_compare": "",
      "evidence_refs": []
    }
  ],
  "jump_decision_risks": [
    {
      "from_our_price_position": "",
      "to_alternative_tier": "",
      "risk_type": "trade_up | trade_down | lateral_switch | delay_purchase | no_purchase",
      "trigger": "",
      "consumer_logic": "",
      "risk_level": "high | medium | low",
      "required_counter_proof": [],
      "evidence_refs": []
    }
  ]
}
```

Common jump logic:

```text
trade_up
  "If I am already spending this much, I might pay more for a trusted brand."

trade_down
  "If the functions are close enough, I will buy the cheaper option."

lateral_switch
  "A different product type solves the same job well enough."

delay_purchase
  "I will wait for promotion, previous generation, used/refurbished, or a later version."

no_purchase
  "The problem is not painful enough to buy anything now."
```

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

`Price Ladder Pull` measures whether a competitor or substitute can pull consumers upward, downward, sideways, into delayed purchase, or into non-consumption.

Segment-level variant:

```text
Segment Threat Score =
  Segment Job Overlap * 0.25
+ Segment Price Anchor Strength * 0.20
+ Segment Channel Reach * 0.15
+ Segment Trust Fit * 0.15
+ Feature / Benefit Relevance * 0.15
+ Switching Barrier * 0.10
```

## Evidence Requirement

A top competitor must have at least two local evidence signals unless it is explicitly marked as a hypothesis.

Valid local evidence signals:

```text
local SERP, ranking, review, or comparison page appearance
local marketplace, retailer, or official-channel availability
local price evidence
local review, forum, social, or video discussion
internal benchmark or user-provided competitor list
```

If a user-provided competitor has weak or missing local evidence, mark:

```text
user_provided_but_local_evidence_missing
```

## User Calibration

When Gate 2 review is used, show the candidate review list and ask the user to:

```text
include
exclude
mark unsure
add missing competitor
add internal note
```

Do not let user selection erase evidence. If the user excludes a competitor with strong evidence, preserve it in `excluded_but_evidence_strong` with the user's reason.
