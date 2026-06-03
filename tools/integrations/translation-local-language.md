# Translation And Local Language

Capability slot: `translation_and_local_language_processing`

Required capabilities: translation, local-language queries, phrase
normalization, and theme clustering.

Use this to generate local-language queries, preserve original consumer wording,
translate evidence, cluster themes, and avoid English-first assumptions in
country-specific reports.

## Outputs

```yaml
outputs:
  - local_query_bank
  - original_phrase_map
  - translated_summary
  - normalized_theme_labels
  - translation_limitations
```

## Rules

- Keep original language for search phrases, consumer quotes, objections, and category names.
- Pair original phrases with explanations in the user-supplied report_language when rendered.
- Mark uncertain translations, slang, sarcasm, or ambiguous product terms.
- Do not let translation smooth away dissenting viewpoints.
