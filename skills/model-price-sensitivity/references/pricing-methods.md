# Pricing Methods

Use this when building S04 core pricing outputs.

## Pricing Logic

S04 combines four lenses:

```text
market anchors
  What does the local market make the price feel like?

opening strategy
  Should the product open high, open at parity, attack with price, or preserve a niche high-price position?

consumer value
  What segments/scenarios can believe and pay for the value?

commercial constraints
  Can the business/channel sustain public anchor price, transaction price, promo floor, and channel floor?

validation design
  What must be tested before a confident pricing decision?
```

## COGS And Margin Basics

COGS means cost of goods sold: the direct per-unit cost of making or acquiring the product sold. For hardware, treat BOM/component cost, assembly/manufacturing, packaging, and relevant inbound logistics/duties as likely COGS inputs, subject to the user's finance/accounting policy.

Keep these concepts separate:

```text
BOM
  Bill of materials: component/material cost. It is often a major part of COGS but not always the whole COGS.

COGS
  Direct sold-product cost used for gross margin. Usually excludes marketing, R&D, sales commissions, and general overhead.

MSRP/list price/public anchor price
  Public-facing recommended retail price.

Transaction price
  The realistic price paid after discount, bundle, trade-in, financing, channel subsidy, member price, or limited-time offer.

Net selling price
  Money retained after retailer/marketplace margin, channel fees, discounts, coupons, offer costs, shipping subsidies, payment/financing fees, or VAT/tax treatment depending on the accounting view.

Floor price
  Lowest acceptable net price after required margin and channel constraints.

Revenue-max price
  Price that produces the highest modeled revenue under demand assumptions.

Profit-max price
  Price that produces the highest modeled contribution profit under private unit economics and demand assumptions.
```

Use simple formulas when private inputs are available:

```text
Gross Margin = (Net Selling Price - COGS) / Net Selling Price

Minimum Net Selling Price = COGS / (1 - Target Gross Margin)

Estimated Net Selling Price =
  MSRP
  - retailer_or_channel_margin
  - marketplace_or_payment_fees
  - expected_discounts_or_coupons
  - shipping_or_financing_subsidy
  - taxes_or_duties_when_accounted_from_price
```

Do not decide whether a price is commercially viable from market evidence alone. A price can look attractive to consumers and still fail if channel margins, promo budget, return rates, warranty exposure, or COGS make the net margin unacceptable.

Do not collapse public anchor price, transaction price, promo floor, channel floor, revenue-max price, and profit-max price into one recommendation. They answer different management questions.

## Local Price Credibility

Classify target price against:

- Entry, mainstream, premium, flagship, previous-generation/refurbished, and substitute bands
- Direct competitor anchors
- Premium and budget anchors
- Local tax/VAT, shipping, financing, subscription, warranty, and promo display norms

Do not treat a target price as credible just because it sits inside a price band. It also needs proof, channel fit, segment WTP, and risk control.

## Segment WTP Hypothesis

Segment WTP is a hypothesis unless direct WTP research or reliable internal sales data exists.

Create a segment WTP record by combining:

```text
S01 segment_price_sensitivity_seed
S01 value_proof_requirement_matrix
S02 scenario_price_implication_seed
S03 price_message_seed
S03 objection_matrix
S03 claim_risk_and_proof_gate
```

WTP hypotheses should identify:

- Acceptable price corridor hypothesis
- Premium tolerance hypothesis
- Proof needed to sustain price
- Objections that must be resolved
- Recommended test method

## WTP Direct Conclusion Rule

After building local price credibility, rapid WTP prior, and segment WTP
hypotheses, S04 must produce `wtp_direct_conclusion`. The conclusion should be
commercially readable in one pass:

```text
Can we defend the target price?
For which segments?
Which segments will resist and how will they behave?
What proof, bundle, financing, trade-in, or promo mechanism is required?
What metric or validation test would change the decision?
```

If direct WTP research is missing, use the rapid prior and segment evidence to
make a confidence-capped recommendation. Do not output a precise WTP range when
only public proxies exist, and do not use AI personas as WTP evidence.

## Price-Value Proof Matrix

```json
{
  "price_value_proof_matrix": [
    {
      "segment_id": "",
      "scenario_refs": [],
      "price_position": "below_anchor | parity | slight_premium | major_premium | unclear",
      "value_argument": "",
      "proof_required": [],
      "proof_status": "available | partial | missing | risky",
      "message_refs": [],
      "claim_risk": "high | medium | low",
      "confidence": "high | medium | low",
      "evidence_refs": []
    }
  ]
}
```

## Promo And Subscription Guidance

```json
{
  "promo_subscription_guidance": {
    "promotion_dependence": "low | medium | high | unknown",
    "recommended_launch_offer_hypotheses": [],
    "discount_risk": "",
    "bundle_or_freebie_hypotheses": [],
    "financing_or_installment_guidance": "",
    "subscription_or_recurring_cost_guidance": "",
    "risk_reversal_guidance": "",
    "confidence": "high | medium | low",
    "evidence_refs": [],
    "data_gaps": []
  }
}
```

## Pricing Decision Options

Produce only when internal constraints and enough market evidence exist.

```json
{
  "pricing_decision_options": [
    {
      "option_id": "",
      "option_type": "value_entry | parity | slight_premium | premium | flagship | promo_led | subscription_led | test_only",
      "price_or_band": "",
      "why_it_could_work": "",
      "proof_required": [],
      "main_risks": [],
      "conditions_required": [],
      "recommended_next_step": "approve_for_test | research_first | finance_review | channel_review | avoid",
      "confidence": "high | medium | low",
      "evidence_refs": []
    }
  ]
}
```

## Pricing Handoff Summary

```json
{
  "pricing_handoff_summary": {
    "recommended_pricing_posture": "value | parity | slight_premium | premium_with_proof | test_before_decision | blocked",
    "most_supported_price_band": "",
    "highest_risk_price_band": "",
    "segments_with_high_sensitivity": [],
    "segments_with_premium_potential": [],
    "proof_blockers": [],
    "test_required": true,
    "private_constraints_needed": [],
    "handoff_to_s07": [],
    "handoff_to_s08": [],
    "handoff_to_s13": []
  }
}
```
