# MCP_CONNECTORS.md

## Purpose

This file defines the MCP connector layer used by `build-consumer-market-map`.

The main skill decides what evidence is needed.
This file decides which MCP connector should be used, how it should be routed, and what compliance rules apply.

---

## Design Principle

Use the least invasive tool that can answer the research question.

Default priority:

```text
Official API / internal approved data
  ↓
Search / SERP discovery
  ↓
Public page extraction
  ↓
Structured scraping
  ↓
Browser automation
  ↓
Large-scale web data provider
  ↓
Manual upload
  ↓
Assumption-based analysis with clear data gaps
```

Do not use browser automation or large-scale crawling when a simple search or official API is enough.

---

## Connector Capability Classes

```yaml
capability_classes:
  web_search:
    description: Discover sources, competitors, local keywords, market pages, forum threads, and public references.

  serp_search:
    description: Geo-targeted search result collection for local competitor, price, review, and channel discovery.

  browser_automation:
    description: Interact with public pages requiring JavaScript rendering, filters, dropdowns, pagination, screenshots, or navigation.

  web_scraping:
    description: Extract public webpage content into markdown, text, tables, or JSON.

  structured_extraction:
    description: Convert unstructured public pages into structured product, price, review, rating, or competitor tables.

  marketplace_review_mining:
    description: Collect and normalize public product reviews from local marketplaces or retailers where permitted.

  social_listening:
    description: Discover and summarize public consumer discussions, social posts, comments, themes, sentiment, and creator mentions where permitted.

  video_comment_mining:
    description: Extract public comments and engagement signals from video platforms where permitted.

  site_specific_comment_collection:
    description: Profile and collect permitted public comments from high-value country-specific forums, specialist media comment areas, deal communities, review pages, Q&A pages, and similar sources with pagination and coverage audit.

  app_store_review_mining:
    description: Collect public app ratings and reviews for companion apps and competitor apps.

  price_monitoring:
    description: Track local retail prices, discounts, historical lows, promo floors, subscriptions, bundles, and channel price differences.

  competitor_discovery:
    description: Identify direct competitors, substitutes, premium anchors, budget anchors, and category bestsellers.

  translation_and_local_language_processing:
    description: Generate local-language queries, preserve original consumer wording, translate evidence, and cluster themes.

  internal_sales_data_access:
    description: Read approved internal sales, previous-generation product, order, revenue, channel, and sell-through data.

  internal_review_data_access:
    description: Read approved internal reviews, ratings, NPS surveys, return reasons, and product feedback.

  internal_support_data_access:
    description: Read approved support tickets, complaint categories, RMA reasons, warranty claims, and customer service notes.

  internal_app_analytics_access:
    description: Read approved activation, retention, feature usage, subscription, churn, and app funnel data.
```

---

## Connector Registry Schema

```yaml
connectors:
  - id: example_search_mcp
    display_name: Example Search MCP
    provider_type: search_research
    capability_classes:
      - web_search
      - serp_search
      - competitor_discovery
    enabled: false
    trust_level: medium
    data_scope: public_only
    allowed_source_types:
      - search_results
      - public_web_pages
    allowed_countries:
      - "*"
    allowed_languages:
      - "*"
    requires_api_key: true
    credential_location: env
    credential_env_vars:
      - EXAMPLE_SEARCH_API_KEY
    output_formats:
      - json
      - markdown
    cost_model: usage_based
    rate_limits: "configured_by_provider"
    pii_policy: exclude
    data_retention_policy: no_raw_personal_data_storage
    best_for:
      - broad competitor discovery
      - local source discovery
      - local query expansion
    avoid_for:
      - private data
      - authenticated content
      - large-scale review crawling
    fallback_connector_ids:
      - example_web_scrape_mcp
```

---

## Connector Slots

