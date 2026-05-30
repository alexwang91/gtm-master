# Build Consumer Market Map - Complete Methodology

## 1. Objective

`build-consumer-market-map` is the first GTM skill for 2C hardware products.

Its purpose is to take a **product**, a **target country/region**, and a **target price range**, then autonomously build a localized consumer GTM market map.

The skill is designed for teams that receive a product from product/sales/sourcing teams and need to decide:

- Who should buy it in a specific country?
- What local consumer problem does it solve?
- What local alternatives and competitors matter?
- Is the proposed price credible locally?
- Which channels and touchpoints influence buying?
- What NPS structure can be inferred versus competitors?
- Is growth likely to be earned through loyalty/word-of-mouth or bought through marketing spend?
- What should the initial GTM priority be?

The skill should **not** ask the user to guess the target consumer. It infers target segments from evidence.

---

## 2. Minimal Inputs

The user only needs to provide:

```json
{
  "product_category": "",
  "product_name_or_codename": "",
  "product_spec_or_feature_list": "",
  "target_country_or_region": "",
  "target_price_range": ""
}
```

Optional inputs:

```json
{
  "launch_language": "",
  "launch_timing": "",
  "planned_channels": [],
  "known_competitors": [],
  "previous_generation_sales_data": "",
  "previous_generation_reviews": "",
  "return_reasons": "",
  "customer_service_logs": "",
  "app_analytics": "",
  "brand_positioning_constraints": "",
  "claim_or_compliance_constraints": ""
}
```

The user should **not** be required to provide:

- Competitor list
- Forum links
- Local review links
- Local social platforms
- Existing target personas
- Consumer pain points
- Price benchmark tables

These are discovered by the skill through approved tools, MCP connectors, APIs, public web research, internal data connectors, or compliant crawling.

---

## 3. Methodology Overview

```text
Product input
  鈫?Product capability normalization
  鈫?MCP-driven local evidence discovery
  鈫?Competitor and substitute mapping
  鈫?Local consumer opinion mining
  鈫?TAM / SAM / SOM estimation
  鈫?Consumer segmentation
  鈫?Persona cards
  鈫?Channel and touchpoint mapping
  鈫?Local price sensitivity analysis
  鈫?Bain-style NPS and Earned Growth dashboard
  鈫?GTM priority recommendation
  鈫?Evidence, assumptions, data gaps, and next tests
```

---

## 4. Evidence Classification

Every major conclusion must be labeled:

```text
[EVIDENCE]          Directly supported by data, consumer statements, internal data, public review, survey, or source.
[STRONG INFERENCE]  Supported by multiple signals but not directly measured.
[WEAK INFERENCE]    Plausible but evidence is thin.
[ASSUMPTION]        Required for the model, but still needs validation.
```

This prevents the skill from sounding more certain than the evidence allows.

---

## 5. Product Capability Normalization

The product specification is transformed into a structured capability map.

### 5.1 Classification

Each feature is classified as one of:

- Category entry feature
- Competitive feature
- Differentiating feature
- Premium justification feature
- Trust-building feature
- Retention / subscription feature
- Risky or hard-to-prove claim
- Commodity or low-value feature

### 5.2 Output Schema

```json
{
  "product_category": "",
  "device_type": "",
  "core_capabilities": [],
  "secondary_capabilities": [],
  "differentiators": [],
  "commodity_features": [],
  "premium_justification_features": [],
  "subscription_or_retention_features": [],
  "potential_claims": [],
  "risky_claims": [],
  "likely_substitutes": [],
  "initial_price_band_hypothesis": ""
}
```

### 5.3 Rule

A feature is not automatically a selling point.

A feature becomes a selling point only if it:

- Solves a local consumer problem
- Creates perceived value
- Builds trust
- Increases willingness to pay
- Improves conversion
- Improves retention
- Differentiates against local competitors

---

## 6. MCP-Driven Local Evidence Discovery

The skill uses `MCP_CONNECTORS.md` as the configuration layer.

The main skill decides **what evidence is needed**. The MCP layer decides **which tool should collect it**.

### 6.1 Evidence to Discover

Where legally and technically permitted, discover:

1. Local direct competitors
2. Local substitutes
3. Local bestsellers
4. Local marketplace prices
5. Local retailer prices
6. Local reviews
7. Local consumer discussions
8. Local social content and comments
9. Video reviews and comments
10. App store reviews for competitor apps
11. Price comparison pages
12. Deal forum discussions
13. Expert reviews
14. Local channel availability
15. Local creator / influencer ecosystem signals

