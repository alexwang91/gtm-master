---
name: build-consumer-market-map
description: Builds S01 localized consumer market context for the GTM intelligence report suite from product specs, launch country or region, and target price range. Use for 2C hardware market mapping, local competitor and substitute discovery, consumer voice mining, TAM/SAM/SOM seed analysis, initial segmentation, channel and touchpoint mapping, price anchor panels, NPS/NSS proxy seed panels, evidence logs, compressed handoff packs, and HTML report section drafts. This skill is the first analysis skill after gtm-master and should preserve evidence provenance, quantify judgments with rubrics, and hand off compressed context to downstream GTM skills.
---

# Build Consumer Market Map

## Role

Use this skill as S01 in the GTM intelligence report suite. It creates the market fact layer for a specific hardware product, country or region, and target price range.

S01 must preserve the full methodology in `references/methodology.md`; do not remove required analysis steps. The operational change is that every step must produce structured, evidence-backed, quantified outputs that can be handed off without forcing downstream skills to reread the full artifact.

## Required Inputs

Ask only for missing critical fields:

```json
{
  "product_features_and_specs": "",
  "launch_country_or_region": "",
  "target_price_range": ""
}
```

Optional high-value private inputs:

```json
{
  "product_specification_files": [],
  "previous_generation_sales_price_channel_performance": "",
  "customer_reviews_and_nss_or_nps": "",
  "brand_positioning_self_perception_and_tone": "",
  "competitor_list_internal_benchmark_channel_plan": "",
  "historical_ads_kol_landing_pages_and_creatives": ""
}
```

## Load Order

Read only what the current task needs:

1. Read `references/output-contract.md` before producing any artifact, handoff, or report section.
2. Read `references/module-additions.md` when executing Product-Market Search Preflight, Coverage Map, Voice Atom Table, Competitor Threat Score, Segment Distinctness Check, or Handoff Pack.
3. Read `references/localization-preflight.md` before assuming local marketplaces, retailers, price comparison sites, forums, social platforms, languages, price display norms, or compliance constraints.
4. Read `references/site-specific-comment-collection.md` before declaring local consumer voice unavailable, selecting high-value forums/comment sources, enumerating thread pages, exporting comment archives, or building NSS/NPS proxy inputs from public comments.
5. Read `references/consumer-voice-nss-bain-pipeline.md` before converting reviews/comments/surveys/support text into voice atoms, theme clusters, NSS/NPS proxy inputs, Bain driver inputs, or journey episode inputs.
6. Read `references/market-sizing-tam-sam-som-seed.md` before building TAM/SAM/SOM seed ranges, assumption trees, segment-level market sizing, comparable-market proxies, market sizing confidence, or user-provided market sizing hypotheses.
7. Read `references/segment-persona-inference.md` before creating segment candidates, segment seed packs, segment priority rankings, segment distinctness results, persona cards, or segment-level channel maps.
8. Read `references/channel-touchpoint-mapping.md` before mapping discovery, comparison, purchase, proof/trust, complaint/support, retention/advocacy touchpoints, retailer/marketplace candidates, content proof needs, channel fit scores, or user-provided channel hypotheses.
9. Read `references/price-anchor-sensitivity-seed.md` before building local price corridor, price anchor panel, competitor price gap table, segment price sensitivity seeds, value proof requirements, promotion/subscription sensitivity, or user-provided price hypotheses.
10. Read `references/nss-nps-earned-growth-seed.md` before building NSS/NPS proxy seed panels, competitor NSS/NPS comparison seed, NPS driver tornado seed, journey episode NSS seed, earned growth proxy seed, Net Promoter System loop seed, hardware experience diagnosis, next-generation marketing/sales recommendation seeds, or earned growth notes.
11. Read `references/scoring-rubrics.md` only when a score is required by the active step.
12. Read `references/evidence-research-design.md` only before planning evidence collection, query expansion, source screening, result fusion, extraction schemas, or stop rules.
13. Read `references/evidence-collection-runner.md` before executing collection jobs or converting gathered material into evidence records.
14. Read `references/mcp-connectors.md` only when planning or executing web, MCP, crawling, browser, review, price, social, or internal-data collection.
15. Read `references/evidence-storage-policy.md` only when saving evidence, logs, artifacts, private files, excerpts, comment exports, or handoff evidence refs.
16. Read `references/coverage-and-source-quality.md` before judging evidence coverage, source reliability, confidence caps, or whether to loop back to collection.
17. Read `references/competitor-substitute-mapping.md` before finalizing competitor candidates, substitute taxonomy, competitor roles, segment threats, or top competitor ranking.
18. Read `references/local-search-trends-strategy.md` only when using Google Trends-style data, search-language discovery, autocomplete, or related-query sources.
19. Read `references/html-visual-block-generation.md` before producing S14-ready `visual_blocks` for the HTML market section draft.
20. Read `references/html-section-contract.md` only before producing the HTML market section draft.
21. Read `references/methodology.md` only when a step needs the complete original method.
22. Use `references/original-skill-spec.md` only as source preservation or audit reference.

