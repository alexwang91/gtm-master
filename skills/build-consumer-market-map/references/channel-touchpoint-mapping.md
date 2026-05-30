# Channel and Touchpoint Mapping

Use this after local source discovery, competitor/substitute mapping, consumer voice processing, segment inference, and price anchor collection. It maps where each segment discovers, compares, buys, trusts, complains, returns, and advocates.

This is a market-context layer. S01 should produce channel and touchpoint evidence, fit scores, and hypotheses. It should not select final media budgets, final KOLs, or final creative strategy.

## Inputs

```json
{
  "launch_country_or_region": "",
  "product_category": "",
  "target_price_range": "",
  "localization_preflight": {},
  "local_source_map": {},
  "local_voice_source_map": {},
  "competitor_substitute_map": [],
  "competitor_threat_scores": [],
  "segment_seed_pack": [],
  "persona_cards": [],
  "voice_theme_clusters": [],
  "journey_episode_inputs": [],
  "price_anchor_panel": {},
  "planned_channels_or_internal_channel_plan": "",
  "historical_ads_kol_landing_pages_and_creatives": ""
}
```

## Core Rules

- Do not assume a global channel mix. Discover local commerce, media, review, and community habits.
- Separate discovery, comparison, purchase, proof/trust, complaint, support/return, and advocacy touchpoints.
- Keep retailer/marketplace availability separate from consumer trust and conversion fit.
- Treat internal planned channels as hypotheses unless local evidence supports them.
- Do not choose specific KOLs in S01; identify creator/expert types and evidence sources.
- Do not treat social buzz as purchase intent without comparison, price, review, or purchase-path evidence.

## Touchpoint Taxonomy

```text
discovery
  Search, social/video, creators, media articles, retail browsing, community mentions, ads.

comparison
  Expert reviews, comparison pages, price comparison sites, marketplace listings, forums, video reviews, Q&A, competitor pages.

purchase
  Marketplaces, retailers, DTC site, carrier/operator, offline retail, resellers, app stores or subscription checkout where relevant.

proof_and_trust
  Expert reviewers, certifications, warranty/returns pages, retailer trust, verified reviews, community owner threads, privacy/security proof, local-language support.

complaint_and_support
  Forums, retailer reviews, app reviews, support pages, social comments, complaint boards, return/warranty channels.

retention_and_advocacy
  App experience, community sharing, referral language, repeat purchase, accessories, subscription renewal, support recovery.
```

## Channel Evidence Record

```json
{
  "channel_touchpoint_evidence": [
    {
      "evidence_id": "",
      "channel_or_touchpoint": "",
      "touchpoint_stage": "discovery | comparison | purchase | proof_and_trust | complaint_and_support | retention_and_advocacy",
      "source_type": "serp | marketplace | retailer | price_comparison | expert_review | forum | specialist_media | video | social | app_store | brand_site | internal_private | other",
      "country_or_region": "",
      "segment_refs": [],
      "product_or_competitor_refs": [],
      "evidence_signal": "",
      "local_language_terms": [],
      "source_quality_score": 0,
      "confidence": "high | medium | low",
      "limitations": []
    }
  ]
}
```

## Channel Fit Score

Score a channel for each segment and touchpoint stage.

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
75-100 = strong channel candidate for the segment/stage
55-74  = useful secondary channel candidate
35-54  = test or monitor
0-34   = weak fit or avoid
```

Internal plan alignment is intentionally small. It can preserve a channel hypothesis, but it should not overwhelm local evidence.

## Segment Channel Touchpoint Map

```json
{
  "segment_channel_touchpoint_map": [
    {
      "segment_id": "",
      "segment_name": "",
      "discovery_channels": [],
      "comparison_channels": [],
      "purchase_channels": [],
      "proof_and_trust_touchpoints": [],
      "complaint_and_support_channels": [],
      "retention_and_advocacy_touchpoints": [],
      "trusted_expert_or_creator_types": [],
      "content_formats": [],
      "retailer_or_marketplace_candidates": [],
      "channel_risks": [],
      "channel_fit_scores": [],
      "recommended_channel_role": "primary | secondary | test | monitor | avoid",
      "evidence_refs": [],
      "assumptions": [],
      "data_gaps": [],
      "confidence": "high | medium | low"
    }
  ]
}
```

## Channel Role Definitions

```text
primary
  Strong evidence for reach, trust, intent, and purchase/comparison fit.

