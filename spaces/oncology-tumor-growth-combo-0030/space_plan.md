# Space Plan - oncology-tumor-growth-combo-0030

## Scientific Scope
- Domain: oncology
- Theme: tumor_growth
- Base models: oncology-sbml-lombardo2018-expression-of-pdl1-in-neuroblastoma-model1812070002-model, oncology-sbml-lopes2025-nfkb-model-in-breast-cancer-model2508260001-model

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
