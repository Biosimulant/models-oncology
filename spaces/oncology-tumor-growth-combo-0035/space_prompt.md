# Space Prompt - oncology-tumor-growth-combo-0035

Create a scientifically coherent **oncology / tumor_growth** comparative space using:
- Base models: oncology-sbml-pappalardo2016-pi3k-akt-and-mapk-signaling-pathw-biomd0000000666-model, oncology-sbml-park2019-cetuximab-resistance-in-colorectal-canc-model1909300004-model, oncology-sbml-reppas2015-tumor-control-via-alternating-immunos-biomd0000000749-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
