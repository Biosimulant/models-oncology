# Space Prompt - oncology-tumor-growth-combo-0021

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-hayashi2013-extended-tnf-induced-signaling-with-model2502170002-model, oncology-sbml-hayashi2013-tnf-induced-signaling-dynamics-model-model2502170001-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
