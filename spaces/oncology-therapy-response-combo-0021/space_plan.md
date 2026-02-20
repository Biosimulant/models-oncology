# Space Plan - oncology-therapy-response-combo-0021

## Scientific Scope
- Domain: oncology
- Theme: therapy_response
- Base models: oncology-sbml-kimmel2021-t-cell-competition-and-stochastic-ext-biomd0000001041-model, oncology-sbml-melhem-2017-neutropenia-model-model2211040001-model

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
