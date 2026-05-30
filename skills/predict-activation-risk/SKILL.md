---
name: predict-activation-risk
description: Use when a 2C hardware launch has setup, onboarding, installation, sizing, compatibility, app pairing, expectation mismatch, warranty, support, or return risk that may affect adoption, reviews, channel conversion, or post-purchase satisfaction.
---

# Predict Activation And Return Risk

## Role

Use this skill as S09 in the GTM intelligence report suite. It converts setup, onboarding, compatibility, expectation, support, and return-risk evidence into a prevention plan for launch messaging, retail training, PDP proof, support content, and post-purchase education.

S09 is conditional. If no activation, setup, compatibility, warranty, support, or return concern is triggered, produce a compact skip rationale and data gap rather than a full section.

S09 must not invent return rates, diagnose product defects without evidence, expose private support data, or treat synthetic persona reactions as real post-purchase feedback.

## Required Inputs

```json
{
  "project_brief": {},
  "message_architecture": [],
  "launch_sales_forecast": {},
  "app_or_onboarding_context": {}
}
```

High-value optional inputs:

```json
{
  "setup_steps_or_user_manual": "",
  "compatibility_rules": [],
  "warranty_or_return_policy": "",
  "support_ticket_tags": [],
  "previous_generation_return_reasons": [],
  "retailer_review_complaints": [],
  "unboxing_or_activation_flow": ""
}
```

## Method

1. Run `activation_return_trigger_check` to decide whether the module should render, skip, or ask for private/post-launch material.
2. Map the hardware journey: purchase, unboxing, setup, pairing or installation, first use, first week, support, return.
3. Score each friction by frequency signal, severity, preventability, channel impact, and downstream review risk.
4. Separate product quality risk, expectation mismatch, setup education, compatibility limits, channel promise risk, and support friction.
5. Produce prevention actions that marketing can use without overstating weaknesses: proof placement, expectation setting, setup copy, retail talk tracks, FAQ, and support handoff.
6. Pass only the compressed handoff, HTML section draft, data gaps, and `post_skill_isolation_record` downstream.

## Output Tiers

Core outputs:

```text
activation_return_trigger_check
activation_journey_risk_map
expectation_gap_map
return_prevention_priority
support_education_plan
channel_expectation_guardrails
html_activation_section
post_skill_isolation_record
```

Conditional outputs:

```text
compatibility_risk_matrix
setup_script_or_faq_brief
previous_generation_return_calibration
retailer_pdp_risk_notes
post_launch_return_learning_plan
```

Audit outputs:

```text
activation_evidence_trace
excluded_private_support_data_log
assumption_and_confidence_cap_log
```

## Handoff

S09 may hand off to S10 for sensitive claims, S12 for feedback loops, S13 for validation experiments, and S14 for rendering. Do not hand off raw support tickets, raw review corpora, raw return records, or private warranty notes unless the user explicitly approves.
