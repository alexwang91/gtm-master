# Golden Dry-Run

## What to build

Create a generic no-live-web dry-run that exercises S00 through S08, S13, and S14 using isolated section drafts, handoffs, data gaps, and post-skill isolation records.

## Acceptance criteria

- [ ] `artifacts/dry-runs/generic-hardware-s00-s08-s13-s14-report-state.json` exists.
- [ ] The report state includes `validation_roadmap`.
- [ ] The report state includes `post_skill_isolation_records`.
- [ ] Optional S05/S06/S07 sections can be skipped without failing the body.
- [ ] S09-S12 are omitted unless triggered.

## Blocked by

None - can start immediately.

## Verification command

```powershell
@'
import json
from pathlib import Path
p = Path(r"artifacts/dry-runs/generic-hardware-s00-s08-s13-s14-report-state.json")
data = json.loads(p.read_text(encoding="utf-8"))
assert any(s.get("section_id") == "validation_roadmap" for s in data["sections"])
assert data["post_skill_isolation_records"]
print("golden dry-run OK")
'@ | python -
```
