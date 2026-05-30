# Evidence Research Design

Use this before evidence collection. It turns Product-Market Search Preflight output into a reproducible research plan.

## Principles

- Plan before search.
- Generate multiple research perspectives.
- Expand queries systematically.
- Use the least invasive connector that can answer the evidence need.
- Screen sources before extracting evidence.
- Extract into structured schemas.
- Iterate when search reveals new terms, competitors, or gaps.
- Record what was searched, included, excluded, failed, and missing.

## Research Budget

Use the smallest research budget that can answer the current task.

```yaml
research_budget:
  quick:
    retrieval_passes: 1
    perspectives: [buyer, competitor_user, price_sensitive_buyer]
    target_sources_per_must_have_need: 2
    max_queries_per_query_family: 3
    trends_data: optional
    nss_nps_proxy: skip_unless_provided

  standard:
    retrieval_passes: 1
    perspectives: [buyer, price_sensitive_buyer, competitor_user, dissatisfied_user, retailer_channel, expert_reviewer]
    target_sources_per_must_have_need: 3
    max_queries_per_query_family: 5
    trends_data: use_when_available
    nss_nps_proxy: directional_if_enough_voice

  deep:
    retrieval_passes: 2
    perspectives: [buyer, price_sensitive_buyer, competitor_user, dissatisfied_user, retailer_channel, content_kol, brand_team, expert_reviewer]
    target_sources_per_must_have_need: 5
    max_queries_per_query_family: 8
    trends_data: compare_when_available
    nss_nps_proxy: include_with_confidence_gate
```

Do not exceed the selected budget unless a must-have evidence need is missing or the user asks for deeper research.

## Research Perspective Matrix

Generate questions from multiple GTM perspectives before searching.

```json
{
  "research_perspective_matrix": [
    {
      "perspective": "buyer | price_sensitive_buyer | competitor_user | dissatisfied_user | retailer_channel | content_kol | brand_team | support_return | expert_reviewer",
      "core_question": "",
      "evidence_needed": [],
      "query_seed_refs": [],
      "expected_sources": [],
      "downstream_use": []
    }
  ]
}
```

Recommended default perspectives:

```text
buyer
price_sensitive_buyer
competitor_user
dissatisfied_user
retailer_channel
content_kol
brand_team
expert_reviewer
```

Add `support_return` only when internal support, return, NSS/NPS, or customer voice data exists.

## Evidence Need Matrix

```json
{
  "evidence_need_matrix": [
    {
      "evidence_need": "",
      "used_for": [],
      "priority": "must_have | should_have | nice_to_have",
      "target_country_or_region": "",
      "required_source_types": [],
      "minimum_viable_evidence": "",
      "confidence_rule": "",
      "connector_slots": [],
      "expected_output_schema": ""
    }
  ]
}
```

Default S01 evidence needs:

```text
category mainstream selling points
local search language and related queries
direct competitors
substitutes
local prices and price anchors
marketplace or retailer reviews
consumer discussions and complaints
local voice source landscape
site-specific comment coverage for high-value local sources when permitted
channel and touchpoint signals
market size inputs
NSS/NPS or proxy inputs
historical ads / KOL / landing page signals when provided
internal benchmark or channel plan when provided
```

## Query Expansion Plan

Use the preflight `search_query_seed_pack` as the starting point.

```json
{
  "query_expansion_plan": {
    "base_queries": [],
    "local_language_queries": [],
    "category_queries": [],
    "feature_queries": [],
    "benefit_queries": [],
    "competitor_queries": [],
    "substitute_queries": [],
    "complaint_queries": [],
    "price_queries": [],
    "review_queries": [],
    "comparison_queries": [],
    "local_voice_source_queries": [],
    "site_specific_queries": [],
    "trend_queries": [],
    "new_terms_to_watch": []
  }
}
```

Use these expansion methods:

```text
multi-query generation
local-language translation and synonym expansion
competitor-name expansion
complaint-term expansion
related-query expansion
review-language expansion
pseudo-relevance feedback from first-pass results
```

Avoid query drift: expansion terms must connect to the product category, target country, or a discovered competitor/substitute.

## MCP Routing Plan

```json
{
  "mcp_routing_plan": [
    {
      "job_type": "source_discovery | local_voice_source_discovery | trend_signal_collection | competitor_discovery | price_intelligence | review_mining | consumer_discussion_mining | site_specific_comment_collection | social_listening | market_size_research | channel_research | internal_file_extraction",
      "evidence_need": "",
      "preferred_connector_slots": [],
      "fallback_slots": [],
      "least_invasive_path": true,
      "compliance_notes": [],
      "output_artifacts": []
    }
  ]
}
```