### 6.2 Local-Language Query Generation

The skill generates local-language search queries from:

- Product category
- Use cases
- Product capabilities
- Target price band
- Known or discovered competitors
- Local complaint terms
- Local buying-intent terms
- Local substitute terms

Generic example for a local-language query bank:

```text
[category local term] test [country]
[top competitor] alternative [country]
[core use case local term] user experiences
[feature local term] problem
[business model local term] complaints
best [category local term] [country]
```

Generic example for Chinese-language query expansion:

```text
[品类词] 评测
[品类词] 值不值得买
[竞品名] 替代
[核心卖点] 准不准
[功能词] 差评
[商业模式词] 吐槽
```

---

## 7. Source Ranking and Data Quality

Every source is scored before being used heavily.

### 7.1 Source Scoring Schema

```json
{
  "source_name": "",
  "source_type": "",
  "country_relevance": 0,
  "category_relevance": 0,
  "consumer_intent_quality": 0,
  "review_depth": 0,
  "freshness": 0,
  "sample_size": 0,
  "bias_risk": 0,
  "access_method": "manual_upload | web_search | api | mcp | crawler | browser | unavailable",
  "recommended_use": "primary | secondary | context_only | avoid",
  "reason": ""
}
```

### 7.2 Evidence Priority

1. Internal sales, return, support, and app data
2. Direct survey or NPS data
3. Verified buyer reviews
4. Marketplace and retailer reviews
5. App store reviews
6. Local forums and specialist communities
7. Long-form expert reviews
8. Social comments and short-form content
9. Search snippets and low-context mentions

### 7.3 Bias Risks

Track:

- Incentivized reviews
- Fake reviews
- Platform demographic bias
- Vocal minority bias
- Extreme negative bias
- Influencer sponsorship bias
- Outdated reviews
- Region mismatch
- Language translation loss
- Non-verified purchase

---

## 8. Competitor and Substitute Mapping

The skill autonomously identifies direct competitors and substitutes.

### 8.1 Competitor Schema

```json
{
  "brand": "",
  "product": "",
  "product_type": "",
  "local_price": "",
  "subscription_model": "",
  "channel_presence": [],
  "positioning": "",
  "key_claims": [],
  "strengths": [],
  "weaknesses": [],
  "consumer_complaints": [],
  "consumer_praise": [],
  "opportunity_gaps": [],
  "threat_level": "high | medium | low",
  "evidence_sources": []
}
```

### 8.2 Substitute Logic

Substitutes can include:

- A cheaper device
- A premium ecosystem product
- A different device type
- A mobile app
- A non-electronic product
- A manual habit
- Doing nothing

The skill must not define the competitive set too narrowly.

---

## 9. Local Consumer Opinion Map

The skill extracts structured consumer voice from local reviews, forums, comments, app reviews, and internal feedback.

### 9.1 Extracted Themes

- Purchase reasons
- Pain points
- Positive drivers
- Negative drivers
- Price complaints
- Subscription complaints
- Comfort / usability issues
- Accuracy / trust concerns
- Feature confusion
- Competitor comparisons
- Substitute products
- Influencer mentions
- Channel mentions
- Purchase triggers
- Return reasons
- FAQs

### 9.2 Consumer Voice Schema

```json
{
  "country": "",
  "language": "",
  "source": "",
  "product_or_competitor": "",
  "raw_consumer_statement": "",
  "translated_statement": "",
  "theme": "",
  "sentiment": "positive | neutral | negative | mixed",
  "emotion_strength": 0,
  "purchase_stage": "awareness | consideration | purchase | onboarding | usage | retention | return",
  "evidence_strength": "high | medium | low"
}
```

The original local-language wording must be preserved.

---

## 10. TAM / SAM / SOM Estimation

The skill estimates market opportunity transparently, not as false precision.

Use `market-sizing-tam-sam-som-seed.md` for S01 market sizing. S01 should output ranges, assumption trees, segment-level sizing, comparable-market proxies, confidence scores, and data gaps. Final launch demand forecasting belongs to S08.

### 10.1 Definitions

- **TAM**: total addressable consumer pool for the category or underlying need
- **SAM**: reachable consumers for this product type and price band
- **SOM**: realistic obtainable market for launch period

### 10.2 Assumption Tree

```text
TAM = target population 脳 relevant demographic or need filter 脳 category need incidence

SAM = TAM 脳 price-band affordability 脳 product-type acceptance 脳 channel reach

SOM = SAM 脳 awareness 脳 conversion 脳 launch capacity
```

### 10.3 Output Schema

