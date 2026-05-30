# Creator Fit Methods

Use these methods after input coverage and before scoring.

## Creator Role Definition

Define the creator or expert role before scoring:

```text
awareness_reach
  Introduce the category/product to the right audience.

proof_demonstration
  Demonstrate product performance, setup, durability, compatibility, or use-case proof.

expert_authority
  Provide credibility through specialist knowledge, lab testing, review, or comparison.

community_validation
  Reduce risk through peer/community language, local norms, or owner experience.

comparison_shopper_support
  Help consumers compare alternatives, price/value, specs, and trade-offs.

retail_or_pdp_support
  Create proof that can support PDP, retailer page, Q&A, sales cards, or offline staff.

conversion_or_affiliate
  Drive trackable sales or traffic while respecting attribution and disclosure limits.
```

## Archetype Before Candidate

Always score creator archetypes before specific candidates:

```text
segment -> JTBD scenario -> proof requirement -> trust barrier -> creator role -> platform -> content task
```

Candidate scoring should inherit the archetype role. Do not rate a candidate highly because they are famous if the role mismatch is large.

## Local Creator Discovery Funnel

Use this when candidates are missing, weak, or need local validation.

```text
segment/JTBD -> proof need -> local language terms -> local source strata -> candidate longlist -> evidence coverage -> shortlist for user review
```

Build discovery around category authority and proof fit, not follower count.

## Local Query Bank

Generate queries from five buckets:

```text
category_terms
  Local category names, synonyms, buyer language, and search terms from S01/S03.

proof_terms
  Review, test, unboxing, comparison, setup, durability, accuracy, battery, value, warranty, or local equivalents.

competitor_terms
  Top competitors, substitutes, premium anchors, budget anchors, previous-generation products, and model names from S01.

scenario_terms
  JTBD situations, objections, pain points, and local trigger phrases from S02/S03.

source_terms
  Local platform, forum, specialist media, retailer, affiliate, deal, coupon, or community names from S01.
```

For each query, store:

```json
{
  "query_id": "",
  "query_text": "",
  "language": "",
  "country_or_region": "",
  "intent": "category_authority | competitor_overlap | proof_demo | community_voice | affiliate_deal | retailer_support | risk_check",
  "source_target": "search | youtube | tiktok | instagram | specialist_media | forum | retailer | affiliate | other",
  "upstream_refs": [],
  "expected_candidate_type": ""
}
```

## Source Strata

Search or request evidence by strata:

```text
video_and_social
  Public YouTube, TikTok, Instagram, Shorts/Reels, or local equivalents where accessible.

specialist_review_media
  Local tech/category reviewers, lab testers, expert sites, newsletters, and review publications.

forums_and_communities
  Local forums, Reddit-like communities, enthusiast boards, Facebook groups when accessible, and comment sources from S01.

retail_and_pdp_support
  Retailer Q&A, editorial buying guides, PDP videos, marketplace creator programs, and staff/expert content.

affiliate_and_deal_sources
  Affiliate publishers, coupon/deal creators, comparison sites, and price-watch communities.

competitor_overlap_sources
  Public content around competitor products, previous-generation products, substitutes, and category anchors.
```

Respect access limits. If a platform cannot be accessed or cannot be searched reliably, record the source as blocked or partial.

## Candidate Longlist

A longlist candidate can be a creator, reviewer, expert, publication author, forum authority, affiliate publisher, or retailer expert. Use:

```json
{
  "candidate_id": "",
  "name_or_handle": "",
  "candidate_type": "creator | reviewer | expert_media | forum_authority | affiliate_publisher | retailer_expert | community_admin | other",
  "platforms": [],
  "country_or_language_signal": "",
  "discovery_source": "",
  "matched_queries": [],
  "category_content_refs": [],
  "competitor_content_refs": [],
  "recent_activity_signal": "",
  "public_metric_proxies": {},
  "discovery_priority_score": 0,
  "evidence_coverage_score": 0,
  "promotion_status": "promote_to_scoring | keep_longlist | exclude | needs_user_review",
  "access_status": "accessible | partial | blocked | user_supplied | unknown",
  "privacy_status": "public | user_private | restricted",
  "evidence_refs": []
}
```

