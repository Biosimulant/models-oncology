# Space Prompt - oncology-tumor-growth-combo-0028

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-kuznetsov1994-nonlinear-dynamics-of-immunogenic-biomd0000000762-model, oncology-sbml-l-pez-cort-s2020-prediction-of-breast-cancer-bc-biomd0000001076-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
