# Evidence Storage Policy

Use this policy whenever S01 collects, reads, stores, or hands off evidence.

## Core Rule

Store structured evidence records, not uncontrolled raw web dumps.

Every material claim should point to one or more `evidence_id` values. Handoff packs should reference evidence IDs, not paste long source text.

Use three layers:

```text
structured evidence store
  Canonical fact source for audit, citations, confidence, and source provenance.

rag index manifest
  Retrieval layer for long evidence sets, voice atoms, and artifact sections.

compressed collection summary
  Short context for downstream handoff.
```

Default downstream flow:

```text
handoff pack first
-> RAG retrieval if the handoff is insufficient
-> evidence ledger or full artifact for audit/escalation
```

## Source Categories

```text
public_search
  Search results, SERP snippets, related queries, trends signals, autocomplete.

public_page
  Official pages, competitor pages, expert reviews, media pages, forums.

marketplace_retail
  Retailer pages, marketplace listings, prices, ratings, reviews, discount signals.

consumer_voice
  Public reviews, comments, forum posts, NSS/NPS notes, survey text, user complaints.

internal_private
  User-uploaded product specs, previous-generation sales, channels, brand docs, benchmarks, ads, KOL briefs, landing pages, customer voice.

unavailable_or_blocked
  Sources that were searched but inaccessible, prohibited, login-gated, paywalled, rate-limited, or not found.
```

## Recommended Run Directory

When a local run folder is available, use:

```text
runs/
  <project_id>/
    project_brief.json
    evidence/
      evidence_ledger.jsonl
      competitor_evidence.jsonl
      price_evidence.jsonl
      review_evidence.jsonl
      voice_atoms.jsonl
      site_profiles.jsonl
      comment_records.jsonl
      market_size_evidence.jsonl
      voice_theme_clusters.jsonl
      nss_nps_proxy_classification.jsonl
      bain_driver_inputs.jsonl
      journey_episode_inputs.jsonl
      market_size_evidence.jsonl
      tam_sam_som_assumption_tree.jsonl
      segment_level_tam_sam_som.jsonl
      comparable_market_proxies.jsonl
      market_sizing_confidence.json
      segment_candidate_pool.jsonl
      segment_evidence_strength_scores.jsonl
      segment_seed_pack.jsonl
      persona_cards.jsonl
      channel_touchpoint_evidence.jsonl
      segment_channel_touchpoint_map.jsonl
      retailer_marketplace_candidates.jsonl
      content_proof_map.jsonl
      channel_fit_scores.jsonl
      local_price_corridor.json
      price_anchor_panel.json
      competitor_price_gap_table.jsonl
      segment_price_sensitivity_seeds.jsonl
      value_proof_requirement_matrix.jsonl
      promotion_subscription_sensitivity_seed.jsonl
      nss_nps_proxy_seed_panel.json
      competitor_nss_nps_comparison_seed.jsonl
      nps_driver_tornado_seed.jsonl
      journey_episode_nss_seed.jsonl
      earned_growth_proxy_seed.json
      net_promoter_system_loop_seed.json
      hardware_experience_diagnosis_seed.jsonl
      next_generation_marketing_sales_seed.json
      internal_private_evidence.jsonl
      source_quality_scores.jsonl
      compressed_collection_summary.json
    logs/
      search_and_screening_log.jsonl
      collection_jobs.jsonl
      comment_collection_log.jsonl
      failed_sources.jsonl
      context_escalations.jsonl
    indexes/
      rag_index_manifest.json
    artifacts/
      s01_full_artifact.md
      s01_handoff_pack.json
      s01_html_section.json
      comment_exports/
    report/
      report_state.json
```

If the runtime cannot write files, still produce these objects in the response or current artifact bundle and keep the same names.

## Evidence Ledger Record

