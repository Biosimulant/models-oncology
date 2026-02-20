# Space Plan - oncology-tumor-growth-combo-0032

## Scientific Scope
- Domain: oncology
- Theme: tumor_growth
- Base models: oncology-sbml-monro2008-chemotherapy-resistance-biomd0000000776-model, oncology-sbml-morrison1989-folate-cycle-biomd0000000018-model, oncology-sbml-murphy2016-differences-in-predictions-of-ode-mod-biomd0000000671-model

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
