# S01 HTML Section Contract

S01 contributes the market context section of the final GTM dashboard.

## Section IDs

```text
market_overview
product_capability_summary
evidence_coverage
category_selling_points_and_local_language
competitor_landscape
consumer_voice
local_voice_sources
comment_collection_coverage
consumer_voice_processing
market_sizing
market_sizing_assumptions
market_sizing_confidence
segment_inference
segment_priority
channel_touchpoints
retailer_marketplace_candidates
content_proof_map
local_price_corridor
price_gap_analysis
segment_price_sensitivity
price_anchor_seed
nss_nps_seed
earned_growth_seed
net_promoter_system_seed
hardware_experience_diagnosis
next_generation_marketing_sales_seed
initial_gtm_priorities
```

## HTML Section Draft

```json
{
  "section_id": "s01_market_context",
  "source_skill": "S01.build-consumer-market-map",
  "section_title": "Localized Consumer Market Map",
  "executive_takeaway": "",
  "narrative_blocks": [],
  "metric_cards": [
    {
      "label": "Market Confidence",
      "value": "",
      "evidence_level": "",
      "note": ""
    }
  ],
  "visual_blocks": [],
  "tables": [],
  "charts": [],
  "callouts": [],
  "confidence_badges": [],
  "citations": [],
  "data_gaps": [],
  "next_actions": []
}
```

## S14 Visual Block Contract

S01 must produce `visual_blocks` that S14 can render directly. Use only data-backed values from the full artifact or compressed handoff; do not invent scores to make the section look complete. Read `html-visual-block-generation.md` for block-level transformation rules, scoring fallbacks, and thin-output checks.

```json
{
  "visual_blocks": [
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
  ]
}
```

Default S01 main-body `visual_blocks`:

```yaml
required_visual_blocks:
  - title: Evidence Coverage Gate
    type: status_panel
    data_source: coverage_summary + source_quality_summary + confidence_caps + local_source_map
    core_question: Can downstream modules trust this local market map, and which named sources support it?
    display_requirement: Render source names, links, source roles, access status, evidence quality, and logos/favicons when available; do not reduce this to plain status labels.

  - title: Product Capability To Local Selling-Point Fit
    type: matrix_heatmap
    data_source: category_selling_point_map + adjacent_category_selling_point_map + similar_product_driver_map + selling_point_fit_scores + feature_to_local_language_map
    core_question: Which fixed product features map to local and adjacent-category benefits, search language, proof needs, and marketing watchouts?
    display_requirement: Include enough mainstream and similar-category drivers to make positioning legible; mark strongest fit, weak fit, proof gap, and fixed-product marketing watchout.

  - title: Competitor And Substitute Threat Ranking
    type: ranked_bar
    data_source: competitor_threat_scores + top_competitors_and_substitutes
    core_question: Who most shapes local comparison and switching risk?

  - title: Local Price Corridor Seed
    type: range_chart
    data_source: local_price_corridor + price_anchor_panel + competitor_price_gap_table + price_ladder_scan + jump_decision_risks
    core_question: Where does target price sit against local anchors, tier jumps, and competitor/substitute price pressure?
    display_requirement: Prefer a readable price ladder with target price overlay, low/mid/premium zones, competitor anchors, jump-down options, jump-up options, and concise interpretation.

  - title: Consumer Voice And Fixed-Product Marketing Watchouts
    type: matrix_heatmap
    data_source: local_voice_source_map + voice_storage_compression_policy + top1_previous_generation_voice_scope + voice_collection_coverage_report + bain_nss_journey_seed_panel + consumer_voice_processing_summary + voice_theme_clusters + pain_theme_clusters + purchase_triggers + objections + nss_nps_proxy_source_mix + nps_driver_tornado_seed + bain_driver_inputs + journey_episode_inputs + selling_point_voice_alignment
    core_question: Since the product is fixed, what should marketing emphasize, prove, avoid, or localize based on local consumer voice?
    display_requirement: This must be a large block in standard/deep mode. Show named local sources, access status, collection role, raw artifact refs, compressed handoff policy, TOP1 competitor and previous-generation deep-dive coverage, then connect consumer praise, pain, purchase triggers, objections, NSS/NPS proxy drivers, and hardware journey episodes back to product selling points and proof requirements.

  - title: Segment Priority And Evidence Strength
    type: ranked_bar
    data_source: segment_priority_ranking + segment_evidence_strength_scores + segment_level_tam_sam_som
    core_question: Which segments should GTM investigate and prioritize first?
    display_requirement: Treat as initial ranking only. Show hypothesis labels and validation needs until supported by local voice, channel, conversion, or sales evidence.

  - title: Segment Channel Touchpoint Fit
    type: matrix_heatmap
    data_source: segment_channel_touchpoint_map + channel_fit_scores + retailer_marketplace_candidates
    core_question: Where can each priority segment be reached, educated, and converted?
```

