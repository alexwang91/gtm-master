# S13 Upstream Input Map

Use this to decide whether S13 can create a validation roadmap or only a planning shell.

## Required Input Groups

```json
{
  "required_input_groups": [
    "project_brief",
    "handoff_packs_or_report_state",
    "data_gap_log_or_confidence_caps"
  ]
}
```

## Source Skill Map

```text
S01 market context
  competitor candidates, source coverage, market sizing gaps, segment hypotheses, local price corridor, channel fit, consumer voice, NSS/NPS proxy gaps.

S02 JTBD scenarios
  scenario priority, proof requirements, anti-JTBD risks, local trigger phrases, validation questions.

S03 message architecture
  claim/proof risks, objections, price message seeds, local language message seeds, message test backlog.

S04 pricing model
  Opening price strategy, launch price architecture, rapid price prior, WTP calibration plan, WTP test plan, Van Westendorp, Gabor-Granger, conjoint/DCE, pricing decision gate, private profit/revenue optimizer readiness, private calculator readiness, price path, price risk guardrails.

S05 copy scoring
  copy quality gaps, claim/copy risks, copy revision briefs, copy test backlog.

S06 creator/KOL fit
  creator assumptions, budget/outcome confidence, candidate review gate, creator test backlog.

S07 DTC conversion
  page experiment plan, tracking readiness, CVR assumption ladder, funnel friction, competitor/previous-generation page gaps.

S08 forecast
  sensitivity drivers, forecast confidence caps, validation_need_map, inventory/channel/marketing response uncertainties.

S09-S12 future optional modules
  use only when their handoff packs exist.
```

## Missing Behavior

```text
project_brief missing
  Block S13. A validation roadmap needs product, country, and launch decision context.

only data_gap_log exists
  Produce fast gap triage and request handoff packs for standard roadmap.

handoff packs exist but no data_gap_log
  Infer gaps from confidence caps and missing fields, then mark gap coverage as incomplete.

S05-S07 skipped
  Do not show them as failures. Add tests only if their decision areas are still relevant.

S09-S12 absent
  Omit from body unless the user requested post-purchase validation.
```

## Context Behavior

```text
handoff_only_default
  Use compressed handoffs and data_gap_log first. Do not load full upstream artifacts by default.

field_level_escalation
  If a required validation field is missing, retrieve only that field or evidence ref, not the entire upstream module.

defer_low_priority
  If too many gaps exist, score them first and move low-priority items to excluded_or_deferred_tests_log.

lookup_is_not_research
  S13 lookup may check whether a validation method or channel test is feasible. It may not redo S01-S08 collection.
```
