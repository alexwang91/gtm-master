# NSS/NPS and Earned Growth Seed

Use this after consumer voice processing has produced deduped source-item classifications, Bain driver inputs, journey episode inputs, and voice theme clusters. It creates the S01 NSS/NPS and Earned Growth seed panel for the market context report.

S01 does not replace a surveyed Net Promoter System. It can summarize uploaded NSS/NPS data, or create a clearly labeled proxy from public/internal voice evidence when confidence gates pass.

## Inputs

```json
{
  "consumer_voice_processing_summary": {},
  "nss_nps_proxy_classification_table": [],
  "bain_driver_inputs": [],
  "journey_episode_inputs": [],
  "voice_theme_clusters": [],
  "segment_seed_pack": [],
  "segment_price_sensitivity_seeds": [],
  "activation_or_return_signals": [],
  "customer_reviews_and_nss_or_nps": "",
  "previous_generation_sales_price_channel_performance": "",
  "internal_customer_voice": ""
}
```

## Core Rules

- Never label inferred proxy as surveyed NSS/NPS.
- Calculate proxy from deduped source items, not voice atom counts.
- Keep surveyed, internal, public, competitor, and previous-generation evidence separated before any blended view.
- If thresholds are not met, output directional driver and journey inputs without calculating proxy NSS/NPS.
- Earned Growth in S01 is a seed/proxy only unless direct repeat, referral, organic, and paid acquisition data is provided.
- Treat NSS/NPS as an operating system input: the score is less important than the drivers, closed-loop actions, root causes, and economics.
- Convert every major promoter/detractor driver into either a product experience diagnosis, a GTM proof need, a sales enablement need, or a data gap.
- Do not expose private NSS/NPS, sales, referral, or channel data in public report sections unless approved.

## Bain Logic Alignment

S01 follows Bain-style Net Promoter logic as an operating loop, not as a vanity score.

1. Classification: sort evidence into promoter-like, passive-like, detractor-like, or unclassified records. Surveyed NSS/NPS uses explicit survey ratings. Proxy NSS/NPS uses deduped source items and must stay labeled as proxy.
2. Diagnosis: extract "why" and "what could be better" signals into driver, journey episode, and root-cause candidates.
3. Inner loop: identify individual or frontline-closeable issues, such as support recovery, setup guidance, delivery/return problems, warranty confusion, retailer misinformation, or first-use friction.
4. Outer loop: identify systemic changes that a frontline team cannot solve alone, such as hardware design, firmware/app reliability, core feature performance, pricing structure, channel policy, claim proof, packaging, warranty terms, or sales training.
5. Economics: connect loyalty signals to repeat, referral, organic/direct discovery, return risk, churn risk, and conversion quality. Without direct financial or attribution data, output readiness signals and data gaps only.
6. Action: every high-impact driver needs an owner hint, evidence refs, confidence, and next action. Do not stop at a score.

## NSS/NPS Seed Panel

```json
{
  "nss_nps_proxy_seed_panel": {
    "panel_status": "surveyed | proxy_calculated | directional_only | not_calculated",
    "nps_type": "surveyed | proxy | blended | unavailable",
    "sample_size_after_dedupe": 0,
    "source_mix": {
      "surveyed_nss_nps": 0,
      "internal_customer_voice": 0,
      "marketplace_reviews": 0,
      "forum_or_comment_sources": 0,
      "app_reviews": 0,
      "social_or_video_comments": 0,
      "competitor_voice": 0
    },
    "classification_counts": {
      "promoter_like": 0,
      "passive_like": 0,
      "detractor_like": 0,
      "unclassified": 0
    },
    "classification_percentages": {
      "promoter_like_pct": 0,
      "passive_like_pct": 0,
      "detractor_like_pct": 0,
      "unclassified_pct": 0
    },
    "nps_proxy_score": 0,
    "proxy_confidence_score": 0,
    "confidence": "high | medium | low",
    "confidence_cap": "high | medium | low | assumption_only",
    "evidence_refs": [],
    "data_gaps": [],
    "limitations": []
  }
}
```

Proxy formula:

```text
NPS proxy = % promoter_like - % detractor_like
```

Only calculate `nps_proxy_score` when the proxy calculation gate in `consumer-voice-nss-bain-pipeline.md` passes.

## Competitor NSS/NPS Comparison Seed

