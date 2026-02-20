# Space Plan - oncology-tumor-growth-combo-0017

## Scientific Scope
- Domain: oncology
- Theme: tumor_growth
- Base models: oncology-sbml-faratian2009-role-of-pten-in-trastuzumab-resista-biomd0000000424-model, oncology-sbml-fassoni2019-oncogenesis-encompassing-mutations-a-biomd0000000807-model

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
