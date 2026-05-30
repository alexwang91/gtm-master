# S03 HTML Section Contract

S03 contributes the message architecture section of the final GTM dashboard.

## Default Section IDs

```text
message_overview
message_input_coverage
segment_message_architecture
feature_benefit_proof_matrix
objection_matrix
claim_risk_and_proof_gate
local_language_message_seed
price_message_seed
message_market_fit_scorecard
message_investment_allocation_seed
```

Conditional section IDs:

```text
competitive_contrast_matrix
behavioral_lever_message_seed
retail_sales_talk_track_seed
landing_page_message_block_seed
creator_brief_message_seed
compliance_review_queue
message_test_backlog
```

## HTML Section Draft

```json
{
  "section_id": "s03_message_architecture",
  "source_skill": "S03.match-messages-to-segments",
  "section_title": "Segment Message Architecture",
  "executive_takeaway": "",
  "narrative_blocks": [],
  "metric_cards": [],
  "visual_blocks": [],
  "tables": [],
  "charts": [],
  "callouts": [],
  "confidence_badges": [],
  "citations": [],
  "data_gaps": [],
  "next_actions": []
}
```

## S14 Visual Block Contract

S03 must produce `visual_blocks` that S14 can render directly. The visuals should make claim readiness, message-market fit, proof gaps, and objection risk obvious before anyone reads detailed tables. Read `html-visual-block-generation.md` for block-level transformation rules, scoring fallbacks, and thin-output checks.

```json
{
  "visual_blocks": [
    {
      "type": "status_panel | ranked_bar | matrix_heatmap | range_chart",
      "title": "",
      "subtitle": "",
      "data_source": "",
      "items": [],
      "rows": [],
      "columns": [],
      "note": "",
      "evidence_refs": [],
      "confidence": "high | medium | low | hypothesis_only"
    }
  ]
}
```

Default S03 main-body `visual_blocks`:

```yaml
required_visual_blocks:
  - title: Message Input Coverage Gate
    type: status_panel
    data_source: message_input_coverage_gate + confidence_caps
    core_question: Which upstream gaps cap message confidence?

  - title: Segment Message Fit
    type: matrix_heatmap
    data_source: segment_message_architecture + message_market_fit_scorecard
    core_question: Which message angles should lead for each priority segment?
    display_requirement: Include initial message investment percent and recommended MKT carrier archetype when available. This is a message-testing attention split, not final media budget approval.

  - title: Feature Benefit Proof Readiness
    type: matrix_heatmap
    data_source: feature_benefit_proof_matrix
    core_question: Which claims have proof, partial proof, missing proof, or risk?
    display_requirement: S14 may render this as a proof stack or claim readiness ladder instead of another heatmap when that is easier to read.

  - title: Claim Risk And Proof Gate
    type: status_panel
    data_source: claim_risk_and_proof_gate
    core_question: What can be said now, what needs proof, and what must not be said?
    display_requirement: Treat this as local PR guidance. Include claim boundary, review need, do-not-say notes, and suggested owner when available.

  - title: Objection Severity Ranking
    type: ranked_bar
    data_source: objection_matrix
    core_question: Which objections most threaten conversion or trust?
```

Use `tables` for local-language message seeds, price message seeds, do-not-say notes, compliance review queues, message investment allocation seeds, and message test backlog. These fields often need exact wording and caveats that charts should not compress away.

## Thin Output Gate

Mark the S03 HTML section as `rendered_too_thin` in `data_gaps` if it lacks any of:

```text
executive_takeaway
message input coverage signal
segment-message fit visual block
feature-benefit-proof matrix or visual block
claim risk/proof gate
objection handling table with do-not-say notes
message investment allocation or explicit reason it is not available
next_actions for S04/S05/S06/S07/S13
```

## Default Visuals

```yaml
visuals:
  - name: Message-Market Fit Scorecard
    type: scorecard_table
    data_source: message_market_fit_scorecard

  - name: Segment Message Architecture
    type: message_route_swimlane_or_message_house
    data_source: segment_message_architecture

  - name: Message Investment Allocation Seed
    type: allocation_bar_plus_role_cards
    data_source: message_investment_allocation_seed

  - name: Feature-Benefit-Proof Matrix
    type: proof_stack_or_claim_ladder
    data_source: feature_benefit_proof_matrix

  - name: Objection Handling Matrix
    type: action_table
    data_source: objection_matrix

  - name: Claim Risk And Proof Gate
    type: risk_table
    data_source: claim_risk_and_proof_gate

  - name: Local Language Message Seed
    type: language_table
    data_source: local_language_message_seed

  - name: Price Message Seed
    type: scorecard_table
    data_source: price_message_seed
```

## Rendering Rules

- Render message seeds as architecture, not final copy.
- S03 may recommend initial percent split for message testing/MKT attention across message routes and carrier archetypes. Do not treat this as final media budget approval, final KOL selection, or channel budget allocation.
- Show proof status and claim risk next to any claim-like message.
- Show objections and do-not-claim notes even if they weaken the story.
- Translate objections into implicit proof, reassurance, education, experience, offer, or PR handling guidance rather than direct fear-based copy.
- Keep local-language phrases as seeds, not final translation.
- Treat claim risk and do-not-say notes as a local PR guide for PR, retail scripts, creator briefs, landing pages, and paid ads.
- Price message seeds must state the downstream use: S04 WTP/value proof input, S05 copy test variant, S06 creator/reviewer proof brief, S07 landing-page price/value block, or S13 validation test.
- Render conditional modules only when produced.
- Do not hide missing proof or review-required claims.
