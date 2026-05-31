# S01 Source Accessibility And Competitor Gate

Run id: `huawei-watch-fit-5-pro-hu-2026-05-31`
Mode: `real_product_pilot`
Product: HUAWEI WATCH FIT 5 Pro
Country: Hungary
Language priority: Hungarian first, English only as fallback
Access date: 2026-05-31

## Confirmed Gate

The reviewed deep-voice scope is fixed for this pilot:

- TOP1 external competitor: Samsung Galaxy Watch7 44mm
- Previous-generation product: HUAWEI WATCH FIT 4 Pro
- Internal price/cannibalization risk: HUAWEI WATCH GT 6

Rationale:

- Samsung Galaxy Watch7 44mm has high local visibility, strong Android ecosystem overlap, deep Hungarian review/comment availability, and a much lower current street-price anchor than FIT 5 Pro.
- HUAWEI WATCH FIT 4 Pro is the closest predecessor and has enough public local price/review traces to seed upgrade-friction and inherited-pain analysis.
- HUAWEI WATCH GT 6 is not the TOP1 competitor, but sits dangerously close to FIT 5 Pro in Hungarian public pricing, so it should remain a shelf/positioning confusion risk.

## Current Price And Channel Seed

This is a seed layer only; S04 should re-check prices before final pricing conclusions.

| Object | Public price signal | Channel signal | Notes |
|---|---:|---|---|
| HUAWEI WATCH FIT 5 Pro | 97,840-99,999 Ft visible in public channel traces | Huawei official, Arukereso, Euronics, Alza, MediaMarkt, Yettel, KOKU | Mainline public price appears effectively around 99,990 Ft; Yettel bundle shows 97,840 Ft with FreeBuds SE 4. |
| Samsung Galaxy Watch7 44mm | 54,900 Ft current lowest observed on Arukereso | Arukereso multi-merchant marketplace | Creates a strong value-for-money pressure point against FIT 5 Pro. |
| HUAWEI WATCH FIT 4 Pro | 76,065 Ft lowest / 82,115 Ft selected marketplace offer observed on Arukereso | Arukereso, eMAG, Alza, other retailers | Useful previous-generation price anchor; review count is small but usable as seed evidence. |
| HUAWEI WATCH GT 6 | 70,990 Ft from 46mm category listing and 89,990+ Ft for 41mm listings observed on Arukereso | Arukereso, Yettel and other local retailers | Must be shown as internal range confusion/cannibalization risk, not as TOP1 competitor. |

## Source Accessibility Matrix

