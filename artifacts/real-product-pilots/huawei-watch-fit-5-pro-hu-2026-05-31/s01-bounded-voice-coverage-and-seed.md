# S01 Bounded Voice Coverage And Seed

Run id: `huawei-watch-fit-5-pro-hu-2026-05-31`
Mode: `real_product_pilot`
Access date: 2026-05-31
Status: first bounded collection design plus seed extraction

This file deliberately separates three things:

- `coverage`: what public sources can be accessed and how many source items are visible.
- `seed atoms`: early voice atoms extracted from accessible snippets/pages.
- `NSS/Bain readiness`: whether a proxy score is allowed, or whether only directional drivers may be used.

## Deep Voice Scope

| Object | Role | Confirmed source scope | Coverage stance |
|---|---|---|---|
| Samsung Galaxy Watch7 44mm | TOP1 external competitor | Arukereso product page, Mobilarena review, Mobilarena comments first page, current/latest thread windows | Strong source pool, but full thread is too large for one context. Use bounded windows and coverage report. |
| HUAWEI WATCH FIT 4 Pro | Previous generation | Arukereso product page, MediaMarkt campaign page, Mobilarena FIT 4 launch article/comments, Smarteast local review | Medium source pool. Enough for upgrade and inherited-objection seeds; public buyer review texts are not fully visible from static Arukereso page. |
| HUAWEI WATCH FIT 5 Pro | Target product | Huawei official page, Arukereso product page, Yettel bundle page, Mobilarena launch article/comments, international expert reviews as fallback | Sparse own-buyer voice. Do not calculate own-product NSS/NPS proxy yet. |
| HUAWEI WATCH GT 6 | Internal price/cannibalization risk | Arukereso/Huawei category price traces, official Huawei navigation visibility | Keep as channel/pricing risk, not deep voice object in this pilot. |

## Coverage Report

| Source ref | Product/object | Source type | Visible item count | Collected now | Coverage confidence | Use |
|---|---|---:|---:|---:|---|---|
| `ak-fit5pro` | FIT 5 Pro | price comparison | 0 product reviews visible; offers visible | price/channel facts only | high for price, none for VOC | S01 price/channel, S04 price anchors |
| `yettel-fit5pro` | FIT 5 Pro | operator retail | no public reviews visible | price/bundle facts only | high for channel | S08 channel strategy |
| `ma-fit5pro-news` | FIT 5 Pro | specialist media | article + 6 comments | all visible comments seed-read | high within source | Early questions: payment, charging, strap, upgrade value |
| `huawei-fit5pro-official` | FIT 5 Pro | official product page | no reviews | specs/claims only | high for claims | Selling point and proof map |
| `ak-watch7` | Watch7 44mm | price comparison / buyer review | 34 reviews visible in rating summary | summary + most-helpful review snippet | medium | TOP1 competitor price/review proxy seed |
| `ma-watch7-review` | Watch7 44mm | specialist media | expert review | article-level driver extraction | high | Competitor product strengths/weaknesses |
| `ma-watch7-thread-first` | Watch7 44mm | forum comments | comments #1-#50 page accessible | seed-read first page | medium | Launch/owner comments, battery/payment questions |
| `ma-watch7-thread-latest` | Watch7 44mm | forum comments | latest thread shows IDs past #2100 | seed-read current window | medium | Long-run owner complaints/questions; full collection requires bounded pagination |
| `ak-fit4pro` | FIT 4 Pro | price comparison / buyer review | 9 reviews visible in rating count; offers visible | price/count only | medium | Previous-generation price and review-volume seed |
| `mm-fit4pro-campaign` | FIT 4 Pro | retailer/campaign | MediaMarkt rating counts by color visible | campaign/retail facts only | medium | Launch channel and promo context |
| `ma-fit4pro-news` | FIT 4 Pro | specialist media | article plus comment thread | article facts + comment-thread seed | high | Launch price, channel, feature claims |
| `ma-fit4pro-thread` | FIT 4 Pro | forum comments | current thread shows 127-1 range | seed-read latest visible window | medium | Upgrade friction, price trust, payment, setup, update issues |
| `smarteast-fit4pro-review` | FIT 4 Pro | local review | expert review | article-level driver extraction | medium | Local Hungarian previous-gen evaluation |

## Seed Voice Atoms

These are not the final full extraction. They are enough to determine which drivers must be preserved downstream.

