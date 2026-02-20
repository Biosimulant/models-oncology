# Space Prompt - oncology-therapy-response-combo-0030

Create a scientifically coherent **oncology / therapy_response** comparative space using:
- Base models: oncology-sbml-perez-garcia19-computational-design-of-improved-biomd0000000814-model, oncology-sbml-rodrigues2019-a-mathematical-model-for-chemoimmu-biomd0000000879-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
