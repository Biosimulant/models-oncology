# Ontah2019 - Dynamic analysis of a tumor treatment model using oncolytic virus and chemotherapy with saturated infection rate

This Biosimulant lab wraps `Ontah2019 - Dynamic analysis of a tumor treatment model using oncolytic virus and chemotherapy with saturated infection rate` as a runnable oncology model with a companion visualization module.
This is a mathematical model describing the treatment of tumors using oncolytic virus and chemotherapy. It can be used to explore treatment-response dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: How does the bundled treatment-response model evolve under its baseline source conditions? It runs for 10.0 time units with a communication step of 1.0. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on U, I, V, and C, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **U** peaked at **100.0** and **U** moved by **52.610** native units across 10.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Ontah2019 - Dynamic analysis of a tumor treatment model using oncolytic virus and chemotherapy with saturated infection rate - run interpretation](assets/01-ontah2019-dynamic-analysis-of-a-tumor-treatment-model-using-oncolytic-virus-and-.png)

*Summary table for Ontah2019 - Dynamic analysis of a tumor treatment model using oncolytic virus and chemotherapy with saturated infection rate, reporting the scientific question, observed answer (largest change: **U** at **52.610** native units), evidence (peak observable: **U**), dominant module, and caveat.*

![Ontah2019 - Dynamic analysis of a tumor treatment model using oncolytic virus and chemotherapy with saturated infection rate - timeseries visualization](assets/02-ontah2019-dynamic-analysis-of-a-tumor-treatment-model-using-oncolytic-virus-and-.png)

*Trajectories of U, I, V, and C across the 10.0 simulation. In this run **C** climbed from 30.000 to 35.971 and **U** fell from 100.0 to 47.393 — the largest movements among the focused observables.*

![Ontah2019 - Dynamic analysis of a tumor treatment model using oncolytic virus and chemotherapy with saturated infection rate - bar visualization](assets/03-ontah2019-dynamic-analysis-of-a-tumor-treatment-model-using-oncolytic-virus-and-.png)

*Endpoint ranking of the focused observables. Top 3 by final value: **U** = 47.393, **C** = 35.971, **V** = 5.414, with 1 more observable below.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000877`
- License: `CC0`
- Visual scope: Drug/treatment response and tumour-state change
- Caveat: Values are native SBML quantities; the cleanup does not reinterpret source equations.

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `model_state_1` | `oncology_sbml_ontah2019_dynamic_analysis_of_a_tumor_treatment_biomd0000000877_model.model_state_1` | U observable. |
| `model_state_2` | `oncology_sbml_ontah2019_dynamic_analysis_of_a_tumor_treatment_biomd0000000877_model.model_state_2` | I observable. |
| `model_state_3` | `oncology_sbml_ontah2019_dynamic_analysis_of_a_tumor_treatment_biomd0000000877_model.model_state_3` | V observable. |
| `model_state_4` | `oncology_sbml_ontah2019_dynamic_analysis_of_a_tumor_treatment_biomd0000000877_model.model_state_4` | C observable. |
| `state` | `oncology_sbml_ontah2019_dynamic_analysis_of_a_tumor_treatment_biomd0000000877_model.state` | Full raw SBML observable record for reproducibility and downstream visualisation. |
| `summary` | `oncology_sbml_ontah2019_dynamic_analysis_of_a_tumor_treatment_biomd0000000877_model.summary` | Change and peak summary across the simulated SBML observables. |
| `species_labels` | `oncology_sbml_ontah2019_dynamic_analysis_of_a_tumor_treatment_biomd0000000877_model.species_labels` | Mapping from selected raw SBML observable symbols to display labels. |

## Runtime

- Duration: `10.0`
- Communication step: `1.0`

## Running Locally

```bash
biosimulant labs serve .
```
