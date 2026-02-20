# Space Plan - oncology-tumor-growth-combo-0015

## Scientific Scope
- Domain: oncology
- Theme: tumor_growth
- Base models: oncology-sbml-depillis2007-seeking-bang-bang-solutions-of-mixe-model2003060001-model, oncology-sbml-depillis2013-mathematical-modeling-of-regulatory-biomd0000000908-model

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
