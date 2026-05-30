# Post-Skill Isolation Policy

Use this after every sub-skill finishes and before S00 advances to the next graph node.

## Core Rule

Each sub-skill may think with rich working context while it is active. After it finishes, downstream skills receive only bounded transfer objects:

```text
compressed_handoff_pack
html_section_draft
evidence_updates
decision_updates
data_gaps
quality_gate_result
post_skill_isolation_record
```

The active skill's working context is then considered closed. Isolation means "cold stored and referenceable", not deleted.

## Isolation Sequence

```text
1. Save full_artifact and long evidence outputs as artifact refs, not inline downstream context.
2. Produce compressed_handoff_pack with canonical fields, key findings, do_not_reopen, open questions, and data gaps.
3. Produce html_section_draft for S14/report_state. It must be self-contained enough to render without reopening the full artifact.
4. Merge evidence_updates, decision_updates, risk_updates, and data_gaps into suite-level ledgers.
5. Run quality gates for schema, evidence labels, visual blocks, privacy, and handoff sufficiency.
6. Emit post_skill_isolation_record.
7. Clear active working context. The next skill receives only its allowed runtime input.
```

## Downstream Allowed Context

By default, downstream skills may use only:

```text
project_brief
direct upstream compressed_handoff_pack
active skill method card
allowed evidence refs named by handoff
current task scope
quality gate requirements
```

S14 is special: it also receives accumulated `html_section_drafts`, `report_state`, `citation_index`, `confidence_badge_map`, and `data_gap_log`. It still may not invent missing analysis or open full artifacts by default.

## Reopen Rules

Opening a full artifact, large evidence file, raw source collection, RAG collection, or previous skill working notes requires a `context_escalation`.

Allowed escalation reasons:

```text
missing_required_field
contradiction
low_confidence_blocks_decision
raw_quote_needed
private_data_policy_check
user_requested_audit
render_blocked_by_missing_section_field
```

Forbidden reopen reasons:

```text
curiosity
rewriting upstream analysis
making the downstream answer feel richer
re-running a previous skill without a decision record
filling gaps that should remain visible
```

## Isolation Record

Every completed skill should emit:

```json
{
  "isolation_id": "",
  "skill_id": "",
  "status": "isolated | isolated_with_gaps | blocked",
  "full_artifact_ref": "",
  "compressed_handoff_ref": "",
  "html_section_ref": "",
  "evidence_update_refs": [],
  "decision_update_refs": [],
  "data_gap_refs": [],
  "allowed_downstream_refs": [],
  "withheld_context": [],
  "reopen_conditions": [],
  "privacy_notes": [],
  "quality_gate_status": "pass | pass_with_caveats | fail"
}
```

## Fail Conditions

Fail isolation when:

```text
handoff is missing canonical fields required by downstream
html_section_draft cannot render or lacks visible skip/gap status
full artifact is required for normal downstream operation
private raw data leaks into public handoff or HTML
data gaps are hidden instead of recorded
quality gate result is missing
```

## Practical Interpretation

The suite should behave like a relay:

```text
active skill works deeply
-> writes artifact and compressed relay baton
-> hands baton to next skill
-> leaves the track
```

This prevents context bloat, stale attention, and accidental upstream rewrites while preserving auditability.
