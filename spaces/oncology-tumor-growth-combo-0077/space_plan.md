# Space Plan - oncology-tumor-growth-combo-0077

## Scientific Scope
- Domain: oncology
- Theme: tumor_growth
- Base models: oncology-sbml-chance1960-glycolysis-respiration-biomd0000000281-model, oncology-sbml-chareyron2009-mixed-immunotherapy-and-chemothera-model2001160002-model, oncology-sbml-chen2011-1-bone-marrow-invasion-absolute-model-biomd0000000793-model, oncology-sbml-chen2011-2-bone-marrow-invasion-relative-model-biomd0000000795-model

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
