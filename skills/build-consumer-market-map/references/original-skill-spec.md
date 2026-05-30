---
name: build-consumer-market-map
description: Builds a localized consumer market map for a 2C hardware product from product specifications, target country/region, and approximate price range. The skill autonomously discovers competitors, substitutes, local reviews, local consumer discussions, prices, channels, touchpoints, and category evidence through approved search, browsing, MCP connectors, APIs, or compliant crawling. It outputs TAM/SAM/SOM, consumer segments, personas, local opinions, pain points, channel and media touchpoints, price sensitivity, Bain-style NPS comparison, earned growth analysis, and GTM priorities.
---

# Build Consumer Market Map

## Purpose

Use this skill when a user wants a localized GTM market map for a 2C hardware product.

The user provides:

- Product category
- Product name or codename
- Product specification or feature list
- Target country or region
- Target price range

The skill must infer:

- Local competitor and substitute universe
- Local consumer opinions and pain points
- TAM / SAM / SOM
- Consumer segments and personas
- Local channel and media touchpoints
- Price sensitivity by country and segment
- NPS composition and competitive comparison
- Earned Growth vs Bought Growth view
- GTM priority recommendation

Do not ask the user to predefine the target customer, local competitors, local forums, or local pain points.

---

## Required Inputs

Ask only for missing critical fields.

```json
{
  "product_category": "",
  "product_name_or_codename": "",
  "product_spec_or_feature_list": "",
  "target_country_or_region": "",
  "target_price_range": ""
}
```

Optional fields:

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

Known competitors are seed inputs only. The skill must still check for missing local competitors and substitutes.

---

## Evidence Standard

Label conclusions as:

```text
[EVIDENCE]
[STRONG INFERENCE]
[WEAK INFERENCE]
[ASSUMPTION]
```

Preserve source provenance for all evidence.

---

## Workflow

```text
1. Normalize product capabilities
2. Load MCP connector configuration
3. Discover local competitors, substitutes, sources, prices, reviews, discussions
4. Score source quality
5. Build competitor and substitute map
6. Build local consumer opinion map
7. Estimate TAM / SAM / SOM
8. Build consumer segments
9. Build persona cards
10. Map channels and touchpoints
11. Analyze local price sensitivity
12. Generate Bain-style NPS and Earned Growth dashboard
13. Recommend GTM priorities
14. Report evidence, assumptions, and data gaps
```

---

## Step 1 — Normalize Product Capabilities

Convert product specs into:

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

Classify each feature as:

- Category entry feature
- Competitive feature
- Differentiating feature
- Premium justification feature
- Trust-building feature
- Retention / subscription feature
- Risky or hard-to-prove claim
- Commodity feature

Rule: do not treat every feature as a selling point.

---

## Step 2 — MCP-Driven Local Evidence Discovery

Read `MCP_CONNECTORS.md`.

Autonomously discover, where permitted:

- Direct competitors
- Substitutes
- Bestsellers
- Marketplace prices
- Retailer prices
- Product reviews
- Consumer discussions
- Social content and comments
- Video reviews and comments
- App store reviews
- Price comparison data
- Deal forum discussions
- Expert reviews
- Channel availability
- Creator / influencer ecosystem signals

Generate local-language queries using:

- Product category
- Product features
- Use cases
- Target price band
- Known/discovered competitors
- Complaint terms
- Buying-intent terms
- Substitute terms

If MCP, crawling, browsing, or search fails, log the limitation and use fallback sources. Do not fabricate data.

---

## Step 3 — Source Ranking

Score sources with:

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

Evidence priority:

1. Internal data
2. Direct surveys / NPS
3. Verified buyer reviews
4. Marketplace and retailer reviews
5. App store reviews
6. Local forums
7. Expert reviews
8. Social comments
9. Search snippets

---

## Step 4 — Competitor and Substitute Map

Output:

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

Include both direct competitors and substitutes.

---

## Step 5 — Local Consumer Opinion Map

Extract:

- Purchase reasons
- Pain points
- Product complaints
- Positive drivers
- Negative drivers
- Price complaints
- Subscription complaints
- Comfort / usability issues
- Feature confusion
- Competitor comparisons
- Substitute products
- Influencer mentions
- Channel mentions
- Purchase triggers
- Return reasons
- FAQs

Schema:

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

Preserve local-language wording.

---

## Step 6 — TAM / SAM / SOM

Definitions:

