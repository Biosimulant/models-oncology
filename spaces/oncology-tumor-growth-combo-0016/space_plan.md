# Space Plan - oncology-tumor-growth-combo-0016

## Scientific Scope
- Domain: oncology
- Theme: tumor_growth
- Base models: oncology-sbml-dorvash2019-dynamic-modeling-of-signal-transduct-biomd0000000822-model, oncology-sbml-eftimie2010-immunity-to-melanoma-biomd0000000768-model

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
