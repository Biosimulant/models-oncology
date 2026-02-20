# Space Plan - oncology-therapy-response-combo-0033

## Scientific Scope
- Domain: oncology
- Theme: therapy_response
- Base models: oncology-sbml-chaudhury2020-ec50-expansion-and-killing-mathema-biomd0000001025-model, oncology-sbml-chaudhury2020-first-order-expansion-model-of-car-model2109110005-model, oncology-sbml-chaudhury2020-lotka-volterra-mathematical-model-biomd0000001024-model

## Wiring Plan
- Comparative mode with monitor-only routing.
- Each base model state-like output connects to monitor ports `state_a..state_d`.
- No direct causal links among base models unless explicitly upgraded later.

## Visualization Plan
- Include `StateComparisonMonitor` and `StateMetricsMonitor`.
- Require at least:
  - one timeseries visual,
  - one summary table visual.

## Validation Gates
- space schema validity
- wiring endpoint validity
- smoke run success
- repo manifest/entrypoint validators pass
