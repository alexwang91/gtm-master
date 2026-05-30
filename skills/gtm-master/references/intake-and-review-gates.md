# Intake and Review Gates

Use these gates to keep the user input light while allowing private, high-value context to improve the report.

## Gate 0: Intake Review

Minimum required input:

```text
product features and specs
launch country or region
target price range
```

After receiving the minimum input, ask once for optional private files. Do not block the workflow if the user has none.

Recommended wording:

```text
If you have any of these, uploading them will make the report much more accurate. If not, I can continue with public research and mark the gaps:

- Product specification sheet or product brief
- Previous-generation sales, price, and channel performance
- Customer reviews, NSS/NPS, satisfaction survey, or internal customer voice summary
- Brand positioning, self-perception, tone, or claim boundaries
- Competitor list, internal benchmark, or channel plan
- Historical ads, KOL/influencer briefs, landing pages, creative assets, or campaign learnings
```

Do not ask by default for hardware-irrelevant inputs. Ask for app analytics, subscription data, medical/health evidence, support tickets, or activation funnels only when the product actually has those dimensions.

## Private File Handling

When the user uploads private files:

1. Identify file type and likely value.
2. Summarize what each file can improve.
3. Extract only decision-relevant information.
4. Record the file as internal evidence.
5. Do not quote private content publicly unless the user approves.
6. Keep private evidence separate from public web evidence.

Use this internal evidence priority:

```text
product specifications
previous-generation commercial performance
customer reviews / NSS / NPS / customer voice
brand positioning and tone constraints
internal benchmark and channel plan
historical ads / KOL / landing pages / creative assets
```

## Gate 1: Evidence Plan Review

Before broad web collection, MCP calls, crawling, or browser automation, show a short evidence plan:

```json
{
  "target_country_or_region": "",
  "local_languages": [],
  "evidence_needs": [],
  "likely_connector_slots": [],
  "example_queries": [],
  "sensitive_or_restricted_sources": [],
  "expected_data_gaps": []
}
```

Ask for correction only if the plan might be wrong, sensitive, or expensive. Otherwise continue and log assumptions.

## Gate 2: Market Map Review

After S01, pause when useful and ask the user to confirm:

- Competitor and substitute universe
- 5-10 potential competitors/substitutes discovered by local source discovery and their proposed roles
- Local price anchors
- Initial segments
- Internal context not visible from public evidence
- Sources to exclude or treat cautiously

Continue automatically if the report depth is `quick` or the user requested no interruptions.

## Gate 3: Strategy Direction Review

After messaging and pricing direction are formed, ask for review when:

- Primary segment choice changes the business strategy
- Price implication is materially different from the user's target range
- Brand tone or self-perception conflicts with evidence-backed positioning
- Claims approach compliance, health, children, elderly, safety, or regulated territory

## Gate 4: Final Report Review

Before final HTML composition, confirm:

- Audience and style
- Public vs internal-only sections
- Sensitive private evidence
- Claims and data gaps that must be highlighted
- Any sections to hide, anonymize, or mark as appendix-only

## Interrupt Policy

Default behavior is continue unless a high-impact review gate is triggered.

Respect user preferences:

```json
{
  "review_mode": "auto_continue | ask_at_major_gates | ask_before_each_skill",
  "private_file_policy": "use_uploaded_context | ignore_private_context | ask_before_using_each_file",
  "public_report_policy": "internal_only | public_ready | mixed_with_private_appendix"
}
```
