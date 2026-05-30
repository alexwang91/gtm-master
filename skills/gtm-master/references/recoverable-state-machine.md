# Recoverable State Machine

This reference defines the resumable execution model for GTM Master. It adapts
the marketing-plan progress pattern into a hardware GTM suite that can survive
long research runs, browser interruptions, context compaction, and partial user
review.

## GTM Run State

Persist one run state record per project and report version. The state may live
as markdown plus JSON, but the fields below are canonical.

```json
{
  "run_id": "",
  "project_id": "",
  "report_version": "v1",
  "phase": "intake | evidence | skill_run | review | finalize | finalized",
  "current_skill": "",
  "current_gate": "",
  "resume_pointer": {
    "next_skill": "",
    "next_action": "",
    "required_refs": []
  },
  "selected_run_mode": "quick | standard | deep",
  "skill_status": {},
  "approved_sections": [],
  "pending_review_items": [],
  "state_artifacts": {
    "project_brief_ref": "",
    "evidence_ledger_ref": "",
    "decision_log_ref": "",
    "data_gap_log_ref": "",
    "report_state_ref": ""
  },
  "idempotency_key": "",
  "last_updated": ""
}
```

The exact phase line must be treated as:

```text
phase: intake | evidence | skill_run | review | finalize | finalized
```

## Phase Meanings

- `intake`: S00 has not yet locked the minimum Project Brief.
- `evidence`: S00 or an active skill is collecting allowed evidence.
- `skill_run`: one active skill is producing its output envelope.
- `review`: a user gate, competitor gate, creator gate, pricing gate, or section approval is waiting.
- `finalize`: S14 is rendering or verifying the final artifact bundle.
- `finalized`: the version is complete; revisions create a new version or reopen a named section.

## Resume Rules

1. If `phase` is `intake`, rebuild or confirm the Project Brief.
2. If `phase` is `evidence`, resume only the named evidence plan and do not widen search.
3. If `phase` is `skill_run`, load only the active skill runtime input and the direct handoff refs.
4. If `phase` is `review`, show the pending review item, record the answer, then resume from `resume_pointer`.
5. If `phase` is `finalize`, rerun S14 from report state and section drafts, not from upstream full artifacts.
6. If `phase` is `finalized`, do not silently overwrite; start a new version or reopen a named section with a decision record.

## Idempotency

Use `idempotency_key` for repeated evidence calls, rerenders, or interrupted
skill runs. A rerun may update timestamps and quality reports, but it must not
duplicate evidence records, duplicate data gaps, or overwrite a user-approved
section without a decision log entry.

## S14 Visibility Rule

S14 is not a visible business module. It is the hidden composer that consumes
`html_section_drafts`, evidence ledgers, data gaps, decisions, and quality gate
results. It may render citations, data gaps, module coverage, and audit panels,
but it must not show itself as a strategic analysis section.

## Storage Layout

Recommended run folder:

```text
artifacts/runs/{project_id}/
  project-brief.json
  run-state.json
  evidence-ledger.json
  decision-log.json
  data-gap-log.json
  report-state.json
  skills/
    S01/
      full-artifact.md
      handoff.json
      html-section.json
      isolation-record.json
  renders/
    dashboard.html
    render-quality-report.json
```

## Recovery Quality Gate

A run can advance only when:

- `run-state.json` points to the next action.
- The active skill has a `post_skill_isolation_record`.
- The next skill can start from handoff refs without opening full artifacts.
- Any reopened full artifact has a `context_escalation`.
- S14 can render from report state and section drafts alone.
