# Suite Contract Validator

## What to build

Create one deterministic validator that checks the GTM suite contracts after any documentation or skill change.

## Acceptance criteria

- [ ] `scripts/validate-gtm-suite-contracts.py` exists.
- [ ] The validator parses S00 YAML files.
- [ ] The validator parses JSON fenced blocks.
- [ ] The validator checks implemented skill method-card coverage.
- [ ] The validator checks `post_skill_isolation_record` coverage.
- [ ] The validator checks forbidden example residue.

## Blocked by

None - can start immediately.

## Verification command

```powershell
python scripts\validate-gtm-suite-contracts.py
```
