# GTM Skill Suite

This repository contains agent skills for generating evidence-backed GTM
analysis and static HTML dashboards.

## Files

- `skills/gtm-master/` - Chinese-first multi-skill GTM suite for consumer hardware launches.
- `skills/gtm-for-everything/` - English consulting-style GTM dashboard skill for any product, service, market, or business idea.
- `skills/*/SKILL.md` - executable skill specifications.
- `skills/*/references/` - detailed methods, output contracts, visual rules, and evidence policies.
- `skills/*/evals/evals.json` - lightweight pressure scenarios that protect scope and quality.
- `scripts/validate-gtm-suite-contracts.py` - repository contract validator for the main GTM suite.
- `tools/` - platform-neutral MCP, CLI, browser, search, extraction, price, review, and private-file integration guidance.

## Primary Use Cases

### GTM Master

Input:

- Product features and specifications
- Launch country or region
- Target price range
- Optional private files, previous-generation data, NSS/NPS, channel plans, creative assets, or KOL materials

Output:

- Local market map
- Competitor and substitute proof
- Consumer voice and Bain/NPS proxy boards
- JTBD scenarios
- Message architecture
- Pricing and WTP logic
- Launch demand forecast
- Validation roadmap
- Chinese HTML GTM report

### GTM for everything

Input:

- Offer, product, service, or business idea
- Target market
- Target customer
- Price or business model
- Optional traction, competitors, channels, budget, and constraints

Output:

- English GTM strategy dashboard
- Executive answer
- Market truth
- Customer and JTBD logic
- Positioning and message architecture
- Pricing and offer assessment
- Channel motion
- 30/60/90 launch plan
- Evidence gaps and validation actions

## Skill Structure

```text
skills/
  gtm-master/
    SKILL.md
    references/
    evals/
    agents/
  gtm-for-everything/
    SKILL.md
    references/
    evals/
    agents/
```

## Design Principles

- Decision first, evidence second, action third.
- Structured output contracts before narrative writing.
- Clear confidence labels and data gaps.
- Static HTML dashboards by default.
- Private data stays out of public HTML unless explicitly approved.
- English dashboards use a stop-slop editorial pass based on
  `hardikpandya/stop-slop`.

## Validation

Run this before claiming the suite is stable:

```powershell
python scripts\validate-gtm-suite-contracts.py
```

For new standalone skills, also check:

- `SKILL.md` has valid YAML frontmatter.
- `evals/evals.json` parses as JSON.
- Reference files contain no placeholders or unsupported claims.
