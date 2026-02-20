# Space Prompt - oncology-therapy-response-combo-0015

Create a scientifically coherent **oncology / therapy_response** comparative space using:
- Base models: oncology-sbml-hessemuellerrelogio2023-timing-treatment-toxicit-model2305270001-model, oncology-sbml-kemmer2022-disentangling-erbb-signaling-in-breas-model2205030001-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