```json
{
  "competitor_nss_nps_comparison_seed": [
    {
      "product_or_competitor": "",
      "competitor_role": "",
      "nps_type": "surveyed | proxy | unavailable",
      "sample_size_after_dedupe": 0,
      "promoter_like_pct": 0,
      "passive_like_pct": 0,
      "detractor_like_pct": 0,
      "nps_proxy_score": 0,
      "top_promoter_drivers": [],
      "top_detractor_drivers": [],
      "confidence": "high | medium | low",
      "evidence_refs": [],
      "limitations": []
    }
  ]
}
```

Use comparison only when competitor source coverage is reasonably comparable. If one competitor has rich reviews and another has only snippets, show confidence differences and do not over-rank.

## NPS Driver Tornado Seed

```json
{
  "nps_driver_tornado_seed": [
    {
      "driver_id": "",
      "driver_name": "",
      "driver_category": "",
      "direction": "promoter_driver | detractor_driver | mixed_driver | context_only",
      "driver_impact_score": 0,
      "frequency": 0,
      "mean_emotion_strength": 0,
      "purchase_or_return_impact": 0,
      "nss_nps_class_mix": {},
      "top_segment_refs": [],
      "journey_episode_refs": [],
      "evidence_refs": [],
      "confidence": "high | medium | low"
    }
  ]
}
```

This is directional driver prioritization, not causal proof.

## Hardware Product Experience Diagnosis Seed

Use this to make NSS/NPS useful for hardware product analysis. It translates promoter/detractor drivers into product, sales, marketing, channel, and service implications.

```json
{
  "hardware_experience_diagnosis_seed": [
    {
      "driver_id": "",
      "driver_name": "",
      "driver_category": "hardware_design | core_performance | battery_power | app_connectivity | setup_onboarding | accuracy_trust | comfort_fit | durability_quality | packaging_delivery | warranty_returns | privacy_data | price_value | channel_availability | after_sales_service | other",
      "product_generation": "current | previous_generation | competitor | substitute | unknown",
      "journey_episodes": [],
      "affected_segments": [],
      "promoter_evidence_refs": [],
      "detractor_evidence_refs": [],
      "source_item_count_after_dedupe": 0,
      "business_impact_hypothesis": "",
      "marketing_and_sales_implication": "",
      "next_generation_relevance": "high | medium | low",
      "owner_hint": "product | industrial_design | firmware | app | operations | support | sales | marketing | channel | compliance | unknown",
      "recommended_action_type": "fix | amplify | prove | educate | monitor | research",
      "outer_loop_opportunity_score": 0,
      "confidence": "high | medium | low",
      "data_gaps": []
    }
  ]
}
```

Hardware diagnosis rules:

- A detractor driver becomes a `fix` candidate when it harms setup, reliability, trust, return risk, warranty confidence, or repeated use.
- A promoter driver becomes an `amplify` or `prove` candidate when it can support positioning, retail sales talk tracks, creator briefs, landing-page proof, or next-generation feature investment.
- A mixed driver becomes an `educate`, `prove`, or `research` candidate when the feature value is real but expectation-setting, proof, or onboarding is weak.
- Previous-generation and competitor evidence should be tagged separately so downstream skills can see whether the next generation is fixing a known weakness, defending an advantage, or entering a new standard.

## Bain Outer Loop Opportunity Score

Use this to rank systemic actions from the hardware diagnosis seed.

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

## Journey Episode NSS Seed

```json
{
  "journey_episode_nss_seed": [
    {
      "episode": "",
      "promoter_signals": [],
      "passive_signals": [],
      "detractor_signals": [],
      "dominant_drivers": [],
      "service_recovery_or_close_loop_need": "",
      "proof_or_education_need": "",
      "evidence_refs": [],
      "confidence": "high | medium | low"
    }
  ]
}
```

## Earned Growth Proxy Seed

S01 should distinguish earned and bought growth only as a seed unless attribution data exists.

```json
{
  "earned_growth_proxy_seed": {
    "status": "calculated | directional_only | not_available",
    "earned_growth_signals": {
      "repeat_purchase_or_renewal": [],
      "referral_or_recommendation": [],
      "organic_search_or_direct": [],
      "community_or_word_of_mouth": [],
      "unpaid_review_or_creator": []
    },
    "bought_growth_signals": {
      "paid_search_or_paid_social": [],
      "discount_or_promo_driven": [],
      "paid_influencer_or_affiliate": [],
      "marketplace_promotion": [],
      "retail_trade_spend": []
    },
    "unclassified_growth_signals": [],
    "earned_growth_readiness_score": 0,
    "earned_vs_bought_interpretation": "",
    "confidence": "high | medium | low",
    "evidence_refs": [],
    "data_gaps": []
  }
}
```

