# S14 Output Contract

S14 must produce one final static HTML GTM report, supporting asset refs, citation and confidence maps, and a render quality report.

## Output Envelope

```json
{
  "skill_id": "S14",
  "skill_name": "compose-html-gtm-dashboard",
  "full_html_dashboard": "",
  "static_assets": [],
  "citation_index": [],
  "confidence_badge_map": {},
  "gtm_judgment_cover": {},
  "render_quality_report": {},
  "data_gaps": [],
  "decision_updates": [],
  "post_skill_isolation_record": {},
  "recommended_next_skills": []
}
```

## Full HTML Dashboard

```json
{
  "full_html_dashboard": {
    "artifact_id": "A14.gtm-dashboard-html",
    "title": "[Product] [Country] GTM 报告",
    "language": "zh-CN",
    "format": "single_file_static_html",
    "html_path": "",
    "template_ref": "assets/dashboard-shell.html",
    "rendered_sections": [],
    "skipped_sections": [],
    "privacy_mode": "public_safe | contains_private_local_calculator | contains_approved_private_values",
    "created_from_section_drafts": [],
    "quality_gate_status": "pass | pass_with_caveats | fail"
  }
}
```

## Render Input Gate

```json
{
  "render_input_gate": {
    "status": "pass | pass_with_gaps | fail",
    "available_inputs": [],
    "missing_inputs": [],
    "blocking_gaps": [],
    "non_blocking_gaps": [],
    "sections_available": [],
    "sections_missing": [],
    "action": "render | render_with_gap_notes | request_upstream_rerun | stop"
  }
}
```

## GTM Judgment Cover

```json
{
  "gtm_judgment_cover": {
    "judgment": "enter | defend | cautious_launch | validate_first | pause | unknown",
    "judgment_label": "",
    "core_recommendation": "",
    "opening_move": "",
    "priority_segment": "",
    "must_win_channel": "",
    "price_or_offer_stance": "",
    "top_competitor_threat": "",
    "budget_posture": "",
    "decision_changing_question": "",
    "confidence": "high | medium | low | hypothesis_only",
    "evidence_refs": []
  }
}
```

The cover must be built from upstream decisions and takeaways. It must not be a
checklist of product/country/price inputs, evidence coverage, private-data
handling, or workflow state.

## Section Registry Instance

```json
{
  "section_registry_instance": {
    "section_order": [],
    "sections": [
      {
        "section_id": "",
        "source_skill": "",
        "title": "",
        "status": "rendered | skipped_missing | skipped_not_triggered | rendered_with_gaps",
        "confidence": "high | medium | low | hypothesis_only | unknown",
        "data_source_refs": [],
        "evidence_refs": []
      }
    ]
  }
}
```

## Render Quality Report

```json
{
  "render_quality_report": {
    "status": "pass | pass_with_caveats | fail",
    "checks": [
      {
        "check_id": "",
        "status": "pass | caveat | fail",
        "details": ""
      }
    ],
    "privacy_findings": [],
    "citation_findings": [],
    "layout_findings": [],
    "local_action_findings": [],
    "presentation_language_findings": [],
    "remaining_risks": []
  }
}
```

Render quality must check that supplied `local_team_action` objects are visible
near the relevant section claim. S14 may not invent a local action when upstream
analysis did not supply one; it should record `missing_local_team_action` as a
render caveat instead.

Render quality must also check direct report wording. The main report should not
show workflow terms such as skill IDs, handoff, module coverage, isolation audit,
report audience labels, or `方法论行动方向`. Use `执行摘要`, `关键待确认`, and
`本地行动建议` in visible labels.

## Static Asset Manifest

```json
{
  "static_asset_manifest": {
    "template_files": [
      "assets/dashboard-shell.html",
      "assets/dashboard-shell-mat.html"
    ],
    "external_dependencies": [],
    "network_policy": "offline_static_by_default",
    "allowed_inline_scripts": [
      "local rendering",
      "private calculator",
      "local filtering",
      "print controls"
    ],
    "forbidden_features": [
      "remote scripts",
      "remote fonts",
      "analytics",
      "telemetry",
      "network requests",
      "unapproved private data"
    ]
  }
}
```
