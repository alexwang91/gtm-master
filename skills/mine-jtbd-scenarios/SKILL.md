---
name: mine-jtbd-scenarios
description: Use when converting S01 market context handoffs, consumer voice, segment seeds, competitor complaints, journey episodes, NSS/NPS drivers, and local-language trigger phrases into prioritized JTBD scenarios, proof needs, anti-JTBD risks, compressed handoffs, and HTML report sections for 2C hardware GTM work.
---

# Mine JTBD Scenarios

## Role

Use this skill as S02 in the GTM intelligence report suite. It converts S01 evidence into demand scenarios: what progress consumers are trying to make, what situation triggers the need, what they use today, what proof they require, and what can block purchase or advocacy.

S02 is the bridge between market facts and message strategy. It should preserve S01 evidence provenance, quantify scenario priority, and hand off compact scenario packs to S03, S04, and S14.

## Required Inputs

```json
{
  "project_brief": {},
  "market_context_pack": {}
}
```

High-value S01 fields:

```json
{
  "voice_atom_refs": [],
  "voice_theme_clusters": [],
  "consumer_opinion_map": {},
  "product_capability_map": {},
  "category_selling_point_map": [],
  "selling_point_fit_scores": [],
  "segment_seed_pack": [],
  "segment_priority_ranking": [],
  "segment_level_tam_sam_som": [],
  "market_sizing_confidence": {},
  "initial_gtm_priorities": [],
  "journey_episode_inputs": [],
  "bain_driver_inputs": [],
  "competitor_threat_scores": [],
  "substitute_taxonomy": [],
  "purchase_triggers": [],
  "objections": [],
  "feature_to_local_language_map": [],
  "content_proof_map": [],
  "segment_channel_touchpoint_map": [],
  "channel_fit_scores": [],
  "value_proof_requirement_matrix": [],
  "segment_price_sensitivity_seeds": [],
  "coverage_summary": {},
  "source_quality_summary": {},
  "confidence_caps": {},
  "rag_index_manifest_ref": "",
  "hardware_experience_diagnosis_seed": [],
  "next_generation_marketing_sales_seed": []
}
```

These fields come from `S01.compressed_handoff_pack.canonical_fields`; see `references/upstream-input-map.md` for the exact source map, fallback behavior, and coverage gate.

Optional private inputs:

```json
{
  "customer_interviews_or_survey_text": "",
  "sales_or_retail_objection_notes": "",
  "support_or_return_reason_notes": "",
  "known_strategic_segments": [],
  "brand_positioning_constraints": "",
  "claim_constraints": "",
  "compliance_constraints": ""
}
```

## Load Order

Read only what the current task needs:

1. Read `references/output-contract.md` before producing any artifact, handoff, or report section.
2. Read `references/upstream-input-map.md` before validating S01 handoff fields, checking segment/price/proof/channel inputs, or deciding whether S02 can proceed.
3. Read `references/consumer-electronics-gtm-methods.md` before mapping scenarios to consumer-electronics moments, product-job fit, digital shelf, behavioral science levers, commercial weight, or brand/claim constraints.
4. Read `references/jtbd-methodology.md` before extracting jobs, situations, desired outcomes, current alternatives, or demand scenarios.
5. Read `references/scoring-rubrics.md` before assigning scenario, proof, distinctness, product-job fit, GTM moment, behavioral lever, commercial weight, or anti-JTBD scores.
6. Read `references/proof-and-risk-mapping.md` before creating proof requirements, anti-JTBD risks, validation questions, or do-not-claim notes.
7. Read `references/evidence-usage-policy.md` before using RAG, escalating to full S01 artifacts, collecting extra evidence, or writing local outputs.
8. Read `references/html-visual-block-generation.md` before producing S14-ready `visual_blocks` for the HTML JTBD section draft.
9. Read `references/html-section-contract.md` before producing the HTML JTBD section draft.

## Depth Modes

```text
quick
  Produce core outputs only: input coverage, 3-5 JTBD scenarios, priority scorecard, product-job fit, proof needs, anti-JTBD risks, local trigger phrases, message seeds, price implication seeds, and compact handoff.

standard
  Produce core outputs and only the conditional modules whose triggers are present. Keep audit modules as refs or full-artifact sections, not default HTML tables.

deep
  Add targeted RAG retrieval from S01 evidence refs, richer competitor/substitute contrasts, full source/candidate/cluster audit tables, separate GTM moment maps, and validation question seeds. Use when scenarios will drive positioning, product roadmap, retail, pricing, or compliance decisions.
```

Default to `standard`.

## Output Tiers

S02 should stay lighter than S01. Preserve all methods, but do not render or hand off every intermediate table by default.

Core outputs, always produced:

```text
upstream_input_coverage_gate
jtbd_scenario_pack
scenario_priority_scorecard
scenario_to_segment_matrix
product_job_fit_matrix
proof_requirement_seed
anti_jtbd_risk_list
local_language_trigger_phrase_map
scenario_message_seed
scenario_price_implication_seed
```

Conditional outputs, produced only when triggered:

