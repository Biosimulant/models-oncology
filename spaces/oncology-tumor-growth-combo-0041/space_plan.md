# Space Plan - oncology-tumor-growth-combo-0041

## Scientific Scope
- Domain: oncology
- Theme: tumor_growth
- Base models: oncology-sbml-tang2019-pharmacology-modelling-of-aurkb-and-zak-biomd0000000940-model, oncology-sbml-taoma2024-the-ssa-based-boolean-model-of-cell-cy-model2405030001-model, oncology-sbml-terfve2012-signalling-in-liver-cancer-logical-mo-model1506260000-model

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
