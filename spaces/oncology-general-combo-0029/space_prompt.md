# Space Prompt - oncology-general-combo-0029

Create a scientifically coherent **oncology / general** comparative space using:
- Base models: oncology-sbml-owen1998-tumour-growth-model-biomd0000000670-model, oncology-sbml-raia2010-il13-signalling-medb1-biomd0000000313-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
