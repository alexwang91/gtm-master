# S01 Added Modules

These modules strengthen the original methodology without removing any existing step.

## Module A: Product-Market Search Preflight

### Purpose

Merge product capability normalization with category selling point comparison and local search-language discovery.

### Why It Matters

A product feature is not automatically a marketable selling point. It becomes useful for GTM only when it connects to a known category reason-to-buy, an emerging demand, a competitor comparison, a local consumer problem, or a locally searched phrase. This module turns product specs into search-ready, evidence-ready hypotheses.

### Inputs

- Product specs and feature list
- Target price range
- Product capability map
- Launch country or region
- Known competitors or category anchors
- Search/trends data when available
- Local-language query results

### Method

First classify capabilities, claims, substitutes, premium justification, commodity features, and risky claims. Then compare those capabilities against mainstream category selling points and local search language.

Use search, SERP discovery, Google Trends-style trend signals, marketplace autocomplete, forum language, review text, and competitor page language where permitted.

Google Trends or third-party trends APIs can help compare relative interest between terms, identify related queries, and detect rising local-language demand. Treat trends data as relative search interest, not absolute demand or purchase intent.

### Output

```json
{
  "product_capability_map": {
    "product_category": "",
    "device_type": "",
    "core_capabilities": [],
    "secondary_capabilities": [],
    "differentiators": [],
    "commodity_features": [],
    "premium_justification_features": [],
    "trust_building_features": [],
    "retention_or_repeat_use_features": [],
    "potential_claims": [],
    "risky_claims": [],
    "likely_substitutes": [],
    "initial_price_band_hypothesis": ""
  },
  "category_selling_point_map": [
    {
      "mainstream_selling_point": "",
      "local_language_terms": [],
      "related_queries": [],
      "rising_queries": [],
      "consumer_intent": "problem_search | comparison | review | price | complaint | buying | learning",
      "our_feature_match": "strong | partial | weak | none",
      "education_required": "low | medium | high",
      "trend_signal": "mainstream | rising | niche | weak | unknown",
      "evidence_refs": [],
      "confidence": "high | medium | low"
    }
  ],
  "feature_to_local_language_map": [
    {
      "product_feature": "",
      "possible_selling_point": "",
      "local_search_terms": [],
      "category_terms": [],
      "competitor_terms": [],
      "complaint_terms": [],
      "trend_signal": "mainstream | rising | niche | weak | unknown",
      "search_intent_notes": ""
    }
  ],
  "selling_point_fit_scores": [
    {
      "selling_point": "",
      "fit_score": 0,
      "category_mainstream_fit": 0,
      "local_search_language_match": 0,
      "product_feature_support": 0,
      "competitor_differentiation": 0,
      "trend_signal_score": 0,
      "proof_availability": 0,
      "education_burden": 0,
      "recommendation": "prioritize_for_evidence_collection | validate_before_using | do_not_lead"
    }
  ],
  "search_query_seed_pack": {
    "category_queries": [],
    "feature_queries": [],
    "competitor_queries": [],
    "complaint_queries": [],
    "price_queries": [],
    "review_queries": [],
    "comparison_queries": [],
    "local_language_queries": []
  }
}
```

### Quantification

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

### Handoff Value

- Improves evidence discovery queries.
- Helps S02 identify JTBD wording.
- Helps S03 avoid messaging that does not match local search language.
- Helps S04 understand which benefits can support premium price.

## Module B: Coverage Map

### Purpose

Record what was searched, what was found, what was unavailable, and how complete the evidence base is.

### Why It Matters

Without coverage tracking, a market map can look confident after shallow research. Coverage Map prevents hidden blind spots.

### Inputs

- Project brief
- MCP routing plan
- Search queries
- Source discovery results
- Failed or blocked sources

### Output

```json
{
  "coverage_map": {
    "country_or_region": "",
    "local_languages_used": [],
    "evidence_categories": [
      {
        "category": "competitors | prices | reviews | social_discussions | channels | market_size | nss_nps | benchmarks",
        "queries_or_sources_checked": [],
        "sources_found": [],
        "sources_unavailable": [],
        "coverage_score": 0,
        "coverage_level": "strong | adequate | thin | missing",
        "limitations": []
      }
    ],
    "overall_coverage_score": 0,
    "priority_gaps": []
  }
}
```

