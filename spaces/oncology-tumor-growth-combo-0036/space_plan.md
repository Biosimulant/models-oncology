# Space Plan - oncology-tumor-growth-combo-0036

## Scientific Scope
- Domain: oncology
- Theme: tumor_growth
- Base models: oncology-sbml-ribba2018-mathematical-model-of-tumor-uptake-for-model1909050002-model, oncology-sbml-rommelfanger2011-generalized-logistic-model-of-m-model2109110004-model, oncology-sbml-rommelfanger2011-gompertz-model-of-melanoma-tumo-model2109110003-model

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
