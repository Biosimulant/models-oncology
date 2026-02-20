# Space Prompt - oncology-tumor-growth-combo-0077

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-chance1960-glycolysis-respiration-biomd0000000281-model, oncology-sbml-chareyron2009-mixed-immunotherapy-and-chemothera-model2001160002-model, oncology-sbml-chen2011-1-bone-marrow-invasion-absolute-model-biomd0000000793-model, oncology-sbml-chen2011-2-bone-marrow-invasion-relative-model-biomd0000000795-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
