---
name: score-kol-fit
description: Use when discovering or evaluating creator, KOL, expert, reviewer, media, community, or influencer fit for 2C hardware GTM based on local source discovery, segment trust needs, proof requirements, local platform relevance, audience fit, budget and expected outcome ranges, brand safety, sponsorship disclosure risk, and test readiness.
---

# Score KOL Fit

## Role

Use this skill as S06 in the GTM intelligence report suite. It scores creator/expert types and candidate creators against segment trust needs, proof requirements, local platform/channel evidence, message architecture, budget/outcome feasibility, and brand safety constraints.

S06 is optional. It should run only when creator, expert, reviewer, media, affiliate, community, or retail-influence work matters. If no creator candidates exist, produce creator archetype fit, sourcing criteria, and a candidate discovery plan instead of inventing a shortlist.

S06 must not silently finalize KOL choices, approve creators for contracting, invent private audience data, promise campaign results, or treat follower counts as proof of influence.

## Required Inputs

```json
{
  "project_brief": {},
  "segment_message_architecture": [],
  "proof_requirement_seed": [],
  "creator_brief_message_seed": []
}
```

High-value upstream fields:

```json
{
  "scenario_priority_scorecard": [],
  "scenario_to_segment_matrix": [],
  "product_job_fit_matrix": [],
  "behavioral_science_lever_map": [],
  "claim_risk_and_proof_gate": {},
  "local_language_message_seed": [],
  "content_proof_map": [],
  "feature_to_local_language_map": [],
  "local_source_map": [],
  "local_voice_source_map": [],
  "competitor_candidate_review_list": [],
  "competitor_threat_scores": [],
  "segment_channel_touchpoint_map": [],
  "channel_fit_scores": [],
  "digital_shelf_and_retailer_decision_map": [],
  "copy_quality_scorecard": [],
  "copy_test_backlog": []
}
```

Optional user inputs:

```json
{
  "creator_candidates": [],
  "known_creator_blacklist_or_risk_notes": [],
  "brand_guidelines": "",
  "sponsorship_disclosure_policy": "",
  "target_platforms": [],
  "creator_budget_range": "",
  "campaign_budget_currency": "",
  "creator_rate_cards_or_media_kits": [],
  "product_seeding_cost_or_sample_value": "",
  "creator_campaign_goal": "awareness | proof | comparison | conversion | retail_support | community_validation | launch_event | other",
  "creator_discovery_required": true,
  "candidate_review_list_size": 8,
  "creator_candidate_review_decisions": [],
  "historical_creator_performance_data": "",
  "tracking_or_landing_page_context": "",
  "approved_claims_or_proof_assets": []
}
```

## Load Order

Read only what the current task needs:

1. Read `references/output-contract.md` before producing any artifact, handoff, or report section.
2. Read `references/upstream-input-map.md` before checking whether S06 can score candidates or should produce archetypes and sourcing criteria.
3. Read `references/creator-fit-methods.md` before building creator archetypes, candidate scoring, trust/proof mapping, brand-safety review, or brief packs.
4. Read `references/scoring-rubrics.md` before assigning creator, audience, proof, platform, safety, or test-priority scores.
5. Read `references/evidence-usage-policy.md` before using public creator data, platform metrics, web/MCP search, private creator lists, or performance data.
6. Read `references/html-visual-block-generation.md` before producing S14-ready `visual_blocks`.
7. Read `references/html-section-contract.md` before producing the HTML creator section draft.
8. Read `references/html-section-example.md` only when asked for an output sample, renderer fixture, or stakeholder preview.

## Depth Modes

```text
quick
  Produce creator input coverage, creator archetype fit, candidate scoring if candidates are supplied, major risks, and a compact handoff.

standard
  Produce core outputs plus platform fit, trust/proof fit matrix, recommendation rationale, budget/outcome ranges, brief pack, disclosure risk, and test backlog.

deep
  Add public creator/source discovery plan, query bank, local source/channel map, candidate longlist, category creator norm scan, detailed risk audit, rate/performance assumption trace, performance result interpretation, and candidate evidence trace.
```

Default to `standard`.

## Output Tiers

Core outputs, always produced:

```text
creator_input_coverage_gate
creator_archetype_fit_scorecard
creator_trust_proof_fit_matrix
platform_relevance_map
creator_recommendation_rationale
creator_budget_estimate
creator_expected_outcome_estimate
creator_budget_expectation_confidence
brand_safety_risk_review
sponsorship_disclosure_risk_review
creator_brief_pack
creator_test_backlog
```

Core outputs when candidates exist:

```text
creator_candidate_inventory
creator_candidate_fit_scorecard
candidate_segment_audience_fit
candidate_content_proof_fit
```

Conditional outputs:

```text
creator_candidate_request_list
creator_sourcing_criteria
public_creator_discovery_plan
local_creator_discovery_query_bank
creator_source_channel_map
creator_candidate_longlist
creator_discovery_coverage_report
competitor_creator_overlap_map
creator_candidate_review_gate
creator_candidate_review_list
creator_candidate_decision_log
review_approved_candidate_set
review_excluded_candidate_set
category_creator_norm_scan
affiliate_or_reviewer_program_fit
retail_expert_or_media_fit
creator_performance_result_interpretation
compliance_review_queue
```

Audit outputs:

```text
creator_evidence_trace
candidate_risk_audit
audience_metric_quality_audit
content_sample_audit
performance_data_audit
```

## Conditional Triggers