## Depth Modes

Choose the lightest mode that satisfies the task:

```text
quick
  Produce product-market preflight, basic evidence plan, 3-5 competitor/substitute anchors, initial segment seeds, top data gaps, and a compact handoff. Skip deep trends, iterative retrieval, NSS/NPS proxy, and detailed TAM unless requested.

standard
  Run the full S01 market context workflow once, including local voice source discovery, coverage map, source ranking, competitor threat score, voice atoms, TAM/SAM/SOM seed, segment distinctness, price seed, and HTML section draft.

deep
  Add iterative retrieval, broader local-language expansion, trend-source comparison, site-specific forum/comment enumeration for high-value sources where permitted, NSS/NPS proxy confidence, and richer evidence logs.
```

Default to `standard` for a normal GTM suite run. Use `quick` when the user is exploring or time is limited. Use `deep` only when the user asks for a deeper report, the evidence is thin, or the decision is high stakes.

## Execution Workflow

Follow this sequence. Do not skip the original methodology steps; the added modules make the process measurable and handoff-safe.

```text
1. Build Product-Market Search Preflight
2. Build Local Market Localization Preflight
3. Build Evidence Research Design and MCP routing plan
4. Run Evidence Collection Runner through approved tools
4A. Profile high-value local voice sources and enumerate comments when needed
5. Build Coverage Map
6. Score source quality
7. Build competitor and substitute map
8. Score competitor threat
9. Process consumer voice into atoms, theme clusters, NSS/NPS proxy inputs, Bain driver inputs, and journey episodes
10. Build local consumer opinion map
11. Build Voice Atom Table
12. Estimate TAM / SAM / SOM
13. Infer segment candidates and segment seed pack from evidence
14. Build consumer segments
15. Run Segment Distinctness Check
16. Build persona cards
17. Map channels and touchpoints
18. Analyze local price sensitivity as a seed panel
19. Build NSS/NPS and Earned Growth seed panel, including hardware diagnosis and next-generation GTM action seeds
20. Recommend initial GTM priorities
21. Report evidence, assumptions, and data gaps
22. Produce Handoff Pack
23. Produce HTML section draft with S14-ready visual blocks
```

## Scope Boundary

S01 may produce initial GTM recommendations, but it is not the final strategy skill.

S01 owns:

