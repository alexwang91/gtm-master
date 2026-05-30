# Copy Scoring Methods

Use these methods after copy inventory and before producing scorecards.

## Copy Observation

Create one observation record per editable text item:

```json
{
  "copy_id": "",
  "copy_type": "headline | subheadline | body_copy | PDP_title | PDP_bullets | landing_page_copy | FAQ | ad_caption | script | transcript | retail_talk_track | package_text | claim_list | email_push | concept",
  "placement_context": "paid_social | search_ad | short_video_script | landing_page | marketplace_pdp | retailer_pdp | retail_sales | package_text | creator_brief | email_push | other",
  "language": "",
  "raw_copy": "",
  "visible_claims": [],
  "proof_statements": [],
  "product_cues": [],
  "price_or_promo_cues": [],
  "cta_or_next_step": "",
  "objections_addressed": [],
  "readability_notes": [],
  "fixed_constraints": [],
  "privacy_status": "public | uploaded_private | restricted",
  "evidence_refs": []
}
```

Only evaluate text that is provided or extracted with permission. Fixed visuals and layouts are constraints, not objects of critique.

## Task Definition Gate

Before scoring, label the copy's job:

```text
awareness
  Make the right consumer understand the category/product relevance quickly.

comparison
  Explain why this option is better, safer, easier, or more credible than alternatives.

conversion
  Reduce friction and make the next action obvious.

proof
  Make the claim believable through evidence, demo language, reviews, specs, certification, warranty, or comparison.

objection_handling
  Address price, trust, compatibility, setup, warranty, privacy, durability, or return concerns.

retail_or_pdp_trust
  Help the consumer trust the seller, delivery, return policy, warranty, stock, reviews, or local support.
```

The copy task changes scoring weights. Do not score an awareness hook as if it were a PDP proof block.

## Strategic Fit

Map each copy item to:

```text
segment -> JTBD scenario -> message role -> benefit -> proof requirement -> objection -> channel/placement -> copy task
```

Then score only the fit that can be observed:

```text
copy_message_fit =
  0.25 segment/message match
+ 0.20 JTBD situation match
+ 0.20 benefit clarity
+ 0.15 objection handling
+ 0.10 local-language consistency
+ 0.10 CTA/channel alignment
```

## Proof And Claim Clarity

For hardware products, proof language must be specific, credible, and tied to the promised benefit.

Proof language types:

```text
spec_or_benchmark_statement
demo_or_use_case_statement
side_by_side_comparison_statement
certification_or_lab_statement
expert_or_creator_review_quote
retailer_review_or_rating_statement
warranty_return_service_statement
privacy_security_safety_statement
setup_walkthrough_statement
price_value_breakdown_statement
```

Score lower when proof is vague, untranslated, not local, not source-backed, too hidden in the copy hierarchy, or disconnected from the lead claim.

## Claim Risk

Flag and cap copy that uses:

```text
absolute claims
medical_or_health_adjacent claims
safety/children/elderly claims
privacy/security claims without proof
accuracy/performance claims without test context
battery/durability claims without conditions
certification claims without source
sustainability claims without standard
before/after or guarantee claims
competitor superiority without evidence
```

S05 can identify risk and route review. It cannot approve the claim.

## Local And Cultural Language Fit

Check:

```text
local search terms and consumer wording
translation naturalness
category naming
price display, VAT, shipping, warranty, return expectations
retailer trust wording
consumer objections from local voice evidence
platform and channel copy norms
```

Preserve original local wording in evidence fields and explain it in Chinese in the report.

## Channel Copy Fit

Evaluate whether the text is right for the placement:

```text
paid_social
  one clear message, short hook, proof or curiosity cue, readable length, clear CTA.

search_ad
  keyword/message match, local category term, benefit, proof/offer, landing intent.

short_video_script
  first 2 seconds hook, situation setup, product demonstration language, proof, objection/reversal, CTA.

marketplace_pdp
  title clarity, bullet order, comparison, proof modules, reviews/Q&A language, delivery, returns, warranty, variant clarity.

retailer_pdp
  retailer trust, stock/delivery, sales objection handling, compatibility, warranty, service, comparison.

landing_page
  hero clarity, section order, proof sequence, price/value explanation, FAQ, CTA, friction reduction.

retail_sales_or_package_text
  3-second comprehension, category cue, hero benefit, proof phrase, local compliance, sales objection answer.
```

## Attention Hierarchy For Text

Score copy hierarchy by what the consumer sees first and remembers:

```text
primary_hook
  The first line or first 2 seconds. Must name the job, pain, or benefit clearly.

main_claim
  The dominant claim. Must be specific and proof-compatible.

proof_line
  The evidence line. Must be near the claim when proof is required.

objection_reversal
  The line that lowers risk: return, warranty, setup, compatibility, support, privacy, price.

cta
  The next action. Must match funnel stage and channel.
```

## Revision Brief

Each revision brief must specify:

```text
copy_id
priority
target_segment
copy_task
problem
evidence_refs
change_needed
claim/proof guardrail
expected effect
owner_hint
test_recommendation
```

Do not write polished final copy unless the user explicitly requests final creative generation.
