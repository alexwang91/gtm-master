# Market Sizing TAM/SAM/SOM Seed

Use this after market size evidence collection and before segment priority is finalized. It creates a transparent, assumption-driven TAM/SAM/SOM seed for S01.

S01 does not produce the final launch demand forecast. It builds the market sizing evidence layer and assumption tree that S08 can use later.

## Inputs

```json
{
  "launch_country_or_region": "",
  "product_category": "",
  "target_price_range": "",
  "product_capability_map": {},
  "localization_preflight": {},
  "market_size_evidence": [],
  "voice_theme_clusters": [],
  "segment_seed_pack": [],
  "local_price_corridor": {},
  "segment_price_sensitivity_seeds": [],
  "segment_channel_touchpoint_map": [],
  "retailer_marketplace_candidates": [],
  "previous_generation_sales_price_channel_performance": "",
  "internal_benchmark_or_channel_plan": ""
}
```

## Core Rules

- Use ranges and assumption trees, not false precision.
- Separate evidence-backed values, benchmark proxies, internal private data, and assumptions.
- Do not treat marketplace ranking, search interest, or social buzz as direct market size.
- Do not use comparable-market proxies without labeling the rationale and confidence cap.
- Segment-level estimates must reconcile to total SAM/SOM ranges or explicitly explain overlap.
- Keep S01 SOM as launch-period seed only; S08 owns final forecast.

## Evidence Priority

```text
1. Official statistics for population, households, income, age, internet/device access, and relevant demographics.
2. Direct category penetration, ownership, or incidence data for the target country.
3. Retailer, marketplace, or price-comparison category signals as weak proxies.
4. Industry reports and public summaries with clear country/category match.
5. Internal previous-generation sales, sell-through, channel, and price data.
6. Comparable-market benchmarks with explicit rationale.
7. Assumptions from consumer voice, segment logic, and channel availability.
```

## Assumption Tree

```text
TAM = eligible population or households
  * relevant need / use-case incidence
  * category or substitute acceptance

SAM = TAM
  * product-type fit
  * price-band affordability or willingness filter
  * channel reachability
  * trust / claim / compliance eligibility

SOM = SAM
  * launch awareness reach
  * purchase conversion assumption
  * availability / inventory / channel capacity
  * competitive friction adjustment
```

## TAM/SAM/SOM Seed Schema

```json
{
  "tam_sam_som_seed": {
    "country_or_region": "",
    "product_category": "",
    "currency": "",
    "time_horizon": "launch_period | year_1 | annual_run_rate | unknown",
    "tam_range": {
      "low": 0,
      "mid": 0,
      "high": 0,
      "unit": "people | households | buyers | units | revenue | unknown"
    },
    "sam_range": {
      "low": 0,
      "mid": 0,
      "high": 0,
      "unit": "people | households | buyers | units | revenue | unknown"
    },
    "som_seed_range": {
      "low": 0,
      "mid": 0,
      "high": 0,
      "unit": "buyers | units | revenue | unknown"
    },
    "method": "evidence_based | benchmark_based | internal_data_based | assumption_based | blended",
    "confidence": "high | medium | low",
    "evidence_refs": [],
    "assumption_refs": [],
    "data_gaps": []
  }
}
```

## Assumption Record

```json
{
  "tam_sam_som_assumption_tree": [
    {
      "assumption_id": "",
      "model_layer": "TAM | SAM | SOM",
      "assumption_name": "",
      "value_low": 0,
      "value_mid": 0,
      "value_high": 0,
      "unit": "ratio | count | currency | other",
      "source_type": "official_stat | category_report | marketplace_proxy | internal_private | comparable_market | consumer_voice_inference | analyst_assumption",
      "evidence_refs": [],
      "rationale": "",
      "confidence": "high | medium | low",
      "sensitivity": "high | medium | low",
      "owner_next_validation": "S01 | S08 | user | external_research | not_required",
      "limitations": []
    }
  ]
}
```

## Segment-Level TAM/SAM/SOM

```json
{
  "segment_level_tam_sam_som": [
    {
      "segment_id": "",
      "segment_name": "",
      "tam_relevance": "high | medium | low",
      "tam_range": {},
      "sam_range": {},
      "som_seed_range": {},
      "segment_filters": {
        "need_or_use_case_filter": "",
        "price_filter": "",
        "channel_reach_filter": "",
        "trust_or_claim_filter": "",
        "competitive_friction_filter": ""
      },
      "overlap_risk_with_segments": [],
      "evidence_refs": [],
      "assumption_refs": [],
      "confidence": "high | medium | low",
      "data_gaps": []
    }
  ]
}
```

## Comparable-Market Proxy

Use only when direct country/category evidence is thin.

```json
{
  "comparable_market_proxies": [
    {
      "proxy_market": "",
      "why_comparable": "",
      "where_not_comparable": "",
      "metric_used": "",
      "adjustments": [],
      "confidence_cap": "medium | low | assumption_only",
      "evidence_refs": [],
      "limitations": []
    }
  ]
}
```

## Market Sizing Confidence

```text
Market Sizing Confidence =
  Official / Primary Data Quality * 0.20
+ Country and Category Match * 0.18
+ Assumption Transparency * 0.16
+ Price / Affordability Support * 0.12
+ Channel Reach Support * 0.10
+ Segment Evidence Support * 0.10
+ Internal Data Support * 0.08
+ Sensitivity Risk Inverse * 0.06
```

Interpretation:

```text
80-100 = high confidence seed
60-79  = medium confidence seed
40-59  = low confidence seed
0-39   = assumption-only seed
```

## User-Provided Market Inputs

If the user provides previous-generation sales, channel sell-through, retailer forecasts, internal benchmarks, or executive market assumptions:

- Store as `internal_private` or `user_provided_market_sizing_hypothesis`.
- Use them for internal analysis, not public report claims unless approved.
- Compare them against public market evidence and channel capacity.
- Preserve contradictions and data gaps for S08 validation.

## S08 Handoff

Downstream S08 should receive:

- `tam_sam_som_seed`
- `tam_sam_som_assumption_tree`
- `segment_level_tam_sam_som`
- `comparable_market_proxies`
- `market_sizing_confidence`
- `market_sizing_data_gaps`
- internal private refs when approved

S08 owns final launch demand forecast, conversion assumptions, channel split forecast, inventory risk, and scenario sensitivity.
