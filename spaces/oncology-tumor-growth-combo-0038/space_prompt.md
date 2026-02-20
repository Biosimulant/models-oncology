# Space Prompt - oncology-tumor-growth-combo-0038

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-schattler2016-dynamical-properties-of-a-minimall-model2002030001-model, oncology-sbml-segun2018-model-of-breast-cancer-determing-chemo-model2003050001-model, oncology-sbml-selvaggio2020-microenvironment-control-of-hybrid-model2004040001-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
