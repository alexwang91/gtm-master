<p align="center">
  <img src="assets/gtm-master-logo.svg" width="92" alt="GTM Master logo" />
</p>

<h1 align="center">GTM Master</h1>

<p align="center">
  Enter product features, launch countries, price segments, and report language to generate a B2C hardware GTM HTML report for presentation purposes.
</p>

<p align="center">
  <a href="https://github.com/alexwang91/gtm-master/stargazers">
    <img alt="GitHub stars" src="https://img.shields.io/github/stars/alexwang91/gtm-master?style=social" />
  </a>
  <img alt="Status" src="https://img.shields.io/badge/status-private%20pilot-6B7280" />
  <img alt="Report language" src="https://img.shields.io/badge/report-user--selected-2457D6" />
  <img alt="Output" src="https://img.shields.io/badge/output-offline%20HTML-157F5B" />
  <img alt="Skill suite" src="https://img.shields.io/badge/skills-15%20modules-B25B00" />
  <img alt="Agents" src="https://img.shields.io/badge/agents-Codex%20%7C%20Claude%20Code-111827" />
</p>

GTM Master is a multi-skill GTM intelligence suite for consumer hardware launches. It helps an AI coding agent turn a small launch brief into a structured, evidence-backed GTM report with local market research, competitor logic, consumer voice, pricing judgment, launch forecast, KOL/content direction, validation gaps, citations, and a polished offline HTML dashboard.

The current suite is report-language-required. The agent must ask for `report_language` during intake and must not silently default English, Chinese, or any other language. Chinese, English, and other-language reports use the same GTM contracts; only dashboard-facing wording changes.

## What It Does

Minimum input:

```json
{
  "product_features_and_specs": "",
  "launch_country_or_region": "",
  "target_price_range": "",
  "report_language": ""
}
```

High-value optional inputs:

- product spec sheets
- previous-generation sales, price, channel, return, NSS/NPS, or review data
- brand positioning, claim boundaries, and approved/forbidden wording
- competitor lists, internal benchmarks, channel plans, KOL history, landing pages, PDP copy, or ad copy
- private COGS, margin, channel terms, and MKT budget, preferably kept in local-only calculators when sensitive

Main output:

- a meeting-ready HTML GTM report in the user-selected report language
- named-channel priority and launch action plan
- TOP1 competitor proof and internal price-ladder risk
- segment, JTBD, message, proof, price, channel, KOL, and forecast views
- citations, confidence labels, data gaps, and local-only private pricing tools

## How The Suite Works

```text
GTM Master Run
|-- S00 gtm-master [hidden orchestration]
|   |-- project brief, run state, method routing, report state
|-- S01 build-consumer-market-map [visible]
|   |-- local market, channels, competitor candidates, consumer voice, TAM/SAM/SOM seeds
|-- S02 mine-jtbd-scenarios [visible]
|   |-- JTBD, Four Forces, product-job fit, proof needs, purchase objections
|-- S03 match-messages-to-segments [visible]
|   |-- segment message architecture, feature-benefit-proof, claim risks, touchpoints
|-- S04 model-price-sensitivity [visible]
|   |-- opening price strategy, WTP, price corridor, private calculator spec
|-- S05 score-creative-assets [conditional]
|-- S06 score-kol-fit [conditional]
|-- S07 predict-dtc-conversion [conditional]
|-- S08 forecast-launch-demand [visible]
|   |-- 30/60/90 launch forecast, MKT response, channel readiness, inventory risk
|-- S09 predict-activation-risk [conditional]
|-- S10 generate-health-insights [conditional]
|-- S11 predict-subscription-and-churn [conditional]
|-- S12 mine-review-quality-feedback [conditional/post-launch]
|-- S13 plan-validation-experiments [hidden capability]
+-- S14 compose-html-gtm-dashboard [hidden composer]
    |-- polished offline HTML report, citations, data gaps, calculators
```

S14 is a hidden composer. It should not appear as a strategic business module in the final report.

## Available Skills

| Skill | Role |
|---|---|
| [`gtm-master`](skills/gtm-master/) | S00 orchestrator, run state, methodology routing, handoff isolation, report contract |
| [`build-consumer-market-map`](skills/build-consumer-market-map/) | S01 local market, source map, competitor discovery, consumer voice, segment and channel seeds |
| [`mine-jtbd-scenarios`](skills/mine-jtbd-scenarios/) | S02 JTBD scenarios, Four Forces, product-job fit, anti-JTBD risks |
| [`match-messages-to-segments`](skills/match-messages-to-segments/) | S03 message architecture, proof chain, objections, segment-channel mapping |
| [`model-price-sensitivity`](skills/model-price-sensitivity/) | S04 opening price strategy, WTP, Van Westendorp/MaxDiff test path, private price tools |
| [`score-creative-assets`](skills/score-creative-assets/) | S05 optional copy and editable asset scoring |
| [`score-kol-fit`](skills/score-kol-fit/) | S06 optional KOL/creator fit, budget, expected reach and rationale |
| [`predict-dtc-conversion`](skills/predict-dtc-conversion/) | S07 optional DTC/PDP conversion planning and friction analysis |
| [`forecast-launch-demand`](skills/forecast-launch-demand/) | S08 sales forecast, MKT response, channel readiness, growth S-curve |
| [`predict-activation-risk`](skills/predict-activation-risk/) | S09 setup, activation, compatibility, return, and onboarding risk |
| [`generate-health-insights`](skills/generate-health-insights/) | S10 conditional sensitive claims and insight guardrails |
| [`predict-subscription-and-churn`](skills/predict-subscription-and-churn/) | S11 conditional subscription, retention, churn, service-plan economics |
| [`mine-review-quality-feedback`](skills/mine-review-quality-feedback/) | S12 post-launch review, support, quality, and next-generation feedback loop |
| [`plan-validation-experiments`](skills/plan-validation-experiments/) | S13 hidden validation roadmap and experiment priority |
| [`compose-html-gtm-dashboard`](skills/compose-html-gtm-dashboard/) | S14 hidden static HTML report composer |

