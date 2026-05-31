# S13 Hidden Validation Plan

Run id: `huawei-watch-fit-5-pro-hu-2026-05-31`
Mode: `real_product_pilot`
Product: HUAWEI WATCH FIT 5 Pro
Country: Hungary
Dashboard policy: hidden by default; S14 may use status, data gaps, and top validation actions, but should not render this as a full business section unless explicitly requested.

## Role

S13 does not rerun S01-S08 and does not create new market conclusions. It converts current weak assumptions into the smallest practical validation portfolio.

Priority formula:

`Experiment Priority = impact_on_decision 30% + uncertainty_level 20% + decision_urgency 15% + test_feasibility 15% + cost_efficiency 10% + risk_reduction 10%`

Score interpretation:

- `80-100`: run before decision
- `60-79`: run if budget or timing allows
- `40-59`: monitor as hypothesis
- `<40`: defer

## Validation Input Coverage Gate

| Field | Status | Notes |
|---|---|---|
| Source skills available | ready | S01, S02, S03, S04, S08 handoff artifacts exist. |
| Data gap log | ready | Pilot state and each module list gaps. |
| Confidence caps | ready | FIT 5 Pro NSS/NPS is blocked; S08 is directional only; price is controlled-test-ready. |
| Decision deadlines | missing | No launch date or internal decision calendar provided. |
| Budget / effort context | partial | S08 has budget posture ranges, but no approved MKT or validation budget. |
| Testing channels | partial | Publicly visible channels exist, but test access is unknown. |
| Private data policy | exclude_raw | Do not expose COGS, margin, sell-through, support, inventory, or channel terms. |

Selected scenario mix:

- `B_prelaunch_validation_roadmap`
- `C_price_message_validation`
- `D_channel_conversion_forecast_validation`
- `F_private_internal_validation`

Gate status: `ready_with_gaps`

## Assumption Inventory

| ID | Decision area | Assumption | Current basis | Confidence | Risk |
|---|---|---|---|---|---:|
| A13-01 | pricing/message | `99,990 Ft` can hold if value proof and transaction mechanism are strong. | S04 public proxy model | low_medium | 88 |
| A13-02 | message | Multi-day battery can be the lead competitive wedge versus Watch7. | S01/S02/S03 public source + expert review seed | medium | 82 |
| A13-03 | proof/claim | Hungarian payment support can reduce conversion anxiety if proven clearly. | Mobilarena comment seed + S03 claim gate | low | 86 |
| A13-04 | channel | Alza, MediaMarkt, Euronics, Yettel, Huawei official can cover launch demand. | S01/S08 public channel visibility | medium_low | 78 |
| A13-05 | forecast | S08 relative demand scenarios are directionally useful. | S08 assumption tree | hypothesis_only | 84 |
| A13-06 | competition | Watch7 low-price pressure is the main external conversion risk. | S01/S02/S04 public price and voice seed | medium | 80 |
| A13-07 | internal ladder | FIT 4 Pro and GT 6 can cannibalize or confuse FIT 5 Pro. | S01/S04 public price ladder | medium | 76 |
| A13-08 | proof | Sport/health claims are credible only with bounded, non-medical proof. | S02/S03 proof matrix | low_medium | 72 |
| A13-09 | voice evidence | Public local buyer voice is too thin for FIT 5 Pro NSS/NPS. | S01 coverage report | high | 65 |
| A13-10 | private economics | Promo depth and transaction price need finance/channel guardrails. | Missing private data | hypothesis_only | 90 |

## Validation Question Backlog

| ID | Question | Unlocks | Priority |
|---|---|---|---:|
| VQ13-01 | Can Hungarian shoppers believe `99,990 Ft` after seeing the value stack and bundle? | price posture, message, channel PDP | 92 |
| VQ13-02 | Does payment proof remove a high-severity purchase anxiety, especially around OTP/Curve/bank support? | claim gate, PDP FAQ, retail script | 89 |
| VQ13-03 | Which proof route wins: battery, fashion/material, price-value, payment, or sport? | message investment split, S14 top story | 86 |
| VQ13-04 | How often do shoppers choose FIT 5 Pro over Watch7 / FIT 4 Pro / GT 6 when the choice is framed honestly? | competitor response, price defense | 85 |
| VQ13-05 | Are named Hungarian channels ready enough to carry the product without price/claim confusion? | channel priority, S08 forecast confidence | 82 |
| VQ13-06 | What previous-generation sales/channel pattern should calibrate the S08 demand index? | forecast, inventory, budget | 80 |
| VQ13-07 | Can landing/PDP traffic convert with proof blocks before a stronger promotion is needed? | conversion, budget, S04 price path | 77 |
| VQ13-08 | Are sport/health claims safe and believable without overpromising? | claim gate, PR, creators, retail scripts | 72 |
| VQ13-09 | Can bounded voice extraction strengthen Watch7 and FIT 4 Pro driver maps enough for a directional proxy? | VOC/NSS/Bain seeds | 68 |

