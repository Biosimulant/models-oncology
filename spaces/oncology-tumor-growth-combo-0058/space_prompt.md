# Space Prompt - oncology-tumor-growth-combo-0058

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-aghakhani2022-human-breast-cancer-associated-fib-model2307090001-model, oncology-sbml-al-husari2013-ph-and-lactate-in-tumor-biomd0000000805-model, oncology-sbml-al-tuwairqi2020-dynamics-of-cancer-radiovirother-biomd0000001032-model, oncology-sbml-al-tuwairqi2020-dynamics-of-cancer-virotherapy-p-biomd0000001031-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
