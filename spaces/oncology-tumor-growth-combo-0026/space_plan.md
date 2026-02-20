# Space Plan - oncology-tumor-growth-combo-0026

## Scientific Scope
- Domain: oncology
- Theme: tumor_growth
- Base models: oncology-sbml-khajanchi2015-the-combined-effects-of-optimal-co-biomd0000000897-model, oncology-sbml-kim2007-crosstalk-between-wnt-and-erk-pathways-biomd0000000149-model

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
