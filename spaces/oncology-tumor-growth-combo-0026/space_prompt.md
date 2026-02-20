# Space Prompt - oncology-tumor-growth-combo-0026

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-khajanchi2015-the-combined-effects-of-optimal-co-biomd0000000897-model, oncology-sbml-kim2007-crosstalk-between-wnt-and-erk-pathways-biomd0000000149-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
