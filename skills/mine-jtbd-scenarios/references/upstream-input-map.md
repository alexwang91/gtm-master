# S02 Upstream Input Map

Use this before S02 starts analysis. It answers where each S02 input comes from and what to do when it is missing.

S02 normally receives one object from S01:

```text
S01 compressed_handoff_pack.canonical_fields
```

Do not assume a field exists because S01 "should have" produced it. Check it, record coverage, and either proceed, downgrade confidence, retrieve targeted evidence, or return a data gap.

## Required Input Groups

```json
{
  "required_input_groups": [
    "consumer_voice_signals",
    "segment_signals",
    "price_signals",
    "proof_signals",
    "channel_signals",
    "competitor_and_substitute_signals",
    "journey_and_nss_driver_signals",
    "local_language_signals",
    "product_capability_fit_signals",
    "market_commercial_weight_signals",
    "evidence_quality_signals",
    "brand_claim_constraint_signals"
  ]
}
```

## Field Map

### Consumer Voice Signals

From S01:

```text
voice_atom_refs
voice_theme_clusters
consumer_opinion_map
pain_theme_clusters
purchase_triggers
objections
comment_collection_coverage_reports
```

Use for:

- JTBD candidate extraction
- Trigger context
- Barriers/anxieties
- Local wording
- Anti-JTBD risks

Missing behavior:

- If `voice_atom_refs` and `voice_theme_clusters` are both missing, S02 cannot produce high-confidence JTBD scenarios.
- Use `purchase_triggers` and `objections` as a weaker fallback.
- If all are missing, stop scenario ranking and return a data gap.

### Segment Signals

From S01:

```text
segment_candidate_pool
segment_seed_pack
segment_priority_ranking
segment_evidence_strength_scores
segment_distinctness_results
persona_cards
segment_level_tam_sam_som
segment_competitor_threats
```

Use for:

- Scenario-to-segment matrix
- Segment relevance
- Scenario priority
- Persona-adjacent context without turning personas into jobs

Missing behavior:

- If `segment_seed_pack` is missing but voice evidence exists, S02 may infer temporary scenario audiences and mark them `segment_gap`.
- If user provided a strategic segment, preserve it as `hypothesis_only`.
- Do not create demographic-only segments inside S02.

### Price Signals

From S01:

```text
local_price_corridor
price_anchor_panel
competitor_price_gap_table
segment_price_sensitivity_seeds
value_proof_requirement_matrix
promotion_subscription_sensitivity_seed
price_complaints
user_provided_price_hypotheses
```

Use for:

- Scenario price implication seed
- Price-value barriers
- Premium justification needs
- Subscription/promo resistance
- S04 handoff

Missing behavior:

- If local price evidence is missing, do not score price credibility.
- If only user target price exists, label price implications as `user_hypothesis`.
- Hand off price gaps to S04 instead of inventing WTP.

### Proof Signals

From S01:

```text
content_proof_map
value_proof_requirement_matrix
bain_driver_inputs
nps_driver_tornado_seed
hardware_experience_diagnosis_seed
next_generation_marketing_sales_seed
net_promoter_system_loop_seed
earned_growth_seed_notes
```

Use for:

- Proof requirement seed
- Claims to avoid
- Scenario message seed
- Product capability fit
- Next-generation GTM implications

Missing behavior:

- If proof signals are missing, S02 may still produce scenarios but must mark proof status as `missing`.
- Do not convert a scenario into a message angle without a proof requirement.

### Channel Signals

From S01:

```text
channel_touchpoints
segment_channel_touchpoint_map
retailer_marketplace_candidates
channel_fit_scores
content_proof_map
local_voice_source_map
user_provided_channel_hypotheses
```

Use for:

- Scenario-to-channel/touchpoint mapping
- Reachability component in scenario priority
- Retailer/marketplace objection context
- S03/S07/S14 handoff

Missing behavior:

- If channel evidence is missing, keep scenarios but cap reachability confidence at low.
- User planned channels remain hypotheses until S01 evidence supports them.

### Competitor And Substitute Signals

From S01:

```text
top_competitors_and_substitutes
competitor_candidate_review_list
competitor_threat_scores
substitute_taxonomy
price_ladder_scan
jump_decision_risks
segment_competitor_threats
competitor_nss_nps_comparison_seed
```

Use for:

- Current alternatives
- Switch barriers
- Competitor complaint opportunity
- Trade-up/trade-down/delay risks

Missing behavior:

