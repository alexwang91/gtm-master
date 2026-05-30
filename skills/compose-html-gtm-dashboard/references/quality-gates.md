# S14 Quality Gates

Run these before claiming a dashboard is complete.

## Required Checks

```json
{
  "required_checks": [
    "input_coverage",
    "section_registry",
    "core_section_depth",
    "visual_block_compatibility",
    "no_invented_analysis",
    "citation_integrity",
    "data_gap_visibility",
    "confidence_badge_visibility",
    "dashboard_language_gate",
    "privacy_and_private_calculator",
    "post_skill_isolation_record",
    "offline_static_policy",
    "layout_responsiveness",
    "accessibility_basics"
  ]
}
```

## Check Details

```text
input_coverage
  Required inputs are present or missing inputs are visible in the data-gap panel.

section_registry
  Rendered sections match canonical order and preserve source skill refs.

core_section_depth
  S01-S08 and S13 sections include mandatory views from `s01-s04-display-contract.md`, section-specific contracts, and upstream `visual_blocks` where available. Optional skipped sections such as S05/S06/S07 may render a skip note instead of mandatory visuals. If required data exists but visual_blocks are absent, report `missing_visual_block`; if required data is absent, report `missing_required_view`.

visual_block_compatibility
  Every `visual_blocks.type` is one of `status_panel`, `ranked_bar`, `matrix_heatmap`, or `range_chart`. Non-canonical method names must be mapped before rendering or reported as `missing_visual_block`.

no_invented_analysis
  Executive summary and section text trace back to upstream drafts, decision updates, or data gaps.
  For `validation_roadmap`, S14 renders supplied S13 data only. It must not invent validation experiments, rewrite priority scores, change pass/fail rules, or turn targeted lookup gaps into claims.

citation_integrity
  Evidence refs are rendered as provided. Missing citation details are flagged, not invented.

data_gap_visibility
  Blocking and high-severity data gaps are visible near the executive summary and in the data-gap panel.

confidence_badge_visibility
  Each major section shows confidence or status.

dashboard_language_gate
  The current suite version renders dashboard-facing text in Simplified Chinese by default. Stable IDs, source refs, URLs, known GTM acronyms, product or brand names, and original local-language evidence snippets may remain non-Chinese. English placeholder prose, method names, skipped-section reasons, table values, and data-gap explanations must be translated or glossed before final output.

privacy_and_private_calculator
  Private fields are blank by default; raw private values are not embedded.

post_skill_isolation_record
  The final render records whether it used only section drafts/report state or reopened upstream artifacts through a context escalation.
  If S13 provides `post_skill_isolation_record`, `context_budget_report`, `targeted_lookup_log`, or `excluded_or_deferred_tests_log`, S14 renders them as audit tables or appendix tables.

offline_static_policy
  No external scripts, fonts, analytics, telemetry, fetch, beacon, or external dependency.

renderer_fixture
  `python scripts\render-gtm-dashboard-from-report-state.py` can generate `artifacts/dry-runs/generic-hardware-s00-s08-s13-s14-dashboard.html` from the golden dry-run report state.
  The output includes the S13 validation roadmap, module coverage, data-gap audit, citation index, post-skill isolation audit, local-only private pricing calculator, and passes the dashboard language gate.

layout_responsiveness
  Desktop and mobile layouts remain readable; tables scroll instead of overflowing the page.

accessibility_basics
  Semantic headings, table headers, readable contrast, keyboard-usable controls.
```

## Output

```json
{
  "render_quality_report": {
    "status": "pass | pass_with_caveats | fail",
    "checks": [],
    "privacy_findings": [],
    "citation_findings": [],
    "layout_findings": [],
    "remaining_risks": []
  }
}
```
