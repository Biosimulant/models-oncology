# Space Plan - oncology-tumor-growth-combo-0018

## Scientific Scope
- Domain: oncology
- Theme: tumor_growth
- Base models: oncology-sbml-galante2012-b7-h1-and-a-mathematical-model-for-c-biomd0000000812-model, oncology-sbml-gevertz2018-cancer-treatment-with-oncolytic-viru-biomd0000000816-model

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