```yaml
connector_slots:
  primary_search:
    required_capabilities:
      - web_search
      - serp_search
    purpose: Discover local sources, competitors, substitutes, local keywords, and category pages.

  primary_web_extractor:
    required_capabilities:
      - web_scraping
      - structured_extraction
    purpose: Extract clean public page content, product tables, prices, review snippets, and comparison pages.

  browser_automation:
    required_capabilities:
      - browser_automation
    purpose: Navigate public pages requiring JavaScript rendering, filters, pagination, or screenshots.

  marketplace_reviews:
    required_capabilities:
      - marketplace_review_mining
      - structured_extraction
    purpose: Collect permitted public reviews, ratings, text, dates, variants, and verified-buyer indicators.

  social_listening:
    required_capabilities:
      - social_listening
      - video_comment_mining
    purpose: Discover public consumer discussion themes, creator mentions, sentiment, complaints, and objections.

  site_specific_comment_collection:
    required_capabilities:
      - web_search
      - web_scraping
      - structured_extraction
      - browser_automation
      - site_specific_comment_collection
    purpose: Profile high-value local forums or comment sources, enumerate permitted pages, extract structured comment records, and create coverage reports.

  app_store_reviews:
    required_capabilities:
      - app_store_review_mining
    purpose: Analyze companion app and competitor app ratings, complaints, churn drivers, and UX issues.

  price_intelligence:
    required_capabilities:
      - price_monitoring
      - competitor_discovery
    purpose: Build local price corridor, promo floor, discount range, subscriptions, bundles, and competitor price anchors.

  internal_sales:
    required_capabilities:
      - internal_sales_data_access
    purpose: Read previous-generation sales, revenue, price, discount, channel, and sell-through data.

  internal_customer_voice:
    required_capabilities:
      - internal_review_data_access
      - internal_support_data_access
    purpose: Read internal reviews, return reasons, complaints, NPS surveys, RMA reasons, and support tickets.

  internal_app_analytics:
    required_capabilities:
      - internal_app_analytics_access
    purpose: Read activation, retention, subscription, churn, and feature-usage data.
```

---

## Research Job Types

### Competitor Discovery

```yaml
job_type: competitor_discovery
purpose: Identify local direct competitors, substitutes, premium anchors, budget anchors, and bestsellers.
required_inputs:
  - product_category
  - target_country_or_region
  - target_price_range
preferred_connector_slots:
  - primary_search
  - price_intelligence
  - primary_web_extractor
outputs:
  - competitor_list
  - substitute_list
  - price_anchor_table
  - bestseller_table
  - evidence_log
```

### Local Review Mining

```yaml
job_type: local_review_mining
purpose: Extract consumer praise, complaints, ratings, price objections, feature confusion, and return signals.
required_inputs:
  - competitor_list
  - substitute_list
  - target_country_or_region
preferred_connector_slots:
  - marketplace_reviews
  - primary_web_extractor
  - browser_automation
outputs:
  - review_dataset
  - sentiment_table
  - pain_point_clusters
  - nps_proxy_inputs
  - evidence_log
```

### Social Listening

```yaml
job_type: social_listening
purpose: Find local consumer language, objections, creator influence, discussion themes, and category narratives.
required_inputs:
  - product_category
  - target_country_or_region
  - local_language_queries
preferred_connector_slots:
  - social_listening
  - video_comment_mining
  - primary_search
outputs:
  - consumer_language_map
  - theme_clusters
  - channel_touchpoints
  - influencer_type_map
  - evidence_log
```

### Site-Specific Comment Collection

```yaml
job_type: site_specific_comment_collection
purpose: Profile and collect permitted comments from high-value local forums, specialist media comments, deal communities, review pages, video comments, app reviews, Q&A pages, or public social threads.
required_inputs:
  - local_voice_source_map
  - product_or_competitor_terms
  - target_country_or_region
  - access_and_usage_policy
preferred_connector_slots:
  - site_specific_comment_collection
  - primary_web_extractor
  - browser_automation
fallback_connector_slots:
  - primary_search
  - manual_upload
outputs:
  - site_specific_comment_profiles
  - comment_records
  - voice_atoms
  - comment_collection_coverage_reports
  - nss_bain_inputs
  - failed_sources
```

### Price Intelligence

```yaml
job_type: price_intelligence
purpose: Build local price corridor, promo floor, competitor price gaps, subscription pricing, and discount norms.
required_inputs:
  - product_category
  - competitor_list
  - target_country_or_region
  - target_price_range
preferred_connector_slots:
  - price_intelligence
  - primary_search
  - primary_web_extractor
outputs:
  - local_price_corridor
  - competitor_price_gap_table
  - promo_floor_estimate
  - subscription_price_range
  - price_sensitivity_inputs
  - evidence_log
```

---

## Routing Rules

