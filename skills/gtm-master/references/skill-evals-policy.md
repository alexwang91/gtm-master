# Skill Evals Policy

Every implemented GTM skill keeps a lightweight `evals/evals.json` file. These
evals are not a substitute for live research; they are pressure scenarios that
keep scope boundaries, method coverage, and forbidden outputs stable as the suite
evolves.

## File Contract

Each implemented skill must include:

```text
skills/{skill-name}/evals/evals.json
```

The file contains:

```json
{
  "schema_version": "0.1.0",
  "evals": [
    {
      "name": "architecture_contract",
      "prompt": "A short pressure scenario.",
      "must_include": ["required behavior"],
      "must_not_include": ["forbidden behavior"]
    }
  ]
}
```

The validator checks `evals/evals.json`, `must_include`, `must_not_include`, and
the presence of at least one `architecture_contract` style scenario.

## What Evals Protect

- S00 must route, resume, and isolate rather than write every analysis itself.
- S01-S08 must produce handoff packs, evidence refs, and HTML section drafts.
- S09-S12 must remain conditional and hidden from the current dashboard unless
  triggered.
- S13 must prioritize validation with ICE and targeted lookups, not rerun broad
  research.
- S14 must render from report state and must not appear as a visible business
  module.

## Eval Style

Good evals are small and adversarial:

- minimal input, missing private files
- tempting broad search request
- tempting full-artifact reopen
- tempting unsupported conclusion
- optional branch without trigger
- private pricing data that must stay local

Bad evals are generic success cases that never fail.
