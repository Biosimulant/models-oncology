# Space Plan - oncology-tumor-growth-combo-0021

## Scientific Scope
- Domain: oncology
- Theme: tumor_growth
- Base models: oncology-sbml-hayashi2013-extended-tnf-induced-signaling-with-model2502170002-model, oncology-sbml-hayashi2013-tnf-induced-signaling-dynamics-model-model2502170001-model

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
