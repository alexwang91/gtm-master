---
name: model-price-sensitivity
description: Use when converting S01 price evidence, S02 scenario price implications, and S03 price message seeds into local price credibility models, segment WTP hypotheses, price sensitivity models, promotion/subscription guidance, pricing tests, compressed handoffs, and HTML pricing sections for 2C hardware GTM work.
---

# Model Price Sensitivity

## Role

Use this skill as S04 in the GTM intelligence report suite. It turns local price evidence and message context into a launch pricing model: what opening price posture to use, how public anchor price differs from transaction price, which segments are price sensitive, what proof is needed, what floor protects economics, and what tests must run before launch.

S04 can recommend opening price hypotheses, offer mechanisms, testable price bands, and a 30/60/90 price path. It should not present a final approved price, revenue maximum, or profit maximum when margin, COGS, channel terms, tax, promo policy, demand elasticity, or internal constraints are missing.

## Required Inputs

```json
{
  "project_brief": {},
  "market_context_pack": {},
  "scenario_price_implication_seed": [],
  "price_message_seed": []
}
```

High-value upstream fields:

```json
{
  "local_price_corridor": {},
  "price_anchor_panel": {},
  "competitor_price_gap_table": [],
  "segment_price_sensitivity_seeds": [],
  "value_proof_requirement_matrix": [],
  "promotion_subscription_sensitivity_seed": [],
  "price_ladder_scan": [],
  "jump_decision_risks": [],
  "price_complaints": [],
  "user_provided_price_hypotheses": [],
  "segment_message_architecture": [],
  "objection_matrix": [],
  "claim_risk_and_proof_gate": {},
  "scenario_commercial_weight_map": [],
  "digital_shelf_and_retailer_decision_map": [],
  "segment_priority_ranking": [],
  "segment_level_tam_sam_som": [],
  "channel_fit_scores": [],
  "confidence_caps": {}
}
```

Optional private inputs:

```json
{
  "target_price_or_msrp": "",
  "target_margin_or_floor_price": "",
  "cogs_or_bom": "",
  "channel_margin_terms": "",
  "retailer_or_marketplace_fee_rules": "",
  "promo_discount_policy": "",
  "previous_generation_sales_price_channel_performance": "",
  "inventory_or_forecast_constraints": "",
  "subscription_or_recurring_revenue_model": "",
  "finance_installment_constraints": "",
  "strategic_price_objective": "profit | revenue | share | positioning | channel_entry | inventory_velocity | unknown",
  "base_demand_units": "",
  "reference_price": "",
  "own_price_elasticity": "",
  "mkt_spend_or_budget": "",
  "mkt_response_multiplier": "",
  "channel_availability_multiplier": "",
  "proof_maturity_multiplier": "",
  "stock_availability_multiplier": ""
}
```

Private pricing inputs are requested when S04 starts, not required at S00. If unavailable, continue with hypothesis-only pricing guidance, confidence caps, and a research/test plan.

## Load Order

Read only what the current task needs:

1. Read `references/output-contract.md` before producing any artifact, handoff, or report section.
2. Read `references/upstream-input-map.md` before checking S01/S02/S03 price inputs or deciding whether S04 can proceed.
3. Read `references/pricing-methods.md` before building price credibility, price sensitivity, WTP hypotheses, value proof, promo/subscription, or channel price guidance.
4. Read `references/opening-price-strategy.md` before recommending opening price posture, public anchor, transaction mechanism, price floors, revenue/profit optimizer specs, or 30/60/90 price path.
5. Read `references/rapid-price-prior.md` before building WTP priors when real country research is unavailable, when only public proxies exist, or when the user requests one-click rapid validation.
6. Read `references/pricing-test-design.md` before creating Van Westendorp, Gabor-Granger, conjoint/DCE, monadic price, promo, or landing-page price tests.
7. Read `references/pricing-test-result-interpretation.md` before interpreting uploaded survey, ad A/B, landing-page, marketplace, retail, or internal sales test results.
8. Read `references/pricing-decision-gate.md` before producing pricing decision status, candidate options, blockers, or downstream handoff readiness.
9. Read `references/private-pricing-calculator.md` before designing offline/local HTML pricing calculators, encrypted local snapshots, or derived-only private pricing summaries.
10. Read `references/scoring-rubrics.md` before assigning price credibility, opening strategy, sensitivity, WTP confidence, rapid WTP prior, promo risk, or pricing readiness scores.
11. Read `references/evidence-usage-policy.md` before using evidence refs, RAG, internal private data, or local storage.
12. Read `references/html-visual-block-generation.md` before producing S14-ready `visual_blocks` for the HTML pricing section draft.
13. Read `references/html-section-contract.md` before producing the HTML pricing section draft.

