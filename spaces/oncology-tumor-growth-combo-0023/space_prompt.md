# Space Prompt - oncology-tumor-growth-combo-0023

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-hutchinson2016-vascular-phenotype-identification-model1911130007-model, oncology-sbml-iarosz2015-brain-tumor-biomd0000000775-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
