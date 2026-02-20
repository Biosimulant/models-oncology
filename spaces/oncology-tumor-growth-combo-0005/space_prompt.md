# Space Prompt - oncology-tumor-growth-combo-0005

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-ayush2018-breast-cancer-detection-using-svm-and-model2407130001-model, oncology-sbml-babbs2012-immunotherapy-biomd0000000758-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
