# Space Prompt - oncology-tumor-growth-combo-0070

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-bianconi2012-egfr-and-igf1r-pathway-in-lung-canc-biomd0000000427-model, oncology-sbml-boer1986-interactions-between-macrophages-and-t-model1912110001-model, oncology-sbml-bordel2018-gsmm-for-human-metabolic-reactions-hm-model1707250000-model, oncology-sbml-bouchnita2019-a-multiscale-model-to-design-thera-model1912170004-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