## Source Screening Criteria

Define screening rules before reading deeply.

```json
{
  "source_screening_criteria": {
    "include_if": [
      "target_country_or_region_match",
      "category_or_competitor_relevance",
      "consumer_intent_or_price_or_review_signal",
      "fresh_enough_for_the_evidence_need",
      "public_or_approved_internal_source"
    ],
    "exclude_if": [
      "wrong_country_without_comparable-market rationale",
      "thin_search_snippet_only",
      "obvious_ad_without_disclosure_or_context",
      "private_or_login_required_without_approval",
      "paywall_or_access_control_bypass_required",
      "outdated_for_price_or_channel_decision"
    ],
    "dedupe_rule": "Prefer original source over syndicated copies; retain one canonical source URL per evidence item."
  }
}
```

## Result Fusion and Rerank Rule

Use simple rank fusion when multiple query variants return overlapping sources.

```json
{
  "result_fusion_and_rerank_rule": {
    "signals": [
      "source_quality_score",
      "country_relevance",
      "category_relevance",
      "query_variant_coverage",
      "source_type_priority",
      "freshness",
      "evidence_depth"
    ],
    "preferred_method": "reciprocal_rank_fusion_or_weighted_score",
    "dedupe": true,
    "top_sources_per_evidence_need": 5
  }
}
```

## Extraction Schema Plan

Define the schema before extracting.

```json
{
  "extraction_schema_plan": [
    {
      "source_type": "competitor_page | retailer_price_page | marketplace_review | forum_thread | specialist_media_comment_thread | video_comments | app_reviews | q_and_a | social_post | expert_review | market_size_source | internal_file",
      "target_schema": "competitor_evidence | price_evidence | review_evidence | social_evidence | site_profile | comment_record | comment_coverage_report | market_size_evidence | internal_evidence | voice_atom",
      "fields": [],
      "quality_checks": []
    }
  ]
}
```

## Search and Screening Log

Use a PRISMA-inspired log for transparency.

```json
{
  "search_and_screening_log": [
    {
      "search_id": "",
      "evidence_need": "",
      "connector_slot": "",
      "query_or_source": "",
      "country_or_region": "",
      "language": "",
      "results_found": 0,
      "sources_screened": 0,
      "sources_included": 0,
      "sources_excluded": 0,
      "exclusion_reasons": [],
      "created_evidence_refs": [],
      "status": "success | partial | failed | skipped"
    }
  ]
}
```

## Iterative Retrieval Loop

Run an extra loop only when first-pass search reveals new important competitors, substitutes, local terms, complaints, or gaps. In `quick` mode, record the gap instead of looping unless it blocks the market map.

```text
first-pass search
-> extract candidate terms, competitors, sources, and gaps
-> update query_expansion_plan
-> second-pass targeted search
-> update coverage map
```

Stop after first pass when evidence coverage is adequate and no high-priority gaps appear.

## Coverage Stop Rule

```json
{
  "coverage_stop_rule": {
    "can_stop_if": [
      "must_have evidence needs have adequate or strong coverage",
      "top competitor and substitute set is stable across query variants",
      "price anchors include at least three relevant local sources or limitations are explicit",
      "consumer voice has enough atoms for initial segmentation or limitations are explicit",
      "high-value local voice sources have either comment coverage reports or explicit access/data gaps",
      "no new high-priority competitors or terms appear in the latest pass"
    ],
    "must_continue_or_mark_gap_if": [
      "local-language coverage is thin",
      "competitor universe changes significantly after second pass",
      "price evidence is stale or single-source",
      "consumer voice is mostly expert or ad language",
      "country-specific forums or comment sources are likely relevant but not yet discovered",
      "market size inputs are assumption-only"
    ]
  }
}
```

## Readiness Score

```text
Evidence Plan Readiness Score =
  Evidence Need Coverage * 0.25
+ Query Diversity * 0.20
+ Local Language Coverage * 0.20
+ Connector Fit * 0.15
+ Compliance Safety * 0.10
+ Fallback Completeness * 0.10
```

Interpretation:

```text
80-100 = ready to collect
60-79  = collect with caveats
40-59  = ask user or narrow scope
0-39   = not ready
```
