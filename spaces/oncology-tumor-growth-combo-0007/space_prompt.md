# Space Prompt - oncology-tumor-growth-combo-0007

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-barros2021-cartmath-mathematical-model-of-car-t-biomd0000001020-model, oncology-sbml-bayleyegn2016-interactions-of-cyce-cdk2-cdc25a-a-model2003180002-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
