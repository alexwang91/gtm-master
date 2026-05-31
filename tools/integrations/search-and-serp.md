# Search And SERP

Capability slots: `primary_search`

Required capabilities: `web_search`, `serp_search`, `competitor_discovery`.

Use this for local source discovery, competitor discovery, local keyword
expansion, search-language discovery, forum discovery, retailer discovery, and
country-specific category pages.

## Inputs

```yaml
required:
  - product_category
  - launch_country_or_region
  - target_price_range
optional:
  - local_language_queries
  - known_competitors
  - planned_channels
```

## Outputs

```yaml
outputs:
  - source_candidates
  - local_query_bank
  - competitor_candidates
  - retailer_marketplace_candidates
  - search_result_evidence_records
  - collection_log
```

## Rules

- Prefer local-language and country-specific queries before global English queries.
- Treat search volume and SERP presence as interest or visibility proxies, not market size.
- Save result titles, URLs, snippets, country/language, query, date, and tool used.
- Do not scrape result pages at scale when a SERP API or lightweight search can answer the question.
