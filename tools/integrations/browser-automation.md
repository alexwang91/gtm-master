# Browser Automation

Capability slot: `browser_automation`

Required capability: `browser_automation`.

Use only when a public source requires JavaScript rendering, filters, dropdowns,
pagination, screenshots, consent banners, or visual verification. Search and
web extraction should be tried first when enough.

## Best Uses

```text
JavaScript-rendered retailer pages
paginated comments or reviews
filterable marketplace results
price or availability states hidden behind UI controls
visual source verification
```

## Outputs

```yaml
outputs:
  - visited_url_log
  - pagination_or_filter_log
  - extracted_records
  - screenshot_refs_when_needed
  - blocked_or_failed_source_log
```

## Rules

- Do not bypass paywalls, login walls, anti-bot controls, or source terms.
- Use bounded pagination and record page ranges.
- If pagination count is unknown, define a stop condition before collection.
- Never treat browser automation output as complete without a coverage report.
