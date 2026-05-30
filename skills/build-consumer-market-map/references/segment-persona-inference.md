# Segment and Persona Inference

Use this after consumer voice processing, competitor/substitute mapping, price anchor discovery, market sizing seeds, and channel/touchpoint evidence are available. It turns evidence into initial consumer segments and persona cards without asking the user to predefine the target customer.

This is an inference layer, not a final strategy layer. S01 should produce segment seeds and persona hypotheses that downstream skills can refine.

## Inputs

```json
{
  "product_capability_map": {},
  "selling_point_fit_scores": [],
  "voice_theme_clusters": [],
  "bain_driver_inputs": [],
  "journey_episode_inputs": [],
  "competitor_substitute_map": [],
  "segment_competitor_threats": [],
  "price_anchor_panel": {},
  "price_complaints": [],
  "tam_sam_som_seed": {},
  "channel_touchpoints": [],
  "localization_preflight": {},
  "coverage_summary": {},
  "confidence_caps": {}
}
```

## Core Rules

- Do not create segments from demographics alone.
- Do not create a segment unless it has a distinct motivation, use case, price behavior, channel behavior, or objection pattern.
- Do not overfit to one loud comment source; check coverage and source quality.
- Keep segments launch-usable: three to six segment seeds are usually enough for S01.
- Keep weak segments as hypotheses with explicit gaps instead of deleting them if they may matter commercially.
- Persona cards must be evidence-backed and localized, not fictional biographies.

## User-Provided Commercial Hypotheses

User-provided inputs such as planned target users, internal benchmark segments, sales beliefs, channel plans, previous-generation learnings, or executive priorities can keep a weak segment candidate alive as a commercial hypothesis.

They do not automatically make the segment high confidence.

Rules:

- Mark the source as `user_provided_commercial_hypothesis` or `internal_private`.
- Preserve the candidate when it is commercially important, strategically required, or tied to internal sales/channel data.
- Keep `candidate_confidence` based on evidence, not seniority of the input.
- Add data gaps for missing local voice, price behavior, channel behavior, or competitor/substitute evidence.
- Promote to `testing_segment` rather than `primary_launch_segment` when internal belief is strong but local market evidence is thin.
- If public evidence contradicts the user input, keep both signals and record the contradiction for review.

## Segment Candidate Generation

Generate candidates from five evidence lenses:

```text
motivation_lens
  What outcome or progress is the consumer seeking?

use_case_lens
  What situation, trigger, routine, or journey episode creates demand?

problem_driver_lens
  Which pain, objection, or detractor driver is strong enough to form a targetable group?

price_behavior_lens
  Which buyers differ by willingness to pay, subscription tolerance, promotion dependence, financing need, or trade-up/trade-down behavior?

channel_behavior_lens
  Where do consumers discover, compare, buy, complain, and trust proof?
```

Candidate schema:

```json
{
  "segment_candidate_pool": [
    {
      "candidate_id": "",
      "candidate_name": "",
      "generation_lenses": [],
      "core_motivation": "",
      "primary_use_cases": [],
      "triggering_journey_episodes": [],
      "dominant_voice_theme_refs": [],
      "bain_driver_refs": [],
      "current_substitutes": [],
      "most_relevant_product_features": [],
      "irrelevant_or_low_value_features": [],
      "primary_objections": [],
      "trust_requirements": [],
      "price_behavior_hypothesis": "",
      "channel_behavior_hypothesis": "",
      "local_language_cues": [],
      "evidence_refs": [],
      "assumption_refs": [],
      "candidate_confidence": "high | medium | low"
    }
  ]
}
```

## Segment Evidence Strength

```text
Segment Evidence Strength =
  Voice Theme Support * 0.20
+ Distinct Motivation Support * 0.15
+ Use Case or Journey Support * 0.15
+ Price Behavior Support * 0.12
+ Competitor/Substitute Support * 0.12
+ Channel Evidence Support * 0.10
+ Market Size Support * 0.08
+ Cross-Source Agreement * 0.08
```

Interpretation:

```text
80-100 = strong segment seed
60-79  = usable segment seed
40-59  = weak hypothesis; keep only if commercially important
0-39   = do not promote as a segment
```

## Segment Priority Score

Use the existing S01 Segment Priority Score, but calculate each input from evidence:

