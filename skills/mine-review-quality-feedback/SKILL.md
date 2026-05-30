---
name: mine-review-quality-feedback
description: Use when post-launch reviews, previous-generation reviews, support tickets, returns, RMA logs, retailer reviews, app-store reviews, warranty claims, customer voice exports, or satisfaction survey text should be converted into product quality, GTM, support, and next-generation feedback loops.
---

# Mine Review And Quality Feedback

## Role

Use this skill as S12 in the GTM intelligence report suite. It turns review, support, return, app, warranty, and customer-voice material into quality themes, marketing feedback, channel fixes, support priorities, and next-generation product and sales recommendations.

S12 is conditional. Before launch, it can use previous-generation or competitor feedback as a hypothesis source. After launch, it should separate actual product feedback from market, channel, onboarding, and expectation problems.

S12 must not omit dissenting viewpoints from the collected corpus, fabricate comments, expose private customer records, or turn a convenience sample into a statistically representative conclusion.

## Required Inputs

```json
{
  "project_brief": {},
  "activation_risk_map": [],
  "subscription_churn_model": {},
  "review_or_support_data": []
}
```

High-value optional inputs:

```json
{
  "previous_generation_reviews": [],
  "retailer_reviews": [],
  "app_store_reviews": [],
  "support_ticket_tags": [],
  "return_reasons": [],
  "rma_logs": [],
  "customer_voice_exports": [],
  "survey_verbatims": []
}
```

## Method

1. Run `feedback_loop_trigger_check` to decide whether S12 renders.
2. Keep source layers separate: retailer reviews, forums, app reviews, support, returns, RMA, warranty, survey text, previous generation, and competitor feedback.
3. Collect viewpoints without intentional omission for the scoped source pages or uploaded files, then deduplicate only after preserving source references.
4. Classify each atom by Bain-style promoter/passive/detractor direction when suitable, journey stage, pain point, praise point, purchase trigger, objection, return reason, and root cause.
5. Score feedback by frequency, sentiment intensity, return or support impact, journey severity, recency, and cross-source consistency.
6. Split actions into product quality backlog, marketing promise correction, channel/PDP fix, support education, and next-generation GTM recommendation.
7. Pass only compressed themes, HTML section draft, evidence refs, gaps, and `post_skill_isolation_record` downstream.

## Output Tiers

Core outputs:

```text
feedback_loop_trigger_check
review_support_source_map
voice_atom_collection_scope
feedback_theme_cluster
quality_feedback_priority
product_quality_backlog
gtm_feedback_backlog
feedback_loop_action_map
evidence_graph_updates
html_feedback_section
post_skill_isolation_record
```

Conditional outputs:

```text
previous_generation_feedback_calibration
competitor_feedback_comparison
return_reason_root_cause_map
support_ticket_theme_map
app_store_experience_map
post_launch_learning_plan
```

Audit outputs:

```text
raw_source_index_ref
deduplication_trace
excluded_private_customer_data_log
representativeness_warning
```

## Handoff

S12 may hand off to S01, S02, S03, S09, S13, and S14. Do not pass raw private customer records or raw source corpora by default; pass only compressed themes, counts, evidence refs, and confidence caps.
