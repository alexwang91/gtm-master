# Coverage and Source Quality

Use this after Evidence Collection Runner and before analysis or synthesis.

## Purpose

Coverage Map answers: did we collect enough evidence for each domain?

Source Quality Score answers: can we trust and use each source?

Together they determine confidence caps for downstream claims.

## Coverage Map

```json
{
  "coverage_map": [
    {
      "coverage_category": "selling_points | local_language | competitors | prices | reviews | local_voice_sources | comment_collection | consumer_voice | market_size | channels | trends | internal_private",
      "coverage_score": 0,
      "coverage_level": "strong | adequate | thin | missing",
      "sources_found": [],
      "sources_unavailable": [],
      "local_language_coverage": "strong | adequate | thin | missing | not_applicable",
      "country_match": "direct | comparable_market | mixed | weak | missing",
      "freshness": "fresh | acceptable | stale | unknown",
      "priority_gaps": [],
      "recommended_action": "continue | collect_more | proceed_with_caveat | ask_user | mark_gap"
    }
  ]
}
```

## Coverage Score

```text
Coverage Score =
  Source Type Coverage * 0.25
+ Country Match * 0.20
+ Local Language Coverage * 0.15
+ Source Count Adequacy * 0.15
+ Freshness * 0.10
+ Cross-Source Agreement * 0.10
+ Extraction Completeness * 0.05
```

Interpretation:

```text
80-100 = strong
60-79  = adequate
40-59  = thin
0-39   = missing
```

## Source Quality Score

```text
Source Quality Score =
  Country Relevance * 0.15
+ Category Relevance * 0.15
+ Consumer Intent Quality * 0.15
+ Review / Evidence Depth * 0.15
+ Freshness * 0.10
+ Sample Size * 0.10
+ Verified / High-Intent Signal * 0.10
+ Bias Risk Inverse * 0.07
+ Extraction Confidence * 0.03
```

Interpretation:

```text
80-100 = primary
60-79  = secondary
40-59  = context_only
0-39   = avoid
```

## Source Quality Record

```json
{
  "source_quality_scores": [
    {
      "source_ref": "",
      "source_name": "",
      "source_category": "public_search | public_page | marketplace_retail | consumer_voice | internal_private | unavailable_or_blocked",
      "source_type": "",
      "score": 0,
      "recommended_use": "primary | secondary | context_only | avoid",
      "score_breakdown": {
        "country_relevance": 0,
        "category_relevance": 0,
        "consumer_intent_quality": 0,
        "review_or_evidence_depth": 0,
        "freshness": 0,
        "sample_size": 0,
        "verified_or_high_intent_signal": 0,
        "bias_risk_inverse": 0,
        "extraction_confidence": 0
      },
      "bias_risks": [],
      "usage_permission": "approved_internal | public_context | restricted | unavailable",
      "reason": ""
    }
  ]
}
```

## Confidence Caps

Do not let conclusions sound stronger than the evidence allows.

```json
{
  "confidence_caps": [
    {
      "claim_area": "competitors | price | local_voice_sources | comment_collection | consumer_voice | market_size | channels | nss_nps_proxy | trend_signal",
      "max_confidence": "high | medium | low | assumption_only",
      "reason": "",
      "blocking_gaps": []
    }
  ]
}
```

Default caps:

```text
missing coverage -> assumption_only
thin coverage -> low
adequate coverage -> medium
strong coverage -> high if source quality is also high

trend signal without supporting evidence -> low
single-source price evidence -> low
no local-language consumer voice -> low for JTBD/message claims
no country-specific voice source discovery -> low for consumer voice claims
site-specific comment collection without coverage report -> low for comment-derived claims
incomplete or low-confidence pagination enumeration -> low or medium cap for comment-derived driver frequency
NSS/NPS proxy without enough voice evidence -> do not calculate
private internal evidence only -> high for internal analysis, not public report unless approved
```

## Loopback Rule

If a must-have evidence category is `missing`, return to Evidence Collection Runner unless:

- the user selected quick mode and the gap is non-blocking
- the source is prohibited or unavailable
- the report can proceed with an explicit caveat

If a category is `thin`, choose one:

```text
collect_more
proceed_with_caveat
ask_user_for_private_context
mark_gap
```

## HTML Heatmap

S01 should provide chart-ready coverage data:

```json
{
  "coverage_heatmap": [
    {
      "category": "",
      "coverage_level": "strong | adequate | thin | missing",
      "score": 0,
      "confidence_cap": "high | medium | low | assumption_only",
      "top_sources": [],
      "data_gap_note": ""
    }
  ]
}
```

Show this near the top of the HTML report so readers know where the report is strong and where it is assumption-driven.