- TAM: total addressable consumer pool for category or need
- SAM: reachable consumers for product type and price band
- SOM: realistic obtainable market for launch period

Formula:

```text
TAM = target population × relevant demographic or need filter × category need incidence
SAM = TAM × price-band affordability × product-type acceptance × channel reach
SOM = SAM × awareness × conversion × launch capacity
```

Output:

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

## Step 7 — Consumer Segmentation

Build segments from motivation, use case, willingness to pay, and behavior.

Segment schema:

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

Priority score:

```text
Segment Priority Score =
  Pain Intensity × 0.18
+ Product Fit × 0.18
+ Willingness to Pay × 0.14
+ Reachability × 0.12
+ Local Market Size × 0.12
+ Competitor Gap × 0.10
+ Content Virality × 0.08
+ Retention / Subscription Potential × 0.08
- Trust Barrier × 0.10
- Return / Support Risk × 0.05
```

Output ranking:

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

---

## Step 8 — Persona Cards

For each high-priority segment:

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

---

## Step 9 — Channel and Touchpoint Map

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

## Step 10 — Local Price Sensitivity

### Price Corridor

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

### Competitor Price Gap

```text
Price Gap % = (Our Price - Competitor Price) / Competitor Price
```

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

### Affordability

```text
Affordability Pressure = Product Price / Monthly Disposable Income of Target Segment
Price-to-Category Anchor = Product Price / Local Category Average Price
```

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

### Value-for-Money

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

### Willingness-to-Pay Methods

Recommend tests when possible:

- Van Westendorp
- Gabor-Granger
- Conjoint / Discrete Choice

### Behavioral Price Elasticity

If historical data exists:

```text
Demand = f(Price, Discount, Competitor Price, Channel, Seasonality, Traffic, Promotion, Stock Status)
Price Elasticity = % Change in Demand / % Change in Price
```

Interpretation:

- Below -1.5: high sensitivity
- -1.5 to -0.8: moderate sensitivity
- Above -0.8: low sensitivity

### Promotion and Subscription

Promotion:

```json
{
  "segment": "",
  "discount_sensitivity": "low | medium | high",
  "recommended_discount_mechanic": "none | launch_coupon | bundle | limited_time_offer | financing | trade_in | avoid_discount",
  "risk": []
}
```

Subscription:

```json
{
  "segment": "",
  "subscription_tolerance": "low | medium | high",
  "acceptable_monthly_price_range": "",
  "subscription_risk": [],
  "recommended_subscription_framing": ""
}
```

### Local Price Sensitivity Score

```text
Local Price Sensitivity Score =
  Affordability Pressure × 0.20
+ Competitor Price Gap Pressure × 0.18
+ Price Complaint Intensity × 0.15
+ Promotion Dependence × 0.12
+ Subscription Resistance × 0.12
+ Low Differentiation Risk × 0.10
+ Trust Deficit × 0.08
+ Elasticity Evidence × 0.05
```

```json
{
  "country": "",
  "category": "",
  "target_price_range": "",
  "overall_price_sensitivity": {
    "score": 0,
    "level": "low | medium | high | very_high",
    "reasons": []
  },
  "segment_price_sensitivity": [
    {
      "segment": "",
      "score": 0,
      "level": "low | medium | high | very_high",
      "estimated_wtp_range": "",
      "subscription_tolerance": "low | medium | high",
      "pricing_advice": ""
    }
  ],
  "recommended_tests": []
}
```

---

## Step 11 — Bain-Style NPS and Earned Growth

### NPS Evidence Sources

Priority:

1. Direct NPS survey data
2. Previous-generation NPS
3. Internal reviews and open-text feedback
4. Customer service and return reasons
5. App store reviews
6. E-commerce reviews
7. Public social, forum, and video comments
8. Competitor reviews and discussions
9. Inferred NPS proxy

If direct NPS does not exist, create an NPS proxy and label it clearly.

### NPS Classification

Survey:

- Promoters: 9–10
- Passives: 7–8
- Detractors: 0–6

Proxy uses:

- Recommendation language
- Repurchase intent
- Referral language
- Star rating
- Sentiment intensity
- Complaint severity
- Return or refund intent
- Switching intent
- Competitor comparison

### NPS Formula

```text
NPS = % Promoters - % Detractors
```

Product-level schema:

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

### Required Charts

#### 1. NPS Composition

Stacked bar:

