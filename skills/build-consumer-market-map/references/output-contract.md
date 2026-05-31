# S01 Output Contract

S01 must produce a full artifact for humans, a compressed handoff pack for downstream skills, and an HTML section draft for the final dashboard.

## Output Envelope

```json
{
  "skill_id": "S01",
  "skill_name": "build-consumer-market-map",
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

## HTML Section Draft Requirement

`html_section_draft` must follow `references/html-section-contract.md` and include S14-ready `visual_blocks` in standard and deep mode. The draft is incomplete if it only contains prose, metric cards, or generic tables.

Read `references/html-visual-block-generation.md` before deriving these blocks from S01 scores and evidence fields.

Minimum S01 visual coverage:

```text
evidence coverage gate
product capability to local selling-point fit
competitor/substitute threat
local price corridor seed
segment priority and evidence strength
segment channel/touchpoint fit
```

If any minimum view is missing, add `missing_required_view` or `rendered_too_thin` to `html_section_draft.data_gaps` and to the top-level `data_gaps`.

## Full Artifact

```json
{
  "artifact_id": "A01.market-context-full-artifact",
  "title": "Consumer Market Map: [Product] in [Country]",
  "format": "markdown_with_structured_json_blocks",
  "sections": [
    "executive_summary",
    "product_capability_summary",
    "category_selling_point_and_local_search_language_map",
    "local_market_localization_preflight",
    "evidence_research_design",
    "evidence_collection_runner",
    "source_accessibility_matrix",
    "local_voice_source_map",
    "site_specific_comment_collection",
    "evidence_storage_and_collection_log",
    "coverage_map",
    "source_quality_scores",
    "competitor_and_substitute_map",
    "competitor_candidate_review_gate",
    "competitor_threat_scores",
    "consumer_voice_processing_summary",
    "consumer_opinion_map",
    "voice_atom_table",
    "voice_theme_clusters",
    "nss_nps_proxy_classification_table",
    "bain_driver_inputs",
    "journey_episode_inputs",
    "market_sizing_evidence_summary",
    "tam_sam_som_assumption_tree",
    "comparable_market_proxies",
    "market_sizing_confidence",
    "tam_sam_som_summary",
    "segment_candidate_pool",
    "segment_evidence_strength_scores",
    "segment_priority_table",
    "segment_distinctness_check",
    "persona_cards",
    "channel_touchpoint_map",
    "segment_channel_touchpoint_map",
    "retailer_marketplace_candidates",
    "content_proof_map",
    "channel_fit_scores",
    "local_price_corridor",
    "price_anchor_panel",
    "competitor_price_gap_table",
    "segment_price_sensitivity_seeds",
    "value_proof_requirement_matrix",
    "promotion_subscription_sensitivity_seed",
    "price_anchor_and_sensitivity_seed_panel",
    "competitor_nss_nps_comparison_seed",
    "nps_driver_tornado_seed",
    "journey_episode_nss_seed",
    "earned_growth_proxy_seed",
    "net_promoter_system_loop_seed",
    "hardware_experience_diagnosis_seed",
    "next_generation_marketing_sales_seed",
    "nss_nps_and_earned_growth_seed_panel",
    "initial_gtm_recommendation",
    "evidence_assumptions_and_data_gaps"
  ]
}
```

## Compressed Handoff Pack

```json
{
  "handoff_id": "H01.market-context-pack",
  "from_skill": "S01.build-consumer-market-map",
  "to_skills": [
    "S02.mine-jtbd-scenarios",
    "S04.model-price-sensitivity",
    "S08.forecast-launch-demand",
    "S14.compose-html-gtm-dashboard"
  ],
  "summary": "",
  "canonical_fields": {
    "product_capability_map": {},
    "category_selling_point_map": [],
    "feature_to_local_language_map": [],
    "selling_point_fit_scores": [],
    "search_query_seed_pack": {},
    "localization_preflight": {},
    "local_source_map": {},
    "local_voice_source_map": {},
    "source_accessibility_matrix": [],
    "evidence_research_design": {},
    "evidence_collection_summary": {},
    "evidence_storage_summary": {},
    "site_specific_comment_profiles": [],
    "comment_collection_coverage_reports": [],
    "comment_export_refs": [],
    "rag_index_manifest_ref": "",
    "compressed_collection_summary": {},
    "coverage_summary": {},
    "source_quality_summary": {},
    "confidence_caps": {},
    "top_competitors_and_substitutes": [],
    "competitor_candidate_review_list": [],
    "competitor_candidate_review_gate": {},
    "competitor_threat_scores": [],
    "substitute_taxonomy": [],
    "price_ladder_scan": [],
    "jump_decision_risks": [],
    "segment_competitor_threats": [],
    "consumer_voice_processing_summary": {},
    "voice_atom_refs": [],
    "voice_theme_clusters": [],
    "nss_nps_proxy_classification_table_ref": "",
    "nss_bain_input_refs": [],
    "bain_driver_inputs": [],
    "journey_episode_inputs": [],
    "pain_theme_clusters": [],
    "purchase_triggers": [],
    "objections": [],
    "market_sizing_evidence_summary": {},
    "tam_sam_som_seed": {},
    "tam_sam_som_assumption_tree": [],
    "comparable_market_proxies": [],
    "market_sizing_confidence": {},
    "market_sizing_data_gaps": [],
    "segment_candidate_pool": [],
    "segment_evidence_strength_scores": [],
    "segment_seed_pack": [],
    "segment_priority_ranking": [],
    "segment_distinctness_results": [],
    "persona_cards": [],
    "segment_level_tam_sam_som": [],
    "segment_channel_touchpoint_map": [],
    "channel_touchpoints": [],
    "retailer_marketplace_candidates": [],
    "content_proof_map": [],
    "channel_fit_scores": [],
    "user_provided_channel_hypotheses": [],
    "local_price_corridor": {},
    "price_anchor_panel": {},
    "competitor_price_gap_table": [],
    "segment_price_sensitivity_seeds": [],
    "value_proof_requirement_matrix": [],
    "promotion_subscription_sensitivity_seed": [],
    "user_provided_price_hypotheses": [],
    "price_complaints": [],
    "nss_nps_proxy_seed_panel": {},
    "competitor_nss_nps_comparison_seed": [],
    "nps_driver_tornado_seed": [],
    "journey_episode_nss_seed": [],
    "earned_growth_proxy_seed": {},
    "net_promoter_system_loop_seed": {},
    "hardware_experience_diagnosis_seed": [],
    "next_generation_marketing_sales_seed": {},
    "earned_growth_seed_notes": {},
    "initial_gtm_priorities": []
  },
  "key_findings": [],
  "required_downstream_use": [
    "S02 should use voice_atom_refs, source accessibility, comment coverage refs, pain_theme_clusters, purchase_triggers, objections, and segment_seed_pack.",
    "S02 should preserve hardware experience diagnosis and next-generation recommendation seeds when turning consumer evidence into JTBD scenarios.",
    "S04 should use local_price_corridor, price_anchor_panel, competitor price gap table, value proof requirements, promotion/subscription sensitivity seed, competitor threat scores, price complaints, and segment price sensitivity seeds.",
    "S03 should use next-generation marketing and sales seeds only after S02 has connected them to JTBD scenarios and proof needs.",
    "S08 should use tam_sam_som_seed, segment priority ranking, channel touchpoints, channel fit scores, and conversion assumptions.",
    "S12 should use hardware diagnosis and Net Promoter loop seeds when post-launch review/support data exists.",
    "S14 should render html_section_draft, confidence badges, citations, and data gap notes."
  ],
  "do_not_reopen": [
    "Do not redesign the competitor universe unless a blocking omission is found.",
    "Do not treat S01 price sensitivity as the final pricing model.",
    "Do not treat S01 NSS/NPS proxy as surveyed NSS/NPS."
  ],
  "open_questions": [],
  "data_gaps": [],
  "full_artifact_ref": ""
}
```

## Evidence Update

```json
{
  "evidence_id": "",
  "evidence_type": "competitor | price | review | social_discussion | site_profile | comment_record | comment_coverage_report | nss_bain_input | market_size | internal_sales | internal_customer_voice | benchmark | other",
  "country_or_region": "",
  "language": "",
  "source_name": "",
  "source_url_or_path": "",
  "collected_at": "",
  "tool_or_connector_used": "",
  "claim_supported": "",
  "confidence": "high | medium | low",
  "limitations": []
}
```

## Recommended Next Skills

```json
[
  {
    "skill_id": "S02",
    "reason": "JTBD scenario mining needs consumer voice atoms and pain clusters.",
    "priority": "required | recommended | optional",
    "blocking_data_gaps": []
  }
]
```