| Atom id | Object | Source ref | Viewpoint | Journey | Driver | Direction | Marketing implication |
|---|---|---|---|---|---|---|---|
| va-fit5-001 | FIT 5 Pro | `ma-fit5pro-news` | User asks whether OTP/contactless payment works reliably or repeats prior-generation friction | consideration | payment trust | objection | Payment support must be explained with supported wallet/bank path, not hidden in feature list. |
| va-fit5-002 | FIT 5 Pro | `ma-fit5pro-news` | Users discuss whether Qi or third-party wireless charging works | setup_pairing | charging compatibility | question/objection | Product page and retail FAQ should state charger compatibility clearly. |
| va-fit5-003 | FIT 5 Pro | `ma-fit5pro-news` | User says the device is visually attractive | consideration | design/style | praise | Fashion/design can be a front-row selling point in Hungary. |
| va-fit5-004 | FIT 5 Pro | `ma-fit5pro-news` | User asks about strap compatibility and connector mechanism | purchase | accessory ecosystem | question | Accessory compatibility should be included in retailer Q&A and sales scripts. |
| va-fit5-005 | FIT 5 Pro | `ma-fit5pro-news` | User argues Pro changed less vs FIT 4 Pro; standard FIT 5 may be enough if ECG/arterial stiffness are unused | consideration | upgrade value | objection | Position Pro around premium materials, sports/outdoor, ECG, sapphire and display, not generic smartwatch basics. |
| va-fit5-006 | FIT 5 Pro | `ak-fit5pro` + `yettel-fit5pro` | Public price sits around 98-100k Ft with bundle/promo | purchase | price/value | price signal | Need bundle/value proof because Watch7 and FIT 4 Pro undercut the price. |
| va-fit4-001 | FIT 4 Pro | `ma-fit4pro-thread` | User asks whether sapphire glass still needs a protector | post_purchase | durability/protection | question | Sapphire claim is valuable, but buyers still need practical scratch-resistance guidance. |
| va-fit4-002 | FIT 4 Pro | `ma-fit4pro-thread` | Users flag suspicious low-price eMAG listing and spec mismatch | purchase | price trust | complaint/question | Cheap marketplace offers may hurt price trust; official/authorized-channel proof matters. |
| va-fit4-003 | FIT 4 Pro | `ma-fit4pro-thread` | Owner says they bought near 110k Ft and now lower offers make value feel eroded | post_purchase | retained value | detractor_like | Launch price and promo cadence should avoid making early adopters feel punished. |
| va-fit4-004 | FIT 4 Pro | `ma-fit4pro-thread` | Strap compatibility with FIT 3/4 is confirmed by users | post_purchase | accessory ecosystem | praise | Compatibility is a low-cost reassurance message. |
| va-fit4-005 | FIT 4 Pro | `ma-fit4pro-thread` | User reports contactless payment finally works | first_use | payment | promoter_like | Payment can be a conversion trigger if proven locally. |
| va-fit4-006 | FIT 4 Pro | `ma-fit4pro-thread` | User has caller-name display/setup issue | setup_pairing | phone integration | complaint/question | Setup checklist should include caller ID, permissions, app settings. |
| va-fit4-007 | FIT 4 Pro | `ma-fit4pro-thread` | User reports delayed/unclear firmware update path | app_experience | update reliability | complaint | Support content should explain update route through Huawei Health. |
| va-watch7-001 | Watch7 | `ak-watch7` | Former Huawei watch user considered Samsung for full compatibility with Samsung phone | consideration | ecosystem compatibility | purchase_trigger | Watch7 wins Android/Samsung users through ecosystem confidence. |
| va-watch7-002 | Watch7 | `ak-watch7` | Buyer praises comfort, design, display, animations, functions | first_use | design/app richness | promoter_like | Samsung has high perceived smartwatch completeness. |
| va-watch7-003 | Watch7 | `ak-watch7` | Buyer complains about low battery and inaccurate health measurements | first_7_days | battery/accuracy | detractor_like | FIT 5 Pro should attack on battery endurance and sport/health proof carefully. |
| va-watch7-004 | Watch7 | `ma-watch7-review` | Expert review frames Watch7 as strong for Samsung/Android ecosystem and apps | consideration | app ecosystem | praise | This is Samsung's hardest-to-copy advantage. |
| va-watch7-005 | Watch7 | `ma-watch7-review` | Expert review criticizes 1-1.5 day real battery for 40/44mm under active use | first_7_days | battery | complaint | FIT 5 Pro should make multi-day battery a management-summary-level contrast. |
| va-watch7-006 | Watch7 | `ma-watch7-review` | Expert review questions HR/SpO2/GPS accuracy for serious sport | first_use | sport accuracy | complaint | FIT 5 Pro should not overclaim; use running/cycling/outdoor proof and third-party review validation. |
| va-watch7-007 | Watch7 | `ma-watch7-thread-latest` | Long-run users discuss updates, sleep apnea/health feature availability, and compatibility confusion | app_experience | feature rollout | mixed | Samsung has richer features, but rollout/eligibility confusion creates a messaging opening. |
| va-watch7-008 | Watch7 | `ma-watch7-thread-latest` | User asks where to buy cheapest because price differences are large | purchase | channel/price complexity | objection | Hungarian shoppers actively compare merchant reliability and price spread. |

