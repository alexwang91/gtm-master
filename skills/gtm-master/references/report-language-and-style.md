# Report Language and Style Policy

Use this policy whenever S00 normalizes intake, a sub-skill writes an HTML section draft, or S14 composes the final report.

## Report Output Language

The final HTML report is written in Simplified Chinese (`zh-CN`). The current
renderer (`scripts/render-gtm-dashboard-from-report-state.py`) emits
`<html lang="zh-CN">` and ships Chinese label dictionaries only; there is no
other report-output language today.

- `report_language`: defaults to `zh-CN`. Keep the field in the project brief so
  downstream contracts stay stable, but do not ask the user to choose a report
  language and do not promise English, German, Japanese, or any other output
  language until the renderer ships those dictionaries and a matching golden
  fixture.
- Do not infer a non-Chinese report language from the user's chat language, the
  target country, or the local evidence language.

If a future contributor adds another output language, they must also add the
label dictionaries, a golden dashboard fixture, and a language gate for that
language (see `scripts/validate-gtm-suite-contracts.py`).

## Field Separation

Local evidence language is independent of the Chinese report output:

- `report_language`: language of the final dashboard prose, labels, and charts. Fixed to `zh-CN`.
- `target_language`: local market, search, source, or consumer language for evidence gathering. It usually differs from `report_language` (e.g., Hungarian evidence rendered into a Chinese report).
- `source_language`: original language of an evidence record.

Collect evidence in `target_language`, then present it in the Chinese report with
a short translation or gloss whenever the original phrasing affects a decision.

## Chinese Report Style

The report is for a country sales manager reading upward-reporting Chinese. Keep
the tone concise, evidence-scoped, cautious, and easy to scan:

- State the business point first; remove throat-clearing openers.
- Use concrete terms tied to channel, segment, price, proof, or timing.
- Avoid `而不是...` and `不是...而是...` contrast frames in visible dashboard text.
- Vary sentence length; do not stack three same-rhythm sentences.
- Keep evidence caveats. Do not drop confidence labels, data gaps, or validation conditions to make prose smoother.

## Language Gate

Before a section is ready, check:

1. Dashboard-facing text is Simplified Chinese.
2. Source quotes, product names, URLs, stable IDs, and standard acronyms may remain in source language.
3. Every source-language phrase that affects a decision has a short Chinese gloss or explanation.