```json
{
  "country": "",
  "category": "",
  "tam_estimate": "",
  "sam_estimate": "",
  "som_estimate": "",
  "segment_level_estimates": [
    {
      "segment": "",
      "tam": "",
      "sam": "",
      "som": "",
      "assumption_tree": [],
      "confidence": "high | medium | low",
      "data_gaps": []
    }
  ],
  "method": "evidence_based | benchmark_based | assumption_based | blended",
  "confidence": "high | medium | low",
  "data_gaps": []
}
```

---

## 11. Consumer Segmentation

Use `segment-persona-inference.md` before producing final segment seeds. Generate segment candidates from consumer voice themes, Bain driver inputs, journey episodes, competitor/substitute behavior, price evidence, TAM/SAM/SOM assumptions, and channel/touchpoint signals. Do not ask the user to define segments; infer them, score evidence strength, run distinctness checks, and preserve weak-but-commercially-important candidates as hypotheses with explicit data gaps.

Segmentation is based on motivation, use case, willingness to pay, and behavior - not demographics alone.

### 11.1 Segment Schema

```json
{
  "segment_id": "",
  "segment_name": "",
  "country": "",
  "segment_definition": "",
  "core_motivation": "",
  "primary_use_cases": [],
  "pain_points": [],
  "purchase_triggers": [],
  "current_substitutes": [],
  "most_relevant_product_features": [],
  "irrelevant_or_low_value_features": [],
  "objections": [],
  "trust_requirements": [],
  "channel_preferences": [],
  "media_touchpoints": [],
  "influencer_types": [],
  "price_sensitivity": "low | medium | high | very_high",
  "estimated_wtp_range": "",
  "tam_relevance": "high | medium | low",
  "gtm_priority": "P1 | P2 | P3 | avoid",
  "evidence": [],
  "assumptions": []
}
```

### 11.2 Segment Examples for Wearables

Examples only; do not force them:

- Sleep recovery consumers
- Fitness recovery consumers
- Appearance-first light-health consumers
- Weight-management consumers
- Family-care buyers
- Budget entry consumers
- Professional training consumers
- Safety and location buyers
- Subscription-resistant consumers
- Premium ecosystem buyers

---

## 12. Segment Priority Scoring

Default formula:

```text
Segment Priority Score =
  Pain Intensity 脳 0.18
+ Product Fit 脳 0.18
+ Willingness to Pay 脳 0.14
+ Reachability 脳 0.12
+ Local Market Size 脳 0.12
+ Competitor Gap 脳 0.10
+ Content Virality 脳 0.08
+ Retention / Subscription Potential 脳 0.08
- Trust Barrier 脳 0.10
- Return / Support Risk 脳 0.05
```

Output:

```json
{
  "segment_name": "",
  "priority_score": 0,
  "rank": 0,
  "reason_to_prioritize": "",
  "reason_to_deprioritize": "",
  "recommended_gtm_role": "primary_launch_segment | secondary_segment | testing_segment | avoid"
}
```

Weights can be adjusted for:

- Launch revenue
- Gross profit
- Brand awareness
- PMF validation
- Subscription base
- Inventory clearance
- Premium positioning
- Retail support

---

## 13. Persona Cards

For each priority segment, create a localized persona card.

Persona cards are operational launch artifacts, not fictional biographies. Each card should connect local language, buying trigger, proof need, channel, price concern, and objection to evidence refs or explicit assumptions.

### 13.1 Persona Format

```md
## Persona: [Segment Name]

### Country context

### What they want

### What they dislike about current solutions

### Why this product may fit

### What they need to believe before buying

### Where to reach them

### Price sensitivity

### Recommended GTM angle

### Evidence and assumptions
```

Each card must include:

- Local consumer language
- Core motivation
- Daily-life scenario
- Pain points
- Buying trigger
- Current substitute
- Relevant product features
- Irrelevant features
- Trust barrier
- Price sensitivity
- Channel preference
- Preferred content format
- Influencer type
- Key objection
- Recommended message angle

---

## 14. Channel and Touchpoint Map

For each segment, identify:

- Where they discover products
- Where they compare products
- Where they buy
- Where they complain
- Which creators or experts influence trust
- Which content format drives conversion
- Which retail or marketplace channel fits

Use `channel-touchpoint-mapping.md` before finalizing channel and touchpoint outputs. Separate discovery, comparison, purchase, proof/trust, complaint/support, and retention/advocacy stages. Treat user-provided channel plans as hypotheses until local evidence supports them.

Schema:

```json
{
  "segment": "",
  "discovery_channels": [],
  "comparison_channels": [],
  "purchase_channels": [],
  "complaint_channels": [],
  "trusted_touchpoints": [],
  "influencer_types": [],
  "content_formats": [],
  "channel_risks": [],
  "recommended_channel_strategy": ""
}
```

---

## 15. Local Price Sensitivity Methodology

This is a full pricing module, not a simple price guess.

In S01, use `price-anchor-sensitivity-seed.md` to create the seed price context only. S01 should classify the user's target price against local anchors, price ladder risks, segment-level sensitivity, and required value proof. Final pricing strategy and willingness-to-pay research design belong to S04.

The skill must answer:

- Is the proposed price locally credible?
- Which segment can accept it?
- Which segment cannot accept it?
- Why?
- Which competitor creates the strongest price anchor?
- Does the product sit in entry, mainstream, premium, or flagship territory?
- Will subscription reduce conversion?
- Does discounting create true incremental demand or only pull demand forward?
- Does a lower price improve gross profit or only volume?

### 15.1 Local Price Corridor

Discover local price bands:

```json
{
  "entry_price_band": "",
  "mainstream_price_band": "",
  "premium_price_band": "",
  "flagship_price_band": "",
  "promo_floor": "",
  "typical_discount_range": "",
  "subscription_price_range": "",
  "our_target_price_classification": "entry | mainstream | premium | flagship | price_abnormal",
  "evidence_sources": []
}
```

### 15.2 Competitor Price Gap

```text
Price Gap % = (Our Price - Competitor Price) / Competitor Price
```

Schema:

```json
{
  "competitor": "",
  "local_price": "",
  "price_gap_pct": 0,
  "competitor_role": "direct | premium_anchor | budget_anchor | substitute | previous_generation",
  "consumer_interpretation": "cheaper | comparable | slightly_premium | too_expensive | unclear",
  "required_value_proof": []
}
```

Interpretation:

- 10-20% below mainstream competitors: value-for-money can be tested
- Price parity: differentiation must be clear
- 10-20% above: premium justification required
- More than 30% above: premium positioning only if evidence supports it

### 15.3 Local Affordability Pressure

```text
Affordability Pressure = Product Price / Monthly Disposable Income of Target Segment
```

```text
Price-to-Category Anchor = Product Price / Local Category Average Price
```

Schema:

```json
{
  "country": "",
  "target_segment": "",
  "affordability_pressure": "low | medium | high | very_high",
  "price_to_category_anchor": 0,
  "interpretation": "",
  "confidence": "high | medium | low",
  "assumptions": []
}
```

### 15.4 Perceived Value / Value-for-Money Score

```text
Value-for-Money Score =
  Feature Satisfaction
+ Design Satisfaction
+ Accuracy Trust
+ App / AI Insight Value
+ Brand Trust
+ After-Sales Trust
- Price Complaint Intensity
- Subscription Resistance
- Return Risk
```

Schema:

```json
{
  "segment": "",
  "value_for_money_score": 0,
  "positive_value_drivers": [],
  "negative_value_drivers": [],
  "price_objections": [],
  "premium_justification_factors": [],
  "evidence": []
}
```

### 15.5 Willingness-to-Pay Research

Recommended methods:

#### Van Westendorp

Questions:

1. Too cheap to trust?
2. Good deal?
3. Expensive but acceptable?
4. Too expensive to buy?

Outputs:

- Acceptable price range
- Psychological fair price
- Too-cheap risk
- Too-expensive rejection point

#### Gabor-Granger

Test purchase probability at discrete price points.

Outputs:

- Price-purchase probability curve
- Revenue-maximizing price
- Gross-profit-maximizing price
- Conversion cliff point

#### Conjoint / Discrete Choice

Estimate willingness to pay for:

- Battery life
- Material
- AI insights
- Accuracy claims
- Subscription requirement
- Warranty length
- Brand trust
- Design variants
- Bundles

### 15.6 Behavioral Price Elasticity

If historical sales data exists:

```text
Demand = f(Price, Discount, Competitor Price, Channel, Seasonality, Traffic, Promotion, Stock Status)
```

```text
Price Elasticity = % Change in Demand / % Change in Price
```

Interpretation:

- Below -1.5: high sensitivity
- -1.5 to -0.8: moderate sensitivity
- Above -0.8: low sensitivity

### 15.7 Promotion and Subscription Sensitivity

Promotion schema:

```json
{
  "segment": "",
  "discount_sensitivity": "low | medium | high",
  "recommended_discount_mechanic": "none | launch_coupon | bundle | limited_time_offer | financing | trade_in | avoid_discount",
  "risk": []
}
```

