# S02 HTML Section Contract

S02 contributes the JTBD and demand scenario section of the final GTM dashboard.

## Section IDs

```text
jtbd_overview
upstream_input_coverage
scenario_priority
jtbd_scenario_cards
scenario_to_segment_matrix
product_job_fit_matrix
proof_requirement_seed
anti_jtbd_risks
local_trigger_phrases
scenario_price_implications
```

Conditional section IDs:

```text
scenario_to_journey_matrix
consumer_electronics_gtm_moment_map
digital_shelf_and_retailer_decision_map
behavioral_science_lever_map
scenario_commercial_weight_map
brand_claim_constraint_map
non_consumption_risks
validation_questions
```

## HTML Section Draft

```json
{
  "section_id": "s02_jtbd_scenarios",
  "source_skill": "S02.mine-jtbd-scenarios",
  "section_title": "JTBD Demand Scenarios",
  "executive_takeaway": "",
  "narrative_blocks": [],
  "metric_cards": [
    {
      "label": "Lead Scenarios",
      "value": "",
      "evidence_level": "",
      "note": ""
    }
  ],
  "visual_blocks": [],
  "tables": [],
  "charts": [],
  "callouts": [],
  "confidence_badges": [],
  "citations": [],
  "data_gaps": [],
  "next_actions": []
}
```

## S14 Visual Block Contract

S02 must produce `visual_blocks` that S14 can render directly. The visuals must explain why specific demand scenarios deserve GTM attention, not merely decorate scenario summaries. Read `html-visual-block-generation.md` for block-level transformation rules, scoring fallbacks, and thin-output checks.

```json
{
  "visual_blocks": [
    {
      "type": "status_panel | ranked_bar | matrix_heatmap | range_chart",
      "title": "",
      "subtitle": "",
      "data_source": "",
      "items": [],
      "rows": [],
      "columns": [],
      "note": "",
      "evidence_refs": [],
      "confidence": "high | medium | low | hypothesis_only"
    }
  ]
}
```

Default S02 main-body `visual_blocks`:

```yaml
required_visual_blocks:
  - title: Upstream Input Coverage Gate
    type: status_panel
    data_source: upstream_input_coverage_gate + confidence_caps
    core_question: Is S02 capped by missing S01 inputs?

  - title: Scenario Priority Scorecard
    type: ranked_bar
    data_source: scenario_priority_scorecard
    core_question: Which jobs are commercially important and evidence-supported enough to lead GTM?
    display_requirement: Show a small scoring note near the visual: scenario priority combines job frequency, pain intensity, willingness to switch, product fit, proof readiness, channel reach, commercial value, and non-consumption risk. If exact weights are unavailable, label it as a rubric.

  - title: Scenario To Segment Matrix
    type: matrix_heatmap
    data_source: scenario_to_segment_matrix
    core_question: Which priority segments map to which jobs?

  - title: Product Job Fit And Proof Readiness
    type: matrix_heatmap
    data_source: product_job_fit_matrix + proof_requirement_seed
    core_question: Which jobs can the product credibly satisfy, what should be visually lit up as high-fit, and what proof is missing?
    display_requirement: Highlight high-fit cells, but keep proof-readiness and risk badges visible. Recommended labels: high-fit ready to lead, high-fit proof gap, medium-fit needs reframing, low-fit do not lead.
```

Use `tables` for JTBD scenario cards, local trigger phrase maps, anti-JTBD risks, scenario price implications, and validation questions. Use neutral field labels such as situation, progress sought, desired outcome, current alternative, barrier, proof need, and confidence; do not use dashboard phrasing that reads like "not X, but Y". Use a separate visual block for a conditional module only when its trigger is present and its scores are comparable.

## Thin Output Gate

Mark the S02 HTML section as `rendered_too_thin` in `data_gaps` if it lacks any of:

```text
executive_takeaway
lead 3-5 JTBD scenarios with confidence and evidence refs
scenario priority visual block
scenario-to-segment visual block
proof requirement table or product-job fit visual block
anti-JTBD or non-consumption risk table
next_actions for S03/S04/S13
```

## Default Visuals

