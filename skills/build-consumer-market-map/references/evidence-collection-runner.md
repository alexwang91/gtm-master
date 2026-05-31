# Evidence Collection Runner

Use this after Evidence Research Design. The runner executes collection jobs and turns gathered material into evidence records.

## Core Rules

- Do not synthesize market conclusions during collection.
- Do not hand off raw dumps.
- Do not silently ignore blocked, missing, stale, or low-quality sources.
- Use the least invasive approved connector path.
- Convert every useful source into a structured evidence record.
- Keep private and public evidence separated.
- Record readiness for Coverage Map.

## Runner Output

```json
{
  "collection_runner_output": {
    "collection_jobs": [],
    "evidence_records_created": [],
    "source_accessibility_matrix": [],
    "site_specific_comment_profiles": [],
    "comment_collection_coverage_reports": [],
    "failed_sources": [],
    "rag_index_manifest": {},
    "compressed_collection_summary": {},
    "ready_for_coverage_map": true,
    "readiness_notes": []
  }
}
```

## Depth Mode Job Selection

```yaml
quick:
  default_jobs:
    - local_source_discovery
    - competitor_discovery
    - price_intelligence
    - basic_review_mining
  optional_jobs:
    - local_voice_source_discovery
    - trend_signal_collection
    - market_size_research
  skip_by_default:
    - broad_consumer_discussion_mining
    - site_specific_comment_collection
    - channel_touchpoint_research
    - nss_nps_proxy_collection

standard:
  default_jobs:
    - local_source_discovery
    - local_voice_source_discovery
    - trend_signal_collection
    - competitor_discovery
    - price_intelligence
    - review_mining
    - consumer_discussion_mining
    - market_size_research
    - channel_touchpoint_research
  conditional_jobs:
    - site_specific_comment_collection
    - internal_file_extraction
    - nss_nps_proxy_collection

real_product_pilot:
  default_jobs:
    - all_standard_jobs
    - source_accessibility_mapping
    - competitor_candidate_review_gate
  conditional_jobs:
    - site_specific_comment_collection_for_reviewed_top1_competitor
    - previous_generation_voice_collection_when_available
    - internal_file_extraction
  skip_by_default:
    - broad_unreviewed_category_comment_collection
    - broad_S13_external_lookup

deep:
  default_jobs:
    - all_standard_jobs
    - second_pass_competitor_discovery
    - broader_review_mining
    - broader_consumer_discussion_mining
    - site_specific_comment_collection
    - deeper_channel_touchpoint_research
    - nss_nps_proxy_collection
  conditional_jobs:
    - internal_file_extraction
```

## Collection Job Schema

```json
{
  "job_id": "",
  "job_type": "",
  "evidence_need": "",
  "depth_mode": "quick | standard | real_product_pilot | deep",
  "connector_slot": "",
  "queries_or_sources": [],
  "source_screening_criteria_ref": "",
  "target_extraction_schema": "",
  "status": "success | partial | failed | skipped",
  "records_created": [],
  "sources_failed": [],
  "limitations": [],
  "next_action": "continue | retry_with_fallback | mark_gap | ask_user"
}
```

## Job Types

### local_source_discovery

Collect:

- Candidate search engines, marketplaces, retailers, price comparison sites, deal forums, review sites, forums, communities, video/social platforms, official statistics sources.

Sources:

- Local SERP
- Related searches
- "top retailers / price comparison sites / forums" queries
- Category review pages
- Competitor pages

Output:

- `local_source_map`
- `source_accessibility_matrix`
- `source_quality_scores`
- `failed_sources`

Minimum viable:

- At least one candidate source for price, competitor, review/voice, and market/category context, or explicit data gaps.

### local_voice_source_discovery

Collect:

- Country-specific forums
- Specialist media comment areas
- Deal forums and local shopping communities
- Marketplace or retailer review hubs
- Video review comment sources
- Public social threads where permitted
- App store review sources
- Q&A pages
- Brand or support communities
- Local Reddit-style or country-specific equivalents

Sources:

- Local-language SERP
- Related searches
- Source discovery queries from `localization-preflight.md`
- Product, competitor, previous-generation, complaint, comparison, and alternative terms
- High-value domains revealed by first-pass competitor and review search

