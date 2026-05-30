---
name: score-creative-assets
description: Use when evaluating editable creative text assets such as ad copy, product claims, PDP titles/bullets, landing-page copy blocks, retail talk tracks, creator scripts, email/push copy, package text, or copy concepts against GTM message architecture, proof needs, local language, channel context, claim risk, and test readiness for 2C hardware launches.
---

# Score Creative Text Assets

## Role

Use this skill as S05 in the GTM intelligence report suite. It scores and revises editable creative text assets against the segment message architecture from S03, proof requirements from S02/S03, price and claim guardrails from S04, and local channel context from S01/S02.

S05 is a copy evaluation and revision-brief skill. It does not require users to upload images, videos, packaging visuals, or design files. Fixed visuals, layouts, packaging, and channel placements may be described as constraints, but S05 should only recommend changes to editable text.

S05 must not invent final ads, approve regulated claims, or treat synthetic scoring as performance proof.

## Required Inputs

```json
{
  "project_brief": {},
  "segment_message_architecture": [],
  "feature_benefit_proof_matrix": [],
  "objection_matrix": [],
  "claim_risk_and_proof_gate": {}
}
```

High-value upstream fields:

```json
{
  "local_language_message_seed": [],
  "price_message_seed": [],
  "behavioral_lever_message_seed": [],
  "retail_sales_talk_track_seed": [],
  "landing_page_message_block_seed": [],
  "creator_brief_message_seed": [],
  "content_proof_map": [],
  "value_proof_requirement_matrix": [],
  "digital_shelf_and_retailer_decision_map": [],
  "segment_channel_touchpoint_map": [],
  "channel_fit_scores": [],
  "local_price_credibility_model": {},
  "price_risk_guardrail": [],
  "promo_subscription_guidance": {}
}
```

Optional user inputs:

```json
{
  "copy_assets": [],
  "copy_concepts": [],
  "historical_copy_landing_pages_kol_scripts_and_ads": "",
  "copy_performance_data": "",
  "brand_guidelines": "",
  "approved_claims_or_proof_assets": [],
  "forbidden_claims_or_words": [],
  "fixed_visual_or_layout_constraints": "",
  "target_channels_or_placements": []
}
```

Accepted text asset types:

```text
headline
subheadline
body_copy
ad_caption
short_video_script_or_transcript
creator_script_or_brief
PDP_title
PDP_bullets
PDP_A_plus_text
landing_page_hero_copy
landing_page_section_copy
FAQ_or_QA
retail_sales_talk_track
package_or_label_text
claim_list
email_or_push_copy
search_ad_copy
concept_statement
```

If the user has only an image, video, screenshot, or package design, ask for the editable text, OCR text, transcript, claim list, or page copy. Do not require raw visuals.

If no editable text assets or concepts are supplied, do not score imaginary copy. Produce `copy_asset_request_list`, `copy_scoring_rubric`, and `copy_test_backlog` instead.

## Load Order

Read only what the current task needs:

1. Read `references/output-contract.md` before producing any artifact, handoff, or report section.
2. Read `references/upstream-input-map.md` before checking whether S05 can score copy or must request editable text.
3. Read `references/creative-scoring-methods.md` before scoring message fit, proof clarity, channel fit, local language, or revision needs.
4. Read `references/scoring-rubrics.md` before assigning numeric copy, proof, claim, channel, or test-priority scores.
5. Read `references/evidence-usage-policy.md` before using uploaded private copy, public copy examples, ad libraries, RAG refs, or performance data.
6. Read `references/html-visual-block-generation.md` before producing S14-ready `visual_blocks`.
7. Read `references/html-section-contract.md` before producing the HTML creative section draft.

## Depth Modes

```text
quick
  Produce input coverage, copy inventory, copy scorecard, claim/proof risk notes, and compact revision briefs.

standard
  Produce core outputs plus channel-copy fit, local-language fit, proof/claim clarity audit, and copy test backlog.

deep
  Add copy evidence trace, competitor/category copy norm scan, placement-specific audits, and performance result interpretation when data exists.
```

Default to `standard`.

## Output Tiers

Core outputs, always produced when editable text assets or concepts exist:

