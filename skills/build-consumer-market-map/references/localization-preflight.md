# Local Market Localization Preflight

Use this before assuming any local source, retailer, marketplace, language, channel, price norm, or consumer research location.

## Purpose

Discover the local market context needed to collect evidence correctly. The goal is not to analyze the market yet; the goal is to avoid using the wrong sources, language, price interpretation, or channel assumptions.

## Depth Modes

```yaml
quick:
  required:
    - local_language_plan
    - local_source_map_seed
    - price_display_and_currency_basics
  skip_unless_obvious:
    - compliance_context
    - seasonality_calendar
    - payment_and_financing_norms

standard:
  required:
    - local_language_plan
    - local_source_map
    - price_display_and_currency_basics
    - review_and_community_source_map
    - channel_and_retail_source_map
    - return_warranty_trust_basics
  optional:
    - payment_and_financing_norms
    - seasonality_calendar
    - compliance_context

deep:
  required:
    - all_standard_items
    - payment_and_financing_norms
    - seasonality_calendar
    - compliance_context
    - regional_submarket_notes
    - local_claim_and_certification_context
```

## Output Contract

```json
{
  "localization_preflight": {
    "country_or_region": "",
    "local_language_plan": {
      "primary_languages": [],
      "secondary_languages": [],
      "scripts": [],
      "english_search_usefulness": "high | medium | low",
      "translation_notes": [],
      "transliteration_or_local_names": []
    },
    "local_source_map": {
      "search_engines": [],
      "marketplaces": [],
      "retailers": [],
      "price_comparison_sites": [],
      "deal_forums": [],
      "expert_review_sites": [],
      "forums_and_communities": [],
      "video_platforms": [],
      "social_platforms": [],
      "app_stores": [],
      "official_statistics_or_market_data_sources": [],
      "sources_to_avoid": []
    },
    "local_voice_source_map": {
      "specialist_category_forums": [],
      "specialist_media_comment_threads": [],
      "local_deal_forums": [],
      "marketplace_or_retailer_reviews": [],
      "price_comparison_reviews": [],
      "video_review_comment_sources": [],
      "public_social_threads": [],
      "local_reddit_or_reddit_equivalent": [],
      "brand_or_support_communities": [],
      "app_store_review_sources": [],
      "q_and_a_pages": [],
      "site_specific_collection_candidates": []
    },
    "price_and_commerce_context": {
      "currency": "",
      "vat_or_sales_tax_display": "included | excluded | mixed | unknown",
      "shipping_cost_visibility": "included | separate | mixed | unknown",
      "installment_or_financing_norms": [],
      "bundle_or_promo_norms": [],
      "return_and_warranty_expectations": [],
      "after_sales_trust_signals": []
    },
    "category_language_context": {
      "category_terms": [],
      "benefit_terms": [],
      "complaint_terms": [],
      "review_terms": [],
      "comparison_terms": [],
      "buying_terms": [],
      "price_terms": []
    },
    "local_calendar_context": {
      "shopping_moments": [],
      "seasonality_notes": [],
      "launch_timing_risks": []
    },
    "claim_and_compliance_context": {
      "relevant_only_if": "health | safety | child | elderly | regulated_claim | privacy | wireless | battery | certification",
      "possible_claim_constraints": [],
      "certification_or_trust_marks_to_check": [],
      "privacy_or_data_sensitivity_notes": [],
      "requires_human_review": false
    },
    "source_discovery_queries": [],
    "confidence": "high | medium | low",
    "data_gaps": []
  }
}
```

## How To Discover Local Sources

Do not hard-code local e-commerce or community sources. Discover candidate sources with local-language and English query patterns:

```text
[category] buy / kaufen / acheter / comprar / compra / comprare / comprar online
[category] price comparison / preisvergleich / comparateur prix
[category] test / review / erfahrungen / avis / recensioni / opiniones
[category] best / bestseller / ranking / vergleich
[competitor] price / review / alternative
[category] forum / reddit / community / complaint
[category] local forum / local community / discussion / opinion / experience
[competitor] local forum / discussion / owner experience / problem
[previous generation product] review / forum / complaint / experience
top online retailers [country]
best price comparison sites [country]
best [category] forums [country]
best [category] review sites [country]
```

Translate these patterns into the target country's main language and script. Keep English variants only when English is commonly used for the category or professional reviews.

For country-specific consumer voice, discover the local source landscape first, then search inside high-value domains. Do not hard-code one global community as the default. A country may rely more on specialist media comments, deal forums, video comments, app reviews, local social groups, or a language-specific forum than on Reddit-style sources.

## Source Classification

Classify discovered sources before collection:

```json
{
  "source_name": "",
  "source_url": "",
  "source_type": "search_engine | marketplace | retailer | price_comparison | deal_forum | expert_review | forum | specialist_media_comment_thread | social | video | app_store | q_and_a | official_statistics | brand_site | avoid",
  "source_family": "commerce | review | consumer_voice | market_size | channel | mixed",
  "country_relevance": 0,
  "category_relevance": 0,
  "local_voice_source_fit_score": 0,
  "evidence_domains_supported": ["price", "reviews", "competitors", "channels", "consumer_voice", "market_size"],
  "access_method": "search | extraction | browser | manual_upload | unavailable",
  "site_specific_collection_candidate": false,
  "recommended_use": "primary | secondary | context_only | avoid",
  "reason": ""
}
```

## Local Context Checks

Before collecting price, review, or channel evidence, check:

- Is the source actually used in the target country?
- Is it category-relevant or only generally popular?
- Does it contain buyer intent, review, price, or comparison data?
- Does it contain enough local-language consumer voice to justify a site-specific collection profile?
- Does it require login, scraping, or access restrictions?
- Is the language a real consumer language for this market?
- Are prices VAT-inclusive, tax-exclusive, shipping-inclusive, or unclear?
- Are discounts, bundles, financing, or subscriptions normal in this category?
- Are warranty, return, repair, or after-sales trust major purchase factors?

## Handoff Value

This preflight should feed:

- Evidence Research Design source choices
- MCP connector routing
- Query expansion
- Coverage Map source categories
- Price sensitivity interpretation
- Channel and touchpoint map
- HTML data source notes
