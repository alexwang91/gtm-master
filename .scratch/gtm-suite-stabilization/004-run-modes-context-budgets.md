# Run Modes And Context Budgets

## What to build

Define quick, standard, and deep run modes with explicit context budgets, graph limits, lookup limits, and escalation requirements.

## Acceptance criteria

- [ ] `skills/gtm-master/references/run-modes-and-context-budgets.md` exists.
- [ ] S00 load order references the run-mode document.
- [ ] Quality gates fail context budget overrun without escalation records.
- [ ] S13 lookup budget remains targeted-only.
- [ ] S14 upstream full artifact budget remains zero by default.

## Blocked by

Blocked by `001-golden-dry-run.md` and `003-suite-contract-validator.md`.

## Verification command

```powershell
rg -n "quick|standard|deep|context_budget|targeted_lookup|full artifact" skills\gtm-master
```
