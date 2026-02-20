# Space Prompt - oncology-tumor-growth-combo-0036

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-ribba2018-mathematical-model-of-tumor-uptake-for-model1909050002-model, oncology-sbml-rommelfanger2011-generalized-logistic-model-of-m-model2109110004-model, oncology-sbml-rommelfanger2011-gompertz-model-of-melanoma-tumo-model2109110003-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
