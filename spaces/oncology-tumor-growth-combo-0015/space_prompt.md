# Space Prompt - oncology-tumor-growth-combo-0015

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-depillis2007-seeking-bang-bang-solutions-of-mixe-model2003060001-model, oncology-sbml-depillis2013-mathematical-modeling-of-regulatory-biomd0000000908-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
