# Review And Comment Mining

Capability slots: `marketplace_reviews`, `social_listening`,
`site_specific_comment_collection`.

Required capabilities include `marketplace_review_mining`,
`video_comment_mining`, `site_specific_comment_collection`,
`structured_extraction`, and `browser_automation` when needed.

Use this for marketplace reviews, retailer reviews, local forums, specialist
media comments, video comments, app review comments, deal communities, Q&A pages,
and public social discussions where permitted.

## Outputs

```yaml
outputs:
  - comment_source_profile
  - comment_records
  - coverage_report
  - voice_atom_refs
  - nss_bain_input_refs
  - failed_sources
```

## Coverage Rule

```text
Complete means complete within a declared source, page range, product scope,
language scope, access date, and policy-permitted collection boundary.
```

## Rules

- Deduplicate source items before frequency scoring.
- Keep source-item counts separate from voice-atom counts.
- Preserve local wording when it affects search, JTBD, objections, or proof.
- Do not collect private personal data.
- Do not claim all comments were collected unless the coverage report proves it.
