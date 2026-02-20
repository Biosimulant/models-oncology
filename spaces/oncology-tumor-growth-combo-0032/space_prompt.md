# Space Prompt - oncology-tumor-growth-combo-0032

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-monro2008-chemotherapy-resistance-biomd0000000776-model, oncology-sbml-morrison1989-folate-cycle-biomd0000000018-model, oncology-sbml-murphy2016-differences-in-predictions-of-ode-mod-biomd0000000671-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