```text
creator_candidate_request_list
  Trigger when no creator candidates are supplied and creator work is desired.

public_creator_discovery_plan
  Trigger when local creator discovery is needed but S06 should not browse or scrape yet.

local_creator_discovery_query_bank
  Trigger when the launch country, language, category terms, local platforms, or competitor terms are needed to discover candidates.

creator_candidate_longlist
  Trigger when public discovery is executed or user supplies a broad creator list. Keep candidates as unapproved until reviewed.

creator_discovery_coverage_report
  Trigger whenever S06 performs public creator discovery. It records sources searched, blocked sources, coverage by platform, and remaining blind spots.

competitor_creator_overlap_map
  Trigger when competitor products, previous-generation products, or category anchors are known and creator content can reveal category authority.

creator_candidate_review_gate
  Trigger when S06 has discovered or received more than three candidate creators, reviewers, media, affiliates, forum authorities, or retailer experts. Present 5-10 options for user include/exclude/unsure decisions before final candidate scoring.

creator_candidate_decision_log
  Trigger when user review decisions are supplied or inferred from a prior gate. Do not silently discard excluded candidates; record the reason.

category_creator_norm_scan
  Trigger when the local category has unclear creator/reviewer conventions.

affiliate_or_reviewer_program_fit
  Trigger when affiliate, expert review, marketplace review, or long-tail creator programs matter.

retail_expert_or_media_fit
  Trigger when offline retail, specialist media, lab review, or expert recommendation shapes trust.

creator_performance_result_interpretation
  Trigger when historical creator campaign performance is provided.

creator_budget_estimate and creator_expected_outcome_estimate
  Trigger whenever S06 recommends an archetype or candidate. If rate/performance data is weak, output ranges with explicit assumptions, confidence caps, and data gaps instead of exact values.

compliance_review_queue
  Trigger when creator content may involve health, safety, children, elderly, privacy, medical-adjacent, certification, sustainability, warranty, or performance claims.
```

## Execution Workflow

Follow this sequence:

```text
1. Validate upstream message, proof, channel, and creator input coverage
2. Define creator campaign goal and role: awareness, proof, comparison, conversion, retail support, community validation, or launch event
3. Build creator archetypes from segment trust needs, proof requirements, and local channel behavior
4. If discovery is needed, build a local-language query bank and source-channel map from S01-S03 evidence
5. Discover or request a candidate longlist by source stratum: video/social, specialist media, forums, retailer/PDP support, affiliate/deal, and competitor-overlap sources
6. Build a candidate review gate with 5-10 options, include/exclude/unsure actions, and reason prompts when enough candidates exist
7. Apply user review decisions when supplied; otherwise mark candidate-level outputs as provisional and pending review
8. If candidates exist, inventory candidates with platform, language, content category, audience proxy, proof role, access status, review decision, risk notes, and evidence refs
9. Score creator archetype fit and candidate fit separately
10. Score audience/segment fit, trust/proof fit, platform relevance, discovery priority, evidence coverage, brand safety, claim risk, and disclosure risk
11. Build recommendation rationale: why this archetype/candidate, why not others, what evidence supports the choice, and what uncertainty remains
12. Estimate marketing budget ranges and expected outcome ranges for conservative/base/upside scenarios
13. Build creator brief pack with message role, proof boundaries, do-not-say rules, content task, and measurement plan
14. Build creator test backlog with hypothesis, audience, platform, metric, minimum evidence, and confounders
15. Interpret provided performance data only after checking traffic quality, attribution, timing, spend, and selection bias
16. Produce compressed handoff pack
17. Produce HTML creator section draft with S14-ready visual blocks
```

## Scope Boundary

S06 owns:

- Creator archetype fit
- Local creator discovery plan, query bank, source-channel map, and candidate longlist when discovery is requested
- Candidate review gate and user include/exclude/unsure decision handling
- Candidate creator fit scoring when candidates exist
- Segment/audience and trust/proof fit
- Platform relevance and local creator role
- Recommendation rationale, marketing budget ranges, and expected outcome ranges
- Brand safety and sponsorship disclosure risk
- Creator brief pack and test backlog

S06 does not own:

- Contracting or final creator approval
- Final media budget approval or procurement negotiation
- Guaranteed visits, likes, sales, or conversion lift
- Legal/compliance approval
- Scraping private platform analytics
- Final creative scripts unless requested through S05/S16
- Final HTML composition

## Required Output

Always return the S06 output envelope from `references/output-contract.md`:

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

- Do not infer audience demographics, conversion lift, or brand safety from follower count alone.
- Separate creator archetype recommendations from specific candidate recommendations.
- Label public social metrics as proxies unless verified first-party data is provided.
- Every creator/candidate score must trace to evidence, candidate data, public source, or a stated hypothesis.
- Every recommendation must include a clear rationale, counter-rationale, budget basis, expected-outcome basis, and confidence label.
- Budget outputs are marketing budget estimates. Use ranges, currency labels, and component assumptions; do not present them as approved spend.
- Expected visits, likes, comments, shares, views, CTR, or engagement are estimates. Use conservative/base/upside ranges and never guarantee results.
- Candidate shortlists require human review before outreach or contract use.
- If a candidate review gate is pending, mark candidate scores, budget ranges, and expected outcomes as provisional.
- Excluded candidates must not enter approved scoring, budget, or expected-outcome recommendations unless the user later reverses the decision.
- Do not expose private creator lists, rates, contacts, or campaign performance in public HTML unless approved.
- Default dashboard-facing outputs to Simplified Chinese unless the user requests another report language.
