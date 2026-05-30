# Site-Specific Comment Collection Profile

Use this when S01 discovers a high-value local forum, specialist media comment area, deal community, video comment source, marketplace review page, app review source, or public social thread that may contain country-specific consumer voice.

The goal is maximum permitted, auditable coverage from each selected source. Do not claim that every comment on the internet was collected. Claim only the bounded coverage proven by the collection log.

## When To Trigger

Trigger `site_specific_comment_collection` when:

- The source is country-relevant and category-relevant.
- The source contains consumer comments, forum posts, user reviews, Q&A, or public discussion.
- The source covers the main product, a discovered competitor, a substitute, or a previous-generation product.
- The voice evidence is needed for segmentation, JTBD, message proof, price objections, NSS/NPS proxy, or Bain-style driver analysis.
- Access and usage rules allow collection or a safe fallback.

In `quick` mode, discover candidate sources and record them. Do not run deep enumeration unless the user asks or consumer voice is otherwise missing.

## Local Voice Source Discovery

Do not expect the user to provide local forums. Discover them from the country, product category, local-language terms, competitor names, and previous-generation names.

Source families to look for:

```text
specialist_category_forums
specialist_media_comment_threads
local_deal_forums
marketplace_or_retailer_reviews
price_comparison_reviews
video_review_comments
public_social_threads
local_reddit_or_reddit_equivalent
brand_or_support_communities
app_store_reviews
q_and_a_pages
```

Query families:

```text
[local category term] forum/community/discussion
[local category term] review/opinion/experience/problem
[local category term] best/alternative/compare/versus
[competitor] review/opinion/experience/problem
[competitor] forum/community/discussion
[previous generation product] review/opinion/problem
[category] site:[discovered local domain]
[competitor] site:[discovered local domain]
top [category] forums [country]
best [category] review sites [country]
```

Translate the concepts into the target country's real consumer language and script. Keep English variants only when English is useful in that category or country.

## Source Fit Score

Score each candidate before deep collection.

```text
Local Voice Source Fit Score =
  Country Relevance * 0.16
+ Category Relevance * 0.16
+ Consumer Voice Depth * 0.16
+ Product or Competitor Coverage * 0.14
+ Comment Volume Signal * 0.12
+ Recency * 0.08
+ Extractability * 0.08
+ Source Trust * 0.06
+ Local-Language Value * 0.04
- Access or Terms Risk * 0.10
- Spam or Bias Risk * 0.06
```

Interpretation:

```text
80-100 = primary local voice source; profile and collect when allowed
65-79  = secondary local voice source; collect selectively
45-64  = context source; use for vocabulary or leads
0-44   = avoid or log as low value
```

High-scoring sources should be kept in `local_voice_source_map` even if the user later excludes them from analysis.

## Access And Safety Gate

Before extraction, classify the source:

```json
{
  "access_status": "public | approved_private | login_required | paywalled | blocked | terms_restricted | unavailable",
  "collection_mode": "search_snippet | browser_read | allowed_api | permitted_crawl | manual_upload | skip",
  "allowed_export_policy": "voice_atoms_only | short_excerpts | full_text_internal_only | public_quote_allowed | unavailable",
  "pii_policy": "none_expected | redact_handles | redact_personal_data | restricted",
  "rate_limit_or_crawl_notes": []
}
```

Rules:

- Do not bypass login, paywalls, anti-bot controls, or explicit access restrictions.
- Do not use prohibited scraping. If unsure, use browser-readable summaries, allowed APIs, manual upload, or mark the source restricted.
- Do not store personal data unless explicitly needed and approved; redact handles by default when possible.
- Keep full comment bodies out of compressed handoffs and HTML reports.
- Use short excerpts only when they support a specific claim and usage is permitted.

## Site Profile Schema

```json
{
  "site_profile_id": "",
  "source_name": "",
  "source_url": "",
  "country_or_region": "",
  "language": "",
  "source_family": "",
  "source_fit_score": 0,
  "products_or_competitors_covered": [],
  "seed_urls": [],
  "discovered_threads": [
    {
      "thread_id": "",
      "thread_title": "",
      "canonical_url": "",
      "product_or_competitor": "",
      "thread_type": "forum_thread | review_comments | marketplace_reviews | video_comments | social_thread | q_and_a | app_reviews",
      "estimated_comment_count": 0,
      "date_range": "",
      "relevance_score": 0
    }
  ],
  "pagination_patterns": [],
  "access_and_safety_gate": {},
  "collection_plan": {},
  "limitations": []
}
```

## Thread Discovery

For each selected source:

1. Search within the site for product, competitor, previous-generation, category, complaint, and alternative terms.
2. Canonicalize URLs and merge duplicate threads or redirected URLs.
3. Separate product review pages from long discussion threads.
4. Keep previous-generation and substitute threads when they affect price anchors, complaints, or switching behavior.
5. Record high-value threads that cannot be accessed as failed sources, not as missing evidence.