## NSS / Bain Readiness

| Object | Source-item readiness | Proxy confidence stance | Allowed action |
|---|---|---|---|
| FIT 5 Pro | 6 local Mobilarena comments, 0 Arukereso buyer reviews, no confirmed retailer-review base | `0-39`: do not calculate proxy NSS/NPS | Use directional Bain drivers only. Show data gap. |
| FIT 4 Pro | Arukereso count 9, Mobilarena thread window, local review, retailer rating counts | `40-59`: weak proxy until full review/comment extraction | Use driver ranking; avoid a numeric NPS score unless full collection is completed. |
| Watch7 44mm | Arukereso 34 reviews plus Mobilarena thread over 2000 IDs and expert review | `60-79`: directional proxy possible after bounded extraction/deduping | Calculate directional proxy only after collection windows are fixed and deduped. |

## Bain Driver Seed Panel

| Driver | Main object | Direction | Journey | Driver impact seed | Why it matters for FIT 5 Pro |
|---|---|---|---|---:|---|
| Battery endurance | FIT 5 Pro vs Watch7 | positive for FIT / negative for Watch7 | first_7_days | 82 | This is the cleanest competitive attack because Watch7 has visible battery complaints and FIT 5 Pro claims 7-10 days. |
| Local payment reliability | FIT 5 Pro / FIT 4 Pro / Watch7 | mixed | purchase, first_use | 78 | Hungarian buyers ask specific wallet/bank questions; payment must be proven, not merely listed. |
| Price/value credibility | FIT 5 Pro / FIT 4 Pro / Watch7 / GT 6 | risky | purchase | 76 | FIT 5 Pro sits above Watch7 street price and above FIT 4 Pro discounted price; value proof must be explicit. |
| Ecosystem compatibility | Watch7 | Samsung advantage | setup_pairing, app_experience | 74 | Watch7's strongest pull is Samsung phone integration, health/app ecosystem, and Wear OS depth. |
| Premium material/design | FIT 5 Pro / FIT 4 Pro | Huawei advantage | consideration | 72 | Sapphire, titanium, brightness, thin body and fashion language are credible differentiators. |
| Charging/accessory clarity | FIT 5 Pro / FIT 4 Pro | risk | setup_pairing | 63 | Qi/charger/strap confusion creates unnecessary purchase friction. |
| Sport/outdoor proof | FIT 5 Pro | opportunity | first_use | 61 | Golf, trail run, cycling, diving and GPS claims need proof because serious-sport buyers compare Garmin/Samsung/Apple. |
| Update/feature rollout clarity | Watch7 / FIT 4 Pro | mixed | app_experience | 58 | Both ecosystems have feature availability confusion; clear local support content can reduce anxiety. |

## Handoff To S02/S04/S08

Only pass this compressed pack downstream:

- Competitor gate: Watch7 external TOP1, FIT 4 Pro previous generation, GT 6 internal risk.
- Price anchors: FIT 5 Pro around 98-100k Ft; Watch7 54.9k Ft floor; FIT 4 Pro 76.1k Ft floor; GT 6 risk near/below FIT 5 Pro depending variant.
- Consumer voice themes: battery, payment reliability, price/value, ecosystem compatibility, design/material, charging/accessory clarity, sport/outdoor proof, update/feature rollout clarity.
- NSS policy: FIT 5 Pro no proxy score; Watch7 directional proxy after bounded extraction; FIT 4 Pro weak proxy unless more buyer text is collected.
- Data gaps: retailer reviews, Huawei internal sell-through, support tickets, return reasons, COGS/margin, Telekom/Vodafone/One operator availability, Google Trends/search-language data.

## Next Collection Step

Before S02 final scenario mining, run one bounded extraction pass:

1. Watch7: Arukereso 34 review summary plus Mobilarena windows `1-50`, `1501-1650`, and latest `friss`.
2. FIT 4 Pro: Mobilarena current thread `127-1`, Arukereso 9-review count, MediaMarkt rating counts, Smarteast review.
3. FIT 5 Pro: Mobilarena 6-comment thread, Huawei official page, Arukereso/Yettel/MediaMarkt channel pages, international expert fallback only for technical proof.

