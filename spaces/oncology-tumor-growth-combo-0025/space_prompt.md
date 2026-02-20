# Space Prompt - oncology-tumor-growth-combo-0025

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-jenner2018-treatment-of-oncolytic-virus-biomd0000000789-model, oncology-sbml-jenner2019-oncolytic-virotherapy-for-tumours-fol-biomd0000000850-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
