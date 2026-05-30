# Run Modes And Context Budgets

Use this file before S00 creates a skill execution plan. The goal is to keep long chained reports useful without letting context, evidence collection, or optional branches expand invisibly.

## Run Modes

```yaml
run_modes:
  quick:
    graph: [S01, S02, S03, S04, S08, S13, S14]
    purpose: Fast directional GTM read with visible caveats.
    optional_branch_policy: skip_unless_explicitly_triggered
    evidence_policy: targeted_light_collection_or_user_materials_only
    main_visual_blocks_per_section: 3-5
    appendices: minimal
    default_status_when_evidence_is_thin: pass_with_caveats

  standard:
    graph: [S01, S02, S03, S04, S08, S13, S14]
    optional_branches: [S05, S06, S07]
    purpose: Default pre-launch GTM dashboard.
    optional_branch_policy: run_only_when_user_inputs_or_decision_relevance_trigger_them
    evidence_policy: localized public evidence plus allowed private inputs
    main_visual_blocks_per_section: 4-8
    appendices: citations, data gaps, decision log, validation audit
    default_status_when_evidence_is_thin: pass_with_caveats

  deep:
    graph: [S01, S02, S03, S04, S05, S06, S07, S08, S13, S14]
    optional_branches: [S09, S10, S11, S12]
    purpose: Heavier research run with richer evidence, appendices, and validation audit.
    optional_branch_policy: run_triggered_modules_only
    evidence_policy: deeper localized evidence and approved private/internal materials
    main_visual_blocks_per_section: 6-12
    appendices: evidence maps, source quality, collection logs, validation audit, context audit
    default_status_when_evidence_is_thin: pass_with_caveats_or_blocked
```

Quick, standard, and deep change breadth and evidence depth; they do not relax evidence labeling, private-data policy, or post-skill isolation.

## Default Context Budgets

```yaml
context_budgets:
  per_skill_main_handoff_fields: 20-40
  main_visual_blocks_per_section_default: 4-8
  default_full_artifact_opening: forbidden_without_recorded_context_escalation
  downstream_input_policy: handoff_only
  S13_external_lookup_budget_default: 0
  S13_external_lookup_budget_when_justified: 1-8 targeted lookups
  S14_upstream_full_artifact_budget_default: 0
  S14_allowed_upstream_inputs:
    - report_state
    - html_section_drafts
    - evidence_ledger
    - data_gap_log
    - decision_log
    - quality_gate_results
    - approved local-only calculator specs
```

## Escalation Requirements

A skill exceeds the default context budget only when all of these exist:

```text
context_escalation
  What was opened, why the handoff was insufficient, and what downstream decision it affects.

targeted_lookup_log
  Required for S13 or any validation lookup beyond the current handoff and evidence ledger.

context_budget_report
  Budget item, limit, used amount, and whether the run stayed within mode.

post_skill_isolation_record
  What was passed downstream, what was withheld, and when the full artifact may be reopened.
```

If these records are missing, the quality gate fails rather than silently widening context.

## Mode Selection Rules

```text
No report_depth provided
  Use standard.

User needs fast directional answer
  Use quick.

User provides rich private files, deep evidence expectation, or multi-country/multi-channel validation
  Use deep, but still run only triggered optional modules.

Optional module lacks trigger or required materials
  Emit skipped_not_triggered with data gaps and continue.

Future S09-S12 module lacks trigger
  Omit from body and record only in roadmap or trigger matrix when useful.
```

## Compression Rules

- Each skill writes a full artifact, but downstream normal operation receives only the compressed handoff, evidence refs, and HTML section draft.
- Raw review corpora, search pages, private pricing inputs, and scratch scoring notes stay out of normal downstream context.
- S14 never opens upstream full artifacts by default. If S14 cannot render from report state and section drafts, it reports `missing_required_view` or requests upstream repair.
- S13 can perform targeted validation lookup only for a named validation question; broad search or broad local/RAG ingestion is out of mode unless a deep-run escalation explicitly approves it.
