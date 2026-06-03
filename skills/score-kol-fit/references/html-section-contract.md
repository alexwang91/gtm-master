# S06 HTML Section Contract

S06 contributes the creator/KOL fit section of the final GTM dashboard.

## Section Role

The S06 section should answer:

```text
Which creator/expert roles fit the GTM problem, why they fit, how much marketing budget may be needed, what visits/interactions may be expected, which candidates are usable or risky, and what creator tests should run next?
```

Dashboard-facing text must use the user-supplied report_language.

## Required Section Shape

```json
{
  "section_id": "creator_kol",
  "source_skill": "S06.score-kol-fit",
  "section_title": "达人/KOL 适配与投放预估",
  "status": "rendered | rendered_with_gaps | skipped",
  "confidence": "high | medium | low | hypothesis_only | blocked | unknown",
  "executive_takeaway": "",
  "narrative_blocks": [],
  "metric_cards": [],
  "visual_blocks": [],
  "tables": [],
  "callouts": [],
  "citations": [],
  "data_gaps": [],
  "next_actions": []
}
```

## Default Visual Blocks

```yaml
required_visual_blocks:
  - name: Creator Input Coverage Gate
    type: status_panel
    data_source: creator_input_coverage_gate

  - name: Creator Archetype Fit
    type: ranked_bar
    data_source: creator_archetype_fit_scorecard

  - name: Trust Proof Fit Matrix
    type: matrix_heatmap
    data_source: creator_trust_proof_fit_matrix

  - name: Platform Relevance Map
    type: matrix_heatmap
    data_source: platform_relevance_map

  - name: Creator Budget And Expected Outcome Range
    type: range_chart
    data_source: creator_budget_estimate + creator_expected_outcome_estimate

  - name: Candidate Review Gate
    type: status_panel
    data_source: creator_candidate_review_gate

  - name: Candidate Fit Ranking
    type: ranked_bar
    data_source: creator_candidate_fit_scorecard + creator_candidate_review_gate

  - name: Creator Risk Gate
    type: status_panel
    data_source: brand_safety_risk_review + sponsorship_disclosure_risk_review
```

Use `tables` for candidate review lists, decision logs, recommendation rationales, local discovery query banks, source/channel maps, candidate longlists, competitor-overlap maps, candidate inventories, creator briefs, sourcing criteria, discovery plans, brand-safety audits, budget assumptions, expected outcome assumptions, and performance-data audits.

For a concrete S14-ready example, read `html-section-example.md` only when an example output or renderer fixture is needed.

## Thin Output Rules

Mark the S06 HTML section as `rendered_too_thin` if it lacks any of:

```text
creator role/archetype fit or explicit missing_creator_context gap
trust/proof fit
platform relevance or explicit missing_channel_context gap
discovery coverage or explicit missing_local_creator_source_map gap when public discovery was requested
candidate review gate or explicit missing_creator_candidates gap when more than three candidates exist
recommendation rationale
budget/outcome range or explicit missing_budget_basis / missing_expected_metric_basis gap
candidate scoring or explicit missing_creator_candidates gap
brand safety/disclosure risk status
creator brief or test backlog
```

## Data Gap Codes

```text
missing_creator_candidates
missing_creator_context
missing_channel_context
missing_proof_gate
missing_local_language
missing_local_creator_source_map
low_discovery_coverage
creator_source_access_blocked
pending_creator_candidate_review
creator_candidate_review_decisions_missing
creator_candidate_review_exclusions_applied
missing_visual_block
missing_visual_block_score
missing_budget_basis
missing_expected_metric_basis
outcome_estimate_confidence_capped
budget_estimate_confidence_capped
no_first_party_performance_data
private_creator_list_restricted
public_creator_access_gap
brand_safety_review_required
disclosure_review_required
performance_data_confounders
rendered_too_thin
```
