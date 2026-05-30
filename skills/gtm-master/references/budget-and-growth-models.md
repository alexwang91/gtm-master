# Budget And Growth Models

This reference adapts the marketing-plan budget formulas and growth-pattern
thinking for B2C hardware GTM. Use it mainly in S08 forecasts and S13 validation.

## Revenue-Based

Use Revenue-Based budgeting when the company has a realistic current revenue,
sell-through, or historical launch baseline.

```text
Annual GTM budget = target revenue base * selected GTM allocation percentage
```

hardware adaptation:

- Replace ARR with expected gross revenue, net revenue, or sell-through value.
- Include media, creator seeding, retail demo, channel fees, content, tooling,
  agency, and launch labor in the budget.
- Treat the percentage as a posture: conservative, standard growth, or aggressive
  launch investment.

## Goal-Based

Use Goal-Based budgeting when the unit or revenue goal is fixed and the question
is what investment makes the target plausible.

```text
Required budget = target incremental units * blended CAC
```

For revenue goals:

```text
Required units = target incremental gross revenue / expected AOV
Required budget = required units * blended CAC
```

For products with returns:

```text
Net required units = required units / (1 - expected return rate)
```

## blended CAC

For hardware, blended CAC must include more than ad spend:

- paid media
- creator fees and seeding cost
- sample logistics
- retail display or demo cost
- marketplace fees tied to acquisition
- agency and content production
- launch tooling and tracking
- channel co-op marketing

Never present platform CPA as full CAC unless every excluded cost is listed as a
gap.

## S-curve

Hardware growth rarely follows a smooth line. Model it as layered S-curve
constraints:

- product lifecycle adoption
- retailer onboarding and stock availability
- marketplace ranking and review accumulation
- paid-media learning
- creator/media burst decay
- seasonality and promo calendar
- supply/replenishment constraints

S08 should show base/upside/downside curves and the sensitivity driver tornado.
S13 should convert the highest-uncertainty curve assumptions into validation
tests with pass/fail rules.

## Guardrails

- The model is directional unless calibrated by previous-generation or measured
  current-channel data.
- Separate sell-in, sell-through, DTC orders, waitlist, and retailer commitment.
- Do not convert views, likes, or creator reach directly into sales without an
  explicit bridge and confidence cap.
- Record whether private COGS, channel terms, or inventory inputs are excluded,
  aggregated, or approved for local-only calculation.