Subscription schema:

```json
{
  "segment": "",
  "subscription_tolerance": "low | medium | high",
  "acceptable_monthly_price_range": "",
  "subscription_risk": [],
  "recommended_subscription_framing": ""
}
```

### 15.8 Local Price Sensitivity Score

```text
Local Price Sensitivity Score =
  Affordability Pressure 脳 0.20
+ Competitor Price Gap Pressure 脳 0.18
+ Price Complaint Intensity 脳 0.15
+ Promotion Dependence 脳 0.12
+ Subscription Resistance 脳 0.12
+ Low Differentiation Risk 脳 0.10
+ Trust Deficit 脳 0.08
+ Elasticity Evidence 脳 0.05
```

Interpretation:

```text
0-30: low price sensitivity
31-55: medium price sensitivity
56-75: high price sensitivity
76-100: very high price sensitivity
```

---

## 16. Bain-Style NPS and Earned Growth Dashboard

The skill generates a Bain-style NPS and growth analysis. If direct NPS survey data is unavailable, it creates a clearly labeled **NPS proxy** from reviews and consumer voice.

Use `nss-nps-earned-growth-seed.md` for S01. S01 should build a surveyed/proxy status panel, source mix, proxy confidence, competitor comparison seed, driver tornado seed, journey episode NSS seed, earned growth proxy seed, Net Promoter System loop candidates, hardware experience diagnosis, and next-generation marketing/sales recommendation seeds. It must not present proxy NSS/NPS or earned growth seed as direct survey or attribution proof.

### 16.1 NPS Evidence Priority

1. Direct NPS survey data
2. Previous-generation NPS survey data
3. Internal reviews and open-text feedback
4. Customer service and return reasons
5. App store reviews
6. E-commerce reviews
7. Public social, forum, and video comments
8. Competitor reviews and discussions
9. Inferred NPS proxy from sentiment and recommendation language

### 16.2 NPS Classification

Survey:

- Promoters: 9-10
- Passives: 7-8
- Detractors: 0-6

Proxy classification uses:

- Explicit recommendation language
- Repurchase intent
- Referral language
- Star rating
- Sentiment intensity
- Complaint severity
- Return or refund intent
- Switching intent
- Competitor comparison

### 16.3 NPS Formula

```text
NPS = % Promoters - % Detractors
```

Schema:

```json
{
  "product": "",
  "sample_size": 0,
  "promoters_count": 0,
  "passives_count": 0,
  "detractors_count": 0,
  "promoters_pct": 0,
  "passives_pct": 0,
  "detractors_pct": 0,
  "nps": 0,
  "nps_type": "surveyed | proxy | blended",
  "confidence": "high | medium | low",
  "evidence_sources": []
}
```

### 16.4 Required NPS Charts

#### A. NPS Composition

Stacked bar chart:

- Promoters
- Passives
- Detractors
- Absolute count
- Percentage
- NPS score
- Main product vs competitors

#### B. Industry Benchmark

Horizontal bar chart:

- Main product
- Competitors
- Substitutes where relevant
- Industry average line: `IND. AVG`
- Benchmark type: `published | estimated | unavailable`

#### C. Earned Growth Rate

Stacked column chart:

- Earned Growth: repeat purchase, referral, organic, direct, community, word-of-mouth
- Bought Growth: paid ads, discounts, influencer spend, subsidies, affiliates
- Unclassified Growth

Proxy:

```text
Earned Growth Proxy =
  repeat purchase revenue
+ referral-attributed revenue
+ organic search / direct / unpaid social revenue
+ community or word-of-mouth attributed revenue
+ retained customer expansion revenue
```

```text
Bought Growth Proxy =
  paid search revenue
+ paid social revenue
+ affiliate revenue
+ influencer-paid campaign revenue
+ discount-driven campaign revenue
+ marketplace promotion-driven revenue
```

#### D. NPS Driver Tornado

Driver impact formula:

```text
Driver Impact Score =
  frequency 脳 sentiment_intensity 脳 nps_class_weight 脳 business_severity
```

Drivers:

- Design
- Comfort
- Battery
- Accuracy
- App usability
- AI insight usefulness
- Setup
- Price / value
- Subscription
- Delivery
- Packaging
- Customer service
- Returns / warranty
- Privacy / trust
- Brand credibility

#### E. Journey Episode Mapping

Lifecycle episodes:

1. Discovery
2. Consideration
3. Purchase
4. Delivery
5. Unboxing
6. Setup / pairing
7. First use
8. First 7 days
9. Habit formation
10. App experience
11. Customer service
12. Return / warranty
13. Repurchase / referral