Output:

- `local_voice_source_map`
- `source_accessibility_matrix`
- `site_specific_collection_candidates`
- `source_quality_scores`
- `failed_sources`

Minimum viable:

- At least 3 candidate local voice sources in standard/deep mode, or an explicit `local_voice_source_gap`.
- Each candidate should include source family, country relevance, category relevance, local voice source fit score, access status, and recommended use.
- Do not declare consumer voice unavailable until this job has run or been explicitly skipped by depth mode or access limits.

### source_accessibility_mapping

Build this for every source likely to affect competitor choice, voice mining, price anchors, or channel priority.

```json
{
  "source_accessibility_matrix": [
    {
      "source_name": "",
      "source_url_or_path": "",
      "source_type": "marketplace | retailer | price_comparison | forum | specialist_media | video | app_store | social | official_data | other",
      "country_relevance": "high | medium | low",
      "access_status": "accessible | partial | blocked | login_required | paywalled | policy_restricted | unknown",
      "expected_record_depth": "none | low | medium | high",
      "allowed_collection_level": "source_profile_only | snippets | voice_atoms | structured_records | manual_upload_only | unavailable",
      "connector_slot": "",
      "fallback_path": "",
      "deep_collection_candidate": false,
      "limitations": [],
      "evidence_refs": []
    }
  ]
}
```

Use this matrix before promising comprehensive local comment collection. If a source is blocked or policy-restricted, preserve it as an important data gap rather than trying to bypass access.

### trend_signal_collection

Collect:

- Related queries
- Rising queries
- Relative interest among category, feature, competitor, and complaint terms
- Local-language term variants

Sources:

- Google Trends-style source when available
- SERP related searches
- Marketplace autocomplete where permitted
- Competitor and review language fallback

Output:

- `trend_signal_evidence`
- `feature_to_local_language_map` updates
- `search_query_seed_pack` updates

Minimum viable:

- Directional signal or explicit `trend_signal_unavailable`.

### competitor_discovery

Collect:

- Direct competitors
- Substitutes
- Premium anchors
- Budget anchors
- Ecosystem anchors
- Previous-generation alternatives when relevant

Sources:

- Local SERP
- Marketplaces
- Retailers
- Price comparison sites
- Expert reviews and rankings
- Forums and comparison discussions
- Internal benchmark if provided

Output:

- `competitor_candidate_review_list`
- `competitor_evidence`
- `competitor_substitute_map`
- candidates for `competitor_threat_scores`

Minimum viable:

- 5-10 potential competitors or substitutes for user calibration in standard/deep mode when review mode allows it.
- 3-5 relevant competitors or substitutes in quick mode, or fewer with explicit data gaps.
- Top competitor candidates require at least two local evidence signals unless marked as hypothesis.

### price_intelligence

Use `price-anchor-sensitivity-seed.md` when converting collected prices into corridor, anchor, gap, sensitivity, and proof-requirement outputs.

Collect:

- List price
- Sale price
- Discount range
- Promo floor
- Bundle offers
- Subscription or recurring costs
- Shipping/tax visibility
- Financing/installment cues
- Channel price differences
- Previous-generation, used, refurbished, and cross-tier anchors when relevant
- Local price display context and promotion norms
- User-provided price assumptions when available

Sources:

- Retailer pages
- Marketplaces
- Price comparison sites
- Competitor official pages
- Deal forums
- Internal previous-generation data if provided

Output:

- `price_evidence`
- `local_price_corridor`
- `price_anchor_panel`
- `competitor_price_gap_table`
- `segment_price_sensitivity_seeds`
- `value_proof_requirement_matrix`
- `promotion_subscription_sensitivity_seed`
- `user_provided_price_hypotheses`

Minimum viable:

- At least three local price anchors in standard mode, or a clear price coverage gap.
- At least one budget/mainstream/premium or previous-generation anchor when available, or explicit price ladder gap.
- User target price classified against local anchors as hypothesis, validated, weakly supported, or contradicted.

### review_mining

Collect:

- Ratings
- Review text
- Verified buyer signal when available
- Praise
- Complaints
- Price objections
- Feature confusion
- Return or refund intent
- Recommendation language

