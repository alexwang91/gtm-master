---
name: compose-html-gtm-dashboard
description: Use when rendering GTM suite report_state, html_section_drafts, evidence ledgers, confidence badges, citations, data gaps, private local calculators, and validation sections into a polished static HTML dashboard without inventing missing analysis.
---

# Compose HTML GTM Dashboard

## Role

Use this skill as S14 in the GTM intelligence report suite. It composes upstream section drafts into a polished static HTML dashboard with navigation, executive summary, confidence badges, citations, data gaps, and local-only private calculators.

S14 is a render skill, not an analysis skill. It must not invent findings, change upstream conclusions, hide low-confidence outputs, or fill missing modules with fabricated content.

## Required Inputs

```json
{
  "report_state": {},
  "html_section_drafts": [],
  "evidence_ledger": [],
  "data_gap_log": []
}
```

High-value inputs:

```json
{
  "project_brief": {},
  "decision_log": [],
  "confidence_badge_map": {},
  "citation_index": [],
  "private_pricing_calculator_spec": {},
  "style_preferences": {},
  "output_language": "zh-CN",
  "report_audience": "executive | gtm_team | product_team | research_team | mixed",
  "report_depth": "quick | standard | real_product_pilot | deep"
}
```

## Load Order

Read only what the current task needs:

1. Read `references/output-contract.md` before producing any final dashboard artifact.
2. Read `references/upstream-input-map.md` before checking whether S14 has enough report state and section drafts to render.
3. Read `references/render-architecture.md` before composing sections, executive summary, citations, and data gaps.
4. Read `references/section-registry.md` before choosing section order, required/optional sections, or hidden appendices.
5. Read `references/s01-s04-display-contract.md` before rendering or auditing S01-S04 report sections; for S05-S08 and S13 use their section-specific `html-section-contract.md` and S14 canonical visual block rules.
6. Read `references/visual-system.md` before choosing layout, cards, tables, badges, charts, or responsive behavior.
7. Read `references/privacy-security.md` before rendering private calculators, user-uploaded data, citations, images, or scripts.
8. Read `references/quality-gates.md` before claiming the HTML is complete.
9. Read `references/html-template-contract.md` before using or modifying `assets/dashboard-shell.html`.

## Depth Modes

```text
quick
  Render S01-S08 or available core sections only. Include executive summary, confidence badges, citations, data gaps, and private pricing calculator if supplied.

standard
  Render all available section drafts in the canonical registry order. Include data gaps, decision log summary, citation index, and quality report.

deep
  Add appendices for audit refs, artifact index, methodology notes, evidence ledger, validation roadmap, and module coverage.
```

Default to `standard`.

## Output Tiers

Core outputs, always produced:

```text
render_input_gate
section_registry_instance
executive_summary_panel
dashboard_navigation
confidence_badge_map
citation_index
data_gap_panel
full_html_dashboard
render_quality_report
```

Conditional outputs, produced only when triggered:

```text
private_pricing_calculator_component
validation_roadmap_panel
appendix_artifact_index
methodology_appendix
evidence_ledger_appendix
print_export_notes
static_asset_manifest
```

Conditional triggers:

```text
private_pricing_calculator_component
  Trigger when S04 provides private_pricing_calculator_spec.

validation_roadmap_panel
  Trigger when S13 output exists or when S04/S07/S08 produce validation plans.

appendix_artifact_index
  Trigger when full_artifact refs, audit refs, RAG refs, or collection logs exist.

methodology_appendix
  Trigger in deep mode or when the report audience needs method transparency.

evidence_ledger_appendix
  Trigger in deep mode or when source traceability is a report requirement.

print_export_notes
  Trigger when the user needs PDF/print-friendly handoff.
```

## Execution Workflow

Follow this sequence:

```text
1. Validate render inputs and section draft coverage
2. Normalize section drafts into the section registry
3. Build executive summary only from upstream executive takeaways and decision updates
4. Build confidence badge map from section confidence fields and confidence caps
5. Build citation index from evidence refs; do not invent citation URLs or titles
6. Build data gap panel from upstream data_gap_log and section-level data gaps
7. Render sections in canonical order, skipping absent sections with visible coverage notes when important
8. Render private calculator components only from local-only specs with blank inputs
9. Render appendices only when triggered
10. Run render quality gates
11. Produce full_html_dashboard and static_asset_manifest
```

## Reference Renderer Command

Use the deterministic renderer below as the current S14 smoke-test path for the golden dry-run:

```powershell
python scripts\render-gtm-dashboard-from-report-state.py
```

Default input:

```text
artifacts/dry-runs/generic-hardware-s00-s08-s13-s14-report-state.json
```

Default output:

```text
artifacts/dry-runs/generic-hardware-s00-s08-s13-s14-dashboard.html
```

The generated dashboard must remain single-file, offline-first, Simplified Chinese by default, and must render from report state plus section drafts rather than reopening upstream full artifacts.

## Scope Boundary

S14 owns:

- Final static HTML composition
- Section ordering and navigation
- Visual hierarchy, badges, tables, simple charts, and callouts
- Citation and evidence index rendering
- Data gap and decision log rendering
- Private local calculator rendering with blank local-only inputs
- HTML quality gates

S14 does not own:

- New market research
- New strategic conclusions
- Rewriting upstream recommendations
- Filling missing modules with invented content
- Legal, finance, compliance, or executive approval
- Hosted deployment

## Required Output

Always return the S14 output envelope from `references/output-contract.md`:

```json
{
  "full_html_dashboard": "",
  "static_assets": [],
  "citation_index": [],
  "confidence_badge_map": {},
  "render_quality_report": {},
  "data_gaps": [],
  "decision_updates": [],
  "post_skill_isolation_record": {},
  "recommended_next_skills": []
}
```

## Quality Rules

- Do not invent missing findings, metrics, citations, charts, section content, or confidence levels.
- Default dashboard language is Simplified Chinese (`zh-CN`) unless the user requests another language. Keep original local-language evidence snippets with Chinese explanation or gloss.
- Current suite version is Chinese-first. All dashboard-facing titles, labels, takeaways, table headers, notes, skipped-section reasons, data-gap descriptions, and audit explanations must render in Simplified Chinese. Allowed non-Chinese visible tokens are stable IDs, source refs, URLs, acronyms such as GTM/JTBD/HTML/NSS/NPS/WTP/COGS/MKT/DTC/KOL, and original consumer/search phrases when paired with Chinese explanation.
- Show data gaps and low-confidence sections clearly.
- Keep private COGS, margin, channel terms, internal sales, and raw uploaded private data out of public sections unless explicitly approved.
- Render private calculators with blank fields and local browser calculations only.
- Use no external scripts, external fonts, analytics, telemetry, or network calls in the default static dashboard.
- Escape or sanitize user-provided text before rendering HTML.
- Keep section IDs stable so downstream exports and comments can link to them.
- Keep charts simple and data-backed; use tables or scorecards when chart data is incomplete.
- Run quality gates before claiming the dashboard is complete.
