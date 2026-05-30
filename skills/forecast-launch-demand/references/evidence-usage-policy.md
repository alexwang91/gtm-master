# S08 Evidence Usage Policy

Use this before collecting, storing, citing, or rendering forecast evidence.

## Evidence Classes

```text
public_market_proxy
  Market size, competitor channel visibility, public price, retailer ranking, public availability, and comparable category signals.

upstream_model_output
  S01 market sizing, S04 pricing, S06 creator traffic, and S07 conversion scenarios. Treat as modeled inputs, not measured demand.

private_internal_sales
  Previous-generation sales, sell-through, channel performance, POs, preorder counts, waitlist counts, inventory, and supply plans.

user_hypothesis
  User-provided target, planned channel mix, media reach, or expected units without evidence.

marketing_response_evidence
  Historical spend, reach, traffic, conversion, retail media, creator, promo, or MMM-like response data. Treat raw values as private unless approved.
```

## Public HTML Safety

Public HTML may render:

```text
scenario ranges
confidence labels
assumption categories
aggregated channel shares
inventory risk labels
validation needs
baseline vs marketing incremental sales ranges
```

Public HTML should not render unless approved:

```text
raw PO numbers
raw inventory allocation
raw channel sell-through values
raw revenue targets
raw marketing spend or response data
private retailer terms
COGS, margin, profit, or contribution data
private customer/order rows
```

## Metric Caution

Treat these as measured only when directly supplied with context:

```text
unit sales
sell-in
sell-through
preorder count
waitlist count
retail PO
inventory allocation
sessions
CVR
revenue
return/cancellation rate
```

Modeled market size, public benchmarks, creator estimates, and AI judgments are proxies. Label them as such and record confounders.
