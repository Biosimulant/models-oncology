# Space Prompt - oncology-tumor-growth-combo-0017

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-faratian2009-role-of-pten-in-trastuzumab-resista-biomd0000000424-model, oncology-sbml-fassoni2019-oncogenesis-encompassing-mutations-a-biomd0000000807-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
