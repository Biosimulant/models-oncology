# Space Plan - oncology-tumor-growth-combo-0033

## Scientific Scope
- Domain: oncology
- Theme: tumor_growth
- Base models: oncology-sbml-nave2018-prostate-cancer-model-model1910030001-model, oncology-sbml-nazari2018-il6-mediated-stem-cell-driven-tumor-g-biomd0000000819-model, oncology-sbml-nguyen2016-feedback-regulation-in-cell-signallin-biomd0000000651-model

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
