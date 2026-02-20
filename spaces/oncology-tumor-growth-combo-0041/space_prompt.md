# Space Prompt - oncology-tumor-growth-combo-0041

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-tang2019-pharmacology-modelling-of-aurkb-and-zak-biomd0000000940-model, oncology-sbml-taoma2024-the-ssa-based-boolean-model-of-cell-cy-model2405030001-model, oncology-sbml-terfve2012-signalling-in-liver-cancer-logical-mo-model1506260000-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
