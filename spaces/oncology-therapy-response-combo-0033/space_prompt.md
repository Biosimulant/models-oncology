# Space Prompt - oncology-therapy-response-combo-0033

Create a scientifically coherent **oncology / therapy_response** comparative space using:
- Base models: oncology-sbml-chaudhury2020-ec50-expansion-and-killing-mathema-biomd0000001025-model, oncology-sbml-chaudhury2020-first-order-expansion-model-of-car-model2109110005-model, oncology-sbml-chaudhury2020-lotka-volterra-mathematical-model-biomd0000001024-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
