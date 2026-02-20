# Space Prompt - oncology-tumor-growth-combo-0020

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-greene2019-differentiate-spontaneous-and-induced-biomd0000000825-model, oncology-sbml-gulhane2022-sphingolipid-metabolism-and-pi3k-akt-model2402290001-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
