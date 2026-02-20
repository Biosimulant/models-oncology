# Space Plan - oncology-tumor-growth-combo-0067

## Scientific Scope
- Domain: oncology
- Theme: tumor_growth
- Base models: oncology-sbml-barros2021-cartmath-mathematical-model-of-car-t-biomd0000001019-model, oncology-sbml-barros2021-cartmath-mathematical-model-of-car-t-biomd0000001020-model, oncology-sbml-bayleyegn2016-interactions-of-cyce-cdk2-cdc25a-a-model2003180002-model, oncology-sbml-bianconi2012-egfr-and-igf1r-pathway-in-lung-canc-biomd0000000427-model

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
