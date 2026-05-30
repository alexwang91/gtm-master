# S13 Evidence Usage Policy

Use this before using evidence, private data, or synthetic respondents in validation planning.

## Evidence Basis Labels

Every assumption and experiment must label its basis:

```text
measured_internal
public_source
upstream_model_output
survey_or_research_plan
live_experiment_plan
retailer_or_creator_partner_input
user_hypothesis
AI_heuristic
synthetic_hypothesis_generation
missing
```

## Private Data Rules

```text
exclude_raw
  Raw private COGS, margin, sales, channel terms, traffic, conversion, inventory, PO, or partner data cannot appear in public HTML.

aggregate
  Use derived ranges, indexed values, or pass/fail statuses only.

approved
  Use only fields explicitly approved by the user and still avoid unnecessary raw disclosure.
```

S13 may design a `private_data_validation_path` that the user runs locally or with aggregated inputs. The final HTML should show the decision implication, not confidential raw data.

## Source Integrity Rules

```text
public benchmarks
  Useful for priors and test design. Not enough for final product-specific demand.

survey responses
  Useful for perception, preference, WTP direction, and objections. Not measured sales.

ad and landing metrics
  Useful for behavioral interest and funnel friction. Not full-market demand unless tied to controlled conversion and economics.

creator metrics
  Useful for audience and content fit. Likes/views alone are not qualified traffic or sales.

retail sell-in
  Shows channel confidence or purchase order behavior. It is not consumer sell-through.

AI-generated personas
  Useful for hypothesis generation and wording checks only. Never evidence of real consumer behavior.
```

## Lookup Scope Rules

S13 may use web, MCP, RAG, or local lookup only to answer narrow validation feasibility questions. It must not rebuild upstream evidence.

```text
allowed
  survey panel feasibility, platform test constraints, named retailer or marketplace test feasibility, tracking requirements, method freshness, or private-data aggregation path.

not allowed
  broad competitor discovery, broad review mining, market sizing refresh, price corridor rebuild, creator discovery from scratch, or large unscoped local document ingestion.
```

When lookup is used, emit `targeted_lookup_log` and `context_budget_report`.

## Public HTML Policy

Dashboard-facing S13 outputs should:

```text
show validation status clearly
cite upstream evidence refs when available
mark untested assumptions as hypothesis
show private-data exclusion notes
avoid confidential raw values
avoid overclaiming test precision
```
