# S13 Context And Search Budget

Use this before opening full artifacts, RAG collections, local files, web pages, MCP results, or search results.

## Default Runtime

```text
handoff_only
  Use compressed handoffs, data_gap_log, confidence caps, test backlogs, and referenced evidence IDs.

targeted_escalation
  Open only the smallest source needed to resolve a specific validation planning question.

forbidden_default
  Do not run broad web search, broad local file reading, broad RAG retrieval, or full upstream artifact rehydration.
```

## Context Budget Rules

```text
assumption_inventory_main_view
  Keep the main view to the highest-priority assumptions. Aggregate or defer low-priority assumptions.

full_artifact_opening
  Allowed only when a handoff field is missing, contradictory, too thin for pass/fail rules, or the user explicitly requests an audit.

rag_retrieval
  Retrieve only evidence IDs or narrow source clusters named by handoffs. Do not search the whole corpus by vague topic.

local_file_reading
  Read only the relevant file or section. If a file is large, extract the fields needed for the validation question.

web_or_mcp_lookup
  Use only for targeted validation feasibility, platform/channel constraints, or method freshness. Never use S13 lookup to rebuild S01-S08 evidence.
```

## Targeted Lookup Plan

Before any web/MCP/local lookup, define:

```json
{
  "lookup_id": "",
  "decision_unlocked": "",
  "validation_question": "",
  "allowed_source_type": "local_file | evidence_ref | rag_ref | web_search | official_doc | retailer_page | platform_doc | survey_provider | internal_summary",
  "max_queries_or_refs": 0,
  "fields_to_extract": [],
  "stop_condition": "",
  "forbidden_collection": []
}
```

Recommended default caps:

```text
per_validation_question
  1-3 targeted sources or queries.

per_S13_run
  8 targeted external lookups unless the user approves more.

per_source
  Extract only fields needed for the validation plan: feasibility, cost/effort signal, sample/data requirement, tracking constraint, channel constraint, or method caveat.
```

## Escalation Reasons

Record a context escalation when:

```text
missing_required_field
contradiction
low_confidence_blocks_pass_fail_rule
raw_local_wording_needed_for_test_stimulus
private_data_policy_needed
user_requested_audit
method_or_platform_rule_may_have_changed
```

## Targeted Lookup Log

Emit this audit object when lookup happens:

```json
{
  "lookup_id": "",
  "reason": "",
  "source_type": "",
  "queries_or_refs_used": [],
  "fields_extracted": [],
  "decision_impact": "",
  "result": "used | partial | unavailable | deferred",
  "created_evidence_refs": [],
  "limitations": []
}
```

## Context Budget Report

Emit this audit object when S13 finishes:

```json
{
  "context_policy": "handoff_only | targeted_escalation",
  "handoff_packs_used": [],
  "full_artifacts_opened": [],
  "local_files_opened": [],
  "rag_refs_retrieved": [],
  "web_or_mcp_lookups": [],
  "assumptions_in_main_view": 0,
  "assumptions_deferred": 0,
  "reason_if_budget_exceeded": ""
}
```

## Stop Rules

Stop lookup and return a gap when:

```text
the lookup would recreate upstream research
source access requires login, bypass, paywall, or prohibited scraping
results do not change experiment design or priority
the query budget is exhausted
the required answer depends on private internal data the user has not approved
```