```json
{
  "evidence_id": "",
  "source_category": "public_search | public_page | marketplace_retail | consumer_voice | internal_private | unavailable_or_blocked",
  "evidence_type": "competitor | price | review | voice_atom | site_profile | comment_record | comment_coverage_report | nss_bain_input | trend_signal | market_size | channel | creative | internal_benchmark | other",
  "country_or_region": "",
  "language": "",
  "source_name": "",
  "source_url_or_path": "",
  "source_type": "",
  "collected_at": "",
  "connector_slot": "",
  "tool_or_connector_used": "",
  "raw_excerpt_or_value": "",
  "translated_excerpt": "",
  "structured_fields": {},
  "claim_supported": "",
  "confidence": "high | medium | low",
  "limitations": [],
  "pii_status": "none | redacted | restricted",
  "usage_permission": "approved_internal | public_context | restricted | unavailable"
}
```

## RAG Index Manifest

Create a manifest when evidence volume is too large for direct context or when downstream skills may need targeted recall.

```json
{
  "rag_index_manifest": {
    "project_id": "",
    "created_at": "",
    "indexed_collections": [
      {
        "collection_id": "public_competitor_evidence",
        "source_files": [],
        "record_count": 0,
        "allowed_use": "public_context",
        "metadata_fields": [
          "evidence_id",
          "source_category",
          "evidence_type",
          "country_or_region",
          "language",
          "source_quality_score",
          "confidence",
          "usage_permission"
        ]
      }
    ],
    "embedding_policy": {
      "index_short_excerpts_only": true,
      "index_private_evidence_separately": true,
      "do_not_index_raw_html": true,
      "do_not_mix_private_and_public_collections": true
    },
    "retrieval_policy": {
      "default_top_k": 8,
      "prefer_evidence_ids_from_handoff": true,
      "filter_by_country_or_region": true,
      "filter_by_allowed_use": true,
      "rerank_by_source_quality": true
    }
  }
}
```

Recommended collections:

```text
public_competitor_evidence
public_price_evidence
public_review_voice_atoms
public_comment_voice_atoms
public_voice_theme_clusters
public_bain_driver_inputs
public_segment_seed_pack
public_channel_touchpoints
public_price_sensitivity_seed
public_nss_earned_growth_seed
public_site_profiles
public_market_size_sources
public_market_sizing_seed
public_channel_touchpoint_sources
internal_private_evidence
artifact_sections
```

## Compressed Collection Summary

Generate a short summary for handoff and report state.

```json
{
  "compressed_collection_summary": {
    "source_counts": {
      "public_search": 0,
      "public_page": 0,
      "marketplace_retail": 0,
      "consumer_voice": 0,
      "internal_private": 0,
      "unavailable_or_blocked": 0
    },
    "top_evidence_refs": [],
    "comment_collection_summary": {
      "site_profiles": 0,
      "threads_profiled": 0,
      "comment_records": 0,
      "voice_atoms_from_comments": 0,
      "coverage_report_refs": []
    },
    "consumer_voice_processing_summary": {
      "source_items_processed": 0,
      "voice_atoms_created": 0,
      "theme_clusters_created": 0,
      "nss_nps_proxy_status": "",
      "bain_driver_inputs_created": 0
    },
    "segment_inference_summary": {
      "segment_candidates": 0,
      "segment_seeds_promoted": 0,
      "weak_hypothesis_segments": 0,
      "persona_cards": 0
    },
    "channel_touchpoint_summary": {
      "touchpoint_records": 0,
      "segment_channel_maps": 0,
      "retailer_marketplace_candidates": 0,
      "content_proof_items": 0,
      "user_provided_channel_hypotheses": 0
    },
    "price_sensitivity_seed_summary": {
      "local_price_anchors": 0,
      "competitor_price_gap_records": 0,
      "segment_price_sensitivity_seeds": 0,
      "value_proof_requirements": 0,
      "user_provided_price_hypotheses": 0
    },
    "market_sizing_summary": {
      "market_size_evidence_records": 0,
      "assumptions": 0,
      "segment_level_estimates": 0,
      "comparable_market_proxies": 0,
      "confidence": ""
    },
    "nss_earned_growth_summary": {
      "nss_nps_status": "",
      "sample_size_after_dedupe": 0,
      "driver_seed_records": 0,
      "journey_episode_seed_records": 0,
      "earned_growth_status": "",
      "hardware_experience_diagnosis_records": 0,
      "next_generation_recommendation_records": 0
    },
    "coverage_summary": {},
    "highest_confidence_sources": [],
    "lowest_confidence_or_risky_sources": [],
    "private_evidence_used": false,
    "data_gaps": [],
    "rag_index_manifest_ref": ""
  }
}
```

