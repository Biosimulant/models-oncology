# Space Prompt - oncology-tumor-growth-combo-0016

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-dorvash2019-dynamic-modeling-of-signal-transduct-biomd0000000822-model, oncology-sbml-eftimie2010-immunity-to-melanoma-biomd0000000768-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
