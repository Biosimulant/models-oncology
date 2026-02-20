# Space Plan - oncology-tumor-growth-combo-0039

## Scientific Scope
- Domain: oncology
- Theme: tumor_growth
- Base models: oncology-sbml-shariatpanahi2018-mathematical-modeling-of-tumor-model1909090003-model, oncology-sbml-shin-2018-egfr-pyk2-c-met-interaction-network-mo-biomd0000000826-model, oncology-sbml-siddhartha2002-kinetic-modelling-of-cancer-thera-biomd0000001048-model

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