| Source | Type | Role | Access | Expected depth | Collection level | Deep candidate | Limitation |
|---|---|---|---|---|---|---|---|
| Huawei Hungary product page | official_product | Specs and claim source for FIT 5 Pro | accessible | medium | structured records | no | No buyer voice. |
| Huawei Hungary buy page | official_retail | Official product/buy route | partial | low | source profile only | no | Price/content is JS-heavy; use as official route plus cross-check with retailers. |
| Arukereso FIT 5 Pro page | price_comparison | Price, availability, channel list | accessible | medium | structured records | yes for price | No buyer reviews visible yet; use as channel and price proof, not VOC. |
| MediaMarkt FIT 5 Pro pages | retailer | Availability, price, installment, review status | accessible | low | structured records | no | Reviews are sparse; some variants show review-writing only or one rating. |
| Yettel FIT 5 Pro bundle page | operator_retail | Operator bundle, price, FreeBuds SE 4 promo | accessible | medium | structured records | yes for channel | Good for channel strategy; not enough consumer voice. |
| Euronics FIT 5 Pro page | retailer | Price and availability | accessible | low | source profile only | no | Needs direct page extraction in a later channel pass. |
| Alza FIT 5 Pro / Huawei watch pages | retailer | Retail price, reviews, cross-generation comparison | partial | medium | structured records when accessible | yes for previous generation | Search exposes prior-gen ratings; direct dynamic pages may need browser/MCP. |
| Arukereso Samsung Watch7 44mm page | price_comparison | TOP1 competitor price and buyer-review proxy seed | accessible | high | structured records / voice atoms | yes | Static page exposes rating distribution and a sample review; full reviews may need paginated/manual collection. |
| Arukereso FIT 4 Pro page | price_comparison | Previous generation price and buyer-review seed | accessible | medium | structured records / voice atoms | yes | Small sample size; full review text may require paginated/manual collection. |
| Mobilarena FIT 5/5 Pro news thread | specialist_media_comment | Early local Hungarian questions and objections | accessible | low | voice atoms | yes, bounded | Only 6 comments; useful as fresh issue discovery, not representative VOC. |
| Mobilarena Huawei sport-watch thread | forum | Huawei ecosystem, compatibility, app/payment, GT 6/FIT 4 context | accessible | high | voice atoms | yes, bounded | Broader than FIT 5 Pro; must label as category/Huawei ecosystem evidence. |
| PCWPlus FIT 5 Pro review | specialist_media | Expert review, proof/objection seed | accessible | medium | structured records | no | Expert review, not consumer voice; can guide claims and tests. |
| Mobilarena Samsung Watch7 review | specialist_media | TOP1 competitor expert evidence | accessible | medium | structured records | yes for competitor profile | Expert review, not buyer VOC. |
| Mobilarena Samsung Watch7 comments | specialist_media_comment | TOP1 competitor deep voice source | accessible | high | voice atoms / coverage report | yes | Very large thread; must collect by bounded page ranges and coverage report. |
| Mobilarena general smartwatch thread | forum | Category comparison, Garmin/Amazfit/Samsung/Huawei decision language | accessible | high | voice atoms | optional | Use for search-language and category objections only; do not over-count toward FIT 5 Pro. |
| Hungarian YouTube review comments | video_comment | Local spoken-language objections and usage questions | unknown | medium | source profile first | optional | Needs YouTube/search connector and policy-aware comment export. |
| Reddit Huawei / smartwatch threads | social | International fallback for FIT 4 Pro and FIT 5 Pro problems | accessible | medium | snippets / voice atoms | fallback only | Not Hungary-specific; use only when local public voice is thin and label country mismatch. |

## Source Quality Implication

The current source mix is enough to continue S01 and S02, but not enough to calculate a surveyed or high-confidence NSS/NPS for FIT 5 Pro itself.

Use this confidence stance:

- FIT 5 Pro own-buyer NSS/NPS proxy: do not calculate yet. Public local buyer sample is too thin.
- TOP1 competitor Watch7 NSS/NPS proxy: directional proxy is possible after deduped collection from Arukereso plus Mobilarena comment/thread scope.
- Previous-generation FIT 4 Pro proxy: weak-to-directional proxy is possible, because public samples are smaller and split across Arukereso, Alza, Mobilarena/Huawei ecosystem threads, and possible international fallback.
- Bain-style driver inputs: allowed now as directional seed, but must show source-item count, country match, journey episode, and confidence.

## Immediate Next Jobs

1. Create a bounded voice-collection plan:
   - Samsung Watch7 44mm: Arukereso reviews + Mobilarena test comment thread.
   - HUAWEI WATCH FIT 4 Pro: Arukereso reviews + Alza rating/review traces + Huawei/Mobilarena ecosystem thread mentions.
   - HUAWEI WATCH FIT 5 Pro: Mobilarena news comments + MediaMarkt/retailer sparse ratings + PCWPlus expert objections.
2. Build `voice_collection_coverage_report` before extracting insights:
   - pages expected, pages collected, visible source-item count, collected item count, blocked/missing items.
3. Convert only in-scope comments/reviews into voice atoms:
   - pain, praise, purchase trigger, objection, comparison, question, price signal, trust signal.
4. Produce Bain/NSS hardware journey seed panel:
   - purchase, setup/pairing, first use, first 7 days, app experience, payment, sport tracking, sleep/health confidence, warranty/return.
5. Pass only compressed handoff to downstream modules:
   - source refs, count summary, top drivers, data gaps, price/channel risks, not raw comment dumps.

## Current Data Gaps

- No internal sales, margin, COGS, channel sell-through, return, support, or NSS/NPS data.
- No user-provided previous-generation customer files.
- FIT 5 Pro has very sparse post-launch public local buyer voice as of access date.
- Carrier/device-financing depth beyond Yettel is not confirmed yet; Telekom/Vodafone/One should be checked in the S08 channel pass.
- Google Trends/local keyword volumes not collected yet; use a separate search-language pass before final dashboard text.

