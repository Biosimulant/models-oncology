# Space Prompt - oncology-general-combo-0063

Create a scientifically coherent **oncology / general** comparative space using:
- Base models: oncology-sbml-dritschel2018-a-mathematical-model-of-cytotoxic-biomd0000000763-model, oncology-sbml-ghaffari2019-thrombomodulin-gene-expression-afte-model1907140001-model, oncology-sbml-hesse2021-interplay-between-core-clock-and-cance-model2109140001-model, oncology-sbml-jiao2018-feedback-regulation-in-a-stem-cell-mode-biomd0000000898-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
