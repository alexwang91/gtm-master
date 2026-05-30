# S08 Scoring Rubrics

Use 0-100 scores. Label weak evidence as hypothesis.

## Forecast Confidence

```text
Forecast Confidence =
  20% market size evidence
+ 15% segment split evidence
+ 15% channel availability evidence
+ 15% price acceptance evidence
+ 10% conversion/action basis
+ 10% historical or previous-generation calibration
+ 10% inventory/supply context
+ 5% lifecycle/timing/seasonality context
```

Hard caps:

```text
missing market size seed -> max 39
missing price context -> max 59
missing channel context -> max 59
only heuristic conversion -> max 69
no historical or calibration evidence -> max 79
no inventory context -> max 69 for inventory risk
marketing spend supplied without response basis -> max 59 for incremental sales confidence
no lifecycle phase calendar for multi-period forecast -> max 69 for phase curve confidence
private raw data excluded from public HTML -> cap public confidence display at source-limited
```

## Marketing Incremental Sales Confidence

```text
Marketing Incremental Sales Confidence =
  20% spend by phase/channel clarity
+ 20% reach or traffic basis
+ 20% conversion/action basis
+ 15% historical response or platform estimate quality
+ 10% adstock/lag assumption quality
+ 10% saturation/diminishing-return assumption quality
+ 5% cannibalization or pull-forward caveat
```

## Inventory Risk Score

Higher means more risk.

```text
Inventory Risk =
  25% sales range exceeds allocation
+ 20% sales low case below allocation
+ 15% replenishment lead-time risk
+ 15% channel allocation mismatch
+ 10% forecast confidence weakness
+ 10% launch timing volatility
+ 5% return/cancellation uncertainty
```

## Channel Forecast Confidence

```text
Channel Forecast Confidence =
  25% local channel evidence
+ 20% segment-channel fit
+ 15% channel capacity or commitment evidence
+ 15% price and policy fit
+ 10% traffic or conversion basis
+ 10% operational readiness
+ 5% measurement readiness
```

## Validation Priority

```text
Validation Priority =
  30% forecast movement impact
+ 20% uncertainty level
+ 20% decision proximity
+ 15% test or data feasibility
+ 10% cost or inventory risk reduction
+ 5% owner clarity
```
