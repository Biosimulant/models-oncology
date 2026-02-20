# Space Plan - oncology-tumor-growth-combo-0027

## Scientific Scope
- Domain: oncology
- Theme: tumor_growth
- Base models: oncology-sbml-kosinsky2018-radiation-and-pd-l-1-treatment-comb-biomd0000000863-model, oncology-sbml-kronik2010-predicting-outcomes-of-prostate-cance-model2001130003-model

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
