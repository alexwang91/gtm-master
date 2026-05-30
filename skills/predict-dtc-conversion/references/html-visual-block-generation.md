# S07 HTML Visual Block Generation

Use this when producing `html_section_draft.visual_blocks` for S14.

S07 may emit only canonical S14 visual block types:

```text
status_panel
ranked_bar
matrix_heatmap
range_chart
```

## Block 1: Conversion Input Coverage Gate

Use `status_panel` to show run mode, launch page planning stage, page/funnel materials, competitor benchmark availability, previous-generation evidence, offer details, tracking context, performance data, and private-data status.

## Block 1.5: Prelaunch Page Requirement Readiness

Use `status_panel` when there is no owned page/funnel yet. Show whether the launch page/PDP has enough requirements for:

```text
hero promise
segment/use-case clarity
proof assets
comparison framing
price/offer structure
trust policy
CTA path
tracking/event plan
```

If competitor/previous-generation evidence is heterogeneous, render details as `tables` and keep the visual block as a readiness summary.

## Block 1.6: Competitor And Previous-Gen Page Benchmark

Use `matrix_heatmap` only when benchmark rows can be scored on comparable dimensions. Otherwise use tables for observed patterns and recommendations.

## Block 2: Funnel Friction Ranking

Use `ranked_bar` for the highest-friction stages:

```text
message mismatch
proof gap
price/value ambiguity
trust/risk reversal
CTA/form friction
checkout/payment/shipping friction
mobile UX friction
tracking gap
```

## Block 3: Segment Landing Page Fit

Use `matrix_heatmap` for priority segment x page/message block:

```text
hero promise
proof section
price/offer
comparison
trust/warranty
CTA
```

## Block 4: Proof Price Trust Friction

Use `matrix_heatmap` for friction type x funnel stage or segment. Higher scores should mean more friction unless the subtitle clearly states readiness.

## Block 5: CVR Assumption Ladder

Use `range_chart` for conservative/base/upside CVR assumptions only when a basis exists. If the basis is heuristic, mark confidence `hypothesis_only` and show `missing_cvr_basis`.

If no owned page exists and no measured, benchmark, historical, or explicit heuristic basis exists, omit the range chart and show `missing_cvr_basis`. Do not show revenue or sales in S07.

## Block 6: Tracking Readiness

Use `status_panel` for conversion action, UTM/source tracking, funnel events, experiment split, consent/privacy, and reporting owner.

## Block 7: Experiment Priority

Use `ranked_bar` when experiments have comparable priority scores. Use tables when experiments lack scores.

## Final Assembly Rules

```text
1. Order visual_blocks by decision flow:
   coverage -> prelaunch requirement readiness/benchmark when relevant -> friction ranking -> segment/page fit -> proof/price/trust friction -> CVR ladder if valid -> tracking readiness -> experiment priority.
2. Every block needs title, data_source, confidence, and evidence_refs/citations/source note.
3. If page/funnel materials are missing, enter prelaunch mode, show competitor/previous-generation benchmark status, request list, requirement brief, and hypothesis-only recommendations; do not invent page content.
4. CVR ranges must show basis, scenario, confidence, and confounders.
5. Performance data must be interpreted only after validity checks.
6. Add `rendered_too_thin` if fewer than 4 required blocks can be produced in standard mode.
```
