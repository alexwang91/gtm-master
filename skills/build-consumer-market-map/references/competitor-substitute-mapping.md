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

## TOP1 Competitor Proof Board

The dashboard must be able to prove why one competitor is treated as TOP1. Use
this board for the executive comparison surface. It is narrower than the full
competitor map: it explains the highest local threat for GTM decisions.

```text
TOP1 Competitor Proof Score =
  Price Pressure * 0.25
+ Feature Substitution * 0.20
+ Local Channel Overlap * 0.20
+ Voice / Review Evidence * 0.15
+ Ecosystem Or Lock-In Strength * 0.10
+ Decision Journey Interception * 0.10
```

Factor definitions:

```text
Price Pressure
  How strongly the competitor compresses perceived value through lower street
  price, promotion, installment, bundle, or previous-generation discount.

Feature Substitution
  How many lead jobs, benefits, and comparison criteria it can satisfy for the
  same target segment.

Local Channel Overlap
  How often it appears in the same local retailers, marketplaces, operators,
  price-comparison sites, review pages, or search journeys.

Voice / Review Evidence
  Depth, recency, and source quality of local consumer, forum, review, and
  specialist-media discussion.

Ecosystem Or Lock-In Strength
  Phone/app/platform/service/warranty/community advantages that make switching
  harder.

Decision Journey Interception
  Ability to appear at discovery, active evaluation, purchase, setup, or
  post-purchase proof moments before the user's product can close the decision.
```

Required output:

```json
{
  "top1_competitor_proof_board": {
    "selected_top1_candidate_id": "",
    "selected_top1_name": "",
    "selection_status": "reviewed | auto_selected_with_caveats | hypothesis_only | blocked",
    "score_formula": "price_pressure_25 + feature_substitution_20 + local_channel_overlap_20 + voice_review_evidence_15 + ecosystem_lockin_10 + decision_journey_interception_10",
    "factor_scores": [
      {
        "factor": "price_pressure | feature_substitution | local_channel_overlap | voice_review_evidence | ecosystem_lockin | decision_journey_interception",
        "score_0_100": 0,
        "weight": 0,
        "weighted_score": 0,
        "evidence_level": "direct_evidence | cross_source_evidence | internal_evidence | model_inference | weak_hypothesis | needs_validation",
        "evidence_refs": [],
        "calculation_note": "",
        "confidence": "high | medium | low | hypothesis_only"
      }
    ],
    "total_score_0_100": 0,
    "why_this_is_top1": "",
    "why_not_other_candidates": [
      {
        "candidate_id": "",
        "candidate_name": "",
        "score_0_100": 0,
        "reason_not_top1": "",
        "segment_or_price_tier_exception": ""
      }
    ],
    "previous_generation_or_internal_risk_split": "",
    "segment_exceptions": [],
    "local_team_implication": "",
    "evidence_refs": [],
    "data_gaps": [],
    "confidence": "high | medium | low | hypothesis_only"
  }
}
```

Rules:

- TOP1 is not always the cheapest product; it is the strongest local decision
  threat after the weighted proof board.
- Previous generation and internal price-ladder risks can outrank TOP1 for a
  segment, but they should be labeled separately as `previous_generation`,
  `internal_benchmark`, or `price_ladder_risk`.
- If the user confirms a TOP1 candidate with weak local evidence, keep the
  choice but set `selection_status` to `hypothesis_only` or
  `auto_selected_with_caveats`.
- Show 5-10 alternatives in the review list when mode and review gate allow it;
  the board should explain why the selected TOP1 beats those alternatives.

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