```yaml
routing_rules:
  - condition: "need_source_discovery == true"
    use_slots:
      - primary_search
    fallback_slots:
      - primary_web_extractor

  - condition: "need_competitor_prices == true"
    use_slots:
      - price_intelligence
      - primary_search
    fallback_slots:
      - primary_web_extractor
      - browser_automation

  - condition: "need_marketplace_reviews == true"
    use_slots:
      - marketplace_reviews
    fallback_slots:
      - primary_web_extractor
      - browser_automation
      - primary_search

  - condition: "page_requires_js_or_pagination == true"
    use_slots:
      - browser_automation
    fallback_slots:
      - primary_web_extractor

  - condition: "need_social_discussions == true"
    use_slots:
      - social_listening
      - video_comment_mining
    fallback_slots:
      - primary_search

  - condition: "need_site_specific_comment_collection == true"
    use_slots:
      - site_specific_comment_collection
      - primary_web_extractor
      - browser_automation
    fallback_slots:
      - primary_search
      - manual_upload

  - condition: "need_internal_previous_generation_data == true"
    use_slots:
      - internal_sales
      - internal_customer_voice
      - internal_app_analytics
    fallback_slots:
      - manual_upload

  - condition: "source_access_blocked_or_terms_prohibit_collection == true"
    action: "skip_source_and_record_limitation"
    fallback_slots:
      - primary_search
      - alternative_public_source
```

---

## Evidence Schemas

### Competitor Evidence

```json
{
  "evidence_type": "competitor",
  "brand": "",
  "product": "",
  "country": "",
  "source_name": "",
  "source_url": "",
  "price": "",
  "currency": "",
  "positioning": "",
  "claims": [],
  "rating": null,
  "review_count": null,
  "collected_at": "",
  "connector_used": "",
  "confidence": "high | medium | low"
}
```

### Review Evidence

```json
{
  "evidence_type": "review",
  "brand_or_product": "",
  "country": "",
  "language": "",
  "source_name": "",
  "source_url": "",
  "rating": null,
  "review_date": "",
  "raw_text": "",
  "translated_text": "",
  "verified_buyer": null,
  "theme": "",
  "sentiment": "positive | neutral | negative | mixed",
  "emotion_strength": 0,
  "nps_proxy_class": "promoter | passive | detractor | unknown",
  "connector_used": "",
  "confidence": "high | medium | low"
}
```

### Price Evidence

```json
{
  "evidence_type": "price",
  "brand_or_product": "",
  "country": "",
  "channel": "",
  "source_name": "",
  "source_url": "",
  "list_price": "",
  "sale_price": "",
  "currency": "",
  "discount_pct": null,
  "subscription_price": "",
  "bundle_offer": "",
  "shipping_or_tax_note": "",
  "collected_at": "",
  "connector_used": "",
  "confidence": "high | medium | low"
}
```

### Social Evidence

```json
{
  "evidence_type": "social_discussion",
  "platform": "",
  "country": "",
  "language": "",
  "source_name": "",
  "source_url": "",
  "raw_text": "",
  "translated_text": "",
  "theme": "",
  "consumer_stage": "awareness | consideration | purchase | usage | complaint | advocacy",
  "sentiment": "positive | neutral | negative | mixed",
  "engagement_proxy": null,
  "connector_used": "",
  "confidence": "high | medium | low"
}
```

---

## Compliance Policy

```yaml
compliance_policy:
  public_data_only_by_default: true
  private_personal_data_collection: forbidden
  credentials_to_untrusted_connectors: forbidden
  authenticated_user_content_collection: forbidden_unless_explicitly_approved
  bypassing_paywalls_or_access_controls: forbidden
  robots_and_terms_check_required: true
  rate_limit_required: true
  prompt_injection_defense_required: true
  raw_html_as_untrusted_input: true
  source_provenance_required: true
  data_minimization_required: true
  pii_redaction_required: true
  internal_data_requires_approved_scope: true
  health_children_elderly_data_requires_extra_review: true
```

---

## Data Quality Scoring

```yaml
data_quality_score:
  components:
    source_relevance: 0.20
    country_relevance: 0.15
    category_relevance: 0.15
    sample_size: 0.15
    freshness: 0.10
    verified_purchase_or_high_intent: 0.10
    bias_risk_inverse: 0.10
    extraction_confidence: 0.05
  score_interpretation:
    80_100: high_confidence
    60_79: usable_with_caveats
    40_59: directional_only
    0_39: context_only_or_avoid
```

---

## Output Artifacts

```text
artifacts/
  evidence/
    competitor_evidence.jsonl
    review_evidence.jsonl
    price_evidence.jsonl
    social_evidence.jsonl
    internal_evidence.jsonl
  logs/
    mcp_collection_jobs.jsonl
    source_quality_scores.jsonl
    failed_sources.jsonl
  summaries/
    local_source_map.md
    competitor_discovery_summary.md
    price_intelligence_summary.md
    review_mining_summary.md
    social_listening_summary.md
```