## Methodology Coverage

The suite maps imported marketing methods into hardware launch decisions:

- AARRR adapted to hardware launch, retail/PDP activation, purchase conversion, post-purchase activation, referral/review, and revenue
- JTBD and Four Forces for buying scenarios, switching triggers, inertia, and anxiety
- VOC, NSS/NPS proxy, and Bain-style driver logic for consumer voice and journey diagnosis
- Van Westendorp and MaxDiff for WTP, value proof, and price-test design
- ICE for validation prioritization
- ORB for owned, rented, and borrowed channel planning
- 17-item hardware current-state scoring for launch readiness
- budget formulas, CAC-style planning, and growth S-curves for S08 forecast and validation
- copy sweeps for direct, language-appropriate report quality

## Report Principles

The final HTML body should read like a formal GTM report:

- concise, evidence-scoped, and suitable for upward reporting
- direct enough to guide local GTM, sales, channel, product, and research teams
- cautious about unsupported conclusions, with confidence labels and decision-changing questions
- no workflow log language in the main body
- no skill IDs, handoff mechanics, report-audience labels, or module coverage as the lead story
- no raw private COGS, margin, or channel terms embedded by default

## Example Prompt

```text
使用 gtm-master，帮我为这个产品生成 standard GTM 报告：

产品：Huawei WATCH FIT 5 Pro
上市国家：匈牙利
价格：99,990 Ft
核心卖点：轻薄设计、睡眠健康、多日续航、运动健康
渠道假设：Huawei official、Alza、MediaMarkt、Euronics、Yettel
预算：50,000 美元

如遇到关键不确定项，先标为 data gap，不要编造结论。
最终输出客户指定报告语言的 HTML 报告。
```

## Installation

### Use With Codex

Clone the repo and copy or symlink the skills into your Codex skills directory:

```powershell
git clone https://github.com/alexwang91/gtm-master.git
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills"
Copy-Item -Recurse ".\gtm-master\skills\*" "$env:USERPROFILE\.codex\skills\"
```

Then ask Codex to use `gtm-master` for a hardware GTM report.

### Use With Claude Code Or Agent Skills

```bash
git clone https://github.com/alexwang91/gtm-master.git
mkdir -p .agents/skills
cp -R gtm-master/skills/* .agents/skills/
```

If your agent reads `.claude/skills`, copy or symlink the same folders there.

### Develop In Place

```powershell
git clone https://github.com/alexwang91/gtm-master.git
cd "gtm-master"
python scripts\validate-gtm-suite-contracts.py
```

## Repository Structure

```text
gtm-master/
|-- skills/
|   |-- gtm-master/
|   |-- build-consumer-market-map/
|   |-- mine-jtbd-scenarios/
|   |-- match-messages-to-segments/
|   |-- model-price-sensitivity/
|   |-- forecast-launch-demand/
|   +-- compose-html-gtm-dashboard/
|-- scripts/
|   |-- render-gtm-dashboard-from-report-state.py
|   |-- validate-gtm-suite-contracts.py
|   +-- test_render_chinese_copy_style.py
|-- tools/
|-- docs/
+-- artifacts/
```

## Star History

Star history charts usually render once the repository is public and visible to the Star History API.

<picture>
  <source
    media="(prefers-color-scheme: dark)"
    srcset="https://api.star-history.com/svg?repos=alexwang91/gtm-master&type=Date&theme=dark"
  />
  <source
    media="(prefers-color-scheme: light)"
    srcset="https://api.star-history.com/svg?repos=alexwang91/gtm-master&type=Date"
  />
  <img
    alt="Star History Chart"
    src="https://api.star-history.com/svg?repos=alexwang91/gtm-master&type=Date"
  />
</picture>

## Current Status

This repository is in private pilot. The core architecture, method contracts, recoverable state machine, report-state contract, quality gates, and multi-language HTML report composer contracts are active. Real-product pilots should be treated as evidence-gathering and report-quality tests until private company data, live local evidence, and channel feedback are supplied.

## License

This project is licensed under the MIT License. See [`LICENSE`](LICENSE) for details.