Readiness formula:

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

## Net Promoter System Loop Seed

```json
{
  "net_promoter_system_loop_seed": {
    "inner_loop_candidates": [
      {
        "detractor_driver": "",
        "journey_episode": "",
        "frontline_owner_hint": "",
        "close_loop_action": "",
        "evidence_refs": []
      }
    ],
    "outer_loop_candidates": [
      {
        "systemic_driver": "",
        "root_cause_hypothesis": "",
        "product_or_gtm_owner_hint": "",
        "experiment_or_operating_change": "",
        "evidence_refs": []
      }
    ]
  }
}
```

## Next-Generation Marketing and Sales Recommendation Seed

Use this after the loop seed and hardware diagnosis seed. The goal is to help the next-generation hardware product sell better without overstating evidence.

```json
{
  "next_generation_marketing_sales_seed": {
    "product_opportunities": [
      {
        "opportunity_id": "",
        "source_driver_refs": [],
        "affected_segments": [],
        "recommendation": "",
        "why_it_matters": "",
        "evidence_refs": [],
        "confidence": "high | medium | low",
        "owner_hint": "product | firmware | app | industrial_design | operations",
        "next_step": "fix_in_next_generation | validate_with_test | keep_as_data_gap"
      }
    ],
    "message_opportunities": [
      {
        "opportunity_id": "",
        "source_driver_refs": [],
        "affected_segments": [],
        "recommendation": "",
        "why_it_matters": "",
        "evidence_refs": [],
        "confidence": "high | medium | low",
        "owner_hint": "marketing | brand | content",
        "next_step": "turn_into_message_brief | require_proof_asset | keep_as_data_gap"
      }
    ],
    "sales_enablement_opportunities": [
      {
        "opportunity_id": "",
        "source_driver_refs": [],
        "affected_segments": [],
        "recommendation": "",
        "why_it_matters": "",
        "evidence_refs": [],
        "confidence": "high | medium | low",
        "owner_hint": "sales | retail | marketplace | distributor",
        "next_step": "create_sales_talk_track | train_channel | collect_more_objections"
      }
    ],
    "channel_opportunities": [],
    "service_or_warranty_opportunities": [],
    "proof_assets_needed": [],
    "do_not_claim_or_overpromise": [],
    "recommended_tests": []
  }
}
```

Recommendation rules:

- Product opportunities should come from high-impact detractor fixes, durable promoter strengths, competitor gaps, previous-generation complaints, or return-risk drivers.
- Message opportunities should convert proven promoter drivers into claims only when proof exists; otherwise create `proof_assets_needed`.
- Sales enablement opportunities should address comparison questions, price objections, warranty doubts, setup friction, and retailer or marketplace confusion.
- `do_not_claim_or_overpromise` must include any tempting claim where evidence is weak, local wording is risky, or support/service reality cannot sustain the promise.
- `recommended_tests` should prefer low-cost validation: message test, landing-page proof test, retail objection script test, post-purchase survey, support tag audit, or small NSS follow-up survey.

## Output Summary

```json
{
  "earned_growth_seed_notes": {
    "nss_nps_status": "surveyed | proxy_calculated | directional_only | not_calculated",
    "earned_growth_status": "calculated | directional_only | not_available",
    "top_promoter_drivers": [],
    "top_detractor_drivers": [],
    "top_close_loop_candidates": [],
    "hardware_experience_driver_count": 0,
    "next_generation_recommendation_count": 0,
    "top_product_fix_or_amplify_actions": [],
    "top_marketing_and_sales_actions": [],
    "major_bias_risks": [],
    "blocking_data_gaps": []
  }
}
```

## S01 Handoff Rules

Downstream S02 should use driver and journey signals for JTBD mining. S03 should use marketing and sales recommendations as message/proof seeds, not final copy. S04 should use price-value and objection drivers as pricing inputs. S08 and S11 may use earned growth signals as directional assumptions. S12 may use loop seeds and hardware diagnosis for review/quality feedback after launch. S14 should render proxy status, sample size, source mix, confidence, data gaps, and action seeds prominently.
