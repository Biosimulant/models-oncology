# Space Plan - oncology-tumor-growth-combo-0025

## Scientific Scope
- Domain: oncology
- Theme: tumor_growth
- Base models: oncology-sbml-jenner2018-treatment-of-oncolytic-virus-biomd0000000789-model, oncology-sbml-jenner2019-oncolytic-virotherapy-for-tumours-fol-biomd0000000850-model

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
