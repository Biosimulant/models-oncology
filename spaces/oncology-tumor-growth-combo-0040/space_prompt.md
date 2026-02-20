# Space Prompt - oncology-tumor-growth-combo-0040

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-solis-perez2019-a-fractional-mathematical-model-biomd0000000903-model, oncology-sbml-sotolongo-costa2003-behavior-of-tumors-under-non-biomd0000000785-model, oncology-sbml-sun2018-instantaneous-mutation-rate-in-cancer-in-biomd0000000915-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
