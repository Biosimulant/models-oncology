# Space Plan - oncology-tumor-growth-combo-0001

## Scientific Scope
- Domain: oncology
- Theme: tumor_growth
- Base models: oncology-sbml-abernathy2016-glioblastoma-treatment-biomd0000000757-model, oncology-sbml-afenya2018-peripheral-blodd-dynamics-in-the-dise-model1910020002-model

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