## Storage Rules

- Save source URL or file path, source name, collection time, connector slot, and confidence for every evidence record.
- Save short excerpts only when they support a specific claim.
- Preserve local-language wording for consumer voice when useful, but keep excerpts short.
- Do not save full raw HTML by default.
- Save clean text, structured fields, or extracted tables instead of raw pages.
- Save raw HTML only when needed for extraction debugging and mark it as untrusted, temporary, and not for downstream handoff.
- Keep private uploaded evidence in `internal_private_evidence.jsonl` or an equivalent separated section.
- Do not mix private evidence into public-facing report sections unless the user approves.
- Redact PII before storage.
- Record blocked, unavailable, or prohibited sources in `failed_sources.jsonl`.

## Comment Export Rules

For site-specific forums, communities, review comments, and public discussion sources, use the profile in `site-specific-comment-collection.md`.

Default storage:

```text
site_profiles.jsonl
comment_records.jsonl
voice_atoms.jsonl
comment_collection_log.jsonl
comment_coverage_report.json
comments_index.md
nss_bain_inputs.json
```

Export policy:

- Create `comments_index.md` with thread URLs, counts, evidence IDs, coverage status, and limitations.
- Create `comments_allowed_excerpts.md` only when short excerpts are permitted and useful.
- Create `comments_full_internal.md` only when full-text internal storage is allowed, approved, and necessary for audit or later analysis.
- Never include full comment archives in compressed handoffs or public HTML sections.
- If usage permission is restricted, store only metadata, structured voice atoms without quote text, and source refs.
- If pagination or comment IDs are incomplete, store the gap in `comment_coverage_report.json` before using the source for NSS/NPS proxy or Bain driver analysis.

## Consumer Voice Processing Storage

Use `consumer-voice-nss-bain-pipeline.md` when converting consumer material into reusable analysis records.

Recommended files:

```text
voice_atoms.jsonl
voice_theme_clusters.jsonl
nss_nps_proxy_classification.jsonl
bain_driver_inputs.jsonl
journey_episode_inputs.jsonl
segment_candidate_pool.jsonl
segment_evidence_strength_scores.jsonl
segment_seed_pack.jsonl
persona_cards.jsonl
compressed_collection_summary.json
```

Rules:

- Count NSS/NPS proxy at the deduped source-item level, not by raw atom count.
- Store theme clusters and Bain driver inputs as derived records that point back to atom refs and evidence refs.
- Keep private customer voice classifications separated from public classifications unless the user approves blended internal analysis.
- Store confidence caps and blocking gaps with the derived records.

## Market Sizing Storage

Use `market-sizing-tam-sam-som-seed.md` when generating TAM/SAM/SOM seed outputs.

Recommended files:

```text
market_size_evidence.jsonl
tam_sam_som_seed.json
tam_sam_som_assumption_tree.jsonl
segment_level_tam_sam_som.jsonl
comparable_market_proxies.jsonl
market_sizing_confidence.json
```

Rules:

- Store ranges and assumption records, not single-point false precision.
- Store internal previous-generation sales and retailer forecasts separately unless public use is approved.
- Label marketplace ranking, search interest, and social buzz as weak proxies, not direct market size.
- Every estimate should point to evidence refs, assumption refs, or explicit data gaps.

## Segment Inference Storage

Use `segment-persona-inference.md` when generating segment candidates, segment seed packs, segment priority rankings, and persona cards.

Rules:

- Store segment candidates separately from promoted segment seeds.
- Keep weak but commercially relevant hypotheses with data gaps instead of silently deleting them.
- Persona cards should point to segment IDs, evidence refs, and assumption refs.
- Do not store persona backstory that is not decision-relevant.

## Channel Touchpoint Storage

Use `channel-touchpoint-mapping.md` when generating channel and touchpoint outputs.

Recommended files:

```text
channel_touchpoint_evidence.jsonl
segment_channel_touchpoint_map.jsonl
retailer_marketplace_candidates.jsonl
content_proof_map.jsonl
channel_fit_scores.jsonl
```