- If competitor signals are missing, do not claim competitive whitespace.
- Use substitute/non-consumption risk as a fallback only when S01 produced it.

### Journey And NSS Driver Signals

From S01:

```text
journey_episode_inputs
bain_driver_inputs
journey_episode_nss_seed
nps_driver_tornado_seed
earned_growth_proxy_seed
hardware_experience_diagnosis_seed
```

Use for:

- Trigger situation
- Activation and return risks
- Promoter/detractor driver linkage
- Earned growth or advocacy signal

Missing behavior:

- If NSS/NPS proxy is unavailable, use directional journey and driver signals only.
- Never infer surveyed NSS/NPS inside S02.

### Local Language Signals

From S01:

```text
feature_to_local_language_map
search_query_seed_pack
local_voice_source_map
voice_theme_clusters.local_language_terms
localization_preflight
```

Use for:

- Local trigger phrases
- Search wording
- Objection wording
- S03 local-language message seed

Missing behavior:

- If local-language evidence is missing, produce English/working-language scenario labels and add a local-language data gap.

### Product Capability Fit Signals

From S01:

```text
product_capability_map
category_selling_point_map
selling_point_fit_scores
hardware_experience_diagnosis_seed
value_proof_requirement_matrix
```

Use for:

- Product-job fit matrix
- Product capability fit inside each scenario
- Whether the product can credibly own the job
- Capability gaps and proof needs

Missing behavior:

- If product capability signals are missing, S02 may extract scenarios but cannot score product fit above medium confidence.
- Do not recommend leading with a scenario when the product fit is unknown.

### Market Commercial Weight Signals

From S01:

```text
segment_level_tam_sam_som
market_sizing_confidence
initial_gtm_priorities
segment_priority_ranking
earned_growth_proxy_seed
channel_fit_scores
```

Use for:

- Scenario commercial weight
- Launch priority
- Whether a scenario is commercially material or only a niche insight
- Validation priority

Missing behavior:

- If commercial weight signals are missing, keep scenario priority focused on evidence and product fit.
- Do not imply market size or launch priority from voice intensity alone.

### Evidence Quality Signals

From S01:

```text
coverage_summary
source_quality_summary
confidence_caps
rag_index_manifest_ref
compressed_collection_summary
comment_collection_coverage_reports
```

Use for:

- Confidence caps
- RAG escalation decisions
- Whether a scenario can be ranked or only listed as a hypothesis
- HTML caveats

Missing behavior:

- If quality signals are missing, cap S02 confidence at medium.
- If evidence refs are missing, return a data gap instead of scenario ranking.

### Brand And Claim Constraint Signals

From project brief, S00, or optional private inputs:

```text
brand_positioning_constraints
brand_positioning_self_perception_and_tone
claim_constraints
compliance_constraints
report_audience
known_strategic_segments
```

Use for:

- Brand and claim constraint map
- Claims to avoid
- Safe direction seeds for S03
- Human review triggers

Missing behavior:

- If brand constraints are missing, S02 should not block scenario mining.
- If claim constraints are missing and scenarios touch health, safety, privacy, accuracy, children, elderly, battery, or regulated-adjacent claims, add a data gap and human review trigger.

## Upstream Input Coverage Gate

Before scenario extraction, produce:

```json
{
  "upstream_input_coverage_gate": {
    "status": "pass | pass_with_gaps | fail",
    "input_groups": [
      {
        "group": "",
        "required_for": [],
        "available_fields": [],
        "missing_fields": [],
        "fallback_fields": [],
        "impact_if_missing": "",
        "confidence_cap": "high | medium | low | assumption_only",
        "action": "proceed | proceed_with_cap | retrieve_from_rag | ask_s01_rerun | stop_and_report_gap"
      }
    ],
    "blocking_gaps": [],
    "non_blocking_gaps": [],
    "rag_or_full_artifact_escalations": []
  }
}
```

Gate logic:

```text
pass
  Consumer voice, product capability, segment, competitor/substitute, evidence quality, and at least two of price/proof/channel/commercial-weight signals are available.

pass_with_gaps
  Consumer voice exists, but one or more segment, price, proof, channel, competitor, product fit, commercial weight, evidence quality, brand/claim, or local-language groups are thin.

fail
  Consumer voice and purchase/objection signals are both missing, or no evidence refs are available for scenario extraction.
```

If the gate fails, S02 should not fabricate scenarios. It should return a data gap and recommended S01 rerun or targeted evidence retrieval.