secondary
  Useful supporting channel, but not enough evidence to lead.

test
  Commercially interesting or user-planned channel with incomplete local evidence.

monitor
  Useful for social listening, complaint tracking, or competitor intelligence.

avoid
  Weak fit, high friction, poor trust, policy risk, or wrong audience.
```

## Retailer And Marketplace Candidate Map

Use local source discovery and price intelligence to identify purchase candidates. Do not assume the largest global marketplace is the local purchase default.

```json
{
  "retailer_marketplace_candidates": [
    {
      "channel_id": "",
      "name": "",
      "channel_type": "marketplace | retailer | price_comparison | dtc | offline_retail | carrier_operator | reseller | other",
      "category_relevance": 0,
      "competitor_presence": 0,
      "price_visibility": 0,
      "review_depth": 0,
      "trust_signal": 0,
      "purchase_friction": 0,
      "segment_fit_refs": [],
      "recommended_use": "purchase_anchor | price_anchor | review_source | competitor_monitoring | context_only | avoid",
      "evidence_refs": [],
      "limitations": []
    }
  ]
}
```

## Local Channel Priority Handoff

S01 must hand off named local channels for the management summary. Do not pass only generic categories such as `local ecommerce`, `retail`, or `DTC` when country-level channel discovery has been run.

```json
{
  "local_channel_priority": [
    {
      "rank": 1,
      "channel_name": "",
      "channel_type": "marketplace | retailer | carrier_operator | price_comparison | dtc | offline_retail | reseller | other",
      "country_or_region": "",
      "role": "price_anchor | conversion_test | trust_builder | launch_inventory | bundle_financing | owned_data | competitor_monitoring | other",
      "priority_score": 0,
      "capacity_or_ability_note": "",
      "reason": "",
      "evidence_status": "verified | likely | user_planned | unverified | blocked",
      "evidence_refs": [],
      "next_action": "",
      "limitations": []
    }
  ]
}
```

Rules:

- Use actual local channel names when evidence exists, including local marketplaces, retail chains, carriers, price comparison sites, or official brand channels.
- If a channel is user-provided but not locally verified, keep the actual user-provided name and mark `evidence_status` as `user_planned` or `unverified`.
- Keep generic channel categories only as `channel_type`, not as the visible management-summary recommendation.
- Include enough reason text for S14 to show why each named channel matters: reach, category fit, competitor presence, trust, conversion readiness, margin or price constraints, and validation need.

## Content And Proof Map

```json
{
  "content_proof_map": [
    {
      "segment_id": "",
      "touchpoint_stage": "",
      "content_format": "expert_review | short_video | long_video | comparison_table | owner_forum_thread | marketplace_review | landing_page | FAQ | certification_proof | return_policy | privacy_proof | demo | other",
      "proof_need": "",
      "best_evidence_source": "",
      "local_language_angle": "",
      "risk_or_claim_constraint": "",
      "evidence_refs": [],
      "confidence": "high | medium | low"
    }
  ]
}
```

## User-Provided Channel Plans

If the user provides planned channels, retailer relationships, creator/KOL history, landing pages, or media plans:

- Store them as `internal_private` or `user_provided_channel_hypothesis`.
- Compare them against local evidence.
- Keep unsupported but strategically required channels as `test` or `monitor`, not `primary`.
- Record missing evidence such as local reviews, competitor presence, purchase friction, or segment reach.
- Do not expose private channel plans in public report sections unless approved.

## Handoff Rules

Downstream handoff should include:

- `segment_channel_touchpoint_map`
- `retailer_marketplace_candidates`
- `local_channel_priority`
- `content_proof_map`
- `channel_fit_scores`
- `channel_touchpoint_evidence_refs`
- `user_provided_channel_hypotheses`
- confidence caps and data gaps

S03 should use proof and content needs for message architecture. S04 should use retailer/marketplace and price-comparison evidence for pricing. S06 may use trusted expert/creator types but should not treat them as final KOL selections. S07/S08 should use channel roles as assumptions, not final allocation.
