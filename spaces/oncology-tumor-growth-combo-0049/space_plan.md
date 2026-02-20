# Space Plan - oncology-tumor-growth-combo-0049

## Scientific Scope
- Domain: oncology
- Theme: tumor_growth
- Base models: oncology-sbml-alharbi2019-tumor-normal-model-tnm-of-the-develo-biomd0000001037-model, oncology-sbml-alharbi2019-tumor-normal-vitamins-model-tnvm-of-biomd0000001038-model, oncology-sbml-ayush2018-breast-cancer-detection-using-svm-and-model2407130001-model

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
