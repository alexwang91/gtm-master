# Proof And Risk Mapping

Use this after JTBD scenarios are clustered and before handoff to S03, S04, S13, or S14.

## Proof Requirement Seed

Proof requirements answer: "What must the consumer believe before this scenario can convert?"

```json
{
  "proof_requirement_seed": [
    {
      "proof_id": "",
      "scenario_refs": [],
      "segment_refs": [],
      "claim_or_question": "",
      "proof_type": "spec_or_lab_test | demo_video | comparison_chart | expert_review | certification | warranty_service_proof | user_review | local_retail_proof | app_screenshot | setup_walkthrough | price_value_breakdown | privacy_security | durability_test | other",
      "current_proof_status": "available | partial | missing | risky",
      "proof_requirement_urgency_score": 0,
      "owner_hint": "product | marketing | sales | channel | support | compliance | unknown",
      "evidence_refs": [],
      "confidence": "high | medium | low",
      "handoff_to": ["S03", "S04", "S05", "S07", "S13"]
    }
  ]
}
```

## Anti-JTBD Risk List

Anti-JTBD risks explain why consumers do not buy, do not switch, do not repeat, or do not recommend.

```json
{
  "anti_jtbd_risk_list": [
    {
      "risk_id": "",
      "scenario_refs": [],
      "risk_name": "",
      "risk_type": "non_consumption | trade_down | trade_up | delay_purchase | competitor_stickiness | substitute_suffices | expectation_gap | setup_friction | support_return | trust_claim | price_value | subscription_resistance | privacy | channel_friction | other",
      "risk_mechanism": "",
      "affected_segments": [],
      "journey_episode_refs": [],
      "anti_jtbd_risk_score": 0,
      "mitigation_seed": "",
      "evidence_refs": [],
      "confidence": "high | medium | low",
      "data_gaps": []
    }
  ]
}
```

## Non-Consumption Risk Map

Use this when the consumer may simply do nothing.

```json
{
  "non_consumption_risk_map": [
    {
      "scenario_id": "",
      "reason_for_doing_nothing": "",
      "current_workaround": "",
      "urgency_trigger_needed": "",
      "proof_or_offer_needed": "",
      "confidence": "high | medium | low",
      "evidence_refs": []
    }
  ]
}
```

## Local Trigger Phrase Map

```json
{
  "local_language_trigger_phrase_map": [
    {
      "scenario_id": "",
      "language": "",
      "phrase": "",
      "literal_translation": "",
      "usage_context": "search_query | review_language | forum_phrase | retailer_language | objection | social_video_comment | other",
      "message_implication": "",
      "evidence_refs": [],
      "confidence": "high | medium | low"
    }
  ]
}
```

## Validation Question Seed

Use weak but important scenarios, proof needs, and anti-JTBD risks to build validation prompts.

```json
{
  "validation_question_seed": [
    {
      "question_id": "",
      "scenario_refs": [],
      "question_type": "survey | interview | message_test | price_test | landing_page_test | retail_objection_test | support_tag_audit | review_followup",
      "question": "",
      "what_it_validates": "",
      "success_signal": "",
      "failure_signal": "",
      "priority": "high | medium | low"
    }
  ]
}
```

## Claims To Avoid

S02 should flag claim risks early but leave final message architecture to S03.

Add a `claims_to_avoid` note when:

- The proof is missing or weak.
- Local consumer wording implies skepticism.
- The claim touches health, safety, children, elderly, privacy, accuracy, battery, certification, or regulated-adjacent areas.
- Competitor evidence shows overpromising creates returns, complaints, or negative reviews.
- The product can satisfy the job only after setup, app pairing, subscription, or service support.