```json
{
  "chart_name": "NPS Composition",
  "chart_type": "stacked_bar",
  "items": [
    {
      "product": "",
      "promoters_count": 0,
      "passives_count": 0,
      "detractors_count": 0,
      "promoters_pct": 0,
      "passives_pct": 0,
      "detractors_pct": 0,
      "nps": 0,
      "nps_type": "surveyed | proxy | blended"
    }
  ]
}
```

#### 2. Industry Benchmark

Horizontal bar with industry average:

```json
{
  "chart_name": "Industry Benchmark",
  "chart_type": "horizontal_bar_with_average_line",
  "industry_average_nps": 0,
  "industry_average_type": "published | estimated | unavailable",
  "items": [
    {
      "product": "",
      "nps": 0,
      "rank": 0,
      "delta_vs_industry_average": 0,
      "nps_type": "surveyed | proxy | blended"
    }
  ]
}
```

#### 3. Earned Growth Rate

```json
{
  "chart_name": "Earned Growth Rate",
  "chart_type": "stacked_column",
  "items": [
    {
      "product_or_period": "",
      "total_growth": 0,
      "earned_growth": 0,
      "bought_growth": 0,
      "unclassified_growth": 0,
      "earned_growth_rate": 0,
      "confidence": "high | medium | low",
      "assumptions": []
    }
  ]
}
```

#### 4. NPS Driver Tornado

```text
Driver Impact Score =
  frequency × sentiment_intensity × nps_class_weight × business_severity
```

```json
{
  "chart_name": "NPS Driver Tornado",
  "chart_type": "tornado",
  "items": [
    {
      "driver": "",
      "impact_score": 0,
      "direction": "positive | negative",
      "evidence_count": 0,
      "example_evidence": [],
      "recommended_action": ""
    }
  ]
}
```

#### 5. Journey Episode Mapping

Episodes:

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

```json
{
  "chart_name": "Journey Episode Mapping",
  "chart_type": "multi_line_journey_curve",
  "episodes": [
    {
      "episode": "",
      "main_product_nps_proxy": 0,
      "competitor_nps_proxy": 0,
      "delta": 0,
      "main_positive_drivers": [],
      "main_negative_drivers": [],
      "recommended_action": ""
    }
  ]
}
```

#### 6. Net Promoter System Diagrams

Inner loop:

```text
Customer feedback
  ↓
Classify promoter / passive / detractor
  ↓
Route detractor issue to owner
  ↓
Frontline follow-up or service recovery
  ↓
Issue resolution
  ↓
Close the loop with customer
  ↓
Update driver database and product backlog
```

Outer loop:

```text
Aggregated NPS feedback
  ↓
Driver analysis
  ↓
Root-cause diagnosis
  ↓
Product / service / pricing / channel decision
  ↓
Experiment or operating change
  ↓
Measure NPS and earned growth impact
  ↓
Update GTM memory and next launch plan
```

---

## Step 12 — GTM Recommendation

Output for each segment:

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

Final recommendation must include:

- Primary launch segment
- Secondary segment
- Segments to avoid
- Recommended positioning
- Recommended channels
- Price strategy
- Proof requirements
- NPS risk
- Earned Growth opportunity
- Next validation tests

---

## Final Report Format

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

## Human Review Points

Require human review for:

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

## Guardrails

- Do not assume the target user before analyzing product and market evidence.
- Do not require the user to predefine competitors, forums, local pain points, or personas.
- Do not over-index on demographics when motivation and use case are more important.
- Do not treat social media popularity as purchase intent without validation.
- Do not infer medical claims unless backed by valid certification and evidence.
- Do not collect private personal data.
- Do not violate platform access rules or local data regulations.
- Do not present TAM as precise when assumptions are weak.
- Do not present inferred NPS proxy as surveyed NPS.
- Do not mix NPS sources without labeling source type and confidence.
- Do not present Earned Growth as precise financial result unless attribution data exists.
- Do not fabricate evidence when MCP, crawling, search, or browsing fails.

---

## Minimal Viable Version

If data is limited, still output:

1. Product capability map
2. Competitor and substitute map
3. TAM assumption tree
4. 3–5 likely consumer segments
5. Segment priority ranking
6. Pain points and purchase triggers
7. Channel and touchpoint hypotheses
8. Price sensitivity hypotheses
9. NPS proxy if enough consumer voice exists
10. Data gaps and next validation tests
