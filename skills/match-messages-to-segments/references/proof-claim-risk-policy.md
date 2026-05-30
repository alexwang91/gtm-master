# Proof And Claim Risk Policy

Use this before any message claim is produced.

## Core Rule

Every claim must carry:

```text
proof_status
claim_risk
evidence_refs
do_not_claim notes when relevant
```

## Claim Risk And Proof Gate

```json
{
  "claim_risk_and_proof_gate": {
    "status": "pass | pass_with_cautions | fail",
    "claim_checks": [
      {
        "claim_seed": "",
        "scenario_refs": [],
        "segment_refs": [],
        "claim_type": "performance | health | safety | privacy | accuracy | battery | durability | compatibility | warranty | sustainability | price_value | comparison | other",
        "proof_status": "available | partial | missing | risky",
        "claim_risk": "high | medium | low",
        "safe_direction_seed": "",
        "do_not_claim": "",
        "required_review": "none | product | legal | compliance | support | retail | privacy | other",
        "evidence_refs": [],
        "confidence": "high | medium | low"
      }
    ],
    "blocking_claims": [],
    "review_required": []
  }
}
```

Gate logic:

```text
pass
  Lead claims have available or partial proof and low/medium risk.

pass_with_cautions
  Some claims are partial, locally sensitive, or need owner review before final copy.

fail
  Lead message depends on missing/risky proof or regulated-adjacent claims without constraints.
```

## Compliance Review Queue

```json
{
  "compliance_review_queue": [
    {
      "review_id": "",
      "claim_seed": "",
      "risk_reason": "",
      "required_owner": "legal | compliance | product | privacy | support | retail | other",
      "evidence_refs": [],
      "decision_needed": ""
    }
  ]
}
```

## Sensitive Claim Rules

- Health, medical, safety, children, elderly, accuracy, AI insight, privacy, battery, certification, warranty, and sustainability claims require stronger proof.
- Do not use "best", "most accurate", "guaranteed", "medical grade", "clinically proven", or similar absolute claims unless evidence and constraints explicitly allow it.
- For battery, durability, water resistance, wireless, and compatibility claims, tie wording to exact specs, test conditions, or supported devices.
- For privacy and security claims, avoid broad trust language without policy, certification, or technical proof.
- For competitor comparisons, avoid unsupported superiority and use scenario-specific fit.