- Local market fact layer
- Product-Market Search Preflight: product capability normalization, category selling point comparison, local search language map, and query seeds
- Local Market Localization Preflight: local language, search engine, marketplace, retailer, price comparison, review, community, social, price display, tax/shipping, payment, returns, warranty, seasonality, and claim-context discovery
- Evidence Research Design: research perspectives, evidence needs, query expansion, MCP routing, screening, extraction schemas, result fusion, and stop rules
- Evidence Collection Runner: local source discovery, trend signals, competitors, prices, reviews, consumer discussion, market size, channels, and internal file extraction
- Local voice source discovery and site-specific comment collection profiles for country-specific forums, specialist media comments, deal communities, video comments, marketplace reviews, app reviews, public social threads, and similar sources where permitted
- Local evidence storage, source classification, and collection logs
- Competitor and substitute mapping: candidate pool, role classification, substitute taxonomy, segment-level threats, and top competitor ranking
- Competitor and substitute map
- Consumer voice processing: source-item normalization, voice atom extraction, deduplication, theme clustering, NSS/NPS proxy classification, Bain driver inputs, and journey episode inputs
- Consumer opinion map and voice atoms
- TAM/SAM/SOM seed model: evidence-backed ranges, assumption tree, segment-level sizing, comparable-market proxies, market sizing confidence, and user-provided market sizing hypotheses
- Segment and persona inference: segment candidate generation, evidence strength scoring, segment seed pack, priority ranking, distinctness, and persona cards
- Channel and touchpoint mapping: discovery, comparison, purchase, proof/trust, complaint/support, retention/advocacy stages; retailer/marketplace candidates; content proof needs; channel fit scoring; user-provided channel hypotheses
- Price anchor and sensitivity seed panel: local price corridor, anchor panel, competitor price gaps, segment sensitivity seeds, value proof requirements, promotion/subscription sensitivity, and user-provided price hypotheses
- NSS/NPS and earned growth seed panel: surveyed/proxy status, source mix, proxy confidence, competitor comparison seed, driver tornado seed, journey episode seed, earned growth proxy seed, loop candidates, hardware experience diagnosis, and next-generation marketing/sales recommendation seeds
- Market context handoffs

S01 does not own:

- Final JTBD scenario system
- Final message architecture
- Full pricing model
- Creative asset scoring
- KOL or creator selection
- DTC conversion prediction
- Launch demand forecast
- Final HTML composition

## Required Output

Always return the S01 output envelope from `references/output-contract.md`:

```json
{
  "full_artifact": {},
  "compressed_handoff_pack": {},
  "html_section_draft": {},
  "evidence_updates": [],
  "decision_updates": [],
  "data_gaps": [],
  "post_skill_isolation_record": {},
  "recommended_next_skills": []
}
```

## Quality Rules

- Preserve source provenance for all evidence.
- Label every major conclusion with evidence level and confidence.
- Use rubrics for scoring; do not rely on vague impressions.
- Store evidence as structured records first; use RAG only as a retrieval layer.
- Keep private and public evidence separated in storage and retrieval.
- Keep original local-language consumer wording where useful.
- Do not claim a local forum, community, or comment source was collected completely unless a coverage report proves the bounded page/comment range.
- Do not hand off raw comment dumps; hand off source profile refs, coverage refs, voice atom refs, and NSS/Bain input refs.
- Do not present inferred NSS/NPS proxy as surveyed NSS/NPS.
- Do not calculate NSS/NPS proxy from atom counts alone; classify deduped source items and report thresholds, source mix, and confidence.
- Do not claim earned growth potential unless recommendation, referral, repeat, organic, community, and detractor-drag signals support it.
- Do not stop NSS/NPS analysis at a score; every high-impact driver should become a closed-loop candidate, product diagnosis, GTM proof need, sales enablement need, or explicit data gap.
- Do not create segments from demographics alone; each segment needs evidence-backed motivation, use case, price behavior, channel behavior, or objection differences.
- Do not treat user-planned channels as locally proven channels; preserve them as hypotheses until local evidence supports them.
- Do not treat the user target price as locally validated; test it against local anchors, price complaints, segment sensitivity, and required proof.
- Do not present TAM/SAM/SOM as precise when assumptions are weak.
- Do not treat search volume, marketplace ranking, or social buzz as direct market size; label them as proxies or context only.
- Do not fabricate evidence when search, MCP, crawling, browsing, or private data is unavailable.
- If the handoff pack is incomplete, mark the missing fields explicitly.
