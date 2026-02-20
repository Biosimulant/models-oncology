# Space Prompt - oncology-tumor-growth-combo-0013

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-chen2011-2-bone-marrow-invasion-relative-model-biomd0000000795-model, oncology-sbml-claret2009-predicting-phase-iii-overall-survival-model1708310001-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
