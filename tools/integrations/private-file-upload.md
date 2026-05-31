# Private File Upload

Capability slot: `private_file_upload`

Required capabilities: `manual_upload`, spreadsheet parsing, PDF/document
parsing, and scoped private data extraction.

Use this for product specs, previous-generation sales, channel plans, internal
benchmarks, NSS/NPS exports, support summaries, return reasons, campaign results,
creator rate cards, or confidential pricing constraints.

## Inputs

```yaml
accepted_material:
  - product_specification_files
  - previous_generation_sales_price_channel_performance
  - customer_reviews_and_nss_or_nps
  - internal_benchmarks
  - channel_plan
  - historical_ads_kol_landing_pages_and_creatives
  - creator_rate_cards_or_media_kits
```

## Outputs

```yaml
outputs:
  - extracted_private_evidence_refs
  - derived_summary
  - excluded_private_fields
  - public_html_policy
  - data_gap_updates
```

## Rules

- Private data is restricted by default.
- Prefer derived summaries for handoff and public HTML.
- Keep raw private fields out of prompts and public dashboards unless approved.
- Use local-only calculators for COGS, margin, channel terms, and profit/revenue optimization when confidentiality matters.