## Experiment Priority Scorecard

| Experiment | Impact | Uncertainty | Urgency | Feasibility | Cost efficiency | Risk reduction | Priority |
|---|---:|---:|---:|---:|---:|---:|---:|
| E13-01 Price/value message smoke test | 95 | 86 | 90 | 78 | 82 | 88 | 88 |
| E13-02 Payment proof validation | 90 | 90 | 88 | 72 | 80 | 91 | 86 |
| E13-03 Competitive choice test | 88 | 82 | 84 | 75 | 76 | 86 | 82 |
| E13-04 Channel/PDP readiness audit | 85 | 75 | 86 | 90 | 88 | 78 | 83 |
| E13-05 Private finance/channel guardrail run | 96 | 95 | 88 | 55 | 92 | 95 | 85 |
| E13-06 Previous-generation sales calibration | 90 | 92 | 78 | 58 | 84 | 86 | 81 |
| E13-07 Landing/PDP behavioral A/B | 84 | 82 | 72 | 62 | 66 | 78 | 75 |
| E13-08 Bounded voice extraction expansion | 70 | 62 | 60 | 78 | 72 | 64 | 68 |
| E13-09 Sport/health proof review | 74 | 68 | 62 | 82 | 76 | 70 | 72 |

## Validation Experiment Roadmap

### Phase 0: 1-2 Days, No Market Spend

| ID | Method | Decision unlocked | Requirement | Pass rule | Fail rule |
|---|---|---|---|---|---|
| E13-04 | Channel/PDP readiness audit | Can S14 name channel priorities and proof gaps? | Review Huawei official, Alza, MediaMarkt, Euronics, Yettel, Arukereso pages for price, bundle, payment, warranty, product proof, review status. | At least 4 named channels show consistent price/offer and no severe claim contradiction. | Price/offer/claim mismatch appears in key channels or critical channels are missing. |
| E13-05 | Private finance/channel guardrail run | Can promo or bundle be recommended? | COGS, margin target, channel fee, promo subsidy, bundle cost entered locally or summarized as derived thresholds. | Finance confirms `97,840-99,990 Ft` transaction range clears floor. | Finance floor blocks bundle or light promo. |
| E13-09 | Sport/health proof review | Which claims need compliance caution? | Approved specs, official test conditions, third-party review excerpts, legal/claim constraints. | Health/sport claims can be used with conditions and no medical wording. | Claims require removal or human/legal review before publication. |

### Phase 1: 3-7 Days, Small Research / Content Test

| ID | Method | Decision unlocked | Requirement | Pass rule | Fail rule |
|---|---|---|---|---|---|
| E13-01 | Price/value message smoke test | Whether `99,990 Ft` is supportable in messaging. | 3-5 Hungarian stimulus cards: battery-led, fashion/material-led, price-value bundle, payment proof, sport proof. | Top 2 routes show materially higher comprehension and purchase intent; price objection falls after proof. | Price objection remains dominant across all routes. |
| E13-02 | Payment proof validation | Whether payment can become proof, FAQ, or must stay caveat. | Local bank/wallet support list, setup flow, test device, retail terminal checks if possible. | Payment path works for named supported route and support article can explain it clearly. | Support is partial/confusing; payment must stay as caveat, not lead message. |
| E13-03 | Competitive choice test | Which competitor steals the most demand. | Controlled comparison: FIT 5 Pro vs Watch7 vs FIT 4 Pro vs GT 6, with price, key features, channel/bundle. | FIT 5 Pro wins among at least one priority segment for battery/fashion/health route. | Watch7/FIT 4 Pro/GT 6 dominate even after proof; price/offer must change. |

### Phase 2: 1-3 Weeks, Behavioral / Channel Evidence

