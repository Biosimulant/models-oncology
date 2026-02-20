# Space Plan - oncology-tumor-growth-combo-0040

## Scientific Scope
- Domain: oncology
- Theme: tumor_growth
- Base models: oncology-sbml-solis-perez2019-a-fractional-mathematical-model-biomd0000000903-model, oncology-sbml-sotolongo-costa2003-behavior-of-tumors-under-non-biomd0000000785-model, oncology-sbml-sun2018-instantaneous-mutation-rate-in-cancer-in-biomd0000000915-model

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
