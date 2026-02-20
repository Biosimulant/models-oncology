# Space Prompt - oncology-general-combo-0049

Create a scientifically coherent **oncology / general** comparative space using:
- Base models: oncology-sbml-ribba2012-low-grade-gliomas-tumour-growth-inhibi-biomd0000000521-model, oncology-sbml-riya-2024-interplay-between-the-immunologic-netw-model2402030002-model, oncology-sbml-talemi2015-persistent-telomere-associated-dna-da-model1412200000-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