| ID | Method | Decision unlocked | Requirement | Pass rule | Fail rule |
|---|---|---|---|---|---|
| E13-07 | Landing/PDP behavioral A/B | Whether proof blocks improve action, not just stated intent. | Controlled traffic, event tracking, stable price/offer, variants for battery/value/payment. | Proof variant improves qualified clickout, add-to-cart, FAQ completion, or retailer click relative to control. | CTR rises but downstream action does not; message attracts curiosity but not conversion. |
| E13-06 | Previous-generation sales calibration | Can S08 produce unit ranges? | FIT 4 Pro weekly sales, channel split, ASP/promo, inventory and returns as aggregate or local-only input. | S08 base index can map to units with a documented confidence cap. | Data unavailable or not comparable; S08 remains index-only. |
| E13-08 | Bounded voice extraction expansion | Whether Watch7/FIT 4 Pro driver maps are strong enough for directional proxy. | Fixed source windows and dedupe rules from S01. | Source-item counts and coverage reports support directional Watch7/FIT 4 Pro driver comparison. | Source access or sample quality insufficient; keep only qualitative themes. |

## Survey Test Plan

Use only if the team can access screened Hungarian respondents.

Recommended screener:

- Lives in Hungary.
- Owns or plans to buy a smartwatch/fitness watch in the next 6 months.
- Uses Android or iOS smartphone; separate Samsung phone users.
- Has compared at least one of Huawei, Samsung, Garmin, Amazfit, Apple, Xiaomi, or Fitbit.
- Price comfort around `70,000-120,000 Ft` category range.

Minimum practical sample:

- `n=60-100` for directional message/price learning.
- `n=150+` if segment splits are needed.
- Survey alone cannot validate sell-through, inventory, or ROAS above medium confidence.

Question blocks:

- Concept comprehension.
- Price-value reaction at `89,990 / 94,990 / 99,990 / 104,990 Ft`.
- MaxDiff: battery, sleep, design/material, payment, sport, bundle, warranty.
- Competitive choice: FIT 5 Pro vs Watch7 vs FIT 4 Pro vs GT 6.
- Objection ranking: price, payment, ecosystem, accuracy, channel trust, charging/strap.

## Pricing / Message / Copy Test Plan

| Test | Variants | Primary metric | Secondary metric | Decision |
|---|---|---|---|---|
| Price-value cards | battery-led, material-led, bundle-led, payment-led, sport-led | purchase intent after proof | price objection reduction | Select S14/S03 lead story and S04 proof route. |
| Gabor-Granger lite | `89,990 / 94,990 / 99,990 / 104,990 Ft` | stated purchase likelihood | reason for no | Calibrate whether `99,990 Ft` needs bundle or lower transaction price. |
| MaxDiff value drivers | battery, sleep, material, payment, sport, warranty, gift | relative importance | segment differences | Decide message investment split. |
| PDP proof order | battery first vs material first vs value stack first | qualified clickout/add-to-cart | FAQ/payment clicks | Decide landing/PDP layout. |

## Channel / Conversion / Forecast Test Plan

| Test | Data source | Primary metric | Unlocks |
|---|---|---|---|
| Channel/PDP audit | Huawei, Alza, MediaMarkt, Euronics, Yettel, Arukereso | consistency score, proof completeness, price/offer clarity | channel priority and S14 channel module |
| Retailer clickout tracking | Brand site or campaign page | retailer clickout by channel | channel split confidence |
| Yettel/operator feasibility | Yettel current page + Telekom/One partner status | confirmed availability, bundle/financing terms | operator channel share assumption |
| Previous-generation calibration | FIT 4 Pro aggregate sales/channel data | weekly sell-through, ASP, channel mix | S08 unit forecast |
| Post-launch review/readiness loop | retailer reviews, Arukereso, Mobilarena, support tags | new buyer voice count and detractor themes | NSS/Bain proxy readiness |

## Experiment Design Cards

### E13-01 Price/Value Message Smoke Test

- Hypothesis: `99,990 Ft` becomes acceptable for priority users when the value stack is shown as battery + light design/material + sleep/health + bundle/warranty.
- Method: screened survey or lightweight landing-page concept test.
- Population: Hungarian smartwatch intenders, split by Samsung phone users and non-Samsung users.
- Materials: 4-5 stimulus cards in Hungarian, all using the same price and product image/claim strength.
- Controlled variables: same price, same brand, same channel context, same warranty/bundle visibility unless deliberately tested.
- Primary metric: purchase intent or qualified action after proof exposure.
- Pass: at least two message routes reduce price objection and outperform generic feature listing.
- Fail: price objection remains top blocker and no route beats control.
- Failure action: increase bundle/financing proof, revise transaction mechanism, or re-test lower transaction price.

### E13-02 Payment Proof Validation

