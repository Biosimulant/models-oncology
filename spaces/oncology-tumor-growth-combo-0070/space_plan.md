# Space Plan - oncology-tumor-growth-combo-0070

## Scientific Scope
- Domain: oncology
- Theme: tumor_growth
- Base models: oncology-sbml-bianconi2012-egfr-and-igf1r-pathway-in-lung-canc-biomd0000000427-model, oncology-sbml-boer1986-interactions-between-macrophages-and-t-model1912110001-model, oncology-sbml-bordel2018-gsmm-for-human-metabolic-reactions-hm-model1707250000-model, oncology-sbml-bouchnita2019-a-multiscale-model-to-design-thera-model1912170004-model

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
