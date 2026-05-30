# S07 Evidence Usage Policy

Use this before collecting, storing, citing, or rendering funnel evidence.

## Evidence Classes

```text
public_page_or_PDP
  Public landing pages, PDPs, retailer pages, help pages, policy pages, and public checkout notes.

competitor_or_category_benchmark
  Public competitor pages, marketplace PDPs, local retailer PDPs, review pages, policy pages, and category norm observations. Treat as benchmark evidence, not proof of best practice.

previous_generation_evidence
  Previous product pages, PDPs, launch campaigns, channel results, analytics summaries, reviews, and support feedback. Treat private values as restricted unless approved.

uploaded_private_funnel
  Page drafts, wireframes, checkout flows, offer details, analytics exports, and internal results. Treat as restricted.

performance_data
  Analytics, A/B test, ad, clickout, heatmap, session, CRM, or conversion data. Treat raw rows as private unless approved.

upstream_handoff_evidence
  Prefer evidence IDs from S01-S06 handoffs. Do not reopen full artifacts unless needed.
```

## Public Search Policy

Use web/MCP only when:

```text
landing/PDP URL is supplied
public retailer/PDP trust or checkout context matters
competitor landing/PDP patterns are needed
previous-generation public pages or archived page references are supplied
public policy pages support return, warranty, shipping, or payment checks
```

Respect access limits. Do not bypass paywalls, logins, robots, consent walls, or private analytics systems.

## Metric Caution

Treat these as measured only when directly supplied with context:

```text
sessions
CTR
CVR
add-to-cart rate
checkout start rate
purchase rate
lead rate
CPA
ROAS
revenue
refund/return rate
```

Public benchmarks and AI estimates are proxies. Label them as such and record confounders.

Competitor page patterns can justify requirements or hypotheses, but they cannot justify measured CVR, revenue, sales lift, or demand claims.

## HTML Safety

Public HTML may render:

```text
derived friction scores
confidence labels
experiment plans
aggregated performance summaries
tracking gaps
source refs
```

Public HTML should not render:

```text
raw analytics rows
private URLs or unpublished drafts
customer PII
unapproved revenue, margin, CPA, or ROAS data
session recordings or heatmap raw exports
private checkout/vendor details
```