- Hypothesis: payment anxiety can be reduced if the exact supported bank/wallet path is visible and testable.
- Method: internal setup test + local support article review + optional user comprehension check.
- Population/data: test device, Hungarian account/payment route if available, supported terminal checks where legal/operationally possible.
- Primary metric: successful setup and payment path clarity.
- Pass: supported route can be documented with screenshots and troubleshooting.
- Fail: route is partial, bank-dependent, or too confusing.
- Failure action: keep payment as FAQ/caveat, do not use it as lead claim.

### E13-03 Competitive Choice Test

- Hypothesis: FIT 5 Pro can win a priority segment against Watch7/FIT 4 Pro/GT 6 when comparison is structured around battery, weight/design, health/sleep, and channel offer.
- Method: survey choice task or moderated qualitative comparison.
- Population: Hungary smartwatch intenders.
- Materials: normalized comparison table, same price visibility, honest tradeoffs.
- Primary metric: first choice by segment and reason.
- Pass: FIT 5 Pro wins at least one priority segment and has clear reasons.
- Fail: Watch7 or cheaper Huawei alternatives dominate all priority scenarios.
- Failure action: revise segment targeting, offer, or price proof.

### E13-04 Channel/PDP Readiness Audit

- Hypothesis: named local channels can carry a consistent launch story.
- Method: structured desk audit, no broad market refresh.
- Data: product pages and channel pages already named by S01/S08.
- Primary metric: channel readiness score by price clarity, proof completeness, offer clarity, review status, compatibility/payment FAQ, warranty/returns.
- Pass: priority channels reach minimum readiness and severe mismatches are absent.
- Fail: channel pages are inconsistent or hide critical proof.
- Failure action: fix PDP/retailer content before scaling spend.

### E13-05 Private Finance/Channel Guardrail Run

- Hypothesis: the recommended transaction range and bundle path clear internal floor and channel terms.
- Method: local/offline calculator; upload derived summary only if approved.
- Data: COGS/BOM, target margin, channel fee, promo cost, bundle cost, tax/shipping/returns assumptions.
- Primary metric: lowest allowed transaction price by channel.
- Pass: `97,840-99,990 Ft` range is feasible for priority channels.
- Fail: floor is above intended transaction range.
- Failure action: block promo-heavy strategy and switch to proof-led positioning or finance review.

### E13-06 Previous-Generation Sales Calibration

- Hypothesis: FIT 4 Pro Hungary launch/sell-through can map S08 demand index to unit ranges.
- Method: aggregate internal data analysis.
- Data: weekly units, ASP, channel split, promo, inventory, stockout, returns, major campaign events.
- Primary metric: comparable 30/60/90 day baseline.
- Pass: comparable baseline exists and channel mix is interpretable.
- Fail: data missing, not same-country, or channel context not comparable.
- Failure action: keep S08 as index-only and show data gap.

### E13-07 Landing/PDP Behavioral A/B

- Hypothesis: proof-led PDP modules increase qualified action versus generic product feature listing.
- Method: landing/PDP A/B with controlled traffic.
- Data: clickout, add-to-cart, FAQ clicks, payment section clicks, warranty section clicks, dwell time.
- Primary metric: qualified downstream action, not CTR alone.
- Pass: proof variant improves downstream action with stable bounce/quality.
- Fail: CTR improves without downstream action or price/trust drop-off rises.
- Failure action: revise proof, offer, and checkout/trust path.

### E13-08 Bounded Voice Extraction Expansion

- Hypothesis: Watch7 and FIT 4 Pro source windows are enough to produce directional Bain driver comparison.
- Method: bounded collection, source-item dedupe, coverage report.
- Data: Watch7 Arukereso reviews + Mobilarena windows; FIT 4 Pro Mobilarena/Arukereso/retailer traces.
- Primary metric: deduped source-item count and driver clarity.
- Pass: coverage supports directional driver ranking.
- Fail: sample remains too thin or biased.
- Failure action: no proxy score; keep qualitative driver map only.

## Pass / Fail Decision Rules

| Decision | Can proceed when | Must pause when |
|---|---|---|
| Lead message route | One route has stronger comprehension and lower objection than generic control. | All routes fail to reduce price or trust anxiety. |
| `99,990 Ft` anchor | Price-value proof passes and private floor clears transaction plan. | Proof fails or finance/channel floor blocks the offer. |
| Payment as selling point | Local payment setup and support path pass. | Support is unclear or route is only partial. |
| Channel priority | Named channel pages are consistent and measurable. | Key channels lack price/proof/offer clarity. |
| Unit forecast | Previous-generation or channel data calibrates S08 index. | No internal/channel baseline exists. |
| NSS/Bain proxy | Bounded collection yields enough deduped source items. | Sample thin, access blocked, or country mismatch too high. |

