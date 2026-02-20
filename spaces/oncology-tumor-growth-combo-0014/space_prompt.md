# Space Prompt - oncology-tumor-growth-combo-0014

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-coletti2020-qsp-model-of-prostate-cancer-immunot-model2109110002-model, oncology-sbml-depillis2003-the-dynamics-of-an-optimally-contro-biomd0000000909-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
