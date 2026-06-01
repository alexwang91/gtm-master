# GTM for Everything Output Contract

The dashboard is an English strategy artifact. It should answer what the team
should do, why, and what would change the decision.

## Output Envelope

```json
{
  "skill_id": "gtm-for-everything",
  "full_html_dashboard": "",
  "report_data": {},
  "citation_index": [],
  "assumption_log": [],
  "data_gaps": [],
  "quality_gate_report": {},
  "recommended_next_actions": []
}
```

## Report Data

```json
{
  "project": {
    "title": "",
    "offer": "",
    "target_market": "",
    "target_customer": "",
    "decision_context": "",
    "generated_language": "en"
  },
  "executive_answer": {
    "one_sentence_answer": "",
    "recommended_gtm_wedge": "",
    "expected_outcome_range": "",
    "top_risks": [],
    "next_decision": ""
  },
  "sections": []
}
```

## Required Sections

```json
[
  {
    "section_id": "executive_answer",
    "purpose": "State the GTM answer, decision, and confidence."
  },
  {
    "section_id": "market_truth",
    "purpose": "Show category, demand, customer, status quo, competitors, and evidence quality."
  },
  {
    "section_id": "customer_and_jtbd",
    "purpose": "Define the target segment, buying trigger, job, urgency, proof need, and objections."
  },
  {
    "section_id": "positioning_and_message",
    "purpose": "Turn offer strengths into a message architecture with proof and claim boundaries."
  },
  {
    "section_id": "pricing_and_offer",
    "purpose": "Assess price, value proof, packaging, willingness to pay, and offer design."
  },
  {
    "section_id": "channel_motion",
    "purpose": "Rank channels, owners, budget posture, expected signal, and role in the funnel."
  },
  {
    "section_id": "launch_plan",
    "purpose": "Define 30/60/90 day actions, owners, metrics, and validation gates."
  },
  {
    "section_id": "evidence_and_gaps",
    "purpose": "Show assumptions, sources, limitations, and what needs validation."
  }
]
```

## Section Object

```json
{
  "section_id": "",
  "title": "",
  "executive_takeaway": "",
  "decision": "",
  "confidence": "high | medium | low | assumption",
  "evidence_level": "direct | triangulated | proxy | assumption | missing",
  "visual_blocks": [],
  "tables": [],
  "callouts": [],
  "next_actions": [],
  "citations": [],
  "data_gaps": []
}
```

## Visual Blocks

Allowed block types:

```text
verdict_strip
scorecard
ranked_table
matrix
waterfall
funnel
timeline
range
driver_tree
evidence_board
```

Use one primary visual per section. Add supporting tables only when they change
the decision.
