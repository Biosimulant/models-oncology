# Space Plan - oncology-general-combo-0020

## Scientific Scope
- Domain: oncology
- Theme: general
- Base models: oncology-sbml-lolas2016-tumour-induced-neoneurogenesis-and-per-biomd0000000750-model, oncology-sbml-moore-2004-mathematical-model-for-cml-and-t-cell-biomd0000000733-model

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
