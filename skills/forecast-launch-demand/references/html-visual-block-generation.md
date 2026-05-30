# S08 HTML Visual Block Generation

Use this when producing `html_section_draft.visual_blocks` for S14.

S08 may emit only canonical S14 visual block types:

```text
status_panel
ranked_bar
matrix_heatmap
range_chart
```

## Block 1: Forecast Input Coverage Gate

Use `status_panel` to show market size seed, segment split, channel context, price context, conversion basis, inventory context, historical calibration, and private-data status.

## Block 2: Scenario Sales Forecast

Use `range_chart` for conservative/base/upside unit ranges. The scale must be units, not revenue, unless the section clearly labels a revenue-only chart and permission exists.

Do not show a single-point forecast.

## Block 2.5: Lifecycle Phase Sales Curve

Use `range_chart` when the forecast spans multiple launch phases. Show baseline, marketing incremental, and total units by phase when available. If the chart cannot show stacked ranges, render total phase ranges as the visual block and put baseline/incremental details in a table.

## Block 2.6: Baseline vs Marketing Incremental Sales

Use `range_chart` for baseline vs MKT incremental ranges when marketing investment is supplied. If response evidence is weak, mark confidence `hypothesis_only` and show `missing_marketing_response_basis`.

## Block 3: Segment Sales Split

Use `ranked_bar` when segment ranges can be represented by midpoint or priority-weighted range. Use tables if segment ranges are too uncertain.

## Block 4: Channel Split Forecast

Use `matrix_heatmap` for channel x scenario or channel x segment when scores/ranges are comparable. Use tables for heterogeneous channel notes.

## Block 5: Inventory Risk Map

Use `matrix_heatmap` for channel x scenario risk scores. Higher scores mean more inventory risk unless the subtitle says readiness.

## Block 6: Sensitivity Driver Tornado

Use `ranked_bar` for assumptions that move the forecast most:

```text
market size
segment split
channel availability
price acceptance
conversion/action rate
media or creator reach
inventory cap
timing/seasonality
competitive pressure
marketing spend level
adstock or lag
spend saturation
```

## Block 6.5: Marketing Spend Sensitivity

Use `ranked_bar` for spend response drivers:

```text
channel spend amount
reach or traffic quality
conversion basis
adstock or carryover
saturation threshold
promo pull-forward
creative fatigue
```

## Block 7: Forecast Decision Gate

Use `status_panel` for:

```text
usable for directional strategy
usable for budget planning
usable for inventory planning
usable for channel allocation
requires user review
```

## Block 8: Validation Need Priority

Use `ranked_bar` when validation needs have comparable priority scores. Use tables when they lack scores.

## Final Assembly Rules

```text
1. Order visual_blocks by decision flow:
   coverage -> scenario range -> lifecycle/marketing bridge when relevant -> segment/channel split -> inventory risk -> sensitivity -> decision gate -> validation priority.
2. Every block needs title, data_source, confidence, and evidence_refs/citations/source note.
3. Ranges must show boundary: demand potential, reachable demand, sell-in, sell-through, or supply-constrained shipments.
4. Private raw sales, PO, inventory, or channel data must not appear unless approved.
5. Add `rendered_too_thin` if fewer than 5 required blocks can be produced in standard mode.
```
