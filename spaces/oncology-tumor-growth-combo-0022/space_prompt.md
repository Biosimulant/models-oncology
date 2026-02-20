# Space Prompt - oncology-tumor-growth-combo-0022

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-hu2019-modeling-pancreatic-cancer-dynamics-with-biomd0000000792-model, oncology-sbml-hu2019-pancreatic-cancer-dynamics-biomd0000000744-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
