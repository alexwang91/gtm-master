---
name: gtm-for-everything
description: Use when creating an English GTM strategy dashboard for any product, service, market, creator, app, enterprise offer, consumer product, or business idea, especially when the user wants a consulting-style HTML report, McKinsey-style executive decision surface, concise English narrative, anti-slop prose, or a general GTM framework outside the hardware-specific gtm-master suite.
---

# GTM for Everything

## Role

Use this skill to turn a product, service, business idea, market, or launch plan
into a polished English GTM dashboard. It is broader than `gtm-master`: it can
handle software, hardware, services, marketplaces, content products, agencies,
B2B offers, B2C offers, and early ideas.

The output should feel like a senior strategy team made it: fact-led, tightly
structured, visually calm, and useful for decisions.

## Required Inputs

Minimum input:

```json
{
  "offer": "",
  "target_market_or_country": "",
  "target_customer": "",
  "price_or_business_model": ""
}
```

Useful optional inputs:

```json
{
  "launch_timing": "",
  "current_traction_or_sales": "",
  "competitors_or_alternatives": [],
  "channels_or_partners": [],
  "budget": "",
  "constraints": "",
  "private_materials": [],
  "desired_decision": "launch | reposition | price | channel | fundraising | board_review | sales_plan"
}
```

## Load Order

Read only what the task needs:

1. `references/output-contract.md` before defining the dashboard structure.
2. `references/consulting-dashboard-style.md` before designing the HTML report.
3. `references/stop-slop-editorial-gate.md` before writing or editing English.

## Workflow

1. Define the offer and decision context.
2. Name the market, customer, buyer, user, and economic decision maker.
3. Map the category, competitors, substitutes, and status quo.
4. Build the demand logic: problem, trigger, use case, urgency, proof need, and willingness to pay.
5. Choose a GTM wedge: segment, channel, message, proof, offer, and first conversion motion.
6. Build the launch plan: 30/60/90 days, budget posture, channel sequence, owners, and metrics.
7. Render the English HTML dashboard from structured sections.
8. Run the stop-slop editorial gate and consulting-style visual gate before delivery.

## Output Rules

- Write dashboard-facing text in English only.
- Use a self-contained static HTML file by default.
- Use consulting-style structure: executive answer first, evidence second, action third.
- Prefer tables, scorecards, simple waterfall/ladder/matrix views, and compact charts.
- Avoid decorative hero pages, generic marketing copy, and verbose essays.
- Label inference, assumptions, and data gaps.
- Do not invent facts, sources, prices, or market sizes.
- Use `stop-slop` as an editorial reference. Attribute it when documenting the method.

## English Voice

Use clear business English. Cut filler. Vary sentence rhythm. Write direct
claims with evidence and owners. Avoid slogans, inflated adjectives, vague
"strategic" language, and AI-style transitions.

## When Not To Use

- Use `gtm-master` for the Chinese-first consumer hardware suite.
- Use a specific sub-skill when the user wants only pricing, KOL scoring,
  creative scoring, or launch forecasting inside the existing GTM suite.
- Do not use this skill to replace legal, finance, regulatory, or final
  executive approval.
