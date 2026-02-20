# Space Plan - oncology-general-combo-0049

## Scientific Scope
- Domain: oncology
- Theme: general
- Base models: oncology-sbml-ribba2012-low-grade-gliomas-tumour-growth-inhibi-biomd0000000521-model, oncology-sbml-riya-2024-interplay-between-the-immunologic-netw-model2402030002-model, oncology-sbml-talemi2015-persistent-telomere-associated-dna-da-model1412200000-model

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
