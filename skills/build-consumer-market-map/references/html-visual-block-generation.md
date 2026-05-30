# S01 HTML Visual Block Generation

Use this when producing `html_section_draft.visual_blocks` for S14.

## Core Rule

`visual_blocks` are view models derived from S01 analysis outputs. They must not introduce new findings, new scores, new competitors, new segments, or new price claims.

Each block must include:

```json
{
  "type": "status_panel | ranked_bar | matrix_heatmap | range_chart",
  "title": "",
  "subtitle": "",
  "data_source": "",
  "items": [],
  "rows": [],
  "columns": [],
  "scale_min": 0,
  "scale_max": 100,
  "note": "",
  "evidence_refs": [],
  "confidence": "high | medium | low | hypothesis_only"
}
```

## Shared Scoring Rules

Use existing S01 scores from `scoring-rubrics.md`.

```text
80-100 -> high
60-79  -> medium
40-59  -> low
0-39   -> hypothesis_only or data_gap, depending on source quality
```

If a sub-score is unavailable:

```text
Do not invent it from prose.
Use the closest approved score only if the source field explicitly maps to the same concept.
Otherwise render a table and add `missing_visual_block_score` to data_gaps.
```

Confidence caps:

```text
overall_coverage_score < 40
  Cap S01 visual block confidence at low unless user-provided internal evidence directly supports the block.

consumer_voice_coverage missing
  Cap consumer voice, segment, NSS/NPS, and JTBD-handoff visuals at low or hypothesis_only.

price_coverage missing
  Cap price corridor and price sensitivity seed visuals at hypothesis_only.

local_language_coverage missing
  Cap local search language and message/JTBD phrase visuals at low.
```

## Block 1: Evidence Coverage Gate

Purpose: show whether downstream modules can trust S01.

```json
{
  "type": "status_panel",
  "title": "Evidence Coverage Gate",
  "subtitle": "Shows confidence before downstream recommendations",
  "data_source": "coverage_summary + source_quality_summary + confidence_caps"
}
```

Inputs:

```text
coverage_map.evidence_categories
coverage_summary
source_quality_summary
confidence_caps
market_sizing_confidence
local_voice_source_map
```

Build 3-6 items:

```text
Overall coverage
Local language
Competitors/substitutes
Price anchors
Consumer voice
Market sizing
```

Item mapping:

```json
{
  "label": "Consumer voice",
  "value": "adequate | thin | missing | capped",
  "note": "Score: 64; sources: reviews, forum comments; cap: none",
  "evidence_refs": [],
  "confidence": "medium"
}
```

If no coverage score exists, still render this block as a warning status panel and add `missing_coverage_score`.

## Block 2: Product Capability To Local Selling-Point Fit

Purpose: show how product features map to category reasons-to-buy and local search language.

```json
{
  "type": "matrix_heatmap",
  "title": "Product Capability To Local Selling-Point Fit",
  "subtitle": "Compares product claims against local category benefits and search language",
  "data_source": "category_selling_point_map + selling_point_fit_scores + feature_to_local_language_map",
  "columns": ["Category fit", "Search language", "Product support", "Differentiation", "Proof availability"]
}
```

Rows:

```text
Use top 5-8 selling points by fit_score.
Preserve local language terms in row notes or a companion table.
Do not show more than 8 rows in the main dashboard.
```

Cell scores:

```text
category_mainstream_fit -> Category fit
local_search_language_match -> Search language
product_feature_support -> Product support
competitor_differentiation -> Differentiation
proof_availability -> Proof availability
```

If only `our_feature_match` exists:

```text
strong  -> 85
partial -> 60
weak    -> 35
none    -> 0
```

Add a note that the row uses categorical mapping, not full rubric scoring.

## Block 3: Competitor And Substitute Threat Ranking

Purpose: show who shapes local comparison and switching risk.

```json
{
  "type": "ranked_bar",
  "title": "Competitor And Substitute Threat Ranking",
  "subtitle": "Ranks direct competitors, substitutes, and price-tier jump risks",
  "data_source": "competitor_threat_scores + top_competitors_and_substitutes"
}
```

Rows:

```text
Sort by competitor_threat_score descending.
Show 5-10 competitors/substitutes in the main body.
Keep full candidate pool in appendix or full artifact.
```

Item mapping:

```json
{
  "label": "[Competitor or substitute]",
  "score": 82,
  "score_label": "High threat",
  "note": "Overlap: premium; anchor: strong; channel: marketplace + retail",
  "evidence_refs": []
}
```

If the user provided competitors but S01 has not validated local threat, show them in a table as `user_hypothesis`, not as a ranked threat bar.

## Block 4: Local Price Corridor Seed

Purpose: show target price against local anchors, substitutes, and tier jumps.

```json
{
  "type": "range_chart",
  "title": "Local Price Corridor Seed",
  "subtitle": "Target price versus local anchors and tier jumps",
  "data_source": "local_price_corridor + price_anchor_panel + competitor_price_gap_table"
}
```

