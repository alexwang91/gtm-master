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
    "direct_report_language_gate",
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
  Blocking and high-severity key confirmations are visible near the executive summary and in the key-confirmation panel.

confidence_badge_visibility
  Each major section shows confidence or status.

dashboard_language_gate
  The current suite version renders dashboard-facing text in Simplified Chinese by default. Stable IDs, source refs, URLs, known GTM acronyms, product or brand names, and original local-language evidence snippets may remain non-Chinese. English placeholder prose, method names, skipped-section reasons, table values, and data-gap explanations must be translated or glossed before final output.

direct_report_language_gate
  The main HTML body reads as a meeting-ready GTM report. It must not show skill IDs, handoff mechanics, module coverage, post-skill isolation, context-budget notes, report audience labels, or labels such as `方法论行动方向`. Use business labels such as `执行摘要`, `本地行动建议`, `关键待确认`, `渠道战情室`, `上市日历`, and `证据索引`.
  The visible report tone must be suitable for upward reporting: humble, cautious, evidence-scoped, and non-absolute. Do not use contrastive frames such as `而不是...` or `不是...而是...`; rewrite them into neutral judgment, priority, validation condition, or calibration-signal wording.
  The first screen must be a GTM judgment cover. It should not use its primary cards for confirmed inputs, evidence coverage, private-data boundaries, source records, or workflow status. Product/country/price can appear in title/subtitle or appendix, not as the lead story.

privacy_and_private_calculator
  Private fields are blank by default; raw private values are not embedded.

post_skill_isolation_record
  The final render records whether it used only section drafts/report state or reopened upstream artifacts through a context escalation.
  If validation outputs provide isolation records, context budget reports, targeted lookup logs, or excluded test logs, S14 renders them only as appendix/deep-mode source-governance tables.

offline_static_policy
  No external scripts, fonts, analytics, telemetry, fetch, beacon, or external dependency.

renderer_fixture
  `python scripts\render-gtm-dashboard-from-report-state.py` can generate `artifacts/dry-runs/generic-hardware-s00-s08-s13-s14-dashboard.html` from the golden dry-run report state.
  The output includes the GTM execution summary, validation plan, key-confirmation panel, citation index, optional source-governance appendix, local-only private pricing calculator, and passes the dashboard and direct-report language gates.

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
    "presentation_language_findings": [],
    "remaining_risks": []
  }
}
```
