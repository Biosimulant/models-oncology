# Space Plan - oncology-tumor-growth-combo-0057

## Scientific Scope
- Domain: oncology
- Theme: tumor_growth
- Base models: oncology-sbml-afenya2018-peripheral-blodd-dynamics-in-the-dise-model1910020002-model, oncology-sbml-aghakhani2022-human-breast-cancer-associated-fib-model2307090001-model, oncology-sbml-al-husari2013-ph-and-lactate-in-tumor-biomd0000000805-model, oncology-sbml-al-tuwairqi2020-dynamics-of-cancer-radiovirother-biomd0000001032-model

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
