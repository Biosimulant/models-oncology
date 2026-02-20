# Space Plan - oncology-tumor-growth-combo-0080

## Scientific Scope
- Domain: oncology
- Theme: tumor_growth
- Base models: oncology-sbml-chen2011-2-bone-marrow-invasion-relative-model-biomd0000000795-model, oncology-sbml-claret2009-predicting-phase-iii-overall-survival-model1708310001-model, oncology-sbml-coletti2020-qsp-model-of-prostate-cancer-immunot-model2109110002-model, oncology-sbml-depillis2003-the-dynamics-of-an-optimally-contro-biomd0000000909-model

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
