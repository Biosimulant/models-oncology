# Space Prompt - oncology-tumor-growth-combo-0043

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-west2019-cellular-interactions-constrain-tumor-g-biomd0000000820-model, oncology-sbml-wodarz2001-viruses-as-antitumor-weapons-biomd0000001043-model, oncology-sbml-wodarz2018-1-simple-model-biomd0000000774-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
