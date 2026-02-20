# Space Prompt - oncology-tumor-growth-combo-0030

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-lombardo2018-expression-of-pdl1-in-neuroblastoma-model1812070002-model, oncology-sbml-lopes2025-nfkb-model-in-breast-cancer-model2508260001-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
