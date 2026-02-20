# Space Plan - oncology-tumor-growth-combo-0011

## Scientific Scope
- Domain: oncology
- Theme: tumor_growth
- Base models: oncology-sbml-chakrabarty2010-a-control-theory-approach-to-can-biomd0000000777-model, oncology-sbml-chance1960-glycolysis-respiration-biomd0000000281-model

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
