# Space Prompt - oncology-general-combo-0023

Create a scientifically coherent **oncology / general** comparative space using:
- Base models: oncology-sbml-moore-2004-mathematical-model-for-cml-and-t-cell-biomd0000000733-model, oncology-sbml-nikolaev2019-immunobiochemical-reconstruction-of-biomd0000000865-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
