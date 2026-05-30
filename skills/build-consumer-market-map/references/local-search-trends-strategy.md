# Local Search and Trends Strategy

Use this strategy inside Product-Market Search Preflight and Evidence Plan.

## Positioning

Google Trends-style data is a directional search-language and interest signal. It is not market size, search volume, sales volume, or purchase intent by itself.

Use it to:

- Compare relative interest among category terms, feature terms, competitor terms, and local-language synonyms.
- Find related queries and rising queries.
- Detect whether a selling point is mainstream, rising, niche, weak, or unknown.
- Compare search terms vs topics when cross-language ambiguity matters.
- Generate better local-language query seeds for later evidence discovery.

Do not use it to:

- Estimate TAM/SAM/SOM directly.
- Claim exact demand.
- Conclude purchase intent without review, marketplace, price, or channel evidence.
- Replace consumer voice mining.

## Recommended Source Order

```text
1. Local-language SERP discovery
2. Google Trends / trends API / BigQuery public trends dataset when available
3. Related queries and related topics
4. Marketplace and search autocomplete where permitted
5. Competitor product pages and ad language
6. Review/forum/social consumer language
7. Translation and synonym expansion
```

## Connector Slot Strategy

```yaml
trend_signal_collection:
  preferred_slots:
    - primary_search
    - trends_api
  fallback_slots:
    - serp_search
    - primary_web_extractor
    - manual_trends_review

local_language_expansion:
  preferred_slots:
    - translation_and_local_language_processing
    - primary_search
  fallback_slots:
    - serp_search
    - marketplace_autocomplete

related_query_discovery:
  preferred_slots:
    - trends_api
    - primary_search
  fallback_slots:
    - serp_search
    - primary_web_extractor
```

If no Trends-capable connector is available, continue with local SERP, related search snippets, marketplace language, competitor language, reviews, and clearly mark trend signal as unavailable.

## Query Expansion Pattern

For each capability or selling point, generate:

```json
{
  "base_category_terms": [],
  "feature_terms": [],
  "benefit_terms": [],
  "competitor_terms": [],
  "alternative_terms": [],
  "complaint_terms": [],
  "review_terms": [],
  "price_terms": [],
  "comparison_terms": [],
  "local_language_variants": []
}
```

## Trend Signal Labels

```text
mainstream
  Stable or high relative interest and appears in category/competitor/review language.

rising
  Related/rising query signal or recent growth, but not yet a dominant mainstream term.

niche
  Appears in specialized sources or small subsegments.

weak
  Low or inconsistent signal across search and consumer language.

unknown
  Trends data unavailable or too sparse.
```

## Dashboard Handoff

S01 must pass a compact, display-ready bridge into S14:

```json
{
  "local_search_term_map": [
    {
      "query": "",
      "local_language_variant": "",
      "intent_stage": "category_discovery | comparison_review | price_purchase | complaint_problem",
      "trend_signal_status": "mainstream | rising | niche | weak | unknown",
      "competitor_discovery_use": "",
      "evidence_status": ""
    }
  ],
  "competitor_discovery_queries": [],
  "competitor_candidate_scoring": [],
  "user_calibration_status": "not_started | pending | completed",
  "evidence_status": "live_confirmed | partial | hypothesis_only"
}
```

This handoff lets the dashboard show why a competitor was discovered, which local words produced it, and whether the user has confirmed the candidate list before downstream skills use it.

## Cross-Check Rule

Before prioritizing a selling point, require at least one supporting source outside trend data:

```text
review language
competitor page language
marketplace search/autocomplete
forum/social discussion
expert review
internal customer voice
```