Minimum evidence for candidate scoring:

```text
1 public profile or author page
1-2 relevant public content samples
country/language signal
category or competitor relevance signal
recent activity or evergreen authority signal
```

If the minimum is missing, keep the item in `creator_candidate_longlist` but do not promote it to the scored shortlist.

## Candidate Review Gate

When the longlist has enough options, prepare 5-10 review candidates before final candidate scoring. This is a human correction gate, not a final selection.

Select candidates for review with this balancing rule:

```text
top discovery priority candidates
+ at least one expert/reviewer or specialist media option when available
+ at least one community/forum/owner-voice option when available
+ at least one affiliate/deal or retail-support option when conversion or price sensitivity matters
+ at least one competitor-overlap candidate when available
+ any user-supplied candidate that is not blocked by obvious safety or access issues
```

Review item schema:

```json
{
  "review_item_id": "",
  "candidate_ref": "",
  "display_name": "",
  "candidate_type": "",
  "primary_platform_or_source": "",
  "why_showing_this_option": [],
  "main_proof_role": "",
  "segment_or_scenario_fit": "",
  "known_risks_or_unknowns": [],
  "evidence_refs": [],
  "default_recommendation": "include | exclude | unsure | request_more_evidence",
  "user_decision": "include | exclude | unsure | request_more_evidence | not_reviewed",
  "user_reason": ""
}
```

Decision handling:

```text
include
  Candidate may enter formal candidate fit scoring, budget estimate, and expected outcome estimate.

exclude
  Candidate stays in the decision log and must not enter approved scoring or recommendation tables.

unsure
  Candidate can remain in longlist or test backlog, but budget/outcome estimates must be provisional.

request_more_evidence
  Candidate should get a focused evidence task before scoring.

not_reviewed
  Candidate-level outputs must be labeled `provisional_pending_user_review`.
```

If no review decisions are available, produce the gate and continue only with archetype-level recommendations or clearly provisional candidate-level analysis.

## Competitor Overlap Mapping

Competitor-overlap content is a strong discovery path for hardware because it reveals category authority. Map:

```json
{
  "candidate_ref": "",
  "competitor_or_anchor_ref": "",
  "content_ref": "",
  "overlap_type": "reviewed | compared | ranked | sponsored | affiliate | mentioned | community_discussed",
  "proof_relevance": "",
  "recency": "",
  "risk_notes": [],
  "evidence_refs": []
}
```

Use this to identify who shapes local category consideration, but do not assume a competitor reviewer is available, affordable, or safe for the brand.

## Candidate Inventory

For each candidate, use:

```json
{
  "candidate_id": "",
  "name_or_handle": "",
  "platforms": [],
  "country_or_language": "",
  "content_category": "",
  "creator_role": "",
  "audience_proxy": {},
  "content_sample_refs": [],
  "discovery_refs": [],
  "competitor_overlap_refs": [],
  "access_status": "accessible | partial | blocked | user_supplied | unknown",
  "proof_relevance_notes": [],
  "brand_safety_notes": [],
  "disclosure_or_sponsorship_notes": [],
  "privacy_status": "public | user_private | restricted",
  "evidence_refs": []
}
```

## Trust And Proof Mapping

Hardware creator fit depends on proof type:

```text
lab_or_expert_review
  Best for technical claims, performance, accuracy, durability, compatibility.

hands_on_demonstration
  Best for setup, usability, before/after experience, workflow, portability.

comparison_review
  Best for shopper evaluation, price/value, alternatives, feature tradeoffs.

community_owner_voice
  Best for trust, local fit, support, reliability, long-term use.

retail_or_specialist_media
  Best for local credibility, retailer trust, specialist category norms.

affiliate_or_deal_creator
  Best for promo conversion, price sensitivity, clickout, and offer testing.
```

## Brand Safety And Disclosure

