# Space Prompt - oncology-tumor-growth-combo-0037

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-rouhimoghadam2018-gpr30-pi3k-mapk-stat-signaling-model1807040001-model, oncology-sbml-rouhimoghadam2018-gpr30-pi3k-mapk-stat-signaling-model2002250001-model, oncology-sbml-ruscone2023-logical-model-of-tumor-cell-invasion-model2304070002-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
