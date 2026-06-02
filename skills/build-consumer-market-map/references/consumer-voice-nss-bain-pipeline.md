# Consumer Voice to NSS/Bain Pipeline

Use this after review, forum, comment, app review, social, survey, or internal customer voice evidence has been collected. It turns raw consumer material into reusable voice atoms, theme clusters, NSS/NPS proxy inputs, and Bain-style driver inputs.

The pipeline is a processing layer, not a strategy layer. It should preserve evidence provenance, quantify confidence, and keep surveyed NSS/NPS separate from inferred proxy signals.

## Processing Chain

```text
source item
-> source item record
-> voice atom
-> normalized theme and driver tags
-> deduped voice atom set
-> theme cluster
-> pain / praise / objection / purchase trigger tables
-> NSS/NPS proxy classification inputs
-> Bain driver impact and journey episode inputs
-> handoff refs for S02, S03, S04, S08, S14
```

## Unit Rules

Use clear units so counts are not inflated.

```text
source item
  One review, forum comment, social post, survey answer, support ticket, or app review.

voice atom
  One atomic consumer statement about one driver, objection, need, comparison, price point, trust issue, or journey episode.

theme cluster
  A grouped pattern of semantically similar voice atoms after deduplication and local-language normalization.

driver
  A GTM-relevant root cause or value driver such as comfort, battery, accuracy, app usability, delivery, warranty, subscription, privacy, or price/value.

NSS/NPS proxy classification
  A source-item-level classification, not an atom-level classification, unless the original source item is already atomic.
```

One long comment may create multiple voice atoms, but it should count once for sample-size metrics unless it represents multiple distinct respondents.

## Voice Atom Schema

```json
{
  "voice_atom_id": "",
  "source_item_id": "",
  "evidence_id": "",
  "source_ref": "",
  "site_profile_ref": "",
  "comment_record_ref": "",
  "country_or_region": "",
  "language": "",
  "source_type": "marketplace_review | retailer_review | forum_comment | specialist_media_comment | video_comment | app_review | social_post | survey_response | support_ticket | internal_review | other",
  "speaker_context": "verified_buyer | owner | prospective_buyer | competitor_user | reviewer | forum_user | survey_respondent | internal_customer | support_customer | unknown",
  "product_or_competitor": "",
  "competitor_role_refs": [],
  "raw_statement_policy": "not_stored | short_excerpt | full_text_internal_only",
  "raw_statement": "",
  "translated_statement": "",
  "normalized_local_phrase": "",
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
  "repeat_frequency_signal": 0,
  "evidence_strength": "high | medium | low",
  "dedupe_key": "",
  "usage_permission": "approved_internal | public_context | restricted | unavailable",
  "limitations": []
}
```

## Atomic Extraction Rules

- Split a source item only when it contains separable drivers or decisions.
- Preserve local-language phrasing when it reveals search language, emotional framing, or culturally specific wording.
- Store only short excerpts unless full internal storage is explicitly allowed.
- Do not turn expert-review wording into consumer voice unless the text is a user comment or buyer review.
- Mark uncertain translations or sarcasm as limitations.
- Keep questions and confusion as valid atoms; they often reveal education burden.
- Separate price objection from feature complaint when both appear.
- Separate product quality issues from channel/service problems when possible.

## Deduplication Rules

Deduplicate before frequency-based scoring.

Deduplicate strongly when:

- Same author, same source, same product, same text or near-duplicate.
- Same marketplace review syndicated across retailer pages.
- Same social/video comment copied across platforms.

Do not deduplicate when:

- Different users express the same issue independently.
- The same user reports different journey episodes or drivers.
- A support ticket and public review are linked but represent different operational signals.

Deduplication output:

```json
{
  "dedupe_summary": {
    "source_items_before_dedupe": 0,
    "source_items_after_dedupe": 0,
    "voice_atoms_before_dedupe": 0,
    "voice_atoms_after_dedupe": 0,
    "dedupe_method": "exact | near_duplicate | source_canonicalization | manual_review | mixed",
    "limitations": []
  }
}
```

## TOP1 Competitor And Previous-Generation Deep Dive

For consumer electronics and hardware, S01 should run a focused deep dive after competitor discovery has produced a user-calibrated shortlist.

Deep-dive objects:

```text
TOP1 competitor
  The highest-threat competitor after local visibility, price overlap, review or sales signal, feature overlap, and substitution role are scored.

previous-generation product
  The user's previous-generation product, internal benchmark, or the closest publicly visible predecessor. If unavailable, keep it as a data gap.
```

Full-coverage rule:

```text
"All viewpoints" means all accessible, policy-permitted, in-scope source items inside the confirmed source list, page range, product scope, language scope, and access date.
```

