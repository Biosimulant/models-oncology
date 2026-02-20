# Space Plan - oncology-tumor-growth-combo-0038

## Scientific Scope
- Domain: oncology
- Theme: tumor_growth
- Base models: oncology-sbml-schattler2016-dynamical-properties-of-a-minimall-model2002030001-model, oncology-sbml-segun2018-model-of-breast-cancer-determing-chemo-model2003050001-model, oncology-sbml-selvaggio2020-microenvironment-control-of-hybrid-model2004040001-model

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