```text
Pain Intensity
  From voice_theme_clusters, bain_driver_inputs, and purchase/return impact.

Product Fit
  From product capability map, selling point fit scores, and proof availability.

Willingness To Pay
  From price anchor panel, price complaints, competitor price gaps, and affordability notes.

Reachability
  From channel touchpoints, source map, media behavior, and local search language.

Local Market Size
  From TAM/SAM/SOM seed and segment-level assumptions.

Competitor Gap
  From competitor threat scores, substitutes, and unmet complaint patterns.

Content Virality
  From shareable pain, visible transformation, creator/video evidence, and local community language.

Retention / Repeat Potential
  From journey episode inputs, habit formation, app/subscription signals, and earned-growth drivers.

Trust Barrier
  From privacy, claim proof, brand trust, warranty, return, and accuracy concerns.

Return / Support Risk
  From detractor drivers, setup issues, support/return journey signals, and previous-generation issues.
```

Output:

```json
{
  "segment_priority_ranking": [
    {
      "segment_id": "",
      "segment_name": "",
      "priority_score": 0,
      "rank": 0,
      "score_breakdown": {
        "pain_intensity": 0,
        "product_fit": 0,
        "willingness_to_pay": 0,
        "reachability": 0,
        "local_market_size": 0,
        "competitor_gap": 0,
        "content_virality": 0,
        "retention_or_repeat_potential": 0,
        "trust_barrier": 0,
        "return_or_support_risk": 0
      },
      "reason_to_prioritize": "",
      "reason_to_deprioritize": "",
      "recommended_gtm_role": "primary_launch_segment | secondary_segment | testing_segment | avoid",
      "confidence": "high | medium | low",
      "evidence_refs": [],
      "data_gaps": []
    }
  ]
}
```

## Distinctness And Merge Rules

Run the distinctness check before finalizing segment seeds.

Two segment candidates should be merged when:

- They share the same core motivation and use case.
- Their top objections and price behavior are not meaningfully different.
- Their channel/touchpoint map is effectively the same.
- Their persona cards would lead to the same message and proof requirements.

Split a segment when:

- One group accepts the price and another rejects it for different reasons.
- One group buys for a different job or journey episode.
- One group has a different trust barrier or proof requirement.
- One group is reachable through a materially different channel.

## Segment Seed Pack

```json
{
  "segment_seed_pack": [
    {
      "segment_id": "",
      "segment_name": "",
      "country_or_region": "",
      "segment_definition": "",
      "core_motivation": "",
      "primary_use_cases": [],
      "triggering_journey_episodes": [],
      "pain_points": [],
      "praise_points": [],
      "purchase_triggers": [],
      "current_substitutes": [],
      "most_relevant_product_features": [],
      "irrelevant_or_low_value_features": [],
      "objections": [],
      "trust_requirements": [],
      "price_sensitivity": "low | medium | high | very_high",
      "estimated_wtp_range": "",
      "tam_relevance": "high | medium | low",
      "channel_preferences": [],
      "media_touchpoints": [],
      "influencer_or_expert_types": [],
      "competitor_threat_refs": [],
      "voice_theme_refs": [],
      "bain_driver_refs": [],
      "priority_score_ref": "",
      "distinctness_result_ref": "",
      "confidence": "high | medium | low",
      "evidence_refs": [],
      "assumptions": [],
      "data_gaps": []
    }
  ]
}
```

## Persona Card Contract

Persona cards translate a segment into a human-readable launch planning artifact. They must not invent private life details that are not decision-relevant.

```json
{
  "persona_cards": [
    {
      "persona_id": "",
      "segment_id": "",
      "persona_name": "",
      "country_context": "",
      "plain_language_description": "",
      "what_they_want": [],
      "what_they_dislike_about_current_solutions": [],
      "why_this_product_may_fit": [],
      "what_they_need_to_believe_before_buying": [],
      "where_to_reach_them": [],
      "preferred_proof": [],
      "price_sensitivity": "",
      "current_substitutes": [],
      "key_objection": "",
      "recommended_gtm_angle_seed": "",
      "local_language_cues": [],
      "evidence_refs": [],
      "assumptions": [],
      "confidence": "high | medium | low"
    }
  ]
}
```

Persona card rules:

- Use local consumer wording only when the source permits short excerpts or paraphrase.
- Tie every key belief, objection, and channel to evidence refs or mark it as an assumption.
- Keep persona cards operational: buying trigger, proof need, channel, price concern, and message seed matter more than decorative backstory.
- Do not present persona cards as final targeting strategy; S02 and S03 refine them.

## Handoff Rules

Downstream handoff should include:

- `segment_candidate_pool`
- `segment_seed_pack`
- `segment_priority_ranking`
- `segment_distinctness_results`
- `persona_cards`
- `segment_evidence_strength_scores`
- `segment_level_tam_sam_som`
- `segment_channel_touchpoint_map`
- confidence caps and data gaps

Downstream skills should not reopen raw voice data unless segment evidence is weak, contradicted, or missing required fields.
