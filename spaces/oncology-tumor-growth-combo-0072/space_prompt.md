# Space Prompt - oncology-tumor-growth-combo-0072

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-bordel2018-gsmm-for-human-metabolic-reactions-hm-model1707250000-model, oncology-sbml-bouchnita2019-a-multiscale-model-to-design-thera-model1912170004-model, oncology-sbml-capuani2015-human-core-catabolic-network-model1506170000-model, oncology-sbml-celiku-friedenberg-2022-probabilistic-model-chec-model2207180001-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
