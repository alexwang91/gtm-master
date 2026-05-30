# S09-S12 Trigger Matrix

Use this before enabling the future product-experience loop. S09-S12 are valuable, but they should not run by default for every pre-launch hardware report.

## Global Rule

```text
Default behavior
  Skip S09-S12 unless the product facts, user inputs, or prior module gaps trigger them.

Skip policy
  skip_when_not_triggered
  skip_when_missing_required_private_or_post_launch_materials

S14 behavior
  Omit non-triggered S09-S12 sections from the report body. Show only a short data-gap or roadmap note when the user asks for full-suite coverage or when a trigger is present but required materials are missing.
```

## Trigger Matrix

| Skill | Run when | Useful inputs | Skip when | S14 section |
| --- | --- | --- | --- | --- |
| S09 activation/return risk | Setup, onboarding, app pairing, sizing, installation, expectation mismatch, compatibility risk, return risk, warranty friction, or high post-purchase anxiety affects adoption. | app or onboarding flow, setup steps, compatibility rules, warranty/return policy, support tickets, previous-generation return reasons, user manuals, sizing or installation constraints. | `skip_when_not_triggered`; `skip_when_missing_required_private_or_post_launch_materials` if the only path requires unavailable returns/support data. | Render `activation_return_risk` only when triggered; otherwise omit from body. |
| S10 insight/claim guardrails | Health, wellness, AI insight, safety, children, elderly, regulated-adjacent, biometric, privacy-sensitive, or advisory claims appear in product features or messages. | claim list, sensor or data context, compliance constraints, safety caveats, user populations, local regulatory notes, approved/disallowed wording. | `skip_when_not_triggered`; `skip_when_missing_required_private_or_post_launch_materials` if claim boundaries require unavailable legal/compliance material. | Render `insight_guardrails` only when triggered; otherwise omit from body. |
| S11 subscription/churn | Subscription, paid app, recurring service, consumable, warranty/service plan, paid insights, cloud service, retention loop, or renewal economics matter. | pricing model, service tiers, feature entitlements, renewal rules, churn history, retention touchpoints, app usage or cohort data, support plan economics. | `skip_when_not_triggered`; `skip_when_missing_required_private_or_post_launch_materials` if churn modeling needs unavailable cohort or billing data. | Render `subscription_churn` only when triggered; otherwise omit from body. |
| S12 review-quality feedback | Post-launch reviews, support tickets, returns, NSS/NPS, RMA, app-store reviews, retailer reviews, warranty claims, or quality feedback exist. | review exports, support tags, return reasons, RMA logs, NPS/NSS verbatims, app-store reviews, retailer reviews, previous-generation quality data. | `skip_when_not_triggered`; `skip_when_missing_required_private_or_post_launch_materials` when no post-launch or previous-generation feedback exists. | Render `review_quality_feedback` only when triggered; otherwise omit from body. |

## Pre-Launch Handling

For a pre-launch report, S09-S12 usually stay skipped unless:

- the product experience itself is a launch risk
- messages include sensitive claims
- revenue depends on recurring payment or retention
- the user provides previous-generation or beta feedback

When skipped, S00 should still preserve the trigger decision in `decision_log` and allow S13 to convert any relevant unresolved trigger into a validation experiment.

## Required Skip Record

When S09-S12 are skipped, use a compact record:

```json
{
  "skill_id": "S09 | S10 | S11 | S12",
  "status": "skipped_not_triggered | blocked_missing_materials",
  "trigger_check": [],
  "missing_inputs": [],
  "s14_body_policy": "omit_unless_requested_or_triggered",
  "handoff_ref": ""
}
```

If a future S09-S12 skill is implemented, it must still emit `post_skill_isolation_record` when it runs or skips.
