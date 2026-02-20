# Space Plan - oncology-tumor-growth-combo-0028

## Scientific Scope
- Domain: oncology
- Theme: tumor_growth
- Base models: oncology-sbml-kuznetsov1994-nonlinear-dynamics-of-immunogenic-biomd0000000762-model, oncology-sbml-l-pez-cort-s2020-prediction-of-breast-cancer-bc-biomd0000001076-model

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
