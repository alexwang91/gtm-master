# Message Architecture Methods

Use this when building the S03 core outputs.

## Message Architecture Principle

A good message architecture connects:

```text
segment + scenario + desired progress
-> benefit
-> feature or capability
-> proof
-> objection response
-> safe wording boundary
```

Do not start with the product feature. Start with the scenario and the consumer question.

## Segment Message Architecture

For each lead scenario and segment pair:

1. Identify the consumer's progress need.
2. Identify the message role: lead, support, proof, objection handling, retention, or avoid.
3. Convert the job into a benefit statement seed.
4. Link the benefit to product capabilities.
5. Attach proof requirements and proof status.
6. Attach objections and claims to avoid.
7. Preserve local-language search and objection terms.

## Feature-Benefit-Proof Matrix

Use this chain:

```text
feature/capability
-> functional benefit
-> emotional/social benefit when supported
-> proof type
-> proof status
-> claim risk
```

Hardware proof types:

```text
spec_or_lab_test
expert_review
comparison_chart
demo_video
setup_walkthrough
compatibility_list
warranty_service_proof
privacy_security_proof
user_review_or_rating
retailer_or_marketplace_proof
certification
durability_test
```

## Objection Handling Matrix

Convert anti-JTBD risks into response strategy seeds:

```text
objection
-> why it matters
-> what not to say
-> proof needed
-> response strategy seed
-> downstream owner
```

Common hardware objections:

- Too expensive for the perceived difference
- Hard to set up or pair with app
- Battery or durability concern
- Accuracy or reliability skepticism
- Privacy or data use concern
- Warranty, returns, local support concern
- Better-known competitor feels safer
- Retailer or marketplace trust issue
- Subscription or ongoing cost resistance

## Competitive Contrast

Use competitor contrast only when evidence supports it.

```json
{
  "competitive_contrast_matrix": [
    {
      "scenario_id": "",
      "competitor_or_substitute_ref": "",
      "consumer_comparison_question": "",
      "our_supported_contrast": "",
      "proof_needed": [],
      "do_not_claim": [],
      "confidence": "high | medium | low",
      "evidence_refs": []
    }
  ]
}
```

Rules:

- Prefer "best for [scenario]" framing over broad superiority claims.
- Do not claim a competitor weakness unless it is evidenced and allowed.
- If proof is missing, convert contrast into a validation or proof need.

## Price Message Seed

S03 does not make final pricing decisions. It frames value and objection context for S04.

```json
{
  "price_message_seed": [
    {
      "scenario_id": "",
      "segment_refs": [],
      "price_message_type": "premium_justification | value_for_money | affordability_support | promo_or_bundle | subscription_explanation | risk_reversal | avoid_price_lead",
      "value_argument_seed": "",
      "proof_needed": [],
      "price_objections": [],
      "handoff_to_s04": true,
      "confidence": "high | medium | low"
    }
  ]
}
```

## Local Language Message Seed

```json
{
  "local_language_message_seed": [
    {
      "scenario_id": "",
      "segment_refs": [],
      "language": "",
      "term_or_phrase": "",
      "literal_translation": "",
      "message_use": "headline_seed | proof_label | objection_language | search_term | comparison_phrase | avoid_phrase",
      "reason_to_preserve": "",
      "confidence": "high | medium | low",
      "evidence_refs": []
    }
  ]
}
```

S03 should preserve phrases and intent. S16 owns final localization/transcreation.
