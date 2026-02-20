# Space Prompt - oncology-tumor-growth-combo-0034

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-ontah2019-dynamic-analysis-of-a-tumor-treatment-biomd0000000877-model, oncology-sbml-orton2009-modelling-cancerous-mutations-in-the-e-biomd0000000623-model, oncology-sbml-palaniappan2021-cell-free-modelling-of-second-ge-biomd0000001103-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