Sources:

- Marketplace reviews
- Retailer reviews
- Expert review comments where useful
- App reviews when product has an app
- Site-specific comment profiles when a high-value source was discovered and collection is permitted
- User-uploaded reviews, NSS/NPS, or customer voice

Output:

- `review_evidence`
- `voice_atoms`
- `nss_nps_proxy_inputs`

Minimum viable:

- Enough review/voice evidence to identify initial pain themes, or explicit consumer voice gap.

### consumer_discussion_mining

Collect:

- Forum discussions
- Social posts/comments where permitted
- Video comments
- Community language
- Objections
- Workarounds and substitutes
- Local slang and category vocabulary

Sources:

- Local forums
- Reddit or local equivalent
- YouTube comments
- Public social discussions where permitted
- Deal forums
- Site-specific comment profiles when a local forum, specialist media comment area, or deal community is high value

Output:

- `social_evidence`
- `voice_atoms`
- `channel_touchpoint_candidates`

Minimum viable:

- Directional voice and vocabulary signals, or explicit social/community gap.

### site_specific_comment_collection

Use `site-specific-comment-collection.md` for the full profile, enumeration, extraction, coverage, export, and handoff rules.

Collect:

- Site profiles for selected high-value local voice sources
- Thread discovery results for the product, competitors, substitutes, and previous-generation products
- Accessible pagination or comment range enumeration
- Comment records where permitted
- Voice atoms derived from comments
- NSS/NPS proxy and Bain-style driver inputs where confidence gates allow it
- Completeness and access coverage reports

Sources:

- Candidate sources from `local_voice_source_discovery`
- Local forums and specialist media comment sections
- Deal forums and local shopping communities
- Marketplace, retailer, app store, Q&A, video, and public social comment sources where permitted
- User-uploaded exports for sources that cannot be accessed automatically

Output:

- `site_specific_comment_profiles`
- `comment_records`
- `comment_collection_coverage_reports`
- `voice_atoms`
- `nss_bain_inputs`
- `comment_export_refs`
- `failed_sources`

Minimum viable:

- A site profile and coverage report for every selected high-value source, even if extraction is blocked.
- `comments_index.md` or equivalent refs for collected threads.
- Voice atoms only when usage permission allows short excerpt or structured extraction.
- No full comment dump in the handoff pack.

Run criteria:

- Run by default in `deep` mode for primary local voice sources.
- Run in `standard` mode when consumer voice coverage is thin, the source fit score is 80+, or a previous-generation/competitor thread is clearly decision-critical.
- Skip in `quick` mode unless the user explicitly requests comment-level collection.

### market_size_research

Use `market-sizing-tam-sam-som-seed.md` when converting market size evidence into TAM/SAM/SOM seed ranges, assumption trees, comparable-market proxies, segment-level sizing, and market sizing confidence.

Collect:

- Population or household basis
- Category incidence or penetration proxies
- Relevant demographic or need incidence
- Device ownership or category adoption proxies
- Public market report excerpts
- Internal historical sales if provided
- Comparable-market benchmark inputs when direct local evidence is thin
- Channel reachability and price-band affordability proxies when available
- User-provided market sizing assumptions when available

Sources:

- Official statistics
- Public market reports
- Industry summaries
- Marketplace rankings as weak proxy
- Internal commercial data

Output:

- `market_size_evidence`
- `tam_sam_som_inputs`
- `tam_sam_som_seed`
- `tam_sam_som_assumption_tree`
- `segment_level_tam_sam_som`
- `comparable_market_proxies`
- `market_sizing_confidence`
- `market_sizing_data_gaps`

Minimum viable:

- Enough inputs for an assumption tree, not a precise market size claim.
- Explicit confidence cap when the model relies on comparable markets, marketplace rankings, search interest, or social buzz.

### channel_touchpoint_research

Use `channel-touchpoint-mapping.md` for channel stages, channel fit scoring, retailer/marketplace candidate mapping, content proof mapping, and user-provided channel hypothesis handling.

Collect:

