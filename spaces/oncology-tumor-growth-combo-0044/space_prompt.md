# Space Prompt - oncology-tumor-growth-combo-0044

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-wodarz2018-2-model-with-transit-amplifying-cells-biomd0000000773-model, oncology-sbml-yang2012-cancer-growth-with-angiogenesis-biomd0000000796-model, oncology-sbml-yangzichen2024-metabolic-machine-learning-predic-model2407230001-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
