# Space Prompt - oncology-tumor-growth-combo-0029

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-li2016-model-for-pancreatic-cancer-patients-rece-biomd0000000929-model, oncology-sbml-li2021-hdac3i-finder-a-machine-learning-based-co-model2406210001-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
