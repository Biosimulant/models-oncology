# Space Prompt - oncology-tumor-growth-combo-0031

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-malinzi2018-enhancement-of-chemotherapy-using-on-model2003050002-model, oncology-sbml-merola2008-an-insight-into-tumor-dormancy-equili-biomd0000000911-model, oncology-sbml-mkango2019-dynamics-of-breast-cancer-under-diffe-model1912120005-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