## Sample And Data Requirement Map

| Need | Minimum | Better | Private handling |
|---|---|---|---|
| Message/price survey | `n=60-100` screened Hungary intenders | `n=150+` with segment split | Aggregate results only. |
| Payment proof | Internal setup + supported route docs | Real local terminal checks + user comprehension | No personal payment data. |
| Private pricing | Derived thresholds | Full local calculator run | Raw COGS/margin stays local. |
| Previous-gen calibration | Aggregate weekly FIT 4 Pro sales | Channel-level weekly units, ASP, promo, inventory | Public HTML shows indexed or aggregate only. |
| Channel audit | 5-6 named channel pages | PDP events and retailer clickout data | Partner terms excluded. |
| Voice expansion | Fixed source windows | Full accessible page ranges with coverage reports | Store refs and short excerpts only. |

## Owner / Timeline / Effort Map

| Workstream | Owner hint | Timing | Effort |
|---|---|---|---|
| Channel/PDP readiness | channel + ecommerce + marketing | 1-2 days | low |
| Payment proof | product + support + local market | 2-5 days | medium |
| Price/value message test | marketing + research | 3-7 days | medium |
| Competitive choice test | research + marketing | 3-7 days | medium |
| Private finance guardrail | finance + channel + pricing | 1-3 days | low/medium |
| Previous-gen calibration | sales ops + channel | 2-5 days if data exists | medium |
| Landing/PDP A/B | ecommerce + media + analytics | 1-3 weeks | medium/high |
| Bounded voice expansion | analyst + local language reviewer | 1-3 days | low/medium |

## Private Data Validation Path

Private fields should stay outside public HTML:

- COGS/BOM
- margin target
- channel fees
- bundle cost
- sell-through
- inventory
- PO/channel commitments
- support/payment failure logs
- customer-level data

Allowed public summaries:

- indexed floor status: `clears floor / needs finance review / blocked`
- aggregate channel split
- aggregate sell-through calibration
- confidence upgrade or downgrade
- validation pass/fail status

## Validation Decision Gate

Status: `needs_validation`

Decisions ready with caveats:

- Use Watch7 as TOP1 competitor.
- Keep FIT 4 Pro and GT 6 as internal price ladder risks.
- Use multi-day battery and light fashion/material as lead message candidates.
- Keep `99,990 Ft` as public anchor for the draft dashboard.

Decisions requiring validation:

- Whether `99,990 Ft` can convert without stronger transaction mechanism.
- Whether payment can be used as a selling point.
- Whether named channels can carry consistent proof and price story.
- Whether S08 demand index can become unit forecast.
- Whether Watch7/FIT 4 Pro voice evidence can support a directional Bain/NSS proxy.

Blocked decisions:

- Profit-max or revenue-max price.
- Promo floor/channel floor.
- Inventory quantity.
- Final media budget and ROAS.
- Surveyed NSS/NPS.

Top tests to run first:

1. E13-04 Channel/PDP readiness audit.
2. E13-05 Private finance/channel guardrail run.
3. E13-01 Price/value message smoke test.
4. E13-02 Payment proof validation.
5. E13-03 Competitive choice test.

## S14 Hidden Handoff

S14 should use only these S13 fields:

- Validation gate status: `needs_validation`
- Top tests: E13-04, E13-05, E13-01, E13-02, E13-03
- Data gaps that must be visible:
  - no FIT 5 Pro NSS/NPS proxy
  - no internal COGS/margin/channel floor
  - no previous-generation Hungary sales calibration
  - no MKT budget/media response basis
  - no inventory/channel PO
  - payment proof not yet verified
- S13 section visibility: hidden by default.

S14 must not:

- Present validation plan as completed evidence.
- Render S13 as a major business section unless user asks.
- Convert tests into confirmed conclusions.

## Context Budget Report

Execution mode: handoff-only.

Opened local files:

- `pilot-state.md`
- S13 `SKILL.md`
- S13 output contract, input scenarios, validation methods, scoring rubrics

Web lookup: none.

Full artifact reopen: not needed.

Search budget status: within budget.

## Synthetic Persona Use Log

No AI persona simulation was used as evidence.

Allowed future use:

- survey wording pretest
- objection brainstorming
- local-language stimulus clarity

Prohibited use:

- WTP evidence
- demand forecast evidence
- conversion evidence
- final price decision

