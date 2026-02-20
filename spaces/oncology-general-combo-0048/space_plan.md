# Space Plan - oncology-general-combo-0048

## Scientific Scope
- Domain: oncology
- Theme: general
- Base models: oncology-sbml-owen1998-tumour-growth-model-biomd0000000670-model, oncology-sbml-raia2010-il13-signalling-medb1-biomd0000000313-model, oncology-sbml-raia2011-il13-l1236-biomd0000000314-model

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
