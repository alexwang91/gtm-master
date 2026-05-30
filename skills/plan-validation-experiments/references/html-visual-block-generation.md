# S13 HTML Visual Block Generation

Use this when producing `html_section_draft.visual_blocks` for S14.

S13 may emit only canonical S14 visual block types:

```text
status_panel
ranked_bar
matrix_heatmap
range_chart
```

## Block 1: Validation Input Coverage Gate

Use `status_panel` to show available source skills, missing handoffs, data gap log status, confidence caps, test backlogs, deadline/budget context, and private-data policy.

## Block 2: Experiment Priority Scorecard

Use `ranked_bar` for the top validation experiments. Each item should include priority score, decision unlocked, method, timing, and confidence after pass/fail.

## Block 3: Assumption Risk vs Test Feasibility

Use `matrix_heatmap` for assumption risk score by test feasibility score. Rows can be assumptions or decision areas; columns should be risk, uncertainty, feasibility, and urgency.

## Block 4: Timeline And Decision Unlock Map

Use `matrix_heatmap` for decision area x time window, or test x decision gate, when timing data is comparable. Use tables if dates are narrative only.

## Block 5: Test Cost Effort vs Impact

Use `matrix_heatmap` to compare impact, effort, budget band, and speed. Use ranked bars only when a single priority score is enough.

## Block 6: Validation Decision Gate

Use `status_panel` for:

```text
ready_to_decide
decide_with_caveats
needs_validation
blocked
```

## Block 7: Experiment Portfolio By Module

Use `ranked_bar` to show the number or weighted priority of experiments by source module:

```text
market
JTBD
message
pricing
copy
creator
conversion
forecast
channel
inventory
post_launch
```

## Final Assembly Rules

```text
1. Order visual_blocks by decision flow:
   coverage -> priority -> risk/feasibility -> timeline -> cost/impact -> decision gate -> portfolio.
2. Every block needs title, data_source, confidence, and evidence_refs/citations/source note.
3. Use `hypothesis_only` when the plan relies on synthetic personas, AI heuristics, or unsupported user assumptions.
4. Do not show private raw values. Show only the validation need or aggregate implication.
5. Render `targeted_lookup_log` and `context_budget_report` as audit tables when lookup or context escalation happened.
6. Add `rendered_too_thin` if fewer than 4 required blocks can be produced in standard mode.
```
