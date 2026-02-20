# Space Prompt - oncology-tumor-growth-combo-0055

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-abernathy2016-glioblastoma-treatment-biomd0000000757-model, oncology-sbml-afenya2018-peripheral-blodd-dynamics-in-the-dise-model1910020002-model, oncology-sbml-aghakhani2022-human-breast-cancer-associated-fib-model2307090001-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