## Depth Modes

```text
quick
  Produce core outputs only: input gate, local price credibility, segment WTP hypotheses, price sensitivity model, value proof matrix, price risk guardrails, and compact handoff.

standard
  Produce core outputs and triggered conditional modules. Include at least one recommended WTP test plan when confidence is not high.

deep
  Add full price anchor audit, scenario sensitivity calculations, channel/margin guardrails, test survey design, conjoint/DCE plan, promo/subscription tests, and elasticity assumption seed.
```

Default to `standard`.

## Output Tiers

Core outputs, always produced:

```text
price_input_coverage_gate
opening_price_strategy
launch_price_architecture
local_price_credibility_model
rapid_price_prior
segment_wtp_hypothesis
price_sensitivity_model
price_value_proof_matrix
price_risk_guardrail
wtp_test_plan
promo_subscription_guidance
private_profit_revenue_optimizer_spec
price_path_30_60_90
pricing_decision_gate
pricing_handoff_summary
```

Conditional outputs, produced only when triggered:

```text
van_westendorp_test_design
gabor_granger_test_design
conjoint_dce_test_plan
channel_margin_guardrail
retail_price_integrity_map
subscription_pricing_hypothesis
promo_test_plan
elasticity_assumption_seed
pricing_decision_options
private_pricing_calculator_spec
pricing_test_execution_kit
pricing_test_result_interpretation
```

Audit outputs, preserved in the full artifact or as refs but not default HTML:

```text
price_anchor_audit
competitor_price_gap_audit
price_assumption_log
sensitivity_calculation_trace
private_pricing_input_register
```

Conditional triggers:

```text
van_westendorp_test_design
  Trigger when there is no reliable WTP evidence and the product is high-consideration or price-sensitive.

gabor_granger_test_design
  Trigger when a small set of specific candidate prices or MSRP options needs purchase-intent testing.

conjoint_dce_test_plan
  Trigger when feature/price/bundle tradeoffs are important and sample size or research budget allows.

channel_margin_guardrail
  Trigger when COGS, margin, retail, distributor, marketplace, promo, or MAP/MSRP constraints are provided or required.

retail_price_integrity_map
  Trigger when multiple retailers/marketplaces, promo conflicts, cross-border pricing, or channel conflict matters.

subscription_pricing_hypothesis
  Trigger when subscription, app service, consumables, warranty extension, financing, or recurring cost exists.

promo_test_plan
  Trigger when discounting, bundles, launch offers, coupons, free shipping, installments, or freebies are likely to affect conversion.

elasticity_assumption_seed
  Trigger when S08 forecast, S07 conversion, inventory, or revenue scenario depends on price elasticity.

pricing_decision_options
  Trigger when enough price, proof, segment, channel, and internal constraint evidence exists to propose options.

private_pricing_calculator_spec
  Trigger when COGS, margin, channel terms, promo policy, or retailer fees are confidential and should be calculated in the final HTML without entering the LLM context.

private_profit_revenue_optimizer_spec
  Trigger when revenue-max or profit-max price is requested, when private economics are missing but needed, or when S08 forecast depends on price elasticity, MKT spend, channel availability, or proof maturity.

pricing_test_execution_kit
  Trigger when the user wants a practical way to run price testing, collect respondent results, or upload test result CSVs for later analysis.

pricing_test_result_interpretation
  Trigger when survey, ad A/B, landing-page, marketplace, retail, channel, or internal sales test results are provided.
```

## Execution Workflow

Follow this sequence:

