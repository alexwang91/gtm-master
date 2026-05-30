---
name: gtm-master
description: Orchestrate a multi-skill GTM intelligence report suite for 2C hardware launches. Use when the user provides product features/specs, target launch country or region, and target price range and wants a complete evidence-backed GTM analysis, multi-step research workflow, compressed handoffs between GTM sub-skills, MCP/web research routing, report state management, or final HTML dashboard generation. Also use when building, updating, auditing, or sequencing the GTM sub-skills in this suite.
---

# GTM Master

## Overview

Use this skill as S00, the operating system for the GTM intelligence report suite. It does not replace downstream GTM sub-skills; it routes work, controls context, manages evidence, enforces handoff contracts, and maintains the final HTML report state.

The user-facing promise is minimal input:

```json
{
  "product_features_and_specs": "",
  "launch_country_or_region": "",
  "target_price_range": ""
}
```

Optional inputs can improve quality, but must not be required before the suite can start:

```json
{
  "product_name_or_codename": "",
  "launch_timing": "",
  "product_specification_files": [],
  "previous_generation_sales_price_channel_performance": "",
  "customer_reviews_and_nss_or_nps": "",
  "brand_positioning_self_perception_and_tone": "",
  "competitor_list_internal_benchmark_channel_plan": "",
  "historical_copy_landing_pages_kol_scripts_and_ads": "",
  "copy_assets_or_concepts": [],
  "fixed_visual_or_layout_constraints": "",
  "target_language": "zh-CN by default unless the user requests another report language",
  "claim_constraints": "",
  "compliance_constraints": "",
  "report_audience": "founder | marketing | sales | investor | product | retailer",
  "report_depth": "quick | standard | deep",
  "html_style_preference": "executive | consulting | dashboard | investor_deck"
}
```

For the full optional input list, including S04 private pricing constraints, S06 creator/KOL inputs, S07 conversion materials, S08 forecast/lifecycle/MKT inputs, and S13 validation budget/timeline/testing access inputs, read `references/suite-manifest.yaml` and `references/schemas.md`. Keep this overview compact so S00 remains a router, not a duplicate schema.

## Load Order

Read only what the task needs.

1. Always read `references/suite-manifest.yaml` and `references/codegraph.yaml` before planning a suite run or changing the architecture.
2. Read `references/run-modes-and-context-budgets.md` before choosing quick, standard, or deep mode or allowing any context/search escalation.
3. Read `references/recoverable-state-machine.md` before starting, resuming, interrupting, reviewing, or finalizing a run.
4. Read `references/methodology-crosswalk.yaml` before assigning AARRR, JTBD, Four Forces, VOC, Van Westendorp, MaxDiff, ICE, ORB, budget, growth S-curve, or copy-sweep methods to a sub-skill.
5. Read `references/hardware-current-state-rubric.md` when scoring launch readiness or deciding which validation gap matters first.
6. Read `references/budget-and-growth-models.md` when S08 or S13 uses marketing budget, CAC, lifecycle, or growth-curve assumptions.
7. Read `references/suite-implementation-roadmap.md` before planning build order, deciding the next sub-skill to implement, auditing remaining work, or changing optional expansion scope.
8. Read `references/intake-and-review-gates.md` before asking for optional private files or pausing for user review.
9. Read `references/schemas.md` when creating project briefs, run state, runtime inputs, handoff packs, evidence records, or report sections.
10. Read `references/post-skill-isolation-policy.md` before advancing from one sub-skill to another or changing handoff/runtime isolation rules.
11. Read `references/method-cards.yaml` for the active sub-skill only. Do not load all method details by default.
12. Read `references/methodology-kernel.md` when defining or auditing a sub-skill's scientific method.
13. Read `references/mcp-routing-policy.md` before any web, MCP, crawling, browsing, or internal-data collection plan.
14. Read `references/skill-evals-policy.md` before adding or changing a skill, eval, method card, or suite contract.
15. Read `references/quality-gates.md` before advancing to another sub-skill or claiming a section is ready.
16. Read `references/visual-block-acceptance-matrix.md` before auditing S01-S08/S13 `visual_blocks`, report-state compatibility, or S14 readiness.
17. Read `references/report-data-contract.md` before writing or updating HTML report state.
18. Read `references/html-dashboard-design.md` when composing or reviewing the final visual report.
19. Read `references/marketing-skills-adaptation-map.md` when importing or adapting an external marketing skill pattern.

Use optional references conditionally; do not load future roadmap nodes or inactive sub-skill details by default.

## Operating Principles

