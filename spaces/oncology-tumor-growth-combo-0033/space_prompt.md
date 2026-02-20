# Space Prompt - oncology-tumor-growth-combo-0033

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-nave2018-prostate-cancer-model-model1910030001-model, oncology-sbml-nazari2018-il6-mediated-stem-cell-driven-tumor-g-biomd0000000819-model, oncology-sbml-nguyen2016-feedback-regulation-in-cell-signallin-biomd0000000651-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
