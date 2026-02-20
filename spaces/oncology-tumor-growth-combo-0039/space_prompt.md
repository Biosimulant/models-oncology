# Space Prompt - oncology-tumor-growth-combo-0039

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-shariatpanahi2018-mathematical-modeling-of-tumor-model1909090003-model, oncology-sbml-shin-2018-egfr-pyk2-c-met-interaction-network-mo-biomd0000000826-model, oncology-sbml-siddhartha2002-kinetic-modelling-of-cancer-thera-biomd0000001048-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
