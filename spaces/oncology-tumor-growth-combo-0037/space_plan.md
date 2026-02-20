# Space Plan - oncology-tumor-growth-combo-0037

## Scientific Scope
- Domain: oncology
- Theme: tumor_growth
- Base models: oncology-sbml-rouhimoghadam2018-gpr30-pi3k-mapk-stat-signaling-model1807040001-model, oncology-sbml-rouhimoghadam2018-gpr30-pi3k-mapk-stat-signaling-model2002250001-model, oncology-sbml-ruscone2023-logical-model-of-tumor-cell-invasion-model2304070002-model

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
