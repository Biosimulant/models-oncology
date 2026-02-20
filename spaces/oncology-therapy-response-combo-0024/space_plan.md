# Space Plan - oncology-therapy-response-combo-0024

## Scientific Scope
- Domain: oncology
- Theme: therapy_response
- Base models: oncology-sbml-melhem-2017-neutropenia-model-model2211040001-model, oncology-sbml-mpekris2017-role-of-vascular-normalization-in-be-model2001200002-model

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