#### F. Net Promoter System Diagrams

Inner loop:

```text
Customer feedback
  鈫?Classify promoter / passive / detractor
  鈫?Route detractor issue to owner
  鈫?Frontline follow-up or service recovery
  鈫?Issue resolution
  鈫?Close the loop with customer
  鈫?Update driver database and product backlog
```

Outer loop:

```text
Aggregated NPS feedback
  鈫?Driver analysis
  鈫?Root-cause diagnosis
  鈫?Product / service / pricing / channel decision
  鈫?Experiment or operating change
  鈫?Measure NPS and earned growth impact
  鈫?Update GTM memory and next launch plan
```

#### G. Hardware Product and Next-Generation Action Linkage

For hardware products, NPS and Earned Growth must produce action seeds, not only charts:

- Product diagnosis: map detractor/promoter drivers to hardware design, performance, battery, connectivity, setup, durability, warranty, price-value, channel, and service categories.
- Next-generation product implication: identify what to fix, amplify, prove, monitor, or research in the next generation.
- Marketing implication: identify which promoter drivers can become claims, which claims need proof assets, and which claims should not be used.
- Sales implication: identify retailer/marketplace objection handling, sales talk tracks, channel training needs, and warranty/service confidence gaps.
- Measurement implication: define which NSS/NPS, return, referral, repeat, organic, or support signals are needed to validate the action.

### 16.5 NPS Data Quality Rules

Report:

- Sample size
- Source mix
- Surveyed vs inferred percentage
- Country coverage
- Time period
- Competitor coverage
- Bias risks
- Confidence level

Never present inferred proxy NPS as surveyed NPS.

---

## 17. GTM Priority Recommendation

For each segment:

```json
{
  "segment_name": "",
  "positioning_angle": "",
  "first_screen_message": "",
  "proof_required": [],
  "best_channels": [],
  "best_content_formats": [],
  "best_influencer_types": [],
  "pricing_implication": "",
  "promotion_implication": "",
  "nps_risk": "",
  "earned_growth_opportunity": "",
  "risks": [],
  "validation_tests": []
}
```

The final GTM recommendation must answer:

- Who to target first
- Who to avoid initially
- What to say
- What not to say
- Where to sell
- Where to advertise
- Which proof is required
- What price strategy to test
- Which experience drivers require fixing
- Which NPS loops to implement

---

## 18. Final Report Structure

```md
# Consumer Market Map: [Product] in [Country]

## 1. Executive Summary

## 2. Product Capability Summary

## 3. Data Sources and MCP Collection Log

## 4. Local Competitor and Substitute Map

## 5. Local Consumer Opinion Map

## 6. TAM / SAM / SOM Summary

## 7. Segment Priority Table

## 8. Persona Cards

## 9. Channel and Touchpoint Map

## 10. Local Price Sensitivity Analysis

## 11. Bain-Style NPS and Earned Growth Dashboard

### 11.1 NPS Composition

### 11.2 Industry Benchmark

### 11.3 Earned Growth Rate

### 11.4 NPS Driver Tornado

### 11.5 Journey Episode Mapping

### 11.6 Net Promoter System: Inner and Outer Loop

## 12. GTM Priority Recommendation

## 13. Evidence, Assumptions, and Data Gaps

## 14. Recommended Next Skills
```

---

## 19. Human Review Points

Human review is required for:

1. TAM assumptions
2. Segment scoring weights
3. Competitor and substitute list
4. Price sensitivity assumptions
5. Industry benchmark assumptions
6. NPS proxy methodology
7. Earned Growth attribution assumptions
8. Health, safety, child, elderly, or medical-adjacent claims
9. Third-party scraping or MCP data policy
10. Use of consumer quotes in public-facing materials

---

## 20. Guardrails

- Do not assume the target user before evidence analysis.
- Do not require the user to predefine competitors or personas.
- Do not over-index on demographics.
- Do not treat social popularity as purchase intent.
- Do not make unsupported health or medical claims.
- Do not collect private personal data.
- Do not violate platform terms or local data regulations.
- Do not present TAM as precise if assumptions are weak.
- Do not present inferred NPS proxy as surveyed NPS.
- Do not fabricate evidence when MCP, search, browsing, or crawling fails.
- Do not use NPS as vanity score only; connect it to root causes and operating action.

---

## 21. Minimal Viable Version

If evidence is limited, still output:

