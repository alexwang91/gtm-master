# S05 Upstream Input Map

Use this before deciding whether S05 can score copy or should request editable text assets.

## Minimum Proceed Gate

S05 can produce a useful scoring run when these groups exist:

```text
message_system
  segment_message_architecture, feature_benefit_proof_matrix, objection_matrix

claim_and_proof_gate
  claim_risk_and_proof_gate, proof requirements, approved/forbidden claims when available

editable_text_input
  copy assets, copy concepts, PDP titles/bullets, landing-page copy blocks, ad captions, scripts, transcripts, retail talk tracks, package text, claim lists, or historical copy
```

If `editable_text_input` is missing, stop scoring and produce only:

```text
copy_input_coverage_gate
copy_asset_request_list
copy_scoring_rubric
copy_test_backlog
html_section_draft with data gap `missing_editable_copy`
```

## High-Value Context

```text
local_language_message_seed
  Use to check whether copy preserves local terms and avoids awkward literal translation.

price_message_seed
  Use to check whether price, promo, financing, bundle, warranty, or value framing is aligned with S04.

behavioral_lever_message_seed
  Use to identify whether copy uses authority, social proof, loss aversion, risk reversal, default, scarcity, or commitment cues responsibly.

retail_sales_talk_track_seed
  Use for sales cards, PDP, marketplace Q&A, retail demo scripts, and objection-handling text.

landing_page_message_block_seed
  Use for hero, proof, comparison, CTA, FAQ, and page-order copy evaluation.

creator_brief_message_seed
  Use for creator brief text and scripts; creator selection belongs to S06.

digital_shelf_and_retailer_decision_map
  Use to evaluate PDP/listing text completeness: title, bullets, comparison language, proof, reviews, delivery, returns, warranty, Q&A, and trust cues.

channel_fit_scores
  Use to avoid scoring copy highly for a channel where the segment is weak or unsupported.

local_price_credibility_model and price_risk_guardrail
  Use to evaluate price/value proof, discount language, and promo risk.
```

## Missing Input Handling

```text
missing_message_architecture
  Cannot judge strategic fit. Ask S03 to run or provide message architecture.

missing_proof_gate
  Can judge language clarity but must cap proof/claim confidence at low.

missing_local_language
  Can score generic copy fit, but mark localization confidence low.

missing_channel_context
  Can score copy quality but not placement/channel fit.

missing_editable_copy
  Do not invent copy scorecards. Produce request list and rubric.

fixed_visual_only
  If the user only has fixed images/videos/layouts, ask for OCR text, transcript, or copy blocks; do not critique visuals.

private_copy_restricted
  Do not expose raw private copy, scripts, or exact performance data in public HTML.
```

## Accepted Input Forms

```text
copy_or_concept
  Headlines, body copy, claim list, concept statement, slogan, tagline, message variant.

page_or_listing_text
  Landing page copy, PDP title, PDP bullets, A+ content text, retailer page text, Q&A, FAQ, checkout copy.

script_or_transcript
  Creator script, short video hook, voiceover script, demo script, sales script, transcript.

retail_or_package_text
  Retail sales talk track, shelf-card text, package/label claims, warranty/return explanation.

performance_data
  Spend, impressions, clicks, CTR, CVR, CPA, ROAS, add-to-cart, PDP conversion, retail sell-through, survey/ad recall tied to copy variants.
```
