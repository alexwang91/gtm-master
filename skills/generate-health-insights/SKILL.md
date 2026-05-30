---
name: generate-health-insights
description: Use when a hardware GTM plan includes wellness, health-adjacent, biometric, AI insight, safety, privacy-sensitive, children, elderly, regulated-adjacent, advisory, or sensitive product claims that need proof boundaries, wording guardrails, or retention insight framing.
---

# Generate Insight And Claim Guardrails

## Role

Use this skill as S10 in the GTM intelligence report suite. It defines what can be said, what requires stronger proof, what should be avoided, and which insight or safety claims need human review before they reach copy, creators, PDP, retail training, or customer support.

S10 is conditional. If the product has no health, wellness, AI insight, safety, privacy, children, elderly, regulated-adjacent, or advisory claim trigger, produce a compact skip rationale and data gap.

S10 must not provide legal advice, approve regulated claims, invent clinical proof, or transform unverified sensor outputs into medical or safety promises.

## Required Inputs

```json
{
  "project_brief": {},
  "activation_risk_map": [],
  "device_signal_context": {},
  "claim_list": []
}
```

High-value optional inputs:

```json
{
  "approved_claims": [],
  "forbidden_claims_or_words": [],
  "proof_sources": [],
  "local_compliance_constraints": "",
  "sensitive_user_groups": [],
  "privacy_and_data_handling_notes": ""
}
```

## Method

1. Run `insight_claim_trigger_check` to decide whether S10 renders.
2. Classify claims by sensitivity: factual spec, lifestyle benefit, wellness insight, safety advisory, privacy/data, children/elderly, and regulated-adjacent.
3. Score each claim by proof strength, consumer harm risk, local compliance uncertainty, channel amplification risk, and support burden.
4. Convert claims into allowed wording, needs-proof wording, avoid wording, and human-review queues.
5. Build privacy and safety proof requirements for PDP, creator brief, retail talk track, support FAQ, and validation tests.
6. Pass only compressed guardrails, HTML section draft, data gaps, and `post_skill_isolation_record` downstream.

## Output Tiers

Core outputs:

```text
insight_claim_trigger_check
insight_system_boundaries
claim_guardrail_matrix
privacy_safety_proof_need
human_review_queue
retention_insight_opportunities
html_insight_section
post_skill_isolation_record
```

Conditional outputs:

```text
health_claim_risk_rules
ai_insight_claim_boundaries
children_elderly_safety_guardrails
privacy_disclosure_requirements
creator_claim_brief
support_claim_escalation_notes
```

Audit outputs:

```text
claim_evidence_trace
excluded_sensitive_material_log
compliance_review_gap_log
```

## Handoff

S10 may hand off guardrails to S11, S13, and S14. Do not expose legal notes, sensitive proof files, private claim drafts, or unsupported claim language in public HTML.