1. Product capability map
2. Competitor and substitute map
3. TAM assumption tree
4. 3-5 likely consumer segments
5. Priority ranking
6. Pain points and purchase triggers
7. Channel and touchpoint hypotheses
8. Price sensitivity hypotheses
9. NPS proxy if enough consumer voice exists
10. Data gaps and next validation tests

---

## 22. Quantification and Handoff Strengthening Modules

These modules are additions to the original methodology. They do not replace or remove any required step. Their purpose is to make the process measurable, auditable, and usable by downstream GTM skills without reopening the full artifact.

### 22.1 Product-Market Search Preflight

Merge product capability normalization with category selling point and local search language mapping. This is the S01 preflight module before broad evidence discovery.

This module compares:

- Product capabilities, differentiators, commodity features, risky claims, and likely substitutes
- Product features and claimed strengths
- Mainstream selling points for the product category
- Local-language search terms and related queries
- Competitor benefit language
- Complaint language
- Rising or niche trend signals

The goal is to understand whether the product's proposed selling points connect to the way local consumers already search, compare, complain, and make sense of the category.

Google Trends-style data may support this step by comparing relative search interest, related topics, related queries, and regional interest. Treat this data as directional search interest only, not as exact market size or purchase intent.

Use the detailed schema and scoring formula in `module-additions.md` and `scoring-rubrics.md`.

### 22.1A Local Market Localization Preflight

Add this module after Product-Market Search Preflight and before Evidence Research Design.

This module prevents hard-coded assumptions about the target country. It discovers local market context before deciding where and how to collect evidence.

It should identify:

- Local languages and scripts to use in search
- Search engine and SERP behavior relevant to the country
- Marketplace, retailer, price comparison, expert review, forum, community, social, and video source candidates
- Price display norms, currency, VAT/sales tax visibility, shipping, bundles, installment payment, financing, and discount norms
- Return, warranty, after-sales, and trust expectations
- Local seasonality, shopping moments, and promotion calendar signals
- Claim, compliance, certification, privacy, and safety context when relevant
- Category naming variants, competitor local names, transliterations, and common complaint language

Use `localization-preflight.md` for the exact contract. Keep the preflight light in `quick` mode and expand only in `standard` or `deep`.

### 22.2 Coverage Map

Add a coverage map immediately after local evidence discovery.

The coverage map records:

- Local languages used
- Evidence categories searched
- Queries or sources checked
- Sources found
- Sources unavailable
- Coverage score
- Priority gaps

This prevents shallow research from appearing complete.

Use the detailed schema and scoring formula in `module-additions.md` and `scoring-rubrics.md`.

### 22.2A Evidence Research Design

Before broad evidence collection, create an evidence research design.

This design upgrades the original MCP-driven discovery step into a transparent research plan:

- Generate research perspectives before searching.
- Translate each perspective into evidence needs.
- Expand queries across local language, competitor, complaint, price, review, and comparison terms.
- Route each evidence need to the least invasive connector slot.
- Define source screening criteria before reading results.
- Define extraction schemas before scraping or summarizing.
- Fuse and rerank results across query variants.
- Iterate retrieval when new competitors, terms, or gaps appear.
- Record a PRISMA-style search and screening log.
- Stop only when coverage rules are satisfied or data gaps are explicit.

Use `evidence-research-design.md` for the exact contract.

### 22.2B Evidence Storage and Collection Logs

After the evidence research design and before synthesis, store collected evidence as structured local records.

Do not treat web search output as analysis by itself. Each source should become one or more evidence records with source type, URL or file path, collection time, connector used, confidence, limitations, and supported claim.

Use `evidence-storage-policy.md` for source categories, project run directory layout, JSONL file names, private evidence separation, PII rules, raw HTML restrictions, failed source logging, and handoff evidence references.

### 22.2C Evidence Collection Runner

After Evidence Research Design, run collection jobs through approved tools and convert gathered material into evidence records.

This runner is an execution layer, not a synthesis layer. It should not write market conclusions. It should:

- Execute collection jobs selected by depth mode and evidence needs.
- Use approved connector slots and least-invasive collection paths.
- Convert gathered material into structured evidence records.
- Write collection jobs, failed sources, and limitations.
- Produce compressed collection summary and RAG index manifest when needed.
- Declare whether evidence is ready for Coverage Map.

Use `evidence-collection-runner.md` for the exact job types and contracts.

### 22.2C1 Local Voice Source and Site-Specific Comment Collection

For each country, do not assume the relevant consumer voice source in advance. Discover the local voice landscape first: specialist forums, specialist media comments, deal forums, marketplace reviews, price comparison reviews, video comments, app reviews, public social threads, Q&A pages, and brand/support communities.

