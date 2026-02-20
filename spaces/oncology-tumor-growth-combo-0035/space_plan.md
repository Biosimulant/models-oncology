# Space Plan - oncology-tumor-growth-combo-0035

## Scientific Scope
- Domain: oncology
- Theme: tumor_growth
- Base models: oncology-sbml-pappalardo2016-pi3k-akt-and-mapk-signaling-pathw-biomd0000000666-model, oncology-sbml-park2019-cetuximab-resistance-in-colorectal-canc-model1909300004-model, oncology-sbml-reppas2015-tumor-control-via-alternating-immunos-biomd0000000749-model

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