### Quantification

```text
Coverage Score =
  source_type_coverage * 0.30
+ local_language_coverage * 0.20
+ competitor_coverage * 0.20
+ price_coverage * 0.15
+ consumer_voice_coverage * 0.10
+ local_voice_source_coverage * 0.05
```

## Module C: Voice Atom Table

### Purpose

Convert reviews, comments, forum posts, surveys, NSS/NPS notes, and internal customer voice into reusable atomic evidence.

### Why It Matters

Downstream JTBD and messaging skills need consumer language, not just summaries.

Use `consumer-voice-nss-bain-pipeline.md` for the full source-item, atom, dedupe, theme cluster, NSS/NPS proxy, Bain driver, and journey episode contracts.

### Output

```json
{
  "local_voice_source_map": [
    {
      "source_name": "",
      "source_url": "",
      "source_type": "marketplace_review | retailer_review | forum_comment | specialist_media_comment | video_comment | app_review | social_post | survey_response | support_ticket | internal_review | other",
      "country_or_region": "",
      "language": "",
      "covered_products_or_competitors": [],
      "collection_role": "",
      "access_status": "accessible | blocked | login_required | policy_limited | not_checked",
      "evidence_quality": "high | medium | low | hypothesis_only",
      "raw_artifact_ref": "",
      "downstream_use": []
    }
  ],
  "voice_storage_compression_policy": {
    "raw_storage": "Save accessible permitted source items to local MD artifacts with URL, access date, language, product/competitor, and collection coverage.",
    "handoff_rule": "Pass compressed theme clusters, representative permitted excerpts, source refs, sample counts, coverage gaps, and confidence labels downstream; do not pass full raw dumps.",
    "nss_nps_proxy_rule": "Create NSS/NPS proxy seeds only when deduped sample size, source quality, country match, and classification clarity are sufficient."
  },
  "top1_previous_generation_voice_scope": [
    {
      "object_name": "",
      "object_role": "top1_competitor | previous_generation | internal_benchmark",
      "why_selected": "",
      "target_source_types": [],
      "source_scope_refs": [],
      "collection_depth": "quick | standard | real_product_pilot | deep",
      "coverage_status": "complete_within_scope | partial | blocked | not_started",
      "limitations": []
    }
  ],
  "voice_collection_coverage_report": [
    {
      "source_ref": "",
      "object_refs": [],
      "pages_or_threads_expected": 0,
      "pages_or_threads_collected": 0,
      "source_items_expected_if_count_visible": 0,
      "source_items_collected": 0,
      "source_items_after_dedupe": 0,
      "missing_or_blocked_items": [],
      "raw_artifact_ref": "",
      "coverage_confidence": "high | medium | low"
    }
  ],
  "bain_nss_journey_seed_panel": [
    {
      "viewpoint_type": "pain | praise | purchase_trigger | objection | return_risk | comparison | question",
      "driver_category": "",
      "journey_episode": "purchase | unboxing | setup_pairing | first_use | first_7_days | app_experience | customer_service | return_warranty | repurchase_referral",
      "source_item_count": 0,
      "voice_atom_count_after_dedupe": 0,
      "nss_nps_direction": "promoter_like | passive_like | detractor_like | unclassified | mixed",
      "driver_impact_score": 0,
      "hardware_adaptation_note": "",
      "marketing_or_sales_implication": "",
      "confidence": "high | medium | low"
    }
  ],
  "consumer_voice_processing_summary": {
    "source_items_processed": 0,
    "source_items_after_dedupe": 0,
    "voice_atoms_created": 0,
    "voice_atoms_after_dedupe": 0,
    "theme_clusters_created": 0,
    "nss_nps_proxy_status": "surveyed | proxy_calculated | directional_only | not_calculated",
    "bain_driver_inputs_created": 0,
    "journey_episode_inputs_created": 0,
    "blocking_data_gaps": []
  },
  "voice_atoms": [
    {
      "voice_atom_id": "",
      "source_item_id": "",
      "evidence_id": "",
      "country_or_region": "",
      "language": "",
      "source_ref": "",
      "site_profile_ref": "",
      "comment_record_ref": "",
      "source_type": "marketplace_review | retailer_review | forum_comment | specialist_media_comment | video_comment | app_review | social_post | survey_response | support_ticket | internal_review | other",
      "raw_statement": "",
      "translated_statement": "",
      "normalized_local_phrase": "",
      "speaker_context": "verified_buyer | reviewer | forum_user | survey_respondent | internal_customer | unknown",
      "product_or_competitor": "",
      "claim_type": "praise | complaint | objection | comparison | purchase_trigger | return_reason | recommendation | question | workaround | substitute | price_signal | trust_signal | feature_request | other",
      "theme": "",
      "driver": "",
      "driver_category": "product | app | service | price | channel | brand_trust | privacy | claims | setup | delivery | returns | ecosystem | other",
      "journey_episode": "discovery | consideration | purchase | delivery | unboxing | setup_pairing | first_use | first_7_days | habit_formation | app_experience | customer_service | return_warranty | repurchase_referral | unknown",
      "job_or_need_hint": "",
      "pain_point": "",
      "praise_point": "",
      "purchase_trigger": "",
      "objection": "",
      "comparison_target": "",
      "substitute_or_workaround": "",
      "price_or_value_signal": "",
      "sentiment": "positive | neutral | negative | mixed",
      "emotion_strength": 0,
      "purchase_impact": 0,
      "purchase_stage": "awareness | consideration | purchase | onboarding | usage | retention | return",
      "evidence_strength": "high | medium | low",
      "dedupe_key": "",
      "limitations": []
    }
  ],
  "voice_theme_clusters": [],
  "nss_nps_proxy_classification_table": [],
  "bain_driver_inputs": [],
  "journey_episode_inputs": []
}
```

