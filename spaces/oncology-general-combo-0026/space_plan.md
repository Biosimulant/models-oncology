# Space Plan - oncology-general-combo-0026

## Scientific Scope
- Domain: oncology
- Theme: general
- Base models: oncology-sbml-nikolaev2019-immunobiochemical-reconstruction-of-biomd0000000865-model, oncology-sbml-owen1998-tumour-growth-model-biomd0000000670-model

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