Check:

```text
controversy or unsafe content adjacency
inconsistent category credibility
misleading claims history
undisclosed sponsorship risk
platform policy risk
child/elderly/safety/health/privacy sensitivity
competitor conflict
fake engagement or suspicious audience metrics
```

S06 can flag risk. It cannot approve a creator for use.

## Recommendation Rationale

Every recommended archetype or candidate needs a business-readable rationale:

```json
{
  "recommendation_id": "",
  "target_type": "archetype | candidate",
  "target_ref": "",
  "recommended_role": "",
  "why_recommended": [],
  "why_not_recommended": [],
  "segment_fit_reason": "",
  "proof_fit_reason": "",
  "platform_reason": "",
  "budget_reason": "",
  "expected_outcome_reason": "",
  "risk_reason": "",
  "evidence_refs": [],
  "confidence": "high | medium | low | hypothesis_only"
}
```

Use plain language. The reason should make the trade-off clear enough for a marketer to approve, reject, or request more evidence.

## Marketing Budget Estimate

Estimate marketing budget as a range, not a point number. Use the launch country currency when known; otherwise record the currency gap.

```json
{
  "target_ref": "",
  "currency": "",
  "budget_scenario": "conservative | base | upside",
  "creator_fee_range": {"min": 0, "max": 0},
  "product_seeding_cost_range": {"min": 0, "max": 0},
  "shipping_or_local_logistics_range": {"min": 0, "max": 0},
  "production_or_editing_cost_range": {"min": 0, "max": 0},
  "paid_boosting_range": {"min": 0, "max": 0},
  "agency_or_platform_fee_range": {"min": 0, "max": 0},
  "affiliate_or_commission_assumption": "",
  "tracking_or_landing_setup_cost_range": {"min": 0, "max": 0},
  "contingency_range": {"min": 0, "max": 0},
  "total_marketing_budget_range": {"min": 0, "max": 0},
  "assumptions": [],
  "evidence_refs": [],
  "confidence": "high | medium | low | hypothesis_only"
}
```

Budget is a marketing-cost estimate. It is not a final media allocation, contract approval, procurement quote, or financial forecast.

## Expected Outcome Estimate

Estimate outcomes as ranges for each budget scenario:

```json
{
  "target_ref": "",
  "budget_scenario": "conservative | base | upside",
  "expected_reach_range": {"min": 0, "max": 0},
  "expected_views_or_impressions_range": {"min": 0, "max": 0},
  "expected_likes_range": {"min": 0, "max": 0},
  "expected_comments_range": {"min": 0, "max": 0},
  "expected_shares_or_saves_range": {"min": 0, "max": 0},
  "expected_clicks_or_visits_range": {"min": 0, "max": 0},
  "expected_ctr_range": {"min": 0, "max": 0},
  "expected_engagement_rate_range": {"min": 0, "max": 0},
  "expected_conversions_or_sales_range": {"min": 0, "max": 0},
  "metric_basis": "historical_first_party | creator_public_proxy | platform_benchmark | category_proxy | hypothesis",
  "confounders": [],
  "evidence_refs": [],
  "confidence": "high | medium | low | hypothesis_only"
}
```

Only include conversion or sales ranges when tracking, attribution, channel availability, offer context, and historical or benchmark evidence are sufficient. Otherwise record a hypothesis or data gap.

## Estimate Rules

Use this order of evidence strength:

```text
1. User-provided historical campaign cost and performance
2. Candidate rate cards, media kits, or approved agency quotes
3. Public creator performance proxies from comparable recent content
4. Local platform/category benchmarks from credible sources
5. Category analogies or explicit hypotheses
```

Cap confidence at `low` when only public proxies are available. Cap confidence at `hypothesis_only` when no candidate, rate, or performance evidence exists.

## Brief Pack

Creator briefs should include:

```text
creator_role
target_segment
JTBD scenario
message angle
proof task
do_not_say
required disclosure
content format
measurement plan
review owner
```

Do not write final scripts unless the user explicitly requests final copy generation.