Do not infer missing comments. Deleted comments, login walls, geography restrictions, dynamic-loading failures, unavailable APIs, or platform-policy limits become `voice_collection_coverage_report` gaps.

Required outputs:

```json
{
  "top1_previous_generation_voice_scope": [
    {
      "object_id": "",
      "object_name": "",
      "object_role": "top1_competitor | previous_generation | internal_benchmark",
      "why_selected": "",
      "target_source_types": ["forum_comment", "specialist_media_comment", "video_comment", "retailer_review", "marketplace_review", "internal_review"],
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
      "claim_type_refs": [],
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
  ]
}
```

## Competitive Bain / NPS Proxy Board

When TOP1 competitor, previous-generation, or internal benchmark voice is in
scope, S01 must prepare a comparison board for S14. This board is allowed to be
directional, but it must not call itself surveyed NPS unless the user supplied
surveyed 0-10 NPS/NSS data.

Comparison lanes:

```text
our_product
  Use direct current-product voice only if available. If pre-launch voice is
  absent, show proof agenda and expected objections instead of fake sentiment.

top1_competitor
  Use the confirmed TOP1 competitor source scope and coverage report.

previous_generation_or_internal_benchmark
  Use previous-generation public voice, internal NSS/NPS, or benchmark feedback
  when available. If unavailable, keep as data gap.
```

Required output:

```json
{
  "competitive_bain_voice_board": [
    {
      "lane_id": "",
      "product_or_object_name": "",
      "object_role": "our_product | top1_competitor | previous_generation | internal_benchmark",
      "nss_nps_status": "surveyed | proxy_calculated | directional_only | not_calculated",
      "source_item_count_after_dedupe": 0,
      "source_mix": [],
      "promoter_like_share": "",
      "passive_like_share": "",
      "detractor_like_share": "",
      "proxy_score_if_allowed": "",
      "top_praise_drivers": [],
      "top_pain_drivers": [],
      "purchase_triggers": [],
      "journey_scores": [
        {
          "journey_episode": "purchase | delivery | unboxing | setup_pairing | first_use | first_7_days | app_experience | customer_service | return_warranty | repurchase_referral",
          "score_0_100": 0,
          "direction": "advantage | neutral | risk | unknown",
          "driver_notes": [],
          "evidence_refs": []
        }
      ],
      "direct_comparison_to_our_product": "",
      "marketing_or_sales_implication": "",
      "proof_or_offer_action": "",
      "confidence": "high | medium | low | hypothesis_only",
      "data_gaps": []
    }
  ]
}
```

Board rules:

- Public comments create `NPS Proxy / Bain VOC`, not true NPS.
- If current-product public voice is unavailable before launch, compare TOP1
  and previous-generation voice against the user's fixed product claims,
  proof assets, and expected objections.
- Each lane must show source count, source mix, collection coverage, and
  confidence cap.
- The board must produce at least one local marketing, sales, product-proof, or
  channel implication per high-impact driver.

Hardware journey adaptation should preserve the Bain/NSS/NPS logic while making the journey concrete for physical products:

```text
purchase
delivery
unboxing
setup_pairing
first_use
first_7_days
habit_formation
app_experience
customer_service
return_warranty
repurchase_referral
```

## Theme And Driver Taxonomy

Use category-specific themes, but normalize into stable driver categories so downstream skills can compare products and countries.

Default driver categories:

```text
product.performance
product.design_or_comfort
product.durability
product.battery_or_power
product.accuracy_or_reliability
product.compatibility
app.setup_or_pairing
app.usability
app.insights_or_ai_value
app.subscription_or_paywall
service.delivery
service.support
service.return_or_warranty
price.value_for_money
price.discount_or_promo
price.financing_or_installment
brand.trust_or_reputation
brand.privacy_or_data_safety
channel.availability
claim.proof_or_credibility
ecosystem.lock_in_or_switching
```

## Theme Cluster Schema

```json
{
  "voice_theme_clusters": [
    {
      "cluster_id": "",
      "cluster_name": "",
      "driver_category": "",
      "products_or_competitors": [],
      "atom_refs": [],
      "source_item_count": 0,
      "unique_source_count": 0,
      "sentiment_mix": {
        "positive": 0,
        "neutral": 0,
        "negative": 0,
        "mixed": 0
      },
      "dominant_local_phrases": [],
      "translated_summary": "",
      "pain_intensity_score": 0,
      "praise_strength_score": 0,
      "purchase_impact_score": 0,
      "price_sensitivity_link": "",
      "segment_links": [],
      "evidence_strength": "high | medium | low",
      "confidence_cap": "high | medium | low | assumption_only",
      "limitations": []
    }
  ]
}
```

## NSS/NPS Proxy Classification

Classify source items, not individual atoms, unless the source item is already one atomic statement.

Classification labels:

