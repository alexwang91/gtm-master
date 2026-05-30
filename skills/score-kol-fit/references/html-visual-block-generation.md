# S06 HTML Visual Block Generation

Use this when producing `html_section_draft.visual_blocks` for S14.

S06 may emit only canonical S14 visual block types:

```text
status_panel
ranked_bar
matrix_heatmap
range_chart
```

## Block 1: Creator Input Coverage Gate

Use `status_panel` to show whether S06 has creator candidates, channel context, proof requirements, local language, brand safety constraints, and private-data policy.

## Block 2: Creator Archetype Fit

Use `ranked_bar` when archetypes have comparable scores:

```text
expert reviewer
hands-on demonstrator
comparison shopper reviewer
community owner voice
retail specialist
deal/affiliate creator
```

## Block 3: Trust Proof Fit Matrix

Use `matrix_heatmap` for creator role x proof requirement:

```text
technical proof
demo proof
comparison proof
owner trust
price/value proof
support/warranty proof
```

## Block 4: Platform Relevance Map

Use `matrix_heatmap` for creator role x platform/channel:

```text
YouTube
TikTok/Reels/Shorts
Instagram
specialist media
forums/community
retailer/PDP
affiliate/deal site
```

Use local platform names when S01/S02 evidence provides them.

## Block 5: Candidate Review Gate

Use `status_panel` for:

```text
review status
candidate count in review list
included count
excluded count
unsure or evidence-needed count
provisional policy
```

Use tables for the review list and decision log.

## Block 6: Candidate Fit Ranking

Use `ranked_bar` only when candidates exist and have comparable candidate fit scores.

If `creator_candidate_review_gate.status` is `pending_user_review`, render candidate rankings as provisional and add a visible review callout/table with include/exclude/unsure actions.

If candidates are missing but discovery was run, render `creator_candidate_longlist`, `creator_discovery_coverage_report`, and `competitor_creator_overlap_map` as tables, then add `missing_creator_candidates` until the user approves candidates for scoring.

If candidates are missing and discovery was not run, render sourcing criteria and request list tables, and add `missing_creator_candidates`.

## Block 7: Creator Budget And Expected Outcome Range

Use `range_chart` to show conservative/base/upside ranges for:

```text
total marketing budget
views or impressions
likes
comments
shares or saves
clicks or visits
```

Only show conversion or sales ranges when S06 has enough attribution and benchmark basis. Otherwise render conversion as a data gap or hypothesis table.

## Block 8: Creator Risk Gate

Use `status_panel` for:

```text
brand safety
claim risk
disclosure risk
competitor conflict
metric quality
private list restrictions
```

## Final Assembly Rules

```text
1. Order visual_blocks by decision flow:
   coverage -> archetype fit -> trust/proof fit -> platform relevance -> review gate -> candidate ranking -> budget/outcome range -> risk gate.
2. Every block needs title, data_source, confidence, and evidence_refs/citations/source note.
3. If no candidates exist, show archetype fit plus sourcing criteria; do not fabricate candidate names.
4. If public discovery ran, show coverage limits: searched strata, blocked sources, longlist size, promoted candidates, and why excluded.
5. If candidate review is pending, show review status before candidate budget/outcome estimates.
6. Recommendation tables must show why recommended, why not, budget basis, outcome basis, and risk reason.
7. Public metrics are proxies. Label confidence and data gaps.
8. Add `rendered_too_thin` if fewer than 4 required blocks can be produced in standard mode and no explicit missing-candidate path exists.
```
