---
name: match-messages-to-segments
description: Use when converting S02 JTBD scenarios, proof requirements, anti-JTBD risks, local trigger phrases, product-job fit, and claim constraints into segment-level message architecture, feature-benefit-proof matrices, objection handling, competitive contrast, price message seeds, compressed handoffs, and HTML report sections for 2C hardware GTM work.
---

# Match Messages To Segments

## Role

Use this skill as S03 in the GTM intelligence report suite. It turns prioritized demand scenarios into message architecture: what to say, what proof is needed, what not to claim, and how each segment should understand the product's value.

S03 is not a copywriting skill. It should create structured message systems and handoffs for pricing, creative, creator, funnel, and HTML skills without writing final ads, final landing pages, or final scripts.

## Required Inputs

```json
{
  "project_brief": {},
  "jtbd_scenario_pack": [],
  "proof_requirement_seed": [],
  "anti_jtbd_risk_list": [],
  "local_language_trigger_phrase_map": [],
  "scenario_message_seed": [],
  "scenario_price_implication_seed": []
}
```

High-value S02/S01 fields:

```json
{
  "scenario_to_segment_matrix": [],
  "product_job_fit_matrix": [],
  "scenario_priority_scorecard": [],
  "consumer_electronics_gtm_moment_map": [],
  "behavioral_science_lever_map": [],
  "brand_claim_constraint_map": [],
  "digital_shelf_and_retailer_decision_map": [],
  "scenario_commercial_weight_map": [],
  "value_proof_requirement_matrix": [],
  "content_proof_map": [],
  "competitor_threat_scores": [],
  "feature_to_local_language_map": [],
  "confidence_caps": {}
}
```

Optional private inputs:

```json
{
  "brand_positioning_self_perception_and_tone": "",
  "claim_constraints": "",
  "compliance_constraints": "",
  "historical_ads_kol_landing_pages_and_creatives": "",
  "sales_or_retail_objection_notes": "",
  "approved_claims_or_proof_assets": [],
  "forbidden_claims_or_words": []
}
```

## Load Order

Read only what the current task needs:

1. Read `references/output-contract.md` before producing any artifact, handoff, or report section.
2. Read `references/upstream-input-map.md` before checking S02/S01 input coverage or deciding whether S03 can proceed.
3. Read `references/message-architecture-methods.md` before building segment message architecture, feature-benefit-proof, competitive contrast, or local-language message seeds.
4. Read `references/proof-claim-risk-policy.md` before creating claims, proof status, do-not-claim notes, compliance queues, or sensitive-category language.
5. Read `references/scoring-rubrics.md` before assigning message-market fit, proof readiness, objection severity, or claim risk scores.
6. Read `references/evidence-usage-policy.md` before using evidence refs, RAG, full artifact escalation, or local storage.
7. Read `references/html-visual-block-generation.md` before producing S14-ready `visual_blocks` for the HTML message section draft.
8. Read `references/html-section-contract.md` before producing the HTML message section draft.

## Depth Modes

```text
quick
  Produce core outputs only: input coverage, segment message architecture, feature-benefit-proof matrix, objection matrix, claim/proof gate, local message seeds, and compact handoff.

standard
  Produce core outputs plus triggered conditional modules. Keep audit modules as refs or full-artifact sections, not default HTML.

deep
  Add full source-to-message trace, rejected message angles, richer competitive contrast, retail/landing/creator seeds, and message test backlog.
```

Default to `standard`.

## Output Tiers

Core outputs, always produced:

```text
message_input_coverage_gate
segment_message_architecture
feature_benefit_proof_matrix
objection_matrix
claim_risk_and_proof_gate
local_language_message_seed
price_message_seed
message_market_fit_scorecard
```

Conditional outputs, produced only when triggered:

```text
competitive_contrast_matrix
behavioral_lever_message_seed
retail_sales_talk_track_seed
landing_page_message_block_seed
creator_brief_message_seed
compliance_review_queue
message_test_backlog
```

Audit outputs, preserved in the full artifact or as refs but not default HTML:

```text
message_source_trace
message_variant_pool
rejected_message_angles
claim_evidence_audit
```

Conditional triggers:

```text
competitive_contrast_matrix
  Trigger when competitor/substitute comparison materially affects the message.

behavioral_lever_message_seed
  Trigger when S02 produced behavioral levers or S05/S07 testing is planned.

retail_sales_talk_track_seed
  Trigger when marketplace, retail, distributor, offline, or sales objection handling matters.

landing_page_message_block_seed
  Trigger when DTC, landing page, product page, or funnel conversion matters.

creator_brief_message_seed
  Trigger when creator/KOL/expert content is planned.

compliance_review_queue
  Trigger when claims touch health, safety, children, elderly, privacy, accuracy, battery, certifications, sustainability, warranty, or regulated-adjacent areas.

message_test_backlog
  Trigger when evidence is weak, claims are high-impact, or message-market fit is confidence-capped.
```

## Execution Workflow

Follow this sequence:

```text
1. Validate S02/S01 input coverage and confidence caps
2. Select lead scenarios and segment relationships from S02
3. Convert scenario needs into message jobs: value, proof, objection, risk, price, and local-language needs
4. Build feature-benefit-proof matrix
5. Build segment message architecture
6. Build objection handling matrix and anti-claim notes
7. Build claim risk and proof gate
8. Build local-language message seed without final transcreation
9. Build price message seed for S04
10. Score message-market fit and proof readiness
11. Build conditional message modules only when triggered
12. Produce compressed handoff pack
13. Produce HTML message section draft with S14-ready visual blocks
```

## Scope Boundary

S03 owns:

- Segment-level message architecture
- Feature-benefit-proof matrix
- Objection handling matrix
- Claim risk and proof status
- Price message seed
- Local-language message seed
- Competitive contrast seed when needed
- Conditional seeds for retail, landing page, creator, creative, and message testing

S03 does not own:

- Final ad copy or final landing page copy
- Final price recommendation
- Creative asset scoring
- KOL selection
- Funnel conversion prediction
- Compliance/legal approval
- Final HTML composition

## Required Output

Always return the S03 output envelope from `references/output-contract.md`:

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

- Do not write final copy; produce message architecture and reusable seeds.
- Every message claim needs a proof status: `available`, `partial`, `missing`, or `risky`.
- Do not lead with a feature unless it maps to a JTBD scenario, segment, benefit, and proof requirement.
- Keep local-language phrasing as seed language, not final translation or transcreation.
- Do not overclaim health, safety, accuracy, privacy, battery, compatibility, warranty, sustainability, or certification benefits.
- Keep competitor contrast factual and evidence-backed; do not invent competitor weaknesses.
- Preserve anti-JTBD objections and "do not claim" notes even when they weaken the story.
- Cap message confidence when S02 scenario, product-job fit, or proof confidence is low.
- Use conditional modules only when triggered; keep audit outputs out of default HTML.
