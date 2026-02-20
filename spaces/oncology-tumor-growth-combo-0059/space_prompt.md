# Space Prompt - oncology-tumor-growth-combo-0059

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-al-husari2013-ph-and-lactate-in-tumor-biomd0000000805-model, oncology-sbml-al-tuwairqi2020-dynamics-of-cancer-radiovirother-biomd0000001032-model, oncology-sbml-al-tuwairqi2020-dynamics-of-cancer-virotherapy-p-biomd0000001031-model, oncology-sbml-alharbi2019-tumor-normal-model-tnm-of-the-develo-biomd0000001037-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
