# S07 Conversion Methods

Use these methods after input coverage and before scoring.

## Prelaunch Benchmark Mode

Use this mode when the user's own landing page, PDP, checkout, preorder, or waitlist funnel is not live or not drafted.

Benchmark available competitor, local marketplace/retailer, category, and previous-generation pages against the launch decision that S07 must support. Do not infer that competitor practices are optimal; treat repeated patterns as category norms, proof expectations, or hypotheses to test.

Compare:

```text
hero promise and first-screen clarity
segment/use-case specificity
local language and search-intent wording
proof order: specs, demo, reviews, expert proof, certifications, comparison
objection handling and alternative framing
price/offer presentation, financing, bundles, discount, urgency
trust surface: warranty, return, delivery, payment, support, privacy, stock
CTA flow: buy, preorder, waitlist, retailer clickout, lead capture
mobile scanability and information hierarchy
tracking/event readiness
```

Output:

```json
{
  "competitor_landing_pdp_benchmark": [],
  "previous_generation_funnel_learnings": [],
  "category_page_requirement_brief": [],
  "prelaunch_page_recommendation_pack": [],
  "launch_tracking_requirement_brief": []
}
```

Prelaunch recommendations must be labeled `planning_recommendation` or `hypothesis_only`. Produce CVR ranges only when measured internal results, valid test results, category benchmarks, previous-generation results, or explicit user-approved heuristic assumptions exist.

## Funnel Stage Model

Model the conversion path as stages:

```text
traffic_source -> entry_promise -> landing_or_PDP_hero -> proof_and_comparison -> price_offer -> trust_policy -> CTA -> checkout_or_clickout -> confirmation
```

For preorder or waitlist:

```text
traffic_source -> entry_promise -> launch_reason -> proof -> risk_reversal -> CTA -> form -> confirmation_and_followup
```

For prelaunch planning:

```text
target_segment -> search_or_channel_intent -> expected_page_job -> required_proof -> price_offer_requirement -> trust_requirement -> CTA_requirement -> tracking_requirement
```

## Conversion Hypothesis Formula

Use the formula as a diagnostic scaffold, not as a real CVR claim:

```text
Conversion readiness =
  traffic_intent_fit
* message_continuity
* proof_readiness
* price_value_credibility
* trust_and_risk_reversal
* checkout_or_form_ability
* measurement_readiness
```

Report the components as 0-100 scores and confidence labels. Do not multiply scores into a precise sales forecast.

## Friction Categories

Check:

```text
message mismatch
unclear segment or use case
unsupported proof claim
price shock or value ambiguity
missing comparison or alternative framing
weak reviews, warranty, return, delivery, payment, support, or privacy trust
CTA ambiguity or too many CTAs
mobile readability or load/scan friction
checkout, payment, shipping, tax, stock, or retailer clickout friction
tracking, attribution, or event gaps
```

## Traffic Continuity

For each traffic source, map:

```json
{
  "traffic_source": "",
  "source_intent": "",
  "entry_message_or_ad_promise": "",
  "landing_match": "",
  "proof_needed_on_arrival": "",
  "likely_objection": "",
  "required_tracking": "",
  "confidence": ""
}
```

Creator/KOL traffic must use S06 expected outcome estimates only as traffic assumptions.

## CVR Assumption Ladder

When S07 must provide a conversion assumption to S08, use ranges:

```json
{
  "scenario": "conservative | base | upside",
  "conversion_action": "",
  "cvr_range": {"min": 0, "max": 0},
  "basis": "measured_internal | valid_test_result | platform_or_category_benchmark | historical_proxy | heuristic_hypothesis",
  "confidence": "high | medium | low | hypothesis_only",
  "confounders": []
}
```

If no measured or benchmark basis exists, cap confidence at `hypothesis_only` and avoid revenue conclusions.

If the launch page does not exist, prefer `missing_cvr_basis` plus page/tracking recommendations over invented CVR ranges. Use a CVR ladder only when the basis field can honestly name measured internal data, valid test results, platform/category benchmark, historical proxy, or explicit heuristic hypothesis.

## Previous-Generation Learning Extraction

When previous-generation materials or results are supplied, extract:

```json
{
  "source": "previous_page | previous_pdp | previous_campaign | previous_analytics | previous_reviews | previous_sales_channel_feedback",
  "observed_pattern": "",
  "likely_conversion_driver_or_blocker": "",
  "evidence_strength": "high | medium | low",
  "keep_change_or_test": "keep | change | test | avoid",
  "recommendation_for_next_generation": "",
  "evidence_refs": []
}
```

Never expose private performance values in public HTML unless approved. Summarize private data as direction, range, or confidence cap when needed.

## Experiment Design

Each experiment should include:

```json
{
  "experiment_id": "",
  "hypothesis": "",
  "funnel_stage": "",
  "variant_or_test": "",
  "primary_metric": "",
  "secondary_metrics": [],
  "minimum_traffic_or_sample_note": "",
  "decision_rule": "",
  "confounders": [],
  "owner": "",
  "priority_score": 0
}
```

Prefer the smallest test that reduces the biggest downstream decision uncertainty.
