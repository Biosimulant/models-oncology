# Space Plan - oncology-general-combo-0066

## Scientific Scope
- Domain: oncology
- Theme: general
- Base models: oncology-sbml-ghaffari2019-thrombomodulin-gene-expression-afte-model1907140001-model, oncology-sbml-hesse2021-interplay-between-core-clock-and-cance-model2109140001-model, oncology-sbml-jiao2018-feedback-regulation-in-a-stem-cell-mode-biomd0000000898-model, oncology-sbml-lolas2016-tumour-induced-neoneurogenesis-and-per-biomd0000000750-model

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
