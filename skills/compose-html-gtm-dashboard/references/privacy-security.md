# Privacy And Security

Use this before rendering private or user-provided data into HTML.

## Default Policy

```text
offline_static_by_default
  The dashboard should work as a local HTML file without network access.

public_safe_by_default
  Do not render raw private values unless the user explicitly approves public/private inclusion.

local_only_tools
  Private calculators run in browser memory only unless encrypted export is explicitly enabled.
```

## Forbidden In Default HTML

```text
remote_scripts
remote_fonts
analytics
telemetry
fetch_or_beacon_calls
unapproved_external_images
plain_local_storage_for_private_values
query_string_private_values
raw_private_cogs_margin_channel_sales_values
```

## Sanitization

Escape or sanitize:

```text
section titles
narrative blocks
table cells
metric labels and values
citations
data gaps
decision log text
uploaded filenames
```

If upstream provides raw HTML, treat it as untrusted unless it comes from an approved local template or renderer path.

## Private Pricing Calculator

When rendering `private_pricing_calculator_spec`:

```text
inputs
  Render blank inputs only.

calculation
  Calculate gross margin, minimum net selling price, margin gap, and promo margin locally in browser memory.

sharing
  Allow copy of derived summary only if user clicks the control.

storage
  Do not store raw values by default.
```

## Evidence And Citations

- Do not create citation URLs or titles.
- Keep private/internal refs clearly marked as private or internal.
- Do not expose local file paths in public share mode unless the user approves.
