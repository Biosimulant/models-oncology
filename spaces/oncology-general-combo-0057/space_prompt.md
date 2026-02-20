# Space Prompt - oncology-general-combo-0057

Create a scientifically coherent **oncology / general** comparative space using:
- Base models: oncology-sbml-bukkuri2022-models-of-mendelian-and-reverse-tran-model2312120001-model, oncology-sbml-depillis2008-optimal-control-of-mixed-immunother-biomd0000000913-model, oncology-sbml-dritschel2018-a-mathematical-model-of-cytotoxic-biomd0000000763-model, oncology-sbml-ghaffari2019-thrombomodulin-gene-expression-afte-model1907140001-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
