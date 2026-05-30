# S06 Upstream Input Map

Use this before deciding whether S06 can score candidates or should produce archetypes and sourcing criteria.

## Minimum Proceed Gate

S06 can produce archetype-level output when these groups exist:

```text
message_and_segment_system
  segment_message_architecture, segment refs, JTBD/scenario refs

proof_needs
  proof_requirement_seed, feature_benefit_proof_matrix, claim_risk_and_proof_gate if available

channel_context
  channel_fit_scores, segment_channel_touchpoint_map, local platform/source context, or user target platforms

local_discovery_context
  feature_to_local_language_map, local_source_map, local_voice_source_map, competitor_candidate_review_list, competitor_threat_scores when available
```

S06 can produce candidate-level scoring only when:

```text
creator_candidates
  Candidate names/handles/links/descriptions, platform, content category, or user-provided shortlist.

creator_candidate_review_decisions
  User decisions from a prior review gate. Use to include, exclude, hold as unsure, or request more evidence for candidates before final scoring.
```

S06 can produce budget and outcome estimates when:

```text
budget_or_rate_basis
  User budget range, candidate rate cards, media kits, historical campaign data, or local benchmark/proxy evidence.

measurement_context
  Campaign goal, target platform, trackable link/landing page context, or clear metric priority such as views, likes, comments, saves, or visits.
```

If budget or outcome evidence is missing, still produce archetype/candidate recommendations but mark budget and expected metrics as `hypothesis_only` with explicit gaps.

If candidates are missing, do not invent creator names. Produce:

```text
creator_input_coverage_gate
creator_archetype_fit_scorecard
creator_sourcing_criteria
creator_candidate_request_list
public_creator_discovery_plan
html_section_draft with data gap `missing_creator_candidates`
```

If candidates exist but review decisions are missing, produce:

```text
creator_candidate_review_gate
creator_candidate_review_list
creator_candidate_decision_log with `not_reviewed`
candidate-level scores marked `provisional_pending_user_review`
data gap `pending_creator_candidate_review`
```

## High-Value Inputs

```text
creator_brief_message_seed
  Use as the copy/message boundary for creator content.

local_language_message_seed
  Use to preserve local category wording and avoid awkward creator scripts.

feature_to_local_language_map, local_source_map, and local_voice_source_map
  Use to build local discovery queries and identify country-specific platforms, forums, specialist media, retailer sources, and social channels.

competitor_candidate_review_list and competitor_threat_scores
  Use to find creators or expert sources who already review, compare, rank, or discuss top competitor and substitute products.

behavioral_science_lever_map
  Use to map authority, social proof, risk reversal, scarcity, community, or demonstration roles.

digital_shelf_and_retailer_decision_map
  Use when creator proof should support PDP, retailer, review, Q&A, delivery, warranty, or trust conversion.

copy_quality_scorecard and copy_test_backlog
  Use only if S05 ran; S06 should not require S05.

brand_guidelines and sponsorship_disclosure_policy
  Use to detect tone, disclosure, and brand-safety constraints.

creator_budget_range, creator_rate_cards_or_media_kits, and historical_creator_performance_data
  Use to estimate marketing budget ranges and expected outcome ranges. Treat private inputs as restricted.

tracking_or_landing_page_context
  Use only to estimate visits/clicks or conversion-adjacent outcomes. Without this, cap visit confidence at low.
```

## Missing Input Handling

```text
missing_creator_candidates
  Produce archetypes, sourcing criteria, and request list, not fake candidate scoring.

missing_channel_context
  Can score proof role but cap platform relevance confidence at low.

missing_proof_gate
  Can score audience fit but cap trust/proof confidence at low.

missing_local_language
  Can score generic fit but cap localization confidence at low.

missing_local_creator_source_map
  Can create generic discovery criteria but cap public discovery confidence at low.

low_discovery_coverage
  Keep candidate names in longlist or request list until enough accessible evidence is found.

private_creator_list_restricted
  Do not expose names, handles, rates, contacts, or raw performance data in public HTML.

missing_budget_basis
  Produce ranges only as hypotheses or ask for budget/rate/history inputs.

missing_expected_metric_basis
  Produce expected metric ranges only as hypotheses and avoid conversion/sales estimates.

pending_creator_candidate_review
  Candidate scoring, budget, and outcome estimates exist but are not approved for recommendation use.

creator_candidate_review_decisions_missing
  Ask the user to mark include, exclude, unsure, or request_more_evidence.
```