### Quantification

Use `emotion_strength` from 1-5:

```text
1 = weak or passing mention
2 = mild preference or complaint
3 = clear reason, objection, or satisfaction driver
4 = strong purchase/rejection driver
5 = intense repeated driver tied to buy, return, churn, or referral
```

NSS/NPS proxy must classify deduped source items, not raw atom counts. If sample size, source quality, country match, or classification clarity is weak, output directional themes and data gaps instead of a proxy score.

### Source Discovery And Storage Rules

Before creating voice atoms, S01 must identify where the local voice can come from:

```text
local forums and communities
specialist media and review comment areas
video review comments
retailer and marketplace reviews
price comparison comments where available
user-provided private NSS/NPS, support, sales, or previous-generation files
```

For each source, record name, URL, language, access status, collection role, evidence quality, raw artifact ref, and downstream use. Save accessible permitted source items locally as Markdown. Downstream skills receive only compressed clusters, representative permitted excerpts, source refs, sample counts, confidence labels, and data gaps.

### TOP1 Competitor And Previous-Generation Voice Deep Dive

After competitor discovery and user calibration, S01 should lock two objects for deeper consumer-voice work:

```text
1. TOP1 competitor: highest local threat after price overlap, feature overlap, channel visibility, review or sales signal, and substitution role are scored.
2. Previous-generation product: the user's prior model, internal benchmark, or closest public predecessor.
```

For these two objects, collect all accessible, policy-permitted source items inside the confirmed local source scope. Record page or thread ranges, visible comment counts where available, collected source-item counts, dedupe results, raw MD artifact refs, and every blocked or missing reason.

Then split comments into voice atoms and preserve the Bain/NSS/NPS method:

```text
source item -> voice atom -> theme cluster -> pain/praise/purchase trigger/objection -> source-item NSS/NPS proxy -> Bain Driver Impact Score -> hardware journey episode score
```

Hardware journey scoring should make purchase, unboxing, setup or pairing, first use, first 7 days, app experience, support/return, and repurchase/referral visible. This lets S02/S03/S04/S08/S13 use the same voice evidence for JTBD, messaging proof, pricing objections, demand forecast confidence, and validation planning.

## Module D: Competitor Threat Score

### Purpose

Prioritize which competitors or substitutes matter most for GTM decisions.

### Why It Matters

A long competitor list is not enough. Downstream skills need the strongest price anchors, trust anchors, and positioning threats.

### Output

