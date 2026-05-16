# Jenner2018 - treatment of oncolytic virus

This Biosimulant lab wraps `Jenner2018 - treatment of oncolytic virus` as a runnable oncology model with a companion visualization module.
The paper describes a model of oncolytic virotherapy. It can be used to explore treatment-response dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: How does the bundled treatment-response model evolve under its baseline source conditions? It runs for 10.0 time units with a communication step of 1.0. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on S, V, and I, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **S** peaked at **5.29e+08** and **S** moved by **2.78e+08** native units across 10.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Jenner2018 - treatment of oncolytic virus - run interpretation](assets/01-jenner2018-treatment-of-oncolytic-virus-run-interpretation.png)

*Summary table for Jenner2018 - treatment of oncolytic virus, reporting the scientific question, observed answer (largest change: **S** at **2.78e+08** native units), evidence (peak observable: **S**), dominant module, and caveat.*

![Jenner2018 - treatment of oncolytic virus - timeseries visualization](assets/02-jenner2018-treatment-of-oncolytic-virus-selected-oncology-states.png)

*Trajectories of S, V, and I across the 10.0 simulation. In this run **S** climbed from 2.51e+08 to 5.29e+08 — the largest movements among the focused observables.*

![Jenner2018 - treatment of oncolytic virus - bar visualization](assets/03-jenner2018-treatment-of-oncolytic-virus-latest-selected-values.png)

*Endpoint ranking of the focused observables. Top 3 by final value: **S** = 5.29e+08, **V** = 0, **I** = 0.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000789`
- License: `CC0`
- Visual scope: Drug/treatment response and tumour-state change
- Caveat: Values are native SBML quantities; the cleanup does not reinterpret source equations.

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `model_state_1` | `oncology_sbml_jenner2018_treatment_of_oncolytic_virus_biomd0000000789_model.model_state_1` | S observable. |
| `model_state_2` | `oncology_sbml_jenner2018_treatment_of_oncolytic_virus_biomd0000000789_model.model_state_2` | V observable. |
| `model_state_3` | `oncology_sbml_jenner2018_treatment_of_oncolytic_virus_biomd0000000789_model.model_state_3` | I observable. |
| `state` | `oncology_sbml_jenner2018_treatment_of_oncolytic_virus_biomd0000000789_model.state` | Full raw SBML observable record for reproducibility and downstream visualisation. |
| `summary` | `oncology_sbml_jenner2018_treatment_of_oncolytic_virus_biomd0000000789_model.summary` | Change and peak summary across the simulated SBML observables. |
| `species_labels` | `oncology_sbml_jenner2018_treatment_of_oncolytic_virus_biomd0000000789_model.species_labels` | Mapping from selected raw SBML observable symbols to display labels. |

## Runtime

- Duration: `10.0`
- Communication step: `1.0`

## Running Locally

```bash
biosimulant labs serve .
```
