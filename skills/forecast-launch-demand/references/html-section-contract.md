# S08 HTML Section Contract

S08 contributes the launch forecast section of the final GTM dashboard.

## Section Role

The S08 section should answer:

```text
What is the plausible launch unit-sales range, how does it split by segment and channel, what inventory risks appear under conservative/base/upside scenarios, which assumptions move the sales forecast most, and what must be validated before using the forecast for budget or inventory decisions?
```

When marketing investment matters, the section must also answer:

```text
How does the sales curve change by product lifecycle phase, what part of sales is baseline vs marketing-incremental, and where do spend saturation, lag, or weak response evidence cap confidence?
```

Dashboard-facing text should be Simplified Chinese unless the user requests another language.

## Required Section Shape

```json
{
  "section_id": "launch_forecast",
  "source_skill": "S08.forecast-launch-demand",
  "section_title": "S08 发售销量预测与库存风险",
  "status": "rendered | rendered_with_gaps | skipped",
  "confidence": "high | medium | low | hypothesis_only | blocked | unknown",
  "executive_takeaway": "",
  "narrative_blocks": [],
  "metric_cards": [],
  "visual_blocks": [],
  "tables": [],
  "callouts": [],
  "citations": [],
  "data_gaps": [],
  "next_actions": []
}
```

## Default Visual Blocks

```yaml
required_visual_blocks:
  - name: Forecast Input Coverage Gate
    type: status_panel
    data_source: forecast_input_coverage_gate

  - name: Scenario Sales Forecast
    type: range_chart
    data_source: scenario_sales_forecast

  - name: Lifecycle Phase Sales Curve
    type: range_chart
    data_source: lifecycle_phase_sales_curve

  - name: Baseline vs Marketing Incremental Sales
    type: range_chart
    data_source: baseline_incremental_sales_bridge

  - name: Segment Sales Split
    type: ranked_bar
    data_source: segment_sales_split

  - name: Channel Split Forecast
    type: matrix_heatmap
    data_source: channel_split_forecast

  - name: Inventory Risk Map
    type: matrix_heatmap
    data_source: inventory_risk_map

  - name: Sensitivity Driver Tornado
    type: ranked_bar
    data_source: sensitivity_driver_tornado

  - name: Marketing Spend Sensitivity
    type: ranked_bar
    data_source: marketing_spend_sensitivity_curve + marketing_investment_response_model

  - name: Forecast Decision Gate
    type: status_panel
    data_source: forecast_decision_gate + forecast_confidence_caps

  - name: Validation Need Priority
    type: ranked_bar
    data_source: validation_need_map
```

Use `tables` for assumption trees, source basis matrices, sell-in/sell-through splits, media bridges, creator bridges, DTC conversion bridges, previous-generation calibration, and private-data exclusion logs.

## Thin Output Rules

Mark the S08 HTML section as `rendered_too_thin` if it lacks any of:

```text
input coverage or explicit blocked status
scenario sales range or explicit missing_market_size_seed gap
segment or channel split, or explicit missing_segment_split/missing_channel_context gap
inventory risk map or explicit missing_inventory_context gap
sensitivity drivers
marketing response caveat when MKT input is supplied
forecast decision gate
validation needs
```

## Data Gap Codes

```text
missing_market_size_seed
missing_segment_split
missing_channel_context
missing_price_context
missing_conversion_basis
missing_inventory_context
missing_historical_calibration
missing_lifecycle_phase_calendar
missing_marketing_investment_plan
missing_marketing_response_basis
marketing_response_confidence_capped
baseline_incremental_sales_not_separated
missing_forecast_horizon
gross_revenue_not_permitted
private_forecast_data_excluded
forecast_confidence_capped
missing_visual_block
missing_visual_block_score
rendered_too_thin
```