S01 should still include `tables` for local search phrases, consumer voice themes, NSS/NPS proxy composition, data gaps, and detailed candidate review lists. These are decision evidence, but they are often too heterogeneous for simple charts.
S01 should include a visible local voice source map, TOP1 competitor and previous-generation voice scope, collection coverage report, and raw-storage/compression policy whenever consumer voice is missing, partial, or used downstream.

## Thin Output Gate

Mark the S01 HTML section as `rendered_too_thin` in `data_gaps` if it lacks any of:

```text
executive_takeaway
market confidence or evidence coverage signal
at least 4 required visual_blocks in standard mode
consumer voice or local-language evidence table
competitor/substitute evidence table or visual block
next_actions for S02/S04/S14
```

## Recommended Visuals

```yaml
visuals:
  - name: Evidence Coverage Map
    type: scorecard_or_heatmap
    data_source: coverage_map

  - name: Source Quality Summary
    type: scorecard_table
    data_source: source_quality_summary

  - name: Selling Point Fit Matrix
    type: matrix
    data_source: category_selling_point_map

  - name: Local Search Language Table
    type: ranked_table
    data_source: feature_to_local_language_map

  - name: Competitor Threat Matrix
    type: matrix
    data_source: competitor_threat_scores

  - name: Competitor Candidate Review List
    type: checklist_table
    data_source: competitor_candidate_review_list

  - name: Substitute Taxonomy Map
    type: grouped_table
    data_source: substitute_taxonomy

  - name: Price Ladder and Jump Risk Map
    type: matrix
    data_source: jump_decision_risks

  - name: Segment-Level Competitor Threats
    type: matrix
    data_source: segment_competitor_threats

  - name: Consumer Pain Theme Table
    type: ranked_table
    data_source: voice_atom_table

  - name: Consumer Voice Processing Quality
    type: metric_cards
    data_source: consumer_voice_processing_summary

  - name: Voice Theme Cluster Map
    type: grouped_table
    data_source: voice_theme_clusters

  - name: Bain Driver Input Matrix
    type: matrix
    data_source: bain_driver_inputs

  - name: Journey Episode Signals
    type: journey_table
    data_source: journey_episode_inputs

  - name: Local Voice Source Map
    type: source_map_table
    data_source: local_voice_source_map

  - name: Raw Voice Storage and Compression Policy
    type: policy_table
    data_source: voice_storage_compression_policy

  - name: TOP1 Competitor and Previous Generation Voice Scope
    type: source_scope_table
    data_source: top1_previous_generation_voice_scope

  - name: Voice Collection Coverage Report
    type: coverage_table
    data_source: voice_collection_coverage_report

  - name: Bain NSS/NPS and Hardware Journey Seed Panel
    type: journey_matrix
    data_source: bain_nss_journey_seed_panel

  - name: Comment Collection Coverage
    type: coverage_table
    data_source: comment_collection_coverage_reports

  - name: TAM / SAM / SOM Assumption Tree
    type: funnel_or_tree
    data_source: tam_sam_som_assumption_tree

  - name: TAM / SAM / SOM Seed Ranges
    type: range_cards
    data_source: tam_sam_som_seed

  - name: Segment-Level Market Sizing
    type: stacked_range_table
    data_source: segment_level_tam_sam_som

  - name: Market Sizing Confidence
    type: scorecard
    data_source: market_sizing_confidence

  - name: Comparable-Market Proxy Notes
    type: evidence_table
    data_source: comparable_market_proxies

  - name: Segment Candidate Pool
    type: evidence_table
    data_source: segment_candidate_pool

  - name: Segment Evidence Strength
    type: scorecard_table
    data_source: segment_evidence_strength_scores

  - name: Segment Priority Table
    type: ranked_table
    data_source: segment_priority_ranking

  - name: Segment Distinctness Map
    type: matrix
    data_source: segment_distinctness_check

  - name: Persona Cards
    type: card_grid
    data_source: persona_cards

  - name: Segment Channel Touchpoint Map
    type: journey_matrix
    data_source: segment_channel_touchpoint_map

  - name: Channel Fit Scorecard
    type: scorecard_table
    data_source: channel_fit_scores

  - name: Retailer and Marketplace Candidates
    type: ranked_table
    data_source: retailer_marketplace_candidates

  - name: Content and Proof Map
    type: matrix
    data_source: content_proof_map

  - name: Price Corridor Seed Chart
    type: range_chart
    data_source: local_price_corridor

  - name: Price Anchor Panel
    type: ranked_table
    data_source: price_anchor_panel

  - name: Competitor Price Gap Table
    type: comparison_table
    data_source: competitor_price_gap_table

  - name: Segment Price Sensitivity Seeds
    type: scorecard_table
    data_source: segment_price_sensitivity_seeds

  - name: Value Proof Requirement Matrix
    type: matrix
    data_source: value_proof_requirement_matrix

  - name: Promotion and Subscription Sensitivity Seed
    type: matrix
    data_source: promotion_subscription_sensitivity_seed

  - name: NSS/NPS Proxy Composition
    type: stacked_bar
    data_source: nss_nps_proxy_seed_panel

  - name: Competitor NSS/NPS Comparison Seed
    type: comparison_bar
    data_source: competitor_nss_nps_comparison_seed

  - name: NPS Driver Tornado Seed
    type: tornado_chart
    data_source: nps_driver_tornado_seed

  - name: Journey Episode NSS Signals
    type: journey_table
    data_source: journey_episode_nss_seed

  - name: Earned Growth Proxy Seed
    type: scorecard_or_stacked_column
    data_source: earned_growth_proxy_seed

  - name: Net Promoter System Loop Seed
    type: loop_table
    data_source: net_promoter_system_loop_seed

  - name: Hardware Experience Diagnosis
    type: action_scorecard_table
    data_source: hardware_experience_diagnosis_seed

  - name: Next-Generation Marketing and Sales Seeds
    type: action_table
    data_source: next_generation_marketing_sales_seed
```

