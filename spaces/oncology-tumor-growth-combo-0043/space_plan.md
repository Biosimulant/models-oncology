# Space Plan - oncology-tumor-growth-combo-0043

## Scientific Scope
- Domain: oncology
- Theme: tumor_growth
- Base models: oncology-sbml-west2019-cellular-interactions-constrain-tumor-g-biomd0000000820-model, oncology-sbml-wodarz2001-viruses-as-antitumor-weapons-biomd0000001043-model, oncology-sbml-wodarz2018-1-simple-model-biomd0000000774-model

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
