# Space Plan - oncology-general-combo-0008

## Scientific Scope
- Domain: oncology
- Theme: general
- Base models: oncology-sbml-dritschel2018-a-mathematical-model-of-cytotoxic-biomd0000000763-model, oncology-sbml-ghaffari2019-thrombomodulin-gene-expression-afte-model1907140001-model

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