```text
copy_input_coverage_gate
copy_asset_inventory
copy_message_fit_scorecard
proof_and_claim_clarity_audit
claim_risk_review
local_language_fit_audit
channel_copy_fit_matrix
copy_quality_scorecard
copy_revision_briefs
copy_test_backlog
```

Conditional outputs, produced only when triggered:

```text
copy_asset_request_list
copy_scoring_rubric
competitor_copy_norm_scan
marketplace_pdp_copy_fit
landing_page_copy_fit
retail_sales_copy_fit
short_video_script_hook_audit
package_text_claim_audit
copy_performance_result_interpretation
compliance_review_queue
```

Audit outputs, preserved in the full artifact or refs:

```text
copy_evidence_trace
copy_observation_log
claim_copy_map
revision_rationale_trace
performance_data_audit
```

Conditional triggers:

```text
copy_asset_request_list
  Trigger when no editable text assets or concepts are available.

competitor_copy_norm_scan
  Trigger when public category copy examples are needed to understand local terms, proof conventions, offer language, PDP wording, or channel format expectations.

marketplace_pdp_copy_fit
  Trigger when marketplace or retailer listing text, PDP title/bullets, Q&A, reviews, delivery, warranty, or checkout trust text materially affects conversion.

landing_page_copy_fit
  Trigger when DTC, landing page, hero block, product page, or checkout copy is planned.

retail_sales_copy_fit
  Trigger when offline retail, shelf talker text, sales cards, demo scripts, or sales objection handling matters.

short_video_script_hook_audit
  Trigger when short video scripts, creator scripts, transcripts, captions, or hooks are provided.

copy_performance_result_interpretation
  Trigger when ad A/B, landing-page, marketplace, retail, or historical copy performance data is provided.

compliance_review_queue
  Trigger when copy contains health, safety, children, elderly, privacy, medical-adjacent, before/after, certification, sustainability, warranty, or accuracy claims.
```

## Execution Workflow

Follow this sequence:

```text
1. Validate upstream message/proof/claim inputs and editable text availability
2. Build copy asset inventory with copy IDs, text type, placement, language, owner, and privacy status
3. Extract claims, proof statements, product cues, price/value cues, objections addressed, CTA, and forbidden/risky wording
4. Map each text asset to target segment, JTBD scenario, message role, proof requirement, and channel/placement
5. Score copy-message fit, proof/claim clarity, claim risk, local-language fit, channel-copy fit, and attention hierarchy
6. Identify unsupported, misleading, vague, off-brand, overlong, untranslated, or locally weak wording
7. Build revision briefs that specify what text to change, why, evidence refs, priority, and owner
8. Build copy test backlog with test type, hypothesis, metric, minimum evidence, and channel caveats
9. Interpret provided performance data only after checking test validity and confounders
10. Produce compressed handoff pack
11. Produce HTML creative section draft with S14-ready visual blocks
```

## Scope Boundary

S05 owns:

- Editable copy and claim scoring
- Message fit and proof/claim clarity evaluation
- Claim risk detection for copy assets
- Local language and cultural wording audit
- Channel and placement copy fit scoring
- Revision briefs and copy test backlog

S05 does not own:

- Image, video, packaging visual, layout, or design critique
- Final visual creative direction
- Legal, compliance, or medical approval
- Media budget allocation
- KOL selection
- Funnel conversion forecast
- Final HTML composition

## Required Output

Always return the S05 output envelope from `references/output-contract.md`:

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

- Do not request raw images, videos, or design files for S05. Ask for editable text, OCR text, transcripts, claim lists, or copy blocks.
- Do not score copy that was not supplied, linked as text, extracted with permission, or found through an approved public search path.
- Do not recommend changes to fixed visuals, packaging structure, media format, or layout unless the user says those can be changed.
- Do not treat copy scores, AI judgment, or synthetic persona reactions as actual conversion proof.
- Every score must trace to text observations, upstream message/proof fields, performance data, or declared hypothesis.
- If copy contains an unsupported claim, cap its recommendation status even when the wording is persuasive.
- Preserve private copy as restricted evidence unless the user approves public inclusion.
- Default dashboard-facing outputs to Simplified Chinese unless the user requests another report language.