Rules:

- Store user-provided channel plans as hypotheses or internal private evidence.
- Separate public channel evidence from private planned-channel notes.
- Keep creator/expert types separate from final KOL selection.
- Channel fit scores must point back to evidence refs or explicit assumptions.

## Price Sensitivity Seed Storage

Use `price-anchor-sensitivity-seed.md` when generating price seed outputs.

Recommended files:

```text
local_price_corridor.json
price_anchor_panel.json
competitor_price_gap_table.jsonl
segment_price_sensitivity_seeds.jsonl
value_proof_requirement_matrix.jsonl
promotion_subscription_sensitivity_seed.jsonl
```

Rules:

- Store user target price and internal price assumptions as hypotheses or internal private evidence.
- Keep private margin, channel terms, and discount rules out of public report sections unless approved.
- Price seed outputs must point to local price evidence, voice evidence, or explicit assumptions.
- Do not store S01 price seed as final pricing recommendation.

## NSS/NPS and Earned Growth Seed Storage

Use `nss-nps-earned-growth-seed.md` when generating NSS/NPS and Earned Growth seed outputs.

Recommended files:

```text
nss_nps_proxy_seed_panel.json
competitor_nss_nps_comparison_seed.jsonl
nps_driver_tornado_seed.jsonl
journey_episode_nss_seed.jsonl
earned_growth_proxy_seed.json
net_promoter_system_loop_seed.json
hardware_experience_diagnosis_seed.jsonl
next_generation_marketing_sales_seed.json
```

Rules:

- Store surveyed NSS/NPS separately from proxy classifications.
- Store proxy sample size after deduplication.
- Keep private NSS/NPS, sales, referral, and attribution data out of public reports unless approved.
- Earned growth seed outputs must be labeled `calculated`, `directional_only`, or `not_available`.
- Store hardware diagnosis records as action seeds with owner hints, evidence refs, confidence, and data gaps.
- Store next-generation marketing and sales recommendations as hypotheses until downstream skills validate message, pricing, channel, or forecast impact.

## Private Evidence Rules

Private files can be high-value evidence, but they require stricter handling.

For each private file, record:

```json
{
  "file_ref": "",
  "file_type": "",
  "evidence_value": "",
  "allowed_use": "internal_analysis_only | public_report_allowed | ask_before_public_use",
  "sensitive_fields": [],
  "derived_evidence_ids": []
}
```

Default private-file policy:

```text
Use for internal analysis.
Do not quote directly in public-facing report.
Do not expose raw sales, channel, benchmark, or customer data unless explicitly approved.
```

## Handoff Rules

Compressed handoff packs may include:

- Evidence IDs
- Short finding summaries
- Confidence levels
- Data gap notes
- Source category labels
- RAG collection IDs or manifest refs when targeted retrieval may be needed

Compressed handoff packs should not include:

- Full source text
- Raw HTML
- Private commercial details not needed downstream
- Personal data
- Long consumer quote dumps

## RAG Use Rules

Use RAG for targeted recall, not as the source of truth.

Allowed RAG uses:

- Retrieve voice atoms for a downstream JTBD or messaging question.
- Retrieve price evidence for a pricing detail not included in the handoff.
- Retrieve competitor evidence when a downstream skill needs source-level proof.
- Retrieve public artifact sections for final HTML citations.

Disallowed RAG uses:

- Mixing private and public evidence without explicit filtering.
- Treating retrieved text as verified without checking evidence metadata.
- Retrieving raw HTML.
- Using low-confidence evidence as if it were primary evidence.
- Replacing the evidence ledger with vector retrieval.

## Failed Source Record

```json
{
  "failed_source_id": "",
  "evidence_need": "",
  "query_or_source": "",
  "source_category": "",
  "reason": "not_found | blocked | login_required | paywalled | terms_restricted | rate_limited | low_relevance | stale | other",
  "attempted_at": "",
  "fallback_used": "",
  "impact_on_confidence": "none | low | medium | high"
}
```

## Data Retention Notes

This skill defines the artifact structure, not legal retention policy. When company policy exists, follow it. When uncertain, minimize stored private or personal data and preserve only structured evidence needed for the GTM decision.