```yaml
visuals:
  - name: Upstream Input Coverage Gate
    type: coverage_table
    data_source: upstream_input_coverage_gate

  - name: Scenario Priority Matrix
    type: scatter_or_ranked_table
    data_source: scenario_priority_scorecard

  - name: JTBD Scenario Cards
    type: card_grid
    data_source: jtbd_scenario_pack

  - name: Scenario-To-Segment Matrix
    type: matrix
    data_source: scenario_to_segment_matrix

  - name: Product-Job Fit Matrix
    type: scorecard_table
    data_source: product_job_fit_matrix

  - name: Proof Requirement Seed
    type: action_table
    data_source: proof_requirement_seed

  - name: Anti-JTBD Risk Map
    type: risk_table
    data_source: anti_jtbd_risk_list
    display_requirement: Map each risk to an implicit marketing resolution rather than literal fear-based copy. Examples include proof asset, third-party review, comparison education, onboarding cue, warranty/return reassurance, privacy/safety reassurance, retailer demo, or offer design.

  - name: Local Trigger Phrase Table
    type: language_table
    data_source: local_language_trigger_phrase_map

  - name: Scenario Price Implication Seeds
    type: scorecard_table
    data_source: scenario_price_implication_seed
    display_requirement: Calculate price posture from value urgency, alternative cost, competitor anchor pressure, proof readiness, brand trust, channel norm, and price sensitivity. Output premium_justification, parity_required, promo_dependency, affordability_pressure, or value_uncertainty with confidence.
```

## Conditional Visuals

```yaml
visuals:
  - name: Scenario-To-Journey Matrix
    type: journey_matrix
    data_source: scenario_to_journey_matrix
    trigger: journey_stage_changes_downstream_work

  - name: Consumer Electronics GTM Moment Map
    type: journey_matrix
    data_source: consumer_electronics_gtm_moment_map
    trigger: separate_gtm_moment_analysis_needed

  - name: Digital Shelf And Retailer Decision Map
    type: action_table
    data_source: digital_shelf_and_retailer_decision_map
    trigger: dtc_marketplace_retail_or_channel_conversion_matters

  - name: Behavioral Science Lever Map
    type: hypothesis_table
    data_source: behavioral_science_lever_map
    trigger: message_creative_offer_or_funnel_testing_planned

  - name: Scenario Commercial Weight Map
    type: scorecard_table
    data_source: scenario_commercial_weight_map
    trigger: commercial_prioritization_or_launch_sequence_depends_on_scenarios

  - name: Brand And Claim Constraint Map
    type: risk_table
    data_source: brand_claim_constraint_map
    trigger: regulated_or_sensitive_claims_present

  - name: Non-Consumption Risk Map
    type: grouped_table
    data_source: non_consumption_risk_map
    trigger: doing_nothing_or_workaround_is_material_risk

  - name: Validation Question Seed
    type: experiment_seed_table
    data_source: validation_question_seed
    trigger: weak_confidence_or_commercially_important_hypothesis
```

## Rendering Rules

- Show scenarios as evidence-backed hypotheses, not final positioning.
- Show upstream input coverage before scenario priority when any required input group is missing or confidence-capped.
- Put scenario priority score, evidence strength, confidence, and data gaps next to each lead scenario.
- Show the scenario priority scoring rubric in small text; avoid implying mathematical precision when weights are not evidence-backed.
- Keep local-language phrases visible when they influence search, messaging, or objections.
- Show proof requirements before message recommendations.
- Show product-job fit before recommending lead scenarios; show commercial weight when the conditional module is produced.
- In product-job fit matrices, visually light up high-fit points while keeping proof gaps and marketing watchouts adjacent.
- Show conditional modules only when their trigger is present; otherwise summarize their absence in a small note or omit them.
- Show digital shelf, retailer, setup, support, and advocacy implications only when they change downstream work.
- Mark behavioral science levers as hypotheses for downstream testing, not final creative decisions.
- Show brand and claim constraints near scenario message seeds only when constraints exist.
- Show anti-JTBD risks and non-consumption risks even if they weaken the product story.
- Translate anti-JTBD risks into implicit marketing solutions; do not recommend direct fear-based wording as final copy.
- Do not render audit tables by default; source maps, candidate pools, clusters, and distinctness checks stay in full artifact or deep mode.
- Do not render final copy, final pricing, final channel budget, or final forecast in S02.
- Do not hide weak but commercially important scenarios; label them as validation hypotheses.
