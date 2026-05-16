# Segun2018 - model of breast cancer determing Chemotherapy and Keto diet response

This Biosimulant lab wraps `Segun2018 - model of breast cancer determing Chemotherapy and Keto diet response` as a runnable oncology model with a companion visualization module.
optimal control theory is applied to find out the optimal drug adjustment as an input control of the system therapies to minimize the number of cancerous cells by considering different controlled comb. It can be used to explore treatment-response dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: How does the bundled treatment-response model evolve under its baseline source conditions? It runs for 10.0 time units with a communication step of 1.0. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on N, T, M, and E, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **E** peaked at **1.34e+04** and **E** moved by **1.34e+04** native units across 10.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Segun2018 - model of breast cancer determing Chemotherapy and Keto diet response - run interpretation](assets/01-segun2018-model-of-breast-cancer-determing-chemotherapy-and-keto-diet-response-r.png)

*Summary table for Segun2018 - model of breast cancer determing Chemotherapy and Keto diet response, reporting the scientific question, observed answer (largest change: **E** at **1.34e+04** native units), evidence (peak observable: **E**), dominant module, and caveat.*

![Segun2018 - model of breast cancer determing Chemotherapy and Keto diet response - timeseries visualization](assets/02-segun2018-model-of-breast-cancer-determing-chemotherapy-and-keto-diet-response-s.png)

*Trajectories of N, T, M, and E across the 10.0 simulation. In this run **E** climbed from 20.000 to 1.34e+04 and **N** fell from 2000.0 to 4.39e-163 — the largest movements among the focused observables.*

![Segun2018 - model of breast cancer determing Chemotherapy and Keto diet response - bar visualization](assets/03-segun2018-model-of-breast-cancer-determing-chemotherapy-and-keto-diet-response-l.png)

*Endpoint ranking of the focused observables. Top 3 by final value: **E** = 1.34e+04, **M** = 449.2, **T** = 2.62e-05, with 1 more observable below.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:MODEL2003050001`
- License: `CC0`
- Visual scope: Drug/treatment response and tumour-state change
- Caveat: Values are native SBML quantities; the cleanup does not reinterpret source equations.

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `model_state_1` | `oncology_sbml_segun2018_model_of_breast_cancer_determing_chemo_model2003050001_model.model_state_1` | N observable. |
| `model_state_2` | `oncology_sbml_segun2018_model_of_breast_cancer_determing_chemo_model2003050001_model.model_state_2` | T observable. |
| `model_state_3` | `oncology_sbml_segun2018_model_of_breast_cancer_determing_chemo_model2003050001_model.model_state_3` | M observable. |
| `model_state_4` | `oncology_sbml_segun2018_model_of_breast_cancer_determing_chemo_model2003050001_model.model_state_4` | E observable. |
| `state` | `oncology_sbml_segun2018_model_of_breast_cancer_determing_chemo_model2003050001_model.state` | Full raw SBML observable record for reproducibility and downstream visualisation. |
| `summary` | `oncology_sbml_segun2018_model_of_breast_cancer_determing_chemo_model2003050001_model.summary` | Change and peak summary across the simulated SBML observables. |
| `species_labels` | `oncology_sbml_segun2018_model_of_breast_cancer_determing_chemo_model2003050001_model.species_labels` | Mapping from selected raw SBML observable symbols to display labels. |

## Runtime

- Duration: `10.0`
- Communication step: `1.0`

## Running Locally

```bash
biosimulant labs serve .
```
