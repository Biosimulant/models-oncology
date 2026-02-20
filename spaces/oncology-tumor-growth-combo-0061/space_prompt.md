# Space Prompt - oncology-tumor-growth-combo-0061

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-al-tuwairqi2020-dynamics-of-cancer-virotherapy-p-biomd0000001031-model, oncology-sbml-alharbi2019-tumor-normal-model-tnm-of-the-develo-biomd0000001037-model, oncology-sbml-alharbi2019-tumor-normal-vitamins-model-tnvm-of-biomd0000001038-model, oncology-sbml-ayush2018-breast-cancer-detection-using-svm-and-model2407130001-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