When a high-value local source is found, create a site-specific collection profile before using it heavily. The profile should define access status, permitted collection mode, pagination pattern, thread discovery logic, comment extraction schema, PII policy, export policy, and completeness audit.

This module should answer:

- Which local forums, communities, and comment sources matter in this country?
- Which products, competitors, substitutes, or previous generations do they discuss?
- How much of the accessible thread/comment range was actually collected?
- Which pages, comment IDs, or floor ranges are missing or blocked?
- Which comments became voice atoms, NSS/NPS proxy inputs, and Bain driver inputs?
- What usage limits prevent full-text storage, public quoting, or downstream handoff?

Never claim that all comments were collected unless the bounded source coverage report proves it. Use `site-specific-comment-collection.md` for the exact contracts.

### 22.2D Coverage and Source Quality

After evidence collection, evaluate coverage and source quality before analysis.

This step answers:

- Which evidence categories are strong, adequate, thin, or missing?
- Which sources can be used as primary evidence, secondary evidence, context only, or should be avoided?
- Which conclusions must be capped at medium or low confidence because evidence is thin?
- Should the runner loop back to collect more evidence, or should the gap be made explicit?

Use `coverage-and-source-quality.md` for the exact scoring rules, confidence caps, and HTML heatmap contract.

### 22.2E Competitor and Substitute Mapping

After coverage and source quality are checked, build the competitor and substitute map.

This step should not be a simple list. It must classify:

- Direct competitors
- Substitutes
- Premium anchors
- Budget anchors
- Ecosystem anchors
- Previous-generation or older-model anchors
- Non-consumption or doing-nothing alternatives

Competitor roles are not mutually exclusive. One competitor may be both direct and premium anchor, or substitute and ecosystem anchor.

The map should include a 5-10 item candidate review list when review mode allows it, detailed competitor/substitute records, competitor role arrays, substitute taxonomy, price ladder scan, jump decision risks, segment-level threats, evidence requirements, and top competitor ranking.

Use `competitor-substitute-mapping.md` for the exact contract.

### 22.3 Voice Atom Table

Add a voice atom table after the consumer opinion map.

The voice atom table turns reviews, comments, NSS/NPS notes, survey text, and internal customer voice into atomic records that downstream JTBD and messaging skills can reuse. Before the table is used for segmentation, NSS/NPS proxy, or Bain-style dashboards, run the consumer voice processing pipeline.

Each atom should preserve:

- Original local-language wording
- Translation when needed
- Source reference
- Theme
- Pain point
- Purchase trigger
- Objection
- Sentiment
- Emotion strength
- Purchase stage

This keeps downstream skills grounded in consumer language rather than summaries.

Use `consumer-voice-nss-bain-pipeline.md` to define source-item records, voice atom extraction, deduplication, theme clusters, NSS/NPS proxy classification, Bain driver inputs, and journey episode inputs.

Important rule: NSS/NPS proxy classification is source-item-level, not atom-count-level. A single long review may create multiple atoms but should not inflate the proxy sample size.

### 22.4 Competitor Threat Score

Add competitor threat scoring after the competitor and substitute map.

The score identifies which competitors matter most as price anchors, trust anchors, positioning threats, channel threats, or feature-overlap threats.

The score should consider:

- Positioning overlap
- Price anchor strength
- Channel presence
- Review strength
- Brand trust
- Feature overlap
- Switching barrier

This converts a long competitor list into a prioritized competitive context.

Before finalizing the competitor map in standard or deep mode, present 5-10 potential competitors or substitutes for user calibration when review mode allows it. The user may include, exclude, or add notes. A top competitor should have at least two local evidence signals unless clearly marked as a hypothesis.

### 22.5 Segment Distinctness Check

Add a distinctness check after segmentation.

The check asks whether each segment is meaningfully different in:

- Motivation
- Use case
- Price behavior
- Channel behavior
- Objections or trust barriers

Segments with weak distinctness should be merged, split, or deprioritized. This prevents vague or overlapping personas from contaminating downstream message and channel strategy.

### 22.6 Handoff Pack

Add a compressed handoff pack at the end of S01.

The handoff pack is the default downstream input. Downstream skills should not reopen the full S01 artifact unless a required field is missing, contradicted, or too weakly evidenced.

The S01 handoff should serve:

- S02 `mine-jtbd-scenarios`
- S04 `model-price-sensitivity`
- S08 `forecast-launch-demand`
- S14 `compose-html-gtm-dashboard`

Use `output-contract.md` for the exact schema.