Numeric requirement:

```text
Only render `range_chart` when prices can be normalized to one currency and comparable unit.
If prices are strings, bundles, subscriptions, financing-only, or tax-incomparable, render a table and add `price_range_chart_not_comparable`.
```

Scale:

```text
scale_min = min(anchor_min, target_min, substitute_min) rounded down
scale_max = max(anchor_max, target_max, premium_anchor_max) rounded up
```

Items:

```text
Entry substitute band
Main competitor band
Target price range
Premium jump band
```

Item mapping:

```json
{
  "label": "Main competitor band",
  "min": 280,
  "max": 620,
  "marker": 499,
  "value_label": "280-620 | target 499",
  "note": "Currency: HUF/EUR/etc.; source mix: marketplace + retailer",
  "evidence_refs": []
}
```

S01 must label this as a seed, not a final pricing model.

## Block 5: Segment Priority And Evidence Strength

Purpose: show which segments deserve GTM attention first and how strong the evidence is.

```json
{
  "type": "ranked_bar",
  "title": "Segment Priority And Evidence Strength",
  "subtitle": "Ranks launch segment candidates with evidence caveats",
  "data_source": "segment_priority_ranking + segment_evidence_strength_scores + segment_level_tam_sam_som"
}
```

Rows:

```text
Show top 3-6 segments by segment_priority_score.
If a weak but commercially important segment is retained, label it as hypothesis and include the data gap.
Do not promote demographic-only personas.
```

Score:

```text
Use Segment Priority Score when available.
If absent, use Segment Evidence Strength only for evidence ranking, not priority ranking.
If both are absent, render a table and add `missing_segment_priority_score`.
```

Item mapping:

```json
{
  "label": "[Segment name]",
  "score": 76,
  "score_label": "P1 launch segment",
  "note": "Evidence: usable; WTP: medium; channel: strong; TAM: directional",
  "evidence_refs": []
}
```

## Block 6: Segment Channel Touchpoint Fit

Purpose: show where each priority segment can be reached, educated, converted, and supported.

```json
{
  "type": "matrix_heatmap",
  "title": "Segment Channel Touchpoint Fit",
  "subtitle": "Discovery, comparison, purchase, proof, support, and advocacy fit by segment",
  "data_source": "segment_channel_touchpoint_map + channel_fit_scores + retailer_marketplace_candidates",
  "columns": ["Discovery", "Comparison", "Purchase", "Proof / trust", "Support / advocacy"]
}
```

Rows:

```text
Use top 3-5 segments from Segment Priority And Evidence Strength.
Aggregate channel_fit_scores by journey stage.
Preserve retailer/marketplace candidates in a companion table.
```

Cell score:

```text
Use Channel Fit Score averaged or max-selected within each segment x stage.
If only qualitative channel notes exist, render a grouped table and add `missing_channel_fit_score`.
```

Cell labels:

```text
75-100 = strong
55-74  = useful
35-54  = test
0-34   = weak
```

## Optional Main-Body Blocks

Add these only when they change decisions:

```text
Consumer Voice Driver Ranking
  type: ranked_bar
  source: voice_theme_clusters + nps_driver_tornado_seed + bain_driver_inputs
  trigger: voice drivers affect proof, messaging, product diagnosis, or sales enablement.

TAM/SAM/SOM Seed Ranges
  type: range_chart
  source: tam_sam_som_seed + market_sizing_confidence
  trigger: ranges are numeric, comparable, and needed for launch sizing.

NSS/NPS And Earned Growth Readiness
  type: status_panel
  source: nss_nps_proxy_seed_panel + earned_growth_proxy_seed + net_promoter_system_loop_seed
  trigger: report audience needs experience, advocacy, or next-generation GTM implications.

Retailer And Marketplace Candidate Ranking
  type: ranked_bar
  source: retailer_marketplace_candidates + channel_fit_scores
  trigger: channel selection changes downstream work.
```

## Companion Tables Required In Standard Mode

Visual blocks are not enough. S01 should also include these compact tables when data exists:

```text
local_search_language_table
consumer_voice_theme_table
competitor_candidate_review_table
retailer_marketplace_candidate_table
data_gap_and_confidence_cap_table
```

## Final Assembly Checklist

Before returning `html_section_draft`:

```text
1. Order visual_blocks by decision flow:
   evidence -> selling point -> competitors -> price -> segments -> channels.

2. Each block has title, type, data_source, evidence_refs or source note, and confidence.

3. No chart cell uses a fabricated score.

4. Missing numeric data becomes table + data gap, not a decorative chart.

5. User-provided hypotheses are labeled as hypotheses unless validated by local evidence.

6. Private uploaded inputs are summarized only as approved derived signals.

7. Add `rendered_too_thin` if fewer than 4 required visual_blocks can be produced in standard mode.
```
