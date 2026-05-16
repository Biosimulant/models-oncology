# Chareyron2009 - Mixed immunotherapy and chemotherapy of tumors Feedback design and model updating schemes

This Biosimulant lab wraps `Chareyron2009 - Mixed immunotherapy and chemotherapy of tumors Feedback design and model updating schemes` as a runnable oncology model with a companion visualization module.
Mixed immunotherapy and chemotherapy of tumors: feedback design and model updating schemes.Chareyron S1, Alamir M.Author informationAbstractIn this paper, a recently developed model governing the canc. It can be used to explore treatment-response dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: How does the bundled treatment-response model evolve under its baseline source conditions? It runs for 10.0 time units with a communication step of 1.0. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on T, N, L, C, M, and I, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **C** peaked at **6.4e+09** and **C** moved by **6.4e+09** native units across 10.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Chareyron2009 - Mixed immunotherapy and chemotherapy of tumors Feedback design and model updating schemes - run interpretation](assets/01-chareyron2009-mixed-immunotherapy-and-chemotherapy-of-tumors-feedback-design-and.png)

*Summary table for Chareyron2009 - Mixed immunotherapy and chemotherapy of tumors Feedback design and model updating schemes, reporting the scientific question, observed answer (largest change: **C** at **6.4e+09** native units), evidence (peak observable: **C**), dominant module, and caveat.*

![Chareyron2009 - Mixed immunotherapy and chemotherapy of tumors Feedback design and model updating schemes - timeseries visualization](assets/02-chareyron2009-mixed-immunotherapy-and-chemotherapy-of-tumors-feedback-design-and.png)

*Trajectories of T, N, L, C, M, and I across the 10.0 simulation. In this run **C** climbed from 4e+06 to 6.4e+09 and **T** fell from 5e+07 to 0.00134 — the largest movements among the focused observables.*

![Chareyron2009 - Mixed immunotherapy and chemotherapy of tumors Feedback design and model updating schemes - bar visualization](assets/03-chareyron2009-mixed-immunotherapy-and-chemotherapy-of-tumors-feedback-design-and.png)

*Endpoint ranking of the focused observables. Top 3 by final value: **C** = 6.4e+09, **L** = 6.81e+07, **N** = 5119.7, with 3 more observables below.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:MODEL2001160002`
- License: `CC0`
- Visual scope: Drug/treatment response and tumour-state change
- Caveat: Values are native SBML quantities; the cleanup does not reinterpret source equations.

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `model_state_1` | `oncology_sbml_chareyron2009_mixed_immunotherapy_and_chemothera_model2001160002_model.model_state_1` | T observable. |
| `model_state_2` | `oncology_sbml_chareyron2009_mixed_immunotherapy_and_chemothera_model2001160002_model.model_state_2` | N observable. |
| `model_state_3` | `oncology_sbml_chareyron2009_mixed_immunotherapy_and_chemothera_model2001160002_model.model_state_3` | L observable. |
| `model_state_4` | `oncology_sbml_chareyron2009_mixed_immunotherapy_and_chemothera_model2001160002_model.model_state_4` | C observable. |
| `model_state_5` | `oncology_sbml_chareyron2009_mixed_immunotherapy_and_chemothera_model2001160002_model.model_state_5` | M observable. |
| `model_state_6` | `oncology_sbml_chareyron2009_mixed_immunotherapy_and_chemothera_model2001160002_model.model_state_6` | I observable. |
| `state` | `oncology_sbml_chareyron2009_mixed_immunotherapy_and_chemothera_model2001160002_model.state` | Full raw SBML observable record for reproducibility and downstream visualisation. |
| `summary` | `oncology_sbml_chareyron2009_mixed_immunotherapy_and_chemothera_model2001160002_model.summary` | Change and peak summary across the simulated SBML observables. |
| `species_labels` | `oncology_sbml_chareyron2009_mixed_immunotherapy_and_chemothera_model2001160002_model.species_labels` | Mapping from selected raw SBML observable symbols to display labels. |

## Runtime

- Duration: `10.0`
- Communication step: `1.0`

## Running Locally

```bash
biosimulant labs serve .
```