## Pagination Enumeration

Enumerate all accessible pages for each selected thread or comment area.

Detect:

```text
next/previous links
numeric page links
comment range URLs
cursor or continuation URLs
load-more patterns
visible floor numbers or comment IDs
date-based archive pages
```

Record:

```json
{
  "thread_id": "",
  "pagination_type": "numeric_pages | comment_ranges | cursor | load_more | date_archive | single_page | unknown",
  "expected_pages": 0,
  "visited_pages": [],
  "expected_comment_id_or_floor_ranges": [],
  "observed_comment_id_or_floor_ranges": [],
  "missing_ranges": [],
  "blocked_pages": [],
  "enumeration_confidence": "high | medium | low",
  "bounded_by": "site_reported_total | visible_page_count | discovered_links | unknown"
}
```

If the source uses a pattern like comment range pages, enumerate ranges rather than sampling only the first page.

## Comment Extraction Schema

```json
{
  "comment_record_id": "",
  "site_profile_id": "",
  "thread_id": "",
  "page_url": "",
  "product_or_competitor": "",
  "comment_id_or_floor": "",
  "posted_at": "",
  "author_handle_redacted": "",
  "language": "",
  "raw_text_policy": "not_stored | short_excerpt | full_text_internal_only",
  "raw_excerpt": "",
  "translated_excerpt": "",
  "reply_to_comment_id": "",
  "quoted_comment_ids": [],
  "rating_or_reaction": "",
  "purchase_stage": "awareness | consideration | purchase | onboarding | usage | retention | support | return | unknown",
  "voice_atom_ids": [],
  "usage_permission": "approved_internal | public_context | restricted | unavailable",
  "pii_status": "none | redacted | restricted",
  "limitations": []
}
```

## Completeness Audit

Always output a collection coverage report. This is what prevents "I got everything" from becoming a vague claim.

```text
Comment Collection Coverage Score =
  Visited Expected Pages * 0.30
+ Observed Expected Comment IDs or Floors * 0.25
+ Duplicate Control * 0.15
+ Extraction Success Rate * 0.15
+ Metadata Completeness * 0.10
+ Access Safety * 0.05
```

Interpretation:

```text
85-100 = strong bounded coverage
70-84  = adequate bounded coverage
40-69  = thin coverage; use cautiously
0-39   = missing or failed coverage
```

If the site does not expose total pages or comment counts, set `bounded_by` to the strongest observable boundary and lower enumeration confidence.

## Export Artifacts

Recommended outputs:

```text
runs/<project_id>/evidence/site_profiles.jsonl
runs/<project_id>/evidence/comment_records.jsonl
runs/<project_id>/evidence/voice_atoms.jsonl
runs/<project_id>/logs/comment_collection_log.jsonl
runs/<project_id>/artifacts/comment_exports/<source>/<thread>/comments_index.md
runs/<project_id>/artifacts/comment_exports/<source>/<thread>/comments_allowed_excerpts.md
runs/<project_id>/artifacts/comment_exports/<source>/<thread>/comments_full_internal.md
runs/<project_id>/artifacts/comment_exports/<source>/<thread>/comment_coverage_report.json
runs/<project_id>/artifacts/comment_exports/<source>/<thread>/nss_bain_inputs.json
```

Default:

- Create `comments_index.md` with source links, thread metadata, counts, and evidence IDs.
- Create `comments_allowed_excerpts.md` only when short excerpt storage is allowed.
- Create `comments_full_internal.md` only when full-text internal storage is permitted and useful.
- Always create `voice_atoms.jsonl`, `comment_collection_log.jsonl`, and `comment_coverage_report.json`.

## NSS/NPS And Bain Inputs

Use `consumer-voice-nss-bain-pipeline.md` before calculating proxy outputs or driver tables. Do not label public comment inference as surveyed NPS.

Convert comments into proxy inputs:

```json
{
  "nss_bain_inputs": {
    "source_profile_ref": "",
    "sample_size": 0,
    "source_mix": [],
    "time_period": "",
    "nps_proxy_classification_counts": {
      "promoter_like": 0,
      "passive_like": 0,
      "detractor_like": 0,
      "unclassified": 0
    },
    "driver_frequency_table": [],
    "journey_episode_table": [],
    "price_objection_table": [],
    "switching_or_return_intent_table": [],
    "confidence": "high | medium | low",
    "bias_risks": [],
    "coverage_report_ref": ""
  }
}
```

Classify proxy sentiment with recommendation language, repurchase intent, switching intent, refund/return intent, complaint severity, rating if present, and repeated driver patterns.

## Handoff Rule

Downstream skills receive:

- Source profile IDs
- Comment coverage report refs
- Voice atom refs
- NSS/Bain input refs
- Short summary of dominant themes, objections, and vocabulary
- Data gaps and confidence caps

Downstream skills do not receive raw comment dumps by default.
