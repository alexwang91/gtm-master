# Visual System

Use this to render a work-focused GTM dashboard, not a landing page.

## Design Direction

```text
tone
  Executive, evidence-backed, dense but readable, built for scanning and decision review.

layout
  Sticky left navigation on desktop, top navigation on mobile, full-width report sections, cards only for repeated items or tools.

palette
  Neutral background with restrained accent colors for status: green, amber, red, blue, slate.

typography
  System fonts. No remote fonts. No viewport-scaled font sizes.
```

## Visual Themes

```text
default
  Quiet executive dashboard: dark blue rail, white working surface, restrained enterprise feel.

mat
  Adapted from Zara Zhang's beautiful-html-templates `Mat` template: dark sage canvas, warm bone panels, burnt-orange accent, tactile mid-century mood. Use for reports that should feel considered, design-led, and warm rather than corporate-blue.
```

Use `mat` as an adapted dashboard theme, not as the original slide deck runtime. Keep S14's scrolling report structure, section registry, private calculator, citations, and data-gap visibility.

## Components

```text
metric_card
  Small label, main value, confidence badge, source note.

status_badge
  high, medium, low, hypothesis_only, blocked, unknown.

section_header
  Title, source skill, confidence, section status.

callout
  Use for blockers, caveats, privacy, and next actions.

table
  Compact rows, visible headers, horizontal scroll on mobile.

visual_block
  Use for structured proof views that are more than a table but still offline and dependency-free.

status_panel
  Use for gates, blockers, owners, and readiness states.

simple_bar
  Use only for numeric score-like values. Always show label and value.

matrix_heatmap
  Use for two-dimensional fit or sensitivity views such as segment x scenario, feature x proof, or segment x message.

range_chart
  Use for price corridors, target price versus anchors, TAM/SAM/SOM ranges, and confidence intervals.

private_calculator
  Framed tool component with local-only privacy notice.
```

## Responsive Rules

```text
desktop
  280px left rail, content max width around 1180px.

tablet
  Navigation collapses into a horizontal list.

mobile
  Single column, compact metric grid, tables scroll horizontally.
```

## Accessibility And Readability

- Keep contrast high.
- Do not rely on color alone for status.
- Use semantic headings in order.
- Buttons must have clear text labels.
- Tables must have headers.
- Text must not overlap or require fixed viewport assumptions.
