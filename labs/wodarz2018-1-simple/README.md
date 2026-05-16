# Wodarz2018/1 - simple model

This Biosimulant lab wraps `Wodarz2018/1 - simple model` as a runnable oncology model with a companion visualization module.
The paper describes a basic model of effect of cellular de-differentiation on the dynamics and evolution of tissue and tumor cells. It can be used to explore treatment-response dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: What oncology-relevant state dominates the bundled SBML simulation over the baseline run? It runs for 10.0 time units with a communication step of 1.0. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on S, and D, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **S** peaked at **1.038** and **D** moved by **0.0536** native units across 10.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Wodarz2018/1 - simple model - run interpretation](assets/01-wodarz2018-1-simple-model-run-interpretation.png)

*Summary table for Wodarz2018/1 - simple model, reporting the scientific question, observed answer (largest change: **D** at **0.0536** native units), evidence (peak observable: **S**), dominant module, and caveat.*

![Wodarz2018/1 - simple model - timeseries visualization](assets/02-wodarz2018-1-simple-model-selected-oncology-states.png)

*Trajectories of S, and D across the 10.0 simulation. In this run **D** climbed from 0 to 0.0536 — the largest movements among the focused observables.*

![Wodarz2018/1 - simple model - bar visualization](assets/03-wodarz2018-1-simple-model-latest-selected-values.png)

*Endpoint ranking of the focused observables. Top 2 by final value: **S** = 1.038, **D** = 0.0536.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000774`
- License: `CC0`
- Visual scope: Tumor-system state trajectories and dominant observable changes
- Caveat: Values are native SBML quantities; the cleanup does not reinterpret source equations.

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `model_state_1` | `oncology_sbml_wodarz2018_1_simple_model_biomd0000000774_model.model_state_1` | S observable. |
| `model_state_2` | `oncology_sbml_wodarz2018_1_simple_model_biomd0000000774_model.model_state_2` | D observable. |
| `state` | `oncology_sbml_wodarz2018_1_simple_model_biomd0000000774_model.state` | Full raw SBML observable record for reproducibility and downstream visualisation. |
| `summary` | `oncology_sbml_wodarz2018_1_simple_model_biomd0000000774_model.summary` | Change and peak summary across the simulated SBML observables. |
| `species_labels` | `oncology_sbml_wodarz2018_1_simple_model_biomd0000000774_model.species_labels` | Mapping from selected raw SBML observable symbols to display labels. |

## Runtime

- Duration: `10.0`
- Communication step: `1.0`

## Running Locally

```bash
biosimulant labs serve .
```