## Rendering Rules

- Show S01 as market context, not final strategy.
- Put evidence coverage and data gaps near the top.
- Mark proxy metrics clearly.
- Show NSS/NPS source mix, sample size, and proxy status next to any proxy score.
- Show NSS/NPS and Earned Growth as an action loop: score/status, driver, affected journey, owner hint, recommended action, confidence, and data gap.
- Keep local consumer language where it supports JTBD or messaging.
- Show comment collection as bounded coverage, not as "all local comments."
- Do not render full comment dumps; show themes, short permitted excerpts, source refs, and coverage notes.
- Mark Bain driver inputs as directional unless causal evidence or direct survey analysis exists.
- Mark segment and persona outputs as evidence-backed hypotheses when confidence is low or medium.
- Do not render demographic-only personas.
- Do not render user-planned channels as proven local channels unless local evidence supports them.
- Keep final budget allocation and KOL selection out of S01.
- Mark target price and internal price assumptions as hypotheses unless local price evidence supports them.
- Render TAM/SAM/SOM as ranges with assumption notes, not precise single-point truth.
- Mark earned growth as directional unless direct attribution evidence exists.
- Render hardware experience diagnosis as product and GTM hypotheses, not as confirmed roadmap commitments.
- Render next-generation marketing and sales recommendations with evidence refs and confidence; do not make them final copy, final channel strategy, or final sales scripts in S01.
- Do not hide low-confidence findings.
- Do not render price sensitivity seed output as final pricing recommendation.