Before final scoring, present 5-10 potential competitors/substitutes for user calibration when review mode allows it.

```json
{
  "competitor_candidate_review_list": [
    {
      "candidate_id": "",
      "brand": "",
      "product": "",
      "competitor_role": "direct | substitute | premium_anchor | budget_anchor | previous_generation | ecosystem_anchor",
      "why_candidate": "",
      "local_evidence_refs": [],
      "initial_threat_hypothesis": "high | medium | low",
      "user_action": "include | exclude | unsure | add_note",
      "user_note": ""
    }
  ],
  "competitor_threat_scores": [
    {
      "brand": "",
      "product": "",
      "competitor_role": "direct | substitute | premium_anchor | budget_anchor | previous_generation | ecosystem_anchor",
      "threat_score": 0,
      "threat_level": "high | medium | low",
      "score_breakdown": {
        "positioning_overlap": 0,
        "price_anchor_strength": 0,
        "price_ladder_pull": 0,
        "channel_presence": 0,
        "review_strength": 0,
        "brand_trust": 0,
        "feature_overlap": 0,
        "switching_barrier": 0
      },
      "why_it_matters": "",
      "evidence_refs": []
    }
  ]
}
```

### Candidate Discovery Score

Use this lighter score before the final threat score. Its job is to produce the 5-10 candidate competitors/substitutes for user calibration, not to declare final competitors.

```text
Candidate Discovery Score =
  Price Band Overlap * 0.25
+ Feature Overlap * 0.20
+ Local Channel Visibility * 0.20
+ Review or Sales Signal * 0.20
+ Substitution Role Fit * 0.15
```

After user calibration, only included or explicitly retained hypotheses move into final competitor threat scoring and downstream handoffs.

### Formula

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

Top competitor rule:

```text
A top competitor must have at least two local evidence signals unless it is explicitly marked as a hypothesis.

Valid local evidence signals:
- appears in local SERP, ranking, review, or comparison pages
- has local marketplace, retailer, or official-channel availability
- has local price evidence
- has local reviews, comments, forum discussion, or social/video discussion
- is mentioned in internal benchmark or user-provided competitor list
```

## Module E: Segment Distinctness Check

### Purpose

Check whether proposed consumer segments are meaningfully different and usable for GTM.

### Why It Matters

AI-generated segments often overlap. Distinctness checks prevent vague personas and conflicting downstream messaging.

Use `segment-persona-inference.md` for the full segment candidate generation, segment evidence strength, segment seed pack, priority ranking, persona card, and handoff contracts.

### Output

```json
{
  "segment_candidate_pool": [],
  "segment_evidence_strength_scores": [],
  "segment_seed_pack": [],
  "segment_priority_ranking": [],
  "segment_distinctness_check": [
    {
      "segment_name": "",
      "overlaps_with": [],
      "distinctness_score": 0,
      "distinctive_motivation": "",
      "distinctive_use_case": "",
      "distinctive_wtp_or_price_behavior": "",
      "distinctive_channel_or_touchpoint": "",
      "merge_or_keep": "keep | merge | split | deprioritize",
      "reason": ""
    }
  ],
  "persona_cards": []
}
```

### Formula

```text
Segment Distinctness Score =
  Motivation Difference * 0.30
+ Use Case Difference * 0.25
+ Price Behavior Difference * 0.15
+ Channel Difference * 0.15
+ Objection / Trust Barrier Difference * 0.15
```

## Module F: Handoff Pack

### Purpose

Compress S01 output into stable downstream inputs so later skills do not reopen the full artifact by default.

### Downstream Handoffs

```text
S01 -> S02 mine-jtbd-scenarios:
  voice_atoms, segment_seed_pack, pain_theme_clusters, purchase_triggers, objections

S01 -> S04 model-price-sensitivity:
  price_anchor_panel, competitor_price_gap_table, price_complaints, affordability_notes

S01 -> S08 forecast-launch-demand:
  tam_sam_som_seed, segment_priority_ranking, channel_touchpoints, conversion_assumptions

S01 -> S14 compose-html-gtm-dashboard:
  html_market_section, chart_data, citations, confidence_badges, data_gap_notes
```

### Output

Use `references/output-contract.md` for the full schema.