- Discovery channels
- Comparison channels
- Purchase channels
- Complaint channels
- Proof and trust touchpoints
- Support, return, and warranty touchpoints
- Retention and advocacy touchpoints
- Creator/expert types
- Content formats
- Retail/channel availability
- Retailer and marketplace candidate evidence
- User-provided channel plan evidence when available

Sources:

- SERP
- Marketplace and retailer pages
- Expert review sites
- Video/social platforms
- Deal forums
- Competitor landing pages and ads
- Uploaded historical ads, KOL briefs, landing pages, creatives

Output:

- `channel_touchpoint_evidence`
- `channel_touchpoint_map`
- `segment_channel_touchpoint_map`
- `retailer_marketplace_candidates`
- `content_proof_map`
- `channel_fit_scores`
- `user_provided_channel_hypotheses`

Minimum viable:

- Directional map of discovery, comparison, purchase, proof/trust, complaint/support, and retention/advocacy touchpoints.
- At least one purchase-path or price-comparison candidate and one proof/trust candidate in standard mode, or explicit gaps.

### nss_nps_proxy_collection

Use `nss-nps-earned-growth-seed.md` when converting surveyed NSS/NPS, public voice, internal voice, Bain drivers, and journey episodes into NSS/NPS and Earned Growth seed outputs.

Collect:

- Direct NSS/NPS if uploaded
- Recommendation language
- Referral or repurchase language
- Detractor language
- Refund/return/switching intent
- Strong satisfaction and dissatisfaction drivers
- Earned growth signals: referral, repeat, organic/direct, community, word-of-mouth
- Bought growth signals when internal or public channel evidence is available
- Journey episode close-loop candidates
- Hardware experience diagnosis signals: design, performance, reliability, setup, app/connectivity, durability, warranty, service, price-value, and channel friction
- Next-generation marketing and sales action seeds: proof needs, claims to avoid, sales objections, channel training, and validation tests

Sources:

- Uploaded NSS/NPS or customer voice
- Reviews
- App reviews when relevant
- Forums and public comments

Output:

- `nss_nps_proxy_inputs`
- `nss_nps_proxy_seed_panel`
- `competitor_nss_nps_comparison_seed`
- `nps_driver_tornado_seed`
- `journey_episode_nss_seed`
- `earned_growth_proxy_seed`
- `net_promoter_system_loop_seed`
- `hardware_experience_diagnosis_seed`
- `next_generation_marketing_sales_seed`
- `earned_growth_seed_notes`

Minimum viable:

- Only calculate proxy if confidence gate passes. Otherwise record data gap and output directional driver/journey signals.
- Earned growth seed may be directional only unless attribution or repeat/referral data is available.

### internal_file_extraction

Collect:

- Product specs
- Previous-generation sales, price, channel performance
- Customer reviews, NSS/NPS, customer voice
- Brand positioning and tone
- Competitor benchmark and channel plan
- Historical ads, KOL, landing pages, creative assets

Sources:

- User-uploaded private files

Output:

- `internal_private_evidence`
- Updates to product capability map, competitor map, pricing context, customer voice, brand constraints, and channel context

Minimum viable:

- Structured summary of decision-relevant internal evidence and explicit private-use policy.

## Skip Rules

Skip a job when:

- Its evidence need is not relevant to the product or depth mode.
- The required source category is unavailable and a fallback is enough.
- The job would require prohibited collection.
- The user has not approved private or sensitive source use.

Record skipped jobs with reason.

## Failure Rules

Mark a job as failed or partial when:

- Sources are blocked, login-gated, paywalled, or terms-restricted.
- Results are from the wrong country without comparable-market rationale.
- Sources are stale for price, channel, competitor, or creator decisions.
- Extraction confidence is too low.
- The source has high bias risk and no corroboration.

Create `failed_sources` and data gaps instead of fabricating.

## Ready for Coverage Map

Set `ready_for_coverage_map` to true when:

- Collection jobs have recorded status.
- Evidence records have `evidence_id`, source category, source ref, country/region, confidence, and limitations.
- Site-specific comment jobs have coverage reports and export refs when they ran.
- Failed or skipped jobs are logged.
- Compressed collection summary exists.
- Any RAG index manifest needed for long evidence is created or explicitly skipped.

If not ready, state the blocking gap and recommended next action.
