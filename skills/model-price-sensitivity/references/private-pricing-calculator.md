# Private Pricing Calculator

Use this when COGS, margin, channel policy, retailer terms, promo budget, elasticity assumptions, demand scenarios, or internal sales data are confidential and should not enter the LLM context.

## Privacy Modes

Default to `client_side_blank_inputs`.

```text
client_side_blank_inputs
  Generate formulas, labels, validation rules, and empty HTML input fields only. The user enters private values inside the final HTML file after generation. Calculations run in the browser and are not included in the model context, report handoff, evidence ledger, or citations.

encrypted_local_snapshot
  Allow the browser to export/import an encrypted JSON snapshot with Web Crypto and a user passphrase. This protects saved local state at rest or during transfer. The encrypted blob is not useful to the AI unless the user decrypts it and intentionally shares derived values.

derived_summary_only
  Let the user share non-sensitive outputs, such as "target price passes 35% GM after channel fee" or "floor net price is in the upper mainstream band", without exposing raw COGS or terms.

explicit_private_upload
  Use only when the user explicitly chooses to share private values with the model. Record this in `private_pricing_input_register`, keep it out of public HTML by default, and mark downstream fields as private.
```

## HTML Security Requirements

The private calculator must be safe by design:

```text
network
  No fetch, beacon, analytics, telemetry, remote fonts, CDN scripts, or external images inside the private calculator.

storage
  Keep values in browser memory by default. Do not use localStorage, sessionStorage, cookies, or URL query params for private inputs unless the user explicitly enables encrypted snapshot export.

rendering
  Do not prefill COGS, margin, channel, or internal sales values. Render empty inputs, formulas, and local-only calculation labels.

handoff
  Do not pass raw private values to S07/S08/S13/S14. Pass only formula specs, blank-field schemas, data-gap flags, or user-approved derived summaries such as "profit-max price is above current transaction price."

public_html
  Never render raw private COGS, margin, channel terms, or internal sales data in public-facing sections unless explicitly approved.
```

## Calculator Inputs

```json
{
  "private_input_fields": [
    {
      "field_id": "cogs_or_bom",
      "label": "COGS / BOM per unit",
      "type": "currency",
      "required_for": ["gross_margin", "floor_price"],
      "privacy_level": "private_local_only"
    },
    {
      "field_id": "target_gross_margin",
      "label": "Target gross margin",
      "type": "percent",
      "required_for": ["minimum_net_selling_price"],
      "privacy_level": "private_local_only"
    },
    {
      "field_id": "msrp",
      "label": "MSRP / list price",
      "type": "currency",
      "required_for": ["estimated_net_selling_price"],
      "privacy_level": "private_local_only"
    },
    {
      "field_id": "channel_margin_or_fee",
      "label": "Retailer/channel margin or marketplace fee",
      "type": "currency_or_percent",
      "required_for": ["estimated_net_selling_price"],
      "privacy_level": "private_local_only"
    },
    {
      "field_id": "expected_discount_or_coupon",
      "label": "Expected discount/coupon",
      "type": "currency_or_percent",
      "required_for": ["promo_margin_after_discount"],
      "privacy_level": "private_local_only"
    },
    {
      "field_id": "shipping_financing_or_payment_subsidy",
      "label": "Shipping, financing, or payment subsidy",
      "type": "currency_or_percent",
      "required_for": ["estimated_net_selling_price"],
      "privacy_level": "private_local_only"
    },
    {
      "field_id": "tax_or_vat_treatment",
      "label": "Tax/VAT treatment",
      "type": "currency_or_percent_or_note",
      "required_for": ["estimated_net_selling_price"],
      "privacy_level": "private_local_only"
    },
    {
      "field_id": "base_demand_units",
      "label": "Base demand units",
      "type": "number",
      "required_for": ["estimated_units", "revenue", "contribution_profit"],
      "privacy_level": "private_local_only"
    },
    {
      "field_id": "reference_price",
      "label": "Reference price",
      "type": "currency",
      "required_for": ["price_index", "estimated_units"],
      "privacy_level": "private_local_only"
    },
    {
      "field_id": "own_price_elasticity",
      "label": "Own price elasticity",
      "type": "number",
      "required_for": ["estimated_units", "revenue_max_price", "profit_max_price"],
      "privacy_level": "private_local_only"
    },
    {
      "field_id": "mkt_spend",
      "label": "MKT spend",
      "type": "currency",
      "required_for": ["contribution_profit"],
      "privacy_level": "private_local_only"
    },
    {
      "field_id": "mkt_response_multiplier",
      "label": "MKT response multiplier",
      "type": "number",
      "required_for": ["estimated_units"],
      "privacy_level": "private_local_only"
    },
    {
      "field_id": "channel_availability_multiplier",
      "label": "Channel availability multiplier",
      "type": "number",
      "required_for": ["estimated_units"],
      "privacy_level": "private_local_only"
    },
    {
      "field_id": "proof_maturity_multiplier",
      "label": "Proof maturity multiplier",
      "type": "number",
      "required_for": ["estimated_units"],
      "privacy_level": "private_local_only"
    },
    {
      "field_id": "variable_support_warranty_return_cost",
      "label": "Variable support, warranty, and return cost",
      "type": "currency",
      "required_for": ["unit_contribution", "contribution_profit"],
      "privacy_level": "private_local_only"
    }
  ]
}
```

