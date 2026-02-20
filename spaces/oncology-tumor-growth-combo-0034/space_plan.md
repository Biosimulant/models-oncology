# Space Plan - oncology-tumor-growth-combo-0034

## Scientific Scope
- Domain: oncology
- Theme: tumor_growth
- Base models: oncology-sbml-ontah2019-dynamic-analysis-of-a-tumor-treatment-biomd0000000877-model, oncology-sbml-orton2009-modelling-cancerous-mutations-in-the-e-biomd0000000623-model, oncology-sbml-palaniappan2021-cell-free-modelling-of-second-ge-biomd0000001103-model

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
