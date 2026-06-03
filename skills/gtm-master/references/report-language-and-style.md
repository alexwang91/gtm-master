# Report Language and Style Policy

Use this policy whenever S00 normalizes intake, a sub-skill writes an HTML section draft, or S14 composes the final report.

## Required Intake Field

`report_language` is required. Do not infer it from the user's chat language, target country, local evidence language, browser locale, or old dry-run fixtures.

Accepted values:

- BCP-47 tags: `zh-CN`, `en-US`, `en-GB`, `de-DE`, `fr-FR`, `ja-JP`, etc.
- Clear language names when a tag is not available: `English`, `German`, `Japanese`, `Spanish (Mexico)`.

If `report_language` is missing, ask one short question before broad research or final composition:

```text
Which report language should I use for the final GTM report? Examples: zh-CN, en-US, de-DE, ja-JP.
```

## Field Separation

- `report_language`: language for visible report prose, labels, notes, charts, tables, and recommendations.
- `output_language`: normalized copy of `report_language` used by renderers and sub-skills.
- `target_language`: local market, search, source, or consumer language for evidence gathering. It may differ from `report_language`.
- `source_language`: original language of an evidence record.

## Non-Chinese Report Style

For English and other non-Chinese reports, adapt the Stop Slop principles from hardikpandya/stop-slop as a prose quality gate:

- State the business point directly; remove throat-clearing openers.
- Use active voice and name the actor where the evidence allows it.
- Replace vague business jargon with concrete terms tied to channel, segment, price, proof, or timing.
- Avoid formulaic contrast frames such as `not X, but Y`, dramatic fragments, rhetorical setup questions, and em-dash reveal structures.
- Vary sentence length. Avoid three consecutive sentences with the same rhythm.
- Keep evidence caveats. Do not remove confidence labels, data gaps, or validation conditions to make prose sound smoother.

## Chinese Report Style

For `zh-CN`, keep the existing upward-reporting tone: concise, evidence-scoped, cautious, and easy to scan. Avoid `而不是...` and `不是...而是...` contrast frames in visible dashboard text.

## Language Gate

Before a section is ready, check:

1. User supplied `report_language` is present in the project brief.
2. Dashboard-facing text uses `report_language`.
3. Source quotes, product names, URLs, stable IDs, and standard acronyms may remain in source language.
4. Every source-language phrase has a short gloss or explanation in `report_language` when it affects a decision.
5. Non-Chinese prose passes the Stop Slop style filter without weakening evidence caveats.
