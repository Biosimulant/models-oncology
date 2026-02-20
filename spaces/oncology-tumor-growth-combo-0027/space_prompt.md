# Space Prompt - oncology-tumor-growth-combo-0027

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-kosinsky2018-radiation-and-pd-l-1-treatment-comb-biomd0000000863-model, oncology-sbml-kronik2010-predicting-outcomes-of-prostate-cance-model2001130003-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