```text
1. Validate price input coverage and private constraint availability
2. Normalize local price context: currency, tax, shipping, financing, subscription, bundle, promo, warranty, and channel norms
3. Classify target price against local anchors and competitor/substitute price ladder
4. Build opening_price_strategy and launch_price_architecture: public anchor, expected transaction range, offer mechanism, floors, and strategy score trace
5. Build local price credibility model
6. If real WTP or sales evidence is missing, build rapid_price_prior with factor weights, evidence caps, prior range, and calibration plan
7. Build segment WTP hypotheses from S01 price seeds, S02 scenario price implications, S03 price messages, and rapid_price_prior limits
8. Build price sensitivity model and price-value proof matrix
9. Build price risk guardrails: affordability, premium justification, claim/proof, channel, promo, subscription, return/support, and margin gaps
10. If private pricing data should not enter context, build private calculator and profit/revenue optimizer specs instead of requesting raw values in chat
11. Build price_path_30_60_90 with triggers, allowed moves, forbidden moves, and guardrails
12. Build WTP test plan and triggered pricing research designs
13. Build pricing test execution kit when the user wants to run tests
14. If test results are provided, run result ingestion, data quality gate, interpretation, and decision update
15. Build promo/subscription guidance and triggered retail/channel modules
16. Build pricing decision gate: decision status, blockers, candidate options, and downstream readiness
17. Build pricing handoff summary for S07/S08/S14
18. Produce compressed handoff pack
19. Produce HTML pricing section draft with S14-ready visual blocks
```

## Scope Boundary

S04 owns:

- Local price credibility and anchor interpretation
- Opening price strategy, public anchor vs transaction price architecture, and 30/60/90 price path
- Segment WTP hypotheses
- Price sensitivity model
- Price-value proof requirements
- Promo, subscription, bundle, financing, and risk-reversal guidance
- Pricing research and test plans
- Pricing test result interpretation and decision updates when real results are provided
- Pricing decision gate status and candidate pricing options for review, testing, forecast, or blocking
- Private local pricing calculator specs for confidential COGS, margin, channel, promo, and fee calculations
- Private local profit/revenue optimizer specs for confidential demand, elasticity, COGS, channel, MKT spend, and unit economics inputs
- Price risk guardrails for S07/S08/S14

S04 does not own:

- Final company-approved price without internal constraints
- Final discount budget
- Final margin plan
- Final channel contract terms
- Final revenue forecast
- Final revenue-max or profit-max price without private inputs, elasticity assumptions, and finance/channel approval
- Final creative or landing-page execution

## Required Output

Always return the S04 output envelope from `references/output-contract.md`:

```json
{
  "full_artifact": {},
  "compressed_handoff_pack": {},
  "html_section_draft": {},
  "evidence_updates": [],
  "decision_updates": [],
  "data_gaps": [],
  "post_skill_isolation_record": {},
  "recommended_next_skills": []
}
```

## Quality Rules

- Treat target price as a hypothesis until local anchors, proof, and internal constraints support it.
- Keep surveyed/panel WTP, internal sales data, public price evidence, and inferred proxies separated.
- Do not use AI personas, synthetic respondents, or simulated local consumers as WTP evidence or as the basis for a final price. Use them only to generate hypotheses, localize wording, and pretest survey logic.
- Do not infer exact WTP from search volume, social buzz, or review intensity.
- When real research is unavailable, quantify a rapid WTP prior with explicit factor weights, evidence levels, confidence caps, and calibration actions. Label it as a prior, not measured WTP.
- Treat COGS/BOM, target margin, channel fees, promo policy, and retailer terms as private commercial constraints that may arrive during S04.
- When confidentiality matters, prefer a blank client-side HTML calculator over asking the user to paste raw COGS, margin, or channel terms into the prompt.
- Do not recommend a final price when COGS, margin, channel terms, tax, or promo constraints are missing; provide price hypotheses and test plan instead.
- Separate public anchor price, expected transaction price, promo floor, channel floor, revenue-max price, and profit-max price. Do not collapse them into one "recommended price."
- Do not output revenue-max or profit-max price from public proxies alone. Use a private local optimizer, explicit private upload, or user-approved derived summary.
- Avoid low opening prices for cold, low-volume, scarce, or weakly competitive products unless evidence shows a lower price will unlock real scale.
- Use `pricing_decision_gate` to distinguish `research_first`, `controlled_test_ready`, `finance_review`, `channel_review`, `forecast_ready`, and `blocked`.
- Every price conclusion needs evidence refs, assumptions, confidence, and data gaps.
- Flag price-message mismatch when S03 messages cannot support the price premium.
- Flag channel conflict when retailer, marketplace, DTC, promo, or regional price norms may collide.
- Do not treat uncontrolled ad, marketplace, retail, or time-window results as causal proof. Check randomization, traffic quality, stock, placement, competitor promos, and channel conditions first.
- Separate sell-in, sell-through, click intent, add-to-cart, checkout, preorder, and paid purchase. They imply different evidence strength.
- Keep private margin, COGS, sales, and channel data out of public HTML unless approved.
- Use conditional modules only when triggered; keep audit outputs out of default HTML.
