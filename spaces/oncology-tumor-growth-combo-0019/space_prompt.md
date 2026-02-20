# Space Prompt - oncology-tumor-growth-combo-0019

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-gevertz2018-cancer-treatment-with-oncolytic-viru-biomd0000000817-model, oncology-sbml-giani2019-computational-modeling-to-predict-map3-biomd0000000883-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