- Route before work: identify the task type and active skill before generating analysis.
- Criteria before content: define method, evidence needs, scoring rules, and output schema before writing conclusions.
- Handoff before expansion: downstream sub-skills read compressed handoff packs by default, not upstream full artifacts.
- Run mode before graph breadth: choose quick, standard, or deep before activating optional branches or wider evidence collection.
- Recoverable state before long work: persist run state, resume pointer, evidence ledgers, decisions, data gaps, and skill status after every meaningful boundary.
- Methodology crosswalk before method use: every named method must map to a skill, hardware adaptation, output hook, and confidence limit.
- Post-skill isolation: after each sub-skill writes its handoff, HTML section, evidence updates, decisions, gaps, and isolation record, its working context is closed.
- Evidence before claims: every material conclusion needs provenance, confidence, and evidence level.
- Least invasive collection: prefer official APIs, approved internal data, search, and public extraction before browser automation or crawling.
- One active skill: execute or edit one sub-skill at a time unless S00 explicitly marks a branch as parallel safe.
- Report state as you go: each sub-skill writes a full artifact, compressed handoff, and HTML section draft.
- Verification before done: run the relevant quality gate before declaring a section, handoff, or suite step ready.
- Evals before architecture stable: every implemented skill keeps `evals/evals.json` with pressure scenarios for scope, method, evidence, and forbidden outputs.
- Chinese dashboard by default: write final dashboard-facing summaries, labels, callouts, and recommendations in Simplified Chinese unless the user explicitly requests another output language. Preserve original local-language evidence with translation/gloss when useful.

## Task Router

Classify each request into one task type:

```text
suite_run
  The user wants a GTM report from product specs, country, and price.

build_or_update_skill
  The user wants to create, revise, or audit one of the GTM sub-skills.

evidence_repair
  A section has weak, missing, stale, conflicting, or non-compliant evidence.

handoff_repair
  A downstream sub-skill cannot consume an upstream handoff.

html_report_composition
  The user wants the final dashboard or a report section rendered.

architecture_review
  The user wants to adjust the suite graph, principles, dependencies, or execution model.
```

## Suite Run Protocol

For a normal GTM report run:

1. Build a `Project Brief` from user inputs.
2. Select `report_depth` from `run-modes-and-context-budgets.md`; default to `standard` when the user does not specify.
3. Run Gate 0 from `intake-and-review-gates.md`: ask for optional high-value private files, but do not block if the user has none.
4. Create or resume `GTM Run State` from `recoverable-state-machine.md`; record `phase`, `current_skill`, `resume_pointer`, `selected_run_mode`, and `idempotency_key`.
5. Build a `Skill Execution Plan` from `codegraph.yaml`, `methodology-crosswalk.yaml`, and the selected run mode.
6. If a current-state view is needed, score the 17-section hardware GTM readiness rubric and record explicit gaps.
7. For the active sub-skill, create a `Skill Runtime Input` containing only the project brief, direct upstream handoff pack, active method card, allowed evidence refs, and out-of-scope list.
8. If evidence collection is needed, create an MCP routing plan from `mcp-routing-policy.md` and run Gate 1 before searching or browsing when the plan includes broad web collection, scraping, browser automation, or sensitive sources.
9. Run the active sub-skill or prepare its handoff if the sub-skill is not implemented yet.
10. Require the sub-skill output envelope:

```json
{
  "full_artifact": {},
  "compressed_handoff_pack": {},
  "html_section_draft": {},
  "recoverable_run_state_updates": [],
  "evidence_updates": [],
  "decision_updates": [],
  "data_gaps": [],
  "context_escalations": [],
  "post_skill_isolation_record": {}
}
```

11. Run the quality gate, including the run-mode, context-budget, methodology-crosswalk, evals, and recoverable-state gates.
12. Run post-skill isolation from `references/post-skill-isolation-policy.md`.
13. Update report state, run state, and resume pointer before continuing to the next graph node.

## Handoff-Only Runtime

Downstream sub-skills may read only:

- S00 Project Brief
- Direct upstream compressed handoff pack
- Current active skill method card
- Evidence records referenced by the handoff
- Current task scope and quality gate

Do not open upstream full artifacts by default. Open a full artifact only when one of these escalation reasons applies:

- Handoff is missing a required field.
- Handoff contradicts itself or the project brief.
- Evidence confidence is too low for the downstream decision.
- Raw consumer language or source detail is required.
- The user explicitly requests an upstream audit.

Record every escalation using the schema in `references/schemas.md`.

## Post-Skill Isolation

At the end of every active sub-skill:

- Save the full artifact as a reference, not normal downstream context.
- Pass only the compressed handoff pack and named evidence refs to downstream analysis skills.
- Pass only `html_section_draft` plus accumulated report state to S14.
- Merge evidence, decisions, and data gaps into suite-level ledgers.
- Emit `post_skill_isolation_record`.
- Treat the active skill's working context as closed.

Do not reopen upstream full artifacts unless a recorded context escalation applies.

S14 is the hidden composer, not a visible business module. The dashboard may show
module coverage, data gaps, citations, and isolation audit, but it must not
present S14 itself as a strategic section.

## Subagent Policy

Do not require one subagent per sub-skill. The suite must be subagent-compatible, not subagent-dependent.

Use subagents only when the branch is independent or parallel safe, such as multi-country research, competitor/price/review evidence collection, post-messaging branches, or independent review. S00, final narrative integration, and HTML composition remain controlled by the main agent.

## Human Review

Pause for review or clearly flag required human validation for TAM assumptions, segment weights, price sensitivity, NPS proxy methodology, earned growth attribution, health/medical-adjacent claims, children/elderly safety claims, third-party scraping policy, private/internal data use, and public use of consumer quotes.
