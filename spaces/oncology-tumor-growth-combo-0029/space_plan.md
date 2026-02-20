# Space Plan - oncology-tumor-growth-combo-0029

## Scientific Scope
- Domain: oncology
- Theme: tumor_growth
- Base models: oncology-sbml-li2016-model-for-pancreatic-cancer-patients-rece-biomd0000000929-model, oncology-sbml-li2021-hdac3i-finder-a-machine-learning-based-co-model2406210001-model

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
