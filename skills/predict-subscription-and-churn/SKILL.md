---
name: predict-subscription-and-churn
description: Use when a 2C hardware GTM plan includes subscriptions, paid app tiers, recurring service, consumables, warranties, service plans, cloud features, paid insights, renewal economics, retention loops, or churn risk that affects pricing, messaging, lifecycle value, or launch forecast.
---

# Predict Subscription And Churn

## Role

Use this skill as S11 in the GTM intelligence report suite. It models subscription or recurring-service value, churn risk, retention drivers, and pricing linkage for hardware products that depend on paid services, app value, consumables, warranty plans, or renewal behavior.

S11 is conditional. If no subscription, paid service, consumable, warranty/service plan, or retention loop exists, produce a compact skip rationale and data gap rather than a full section.

S11 must not invent cohort retention, billing conversion, service costs, renewal rates, or customer lifetime value. When data is missing, it should show formulas, assumptions, confidence caps, and validation needs.

## Required Inputs

```json
{
  "project_brief": {},
  "price_sensitivity_model": {},
  "activation_risk_map": [],
  "insight_system_boundaries": {}
}
```

High-value optional inputs:

```json
{
  "subscription_or_service_tiers": [],
  "feature_entitlements": [],
  "renewal_rules": "",
  "retention_touchpoints": [],
  "churn_history": [],
  "usage_or_cohort_data": [],
  "service_cost_notes": ""
}
```

## Method

1. Run `subscription_retention_trigger_check` to decide whether S11 renders.
2. Map recurring value drivers: habit, insight, convenience, warranty, cloud, consumable, service, community, and ecosystem lock-in.
3. Estimate retention risk qualitatively unless real cohort data exists; expose formulas and confidence caps.
4. Link subscription value to S04 price architecture, S08 launch forecast, S09 activation risk, and S10 claim boundaries.
5. Separate monetization advice from proof needs: what can be priced, what needs onboarding, what needs validation, and what should stay optional.
6. Pass only compressed outputs, HTML section draft, data gaps, and `post_skill_isolation_record` downstream.

## Output Tiers

Core outputs:

```text
subscription_retention_trigger_check
subscription_value_driver_map
retention_value_driver_map
churn_risk_model
retention_trigger_plan
pricing_retention_linkage
html_subscription_section
post_skill_isolation_record
```

Conditional outputs:

```text
service_tier_fit_matrix
subscription_price_sensitivity_notes
cohort_retention_proxy_model
renewal_risk_guardrails
post_launch_retention_learning_plan
```

Audit outputs:

```text
retention_assumption_trace
formula_trace
excluded_private_billing_data_log
confidence_cap_log
```

## Handoff

S11 may hand off to S12 for review and quality feedback, S13 for validation experiments, and S14 for rendering. Do not expose raw billing, raw cohort, private service-cost, or customer-level usage data in public HTML.
