# Space Prompt - oncology-tumor-growth-combo-0024

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-iwamoto2010-cell-cycle-reponse-to-dna-damage-biomd0000000939-model, oncology-sbml-jafarnejad2019-mechanistically-detailed-systems-model2003200001-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
