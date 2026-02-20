# Space Plan - oncology-tumor-growth-combo-0042

## Scientific Scope
- Domain: oncology
- Theme: tumor_growth
- Base models: oncology-sbml-tham2008-pdmodel-tumour-shrinkage-by-gemcitabine-biomd0000000234-model, oncology-sbml-unni2019-mathematical-modeling-analysis-and-simu-biomd0000000888-model, oncology-sbml-wei2019-mathematical-modeling-of-tumor-growth-th-model1909090002-model

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
