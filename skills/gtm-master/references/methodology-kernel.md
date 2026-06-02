# Methodology Kernel

Every GTM sub-skill must run as a research method, not as free-form content generation.

## Required Sequence

1. Define the research question.
2. Define observable evidence needed to answer it.
3. Select the method or model before collecting conclusions.
4. Plan MCP, web, internal, or manual evidence collection.
5. Analyze evidence step by step.
6. Apply scoring, clustering, formulas, or judgment rules explicitly.
7. Label confidence and evidence level.
8. Check counterevidence, bias, missing data, and local mismatch.
9. Produce the full artifact, compressed handoff pack, and HTML section draft.
10. Run the quality gate before advancing.

## Evidence Levels

```text
direct_evidence
cross_source_evidence
internal_evidence
model_inference
weak_hypothesis
needs_validation
avoid_or_risk
```

Use `avoid_or_risk` when a claim is legally risky, medically adjacent without proof, contradicted by evidence, or based on prohibited data collection.

## Method Selection Rules

- Market sizing uses an assumption tree, not a single unexplained number.
- Segmentation uses motivation, use case, behavior, and willingness to pay before demographics.
- Pricing uses local anchors, affordability, perceived value, and validation tests before final price advice.
- NPS proxy must be labeled as proxy and separated from surveyed NPS.
- Earned growth proxy must separate organic/referral/retention signals from paid or promotion-driven growth.
- Message and creative claims must connect to proof requirements and risk filters.
- HTML rendering must not invent missing analysis.

## Decision Surface Minimums

Every business-facing module must end with a direct GTM implication, not only an
analysis table. The implication should answer:

```text
What should the local team do?
Who is the target segment?
Which channel, creator, retailer, or proof asset carries the action?
What budget, effort, or evidence band is implied when the module owns it?
What metric or validation signal changes the decision?
```

Use a source-to-decision chain similar to retail measurement and consulting
decision-journey work:

```text
local market facts
-> competitor and price anchors
-> consumer decision journey and local language
-> segment/job fit
-> proof, price, channel, and budget actions
-> validation signal and owner
```

For B2C hardware, a report is incomplete when it names a competitor, price,
segment, channel, or KOL route without explaining why it matters and what the
local team should do next.

## Meeting-Ready Language Rule

Methods run behind the scenes. The main HTML report should not describe the
method as the point of the section. It should surface:

```text
conclusion
evidence basis
local action
owner or team hint
timing or cadence
KPI or decision trigger
confidence and key confirmation
```

Method names such as JTBD, Four Forces, Van Westendorp, MaxDiff, AARRR, ORB,
ICE, and growth S-curve may appear only when they clarify the evidence or test
logic. They should not replace a business recommendation. Internal workflow
terms such as skill IDs, handoff, module coverage, isolation audit, and report
audience labels must stay out of the main report body.

When the user needs a direct HTML report, apply the hardware launch execution
playbook: command center, SKU/offer ladder, named-channel war room, content
seeding waves, retail/PDP readiness, first-sale calendar, service trust loop,
measurement war room, and competitor response playbook.

## Required Cross-Checks For Hardware Reports

- TOP1 competitor proof must be scored and shown separately from previous
  generation, internal benchmark, and price-ladder risks.
- Public reviews and comments can create an `NPS Proxy / Bain VOC` board only
  when labeled as proxy and bounded by source coverage.
- Feature ranking must connect feature -> benefit -> segment/JTBD ->
  touchpoint/channel -> creator or media carrier -> proof need.
- WTP analysis must end with a plain-language conclusion: defend, defend with
  offer/proof, lower effective price, research first, or blocked.
- Channel plans must use local channel names when evidence exists; generic
  labels such as "ecommerce" or "retail" are acceptable only as fallbacks with a
  data gap.

## Countercheck

Before each output, check:

- Does the evidence come from the target country or a comparable market?
- Is the source recent enough for pricing, competitors, channels, or creator/KOL analysis?
- Is the sample biased toward extreme complaints, sponsored reviews, or platform-specific users?
- Is the conclusion stronger than the evidence allows?
- Would a downstream skill know how to use this output without reading the full artifact?
