# S14 Validation Rendering

## What to build

Strengthen S14 so the final dashboard can render S13 validation priorities, context budget audit tables, data-gap visibility, and validation decision gates in Chinese.

## Acceptance criteria

- [ ] S14 registry includes `validation_roadmap`.
- [ ] S14 quality gates mention S13 visual blocks.
- [ ] S14 can render `targeted_lookup_log`, `context_budget_report`, and `post_skill_isolation_record` when supplied.
- [ ] S14 does not invent validation content when S13 is missing or thin.

## Blocked by

Blocked by `001-golden-dry-run.md`.

## Verification command

```powershell
rg -n "validation_roadmap|html_validation_section|context_budget|targeted_lookup|post_skill_isolation" skills\compose-html-gtm-dashboard
```
