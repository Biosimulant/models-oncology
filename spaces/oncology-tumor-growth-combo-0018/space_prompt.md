# Space Prompt - oncology-tumor-growth-combo-0018

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-galante2012-b7-h1-and-a-mathematical-model-for-c-biomd0000000812-model, oncology-sbml-gevertz2018-cancer-treatment-with-oncolytic-viru-biomd0000000816-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
