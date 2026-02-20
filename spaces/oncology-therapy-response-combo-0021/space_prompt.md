# Space Prompt - oncology-therapy-response-combo-0021

Create a scientifically coherent **oncology / therapy_response** comparative space using:
- Base models: oncology-sbml-kimmel2021-t-cell-competition-and-stochastic-ext-biomd0000001041-model, oncology-sbml-melhem-2017-neutropenia-model-model2211040001-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