## Local Formulas

Use deterministic browser-side calculations:

```text
estimated_net_selling_price =
  msrp
  - channel_margin_or_fee
  - expected_discount_or_coupon
  - shipping_financing_or_payment_subsidy
  - tax_or_vat_amount_when_accounted_from_price

gross_margin =
  (estimated_net_selling_price - cogs_or_bom) / estimated_net_selling_price

minimum_net_selling_price =
  cogs_or_bom / (1 - target_gross_margin)

margin_gap =
  estimated_net_selling_price - minimum_net_selling_price

promo_margin_after_discount =
  (estimated_net_selling_price_after_discount - cogs_or_bom) / estimated_net_selling_price_after_discount

price_index =
  estimated_net_selling_price / reference_price

estimated_units =
  base_demand_units
  * POWER(price_index, own_price_elasticity)
  * mkt_response_multiplier
  * channel_availability_multiplier
  * proof_maturity_multiplier

revenue =
  estimated_net_selling_price * estimated_units

unit_contribution =
  estimated_net_selling_price - cogs_or_bom - variable_support_warranty_return_cost

contribution_profit =
  unit_contribution * estimated_units - mkt_spend

revenue_max_price =
  candidate price with highest revenue across the local candidate price grid

profit_max_price =
  candidate price with highest contribution_profit across the local candidate price grid
```

When a field can be either percent or absolute currency, make the HTML control explicit and show the applied interpretation.

## Output Schema

```json
{
  "private_pricing_calculator_spec": {
    "mode": "client_side_blank_inputs | encrypted_local_snapshot | derived_summary_only | explicit_private_upload",
    "html_component_id": "private_pricing_calculator",
    "network_policy": "no_external_requests",
    "storage_policy": "memory_only_by_default",
    "private_input_fields": [],
    "computed_fields": [
      "estimated_net_selling_price",
      "gross_margin",
      "minimum_net_selling_price",
      "margin_gap",
      "promo_margin_after_discount",
      "estimated_units",
      "revenue",
      "unit_contribution",
      "contribution_profit",
      "revenue_max_price",
      "profit_max_price"
    ],
    "formula_notes": [],
    "public_rendering_policy": "do_not_render_raw_private_values",
    "downstream_handoff_policy": "formula_spec_and_user_approved_derived_summary_only",
    "security_warnings": [],
    "confidence_effect": "removes_private_data_gap_only_after_user_runs_local_calculation_or_shares_derived_summary"
  }
}
```

## Profit Revenue Optimizer Component

When S04 needs revenue-max or profit-max price, render a separate local component or a tab inside the private calculator.

```json
{
  "component_id": "private_profit_revenue_optimizer",
  "title": "Private Profit And Revenue Optimizer",
  "privacy_notice": "Demand, elasticity, COGS, channel, and MKT inputs stay local in the browser unless you choose to share a derived summary.",
  "candidate_price_grid": {
    "default_points": 31,
    "editable_min_max": true
  },
  "computed_outputs": [
    "revenue_curve",
    "profit_curve",
    "revenue_max_price",
    "profit_max_price",
    "promo_floor_warning",
    "channel_floor_warning"
  ],
  "forbidden_behaviors": [
    "external_network_requests",
    "remote_scripts_or_fonts",
    "analytics_or_telemetry",
    "prefilled_private_values",
    "plain_local_storage"
  ]
}
```

## Important Boundary

Encryption is useful for storing or transferring a private local snapshot. It does not let the model reason over hidden data. If the AI must reason about private financial constraints, the user must either share explicit values, share a derived summary, or run a local/offline analysis path.
