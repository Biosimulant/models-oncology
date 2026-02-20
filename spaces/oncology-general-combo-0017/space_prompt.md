# Space Prompt - oncology-general-combo-0017

Create a scientifically coherent **oncology / general** comparative space using:
- Base models: oncology-sbml-jiao2018-feedback-regulation-in-a-stem-cell-mode-biomd0000000898-model, oncology-sbml-lolas2016-tumour-induced-neoneurogenesis-and-per-biomd0000000750-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
