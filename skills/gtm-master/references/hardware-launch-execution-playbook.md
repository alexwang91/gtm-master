# Hardware Launch Execution Playbook

Use this reference when the final HTML must become a direct GTM report for a consumer hardware launch. The goal is to convert analysis into a local execution plan, not to add more methodology prose.

## Public Practice Abstraction

Large consumer-electronics launches commonly combine these operating loops:

- Ecosystem narrative: explain why the product fits the brand ecosystem, connected devices, service trust, and future upgrade path.
- Buying path control: connect official store, named local retailers, authorized dealers, marketplace listings, operator or finance options, and service/warranty routes.
- Content and proof loop: provide buying guides, expert reviews, comparison content, tutorials, demonstrations, FAQ, and post-purchase education.
- Local voice loop: collect reviews, forum comments, video comments, service feedback, and satisfaction/NSS/NPS signals; feed them back to product, quality, retail, and message decisions.
- First-sale war room: track channel go-live, stock, price integrity, PDP quality, traffic, conversion, reviews, sentiment, competitor moves, and service incidents during the first launch window.

Do not cite these as brand case studies inside the main report unless the run specifically analyzes those brands. Use them as reusable GTM operating principles.

## Required Report Blocks

When the user asks for a meeting-ready HTML report, S00 should request these output hooks from the relevant sub-skills and S14 should render them when supplied.

```json
{
  "gtm_judgment_cover": {
    "judgment": "enter | defend | cautious_launch | validate_first | pause | unknown",
    "judgment_label": "",
    "core_recommendation": "",
    "opening_move": "",
    "priority_segment": "",
    "must_win_channel": "",
    "price_or_offer_stance": "",
    "top_competitor_threat": "",
    "budget_posture": "",
    "decision_changing_question": "",
    "confidence": ""
  },
  "gtm_command_center": {
    "objective": "",
    "target_segment": "",
    "hero_claim": "",
    "price_or_offer_position": "",
    "top_competitor_threat": "",
    "expected_weekly_sales_range": {},
    "mkt_budget_posture": "",
    "must_win_channel": "",
    "main_risk": "",
    "confidence": ""
  },
  "sku_offer_ladder": [
    {
      "sku_or_offer": "",
      "role": "hero | anchor | bundle | installment | trade_in | service_pack | defense_offer",
      "target_segment": "",
      "price_or_benefit": "",
      "why_it_exists": "",
      "guardrail": "",
      "evidence_refs": []
    }
  ],
  "launch_calendar": [
    {
      "window": "T-30 | T-14 | T-7 | T0 | T+7 | T+30",
      "workstream": "PR | KOL | retail | ecommerce | DTC | operator | service | supply | measurement",
      "action": "",
      "owner_hint": "",
      "required_asset": "",
      "kpi_or_exit_signal": "",
      "risk_if_missing": ""
    }
  ],
  "channel_war_room": [
    {
      "channel_name": "",
      "channel_role": "awareness | proof | comparison | conversion | installment | availability | service_trust | measurement",
      "priority_rank": 0,
      "launch_readiness": "ready | partial | blocked | unknown",
      "budget_percent_seed": 0,
      "required_asset_or_proof": [],
      "first_week_kpi": "",
      "owner_hint": "",
      "evidence_refs": []
    }
  ],
  "content_seeding_wave_plan": [
    {
      "wave": "expert_review | comparison | lifestyle_creator | community_forum | retail_media | owner_review",
      "purpose": "",
      "recommended_candidates_or_archetypes": [],
      "budget_range": {},
      "expected_signal": "",
      "proof_needed": [],
      "timing": "",
      "confidence": ""
    }
  ],
  "retail_pdp_ready_pack": {
    "local_title_or_search_terms": [],
    "hero_proof_assets": [],
    "comparison_table_needs": [],
    "faq_needs": [],
    "warranty_return_payment_messages": [],
    "review_generation_plan": []
  },
  "sales_enablement_pack": [
    {
      "audience": "retailer_sales | operator_sales | ecommerce | support | pr | creator",
      "talk_track": "",
      "objection_card": "",
      "competitor_battlecard_ref": "",
      "demo_or_proof_needed": "",
      "do_not_say": []
    }
  ],
  "service_trust_loop": {
    "warranty_or_return_readiness": "",
    "support_faq_ready": false,
    "review_or_nss_capture_plan": "",
    "quality_issue_escalation_path": "",
    "post_purchase_education_need": []
  },
  "measurement_war_room": [
    {
      "metric": "",
      "cadence": "daily | twice_weekly | weekly",
      "owner_hint": "",
      "why_it_matters": "",
      "decision_trigger": "",
      "data_source": ""
    }
  ],
  "competitive_response_playbook": [
    {
      "competitor_move": "price_drop | bundle | review_push | retailer_promo | claim_attack | stock_advantage | ecosystem_push",
      "early_signal": "",
      "recommended_response": "",
      "budget_or_margin_impact": "",
      "approval_needed": ""
    }
  ]
}
```

## Section Ownership

```text
S03 owns hero message, proof asset need, retail talk track seed, and objection cards.
S04 owns price/offer guardrails, WTP conclusion, promotion posture, and private-profit calculator inputs.
S06 owns content seeding waves, KOL/reviewer fit, budget ranges, expected signals, and proof-risk notes.
S07 owns DTC/PDP readiness when triggered by a live page, landing page, or conversion material.
S08 owns command center, channel war room, launch calendar, measurement war room, forecast bridge, and budget posture.
S12 owns post-launch review/service feedback loops when triggered by available feedback.
S14 renders the blocks without inventing missing actions.
```

## Direct Report Rules

- Use named local channels when they are discovered or user-supplied. Generic labels such as `local ecommerce` or `retail` are allowed only as temporary labels with an evidence gap.
- Every action block must include an owner hint, timing or cadence, KPI or decision trigger, and confidence label.
- Every budget or outcome estimate must show whether it is user-supplied, public proxy, platform estimate, historical proxy, or AI heuristic.
- Do not show internal skill IDs, handoff mechanics, or context-budget notes in the main report. Put them in source governance appendix only when requested.
- Do not make the report longer by adding generic best practices. Add a block only when it changes the local action, proof need, budget decision, channel priority, or validation plan.
