# Space Prompt - oncology-tumor-growth-combo-0042

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-tham2008-pdmodel-tumour-shrinkage-by-gemcitabine-biomd0000000234-model, oncology-sbml-unni2019-mathematical-modeling-analysis-and-simu-biomd0000000888-model, oncology-sbml-wei2019-mathematical-modeling-of-tumor-growth-th-model1909090002-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
