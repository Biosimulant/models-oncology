# Space Plan - oncology-tumor-growth-combo-0044

## Scientific Scope
- Domain: oncology
- Theme: tumor_growth
- Base models: oncology-sbml-wodarz2018-2-model-with-transit-amplifying-cells-biomd0000000773-model, oncology-sbml-yang2012-cancer-growth-with-angiogenesis-biomd0000000796-model, oncology-sbml-yangzichen2024-metabolic-machine-learning-predic-model2407230001-model

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
