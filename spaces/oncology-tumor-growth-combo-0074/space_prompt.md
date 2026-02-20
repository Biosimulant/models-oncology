# Space Prompt - oncology-tumor-growth-combo-0074

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-capuani2015-human-core-catabolic-network-model1506170000-model, oncology-sbml-celiku-friedenberg-2022-probabilistic-model-chec-model2207180001-model, oncology-sbml-chakrabarty2010-a-control-theory-approach-to-can-biomd0000000777-model, oncology-sbml-chance1960-glycolysis-respiration-biomd0000000281-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