```text
promoter_like
  Explicit recommendation, strong satisfaction, repurchase/referral intent, or strong preference over alternatives.

passive_like
  Mild satisfaction, mixed but acceptable experience, price/value caveat without rejection, or neutral usage report.

detractor_like
  Explicit non-recommendation, return/refund/switching intent, severe complaint, trust break, or strong regret.

unclassified
  Ambiguous, purely factual, too short, bot-like, expert voice, or no satisfaction/recommendation signal.
```

NSS/NPS proxy record:

```json
{
  "nss_nps_proxy_classification_table": [
    {
      "source_item_id": "",
      "product_or_competitor": "",
      "classification": "promoter_like | passive_like | detractor_like | unclassified",
      "classification_confidence": "high | medium | low",
      "classification_reasons": [],
      "supporting_atom_refs": [],
      "rating_if_present": "",
      "recommendation_language": "",
      "return_or_switching_signal": "",
      "usage_permission": "approved_internal | public_context | restricted | unavailable",
      "limitations": []
    }
  ]
}
```

Proxy calculation gate:

```text
Calculate proxy only if:
  source_item_count_after_dedupe >= selected depth threshold
  and source quality is not low
  and country match is direct or justified
  and promoter/passive/detractor classification clarity is adequate
  and coverage does not rely on one narrow, biased source unless caveated
```

Default depth thresholds:

```yaml
quick:
  do_not_calculate_unless_direct_nss_or_nps_uploaded: true
standard:
  minimum_source_items_after_dedupe: 30
  minimum_distinct_sources: 2
deep:
  minimum_source_items_after_dedupe: 80
  minimum_distinct_sources: 3
```

If thresholds are not met, output `nss_nps_proxy_not_calculated` with the blocking data gaps.

## Bain Driver Impact Inputs

Driver impact is directional in S01. It supports the Bain-style dashboard and downstream operating hypotheses; it is not proof of causal impact.

```text
Driver Impact Score =
  Normalized Frequency * 0.25
+ Mean Emotion Strength * 0.20
+ Purchase or Return Impact * 0.20
+ NSS/NPS Class Weight * 0.15
+ Recency * 0.10
+ Cross-Source Agreement * 0.10
```

NSS/NPS class weights:

```text
promoter_like = positive driver weight
passive_like = low or mixed driver weight
detractor_like = negative driver weight
unclassified = context only
```

Bain driver input schema:

```json
{
  "bain_driver_inputs": [
    {
      "driver_id": "",
      "driver_name": "",
      "driver_category": "",
      "product_or_competitor": "",
      "atom_refs": [],
      "source_item_count": 0,
      "nss_nps_class_mix": {
        "promoter_like": 0,
        "passive_like": 0,
        "detractor_like": 0,
        "unclassified": 0
      },
      "driver_impact_score": 0,
      "direction": "promoter_driver | detractor_driver | mixed_driver | context_only",
      "journey_episode_refs": [],
      "root_cause_hypothesis": "",
      "operating_action_hint": "",
      "confidence": "high | medium | low",
      "limitations": []
    }
  ]
}
```

## Journey Episode Inputs

```json
{
  "journey_episode_inputs": [
    {
      "episode": "discovery | consideration | purchase | delivery | unboxing | setup_pairing | first_use | first_7_days | habit_formation | app_experience | customer_service | return_warranty | repurchase_referral",
      "atom_refs": [],
      "dominant_drivers": [],
      "positive_signals": [],
      "negative_signals": [],
      "dropoff_or_return_risks": [],
      "proof_or_education_needs": [],
      "confidence": "high | medium | low",
      "limitations": []
    }
  ]
}
```

## Output Summary

Always produce a compact processing summary:

```json
{
  "consumer_voice_processing_summary": {
    "source_items_processed": 0,
    "source_items_after_dedupe": 0,
    "voice_atoms_created": 0,
    "voice_atoms_after_dedupe": 0,
    "theme_clusters_created": 0,
    "nss_nps_proxy_status": "surveyed | proxy_calculated | directional_only | not_calculated",
    "bain_driver_inputs_created": 0,
    "journey_episode_inputs_created": 0,
    "top_confidence_caps": [],
    "blocking_data_gaps": []
  }
}
```

## Handoff Rules

Downstream handoffs should include:

- `consumer_voice_processing_summary`
- `voice_atom_refs`
- `voice_theme_clusters`
- `nss_nps_proxy_classification_table` refs or summary
- `bain_driver_inputs`
- `journey_episode_inputs`
- `top1_previous_generation_voice_scope`
- `voice_collection_coverage_report`
- `bain_nss_journey_seed_panel`
- confidence caps and data gaps

Do not include raw text dumps. Use evidence refs and short permitted excerpts only when needed for a specific claim.
