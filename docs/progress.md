# Progress

This file is the single source of truth for autonomous milestone selection and completion state.

## Milestones

| Milestone | Status | Branch | PR | Verification |
|---|---|---|---|---|
| M1 - Restore full renderer test suite and refresh dry-run artifacts | REVIEW_READY | `m1-full-python-test-discovery` | Pending | GitHub Actions PR CI must pass before merge. |

## M1 Acceptance Tracking

- Full Python test discovery: CI now runs `python -m unittest discover -s scripts -p "test*.py" -v`, rather than only `test_render_*.py`.
- Stale expected labels: current renderer checks and render tests use current report-facing language, including `GTM Master GTM 报告`, `交付范围说明`, `关键待确认与置信度面板`, and `来源与生成审计`.
- Dry-run HTML: the committed golden dry-run dashboard is expected to stay deterministic when regenerated from `artifacts/dry-runs/generic-hardware-s00-s08-s13-s14-report-state.json`; CI regenerates it and fails on drift.
- Main-body label guard: the report-facing body uses current labels and avoids old labels such as `管理层摘要`, `模块覆盖`, and `隔离审计`.
- S14 visibility: S14 remains a hidden HTML composer and is not exposed as a main report business module.
- Public HTML guardrail: public dry-run HTML must not embed private COGS, margin, channel terms, or raw private inputs by default.

## Next Selection Rule

After M1 is merged with passing CI, add the next milestone as `TODO` and select exactly one milestone per branch and PR.
