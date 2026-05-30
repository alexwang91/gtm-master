# S09-S12 Trigger Matrix

## What to build

Define when post-purchase/product-experience modules should run, when they should skip, and what inputs they need before detailed buildout.

## Acceptance criteria

- [ ] `skills/gtm-master/references/s09-s12-trigger-matrix.md` exists.
- [ ] S09 activation/return trigger is explicit.
- [ ] S10 insight/claim guardrail trigger is explicit.
- [ ] S11 subscription/churn trigger is explicit.
- [ ] S12 review-quality feedback trigger is explicit.
- [ ] S14 omission behavior remains explicit for non-triggered future sections.

## Blocked by

Blocked by `004-run-modes-context-budgets.md`.

## Verification command

```powershell
rg -n "S09|S10|S11|S12|skip_when|trigger" skills\gtm-master
```
