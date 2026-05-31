# Price Intelligence

Capability slot: `price_intelligence`

Required capabilities: `price_monitoring`, `competitor_discovery`.

Use this to build `local_price_corridor`, competitor price anchors, promo floor,
discount norms, bundle/subscription price context, financing availability, and
channel price differences.

## Inputs

```yaml
required:
  - product_category
  - launch_country_or_region
  - target_price_range
  - competitor_candidates
optional:
  - known_competitors
  - planned_channels
```

## Outputs

```yaml
outputs:
  - local_price_corridor
  - price_anchor_panel
  - competitor_price_gap_table
  - promo_floor_estimate
  - subscription_or_bundle_price_context
  - price_evidence_records
```

## Rules

- Capture list price, sale price, currency, tax/shipping notes, channel, date, and source URL.
- Separate MSRP, transaction price, promo price, used/refurbished price, and subscription cost.
- Treat stale or cross-border prices as weak proxies unless justified.
- Do not infer margin, COGS, or profit from public price evidence.