```text
consumer_electronics_gtm_moment_map
digital_shelf_and_retailer_decision_map
behavioral_science_lever_map
scenario_commercial_weight_map
brand_claim_constraint_map
validation_question_seed
non_consumption_risk_map
scenario_to_journey_matrix
```

Audit outputs, preserved in the full artifact or as refs but not default HTML:

```text
upstream_input_map
jtbd_source_map
jtbd_candidate_pool
jtbd_scenario_clusters
scenario_distinctness_results
```

Conditional triggers:

```text
digital_shelf_and_retailer_decision_map
  Trigger when DTC, marketplace, retailer, shopping search, store availability, delivery, returns, warranty, or channel conversion matters.

behavioral_science_lever_map
  Trigger when S03/S05/S07 will test message, creative, funnel, proof, offer, or risk-reversal levers.

brand_claim_constraint_map
  Trigger when health, safety, privacy, accuracy, battery, children, elderly, certification, warranty, or regulated-adjacent claims appear.

scenario_commercial_weight_map
  Trigger when market sizing, segment value, inventory, channel priority, or launch sequencing decisions depend on the scenario.

validation_question_seed
  Trigger when a lead scenario is weak, user-provided, commercially important, or confidence-capped.

non_consumption_risk_map
  Trigger when doing nothing, delaying purchase, using a workaround, or staying with a substitute is a meaningful risk.

scenario_to_journey_matrix
  Trigger as a separate table only in standard/deep when journey stage differences change messaging, channel, activation, or support decisions.
```

## Execution Workflow

Follow this sequence:

```text
1. Validate upstream handoff coverage, input group availability, and data gaps
2. Build JTBD source map from S01 evidence refs
3. Extract atomic JTBD candidates from voice themes, atoms, drivers, journey episodes, objections, purchase triggers, and competitor complaints
4. Normalize candidates into situation-motivation-outcome-alternative-barrier statements
5. Cluster candidates into demand scenarios by progress sought and trigger context
6. Run scenario distinctness checks
7. Map scenarios to segments, journey episodes, current alternatives, product capabilities, price signals, and channels
8. Build core product-job fit, proof, anti-JTBD, local phrase, message seed, and price implication outputs
8A. Build conditional consumer-electronics GTM modules only when their triggers are present
9. Score scenario priority and evidence strength
10. Build proof requirement seed
11. Build anti-JTBD and non-consumption risk list
12. Build local-language trigger phrase map
13. Build validation question seed
14. Produce compressed handoff pack
15. Produce HTML JTBD section draft with S14-ready visual blocks
```

## Scope Boundary

S02 owns:

- JTBD candidate extraction from S01 evidence
- Situation, motivation, outcome, alternative, barrier, and proof mapping
- Scenario clustering and distinctness checks
- Scenario priority scoring
- Scenario-to-segment and scenario-to-journey mapping
- Anti-JTBD, non-consumption, and expectation-gap risk identification
- Local-language trigger phrase seeds
- Proof requirement seeds for downstream message, pricing, creative, and sales work
- Upstream input coverage gate for segment, price, proof, channel, competitor, local-language, and consumer voice signals
- Consumer-electronics GTM moment mapping, product-job fit, digital shelf/retailer decision mapping, behavioral science lever hypotheses, commercial scenario weighting, and brand/claim constraints

S02 does not own:

- Final messaging architecture or ad copy
- Final price recommendation
- Creative scoring
- KOL selection
- Demand forecasting
- Final HTML composition

## Required Output

Always return the S02 output envelope from `references/output-contract.md`:

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

- Treat JTBD as progress in context, not a feature request, demographic persona, or generic benefit.
- Do not invent needs unsupported by S01 evidence or explicitly marked user hypotheses.
- Do not proceed silently when segment, price, proof, or channel signals are missing; record the missing group and confidence cap in `upstream_input_coverage_gate`.
- Do not prioritize a scenario only because consumer pain is loud; weigh product fit, commercial materiality, reachability, proof readiness, and evidence quality.
- Do not use behavioral science levers as final creative or manipulation; use them as proof/friction-reduction hypotheses for downstream testing.
- Do not ignore post-purchase experience for consumer electronics; setup, app pairing, support, returns, warranty, and advocacy can change the scenario priority.
- Do not put audit modules into the default HTML section unless deep mode is requested or a confidence dispute needs explanation.
- Do not generate conditional modules just because the schema exists; require a trigger and record it.
- Preserve local-language trigger phrases when they shape search, messaging, or objection handling.
- Keep user-provided strategic segments as hypotheses unless evidence supports them.
- Score every prioritized scenario and show the evidence refs behind it.
- Do not merge scenarios only because demographics overlap; merge by similar situation, motivation, current alternative, and desired outcome.
- Do not split scenarios just because word choice differs; split only when motivation, trigger, proof need, or purchase barrier differs.
- Mark competitor complaint reuse carefully: a complaint about a competitor becomes an opportunity only if the product can credibly solve it.
- Convert weak but commercially important scenarios into validation hypotheses, not high-confidence conclusions.
- Hand off compact fields first; use RAG or full artifact escalation only when the handoff is insufficient.
