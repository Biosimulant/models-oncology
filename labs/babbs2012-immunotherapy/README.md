# Babbs2012 - immunotherapy

This Biosimulant lab wraps `Babbs2012 - immunotherapy` as a runnable oncology model with a companion visualization module.
The paper describes a simple model of tumor immunotherapy. It can be used to explore treatment-response dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: How does the bundled treatment-response model evolve under its baseline source conditions? It runs for 10.0 time units with a communication step of 1.0. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on T, and I, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **T** peaked at **1.002** and **T** moved by **0.00159** native units across 10.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Babbs2012 - immunotherapy - run interpretation](assets/01-babbs2012-immunotherapy-run-interpretation.png)

*Summary table for Babbs2012 - immunotherapy, reporting the scientific question, observed answer (largest change: **T** at **0.00159** native units), evidence (peak observable: **T**), dominant module, and caveat.*

![Babbs2012 - immunotherapy - timeseries visualization](assets/02-babbs2012-immunotherapy-selected-oncology-states.png)

*Trajectories of T, and I across the 10.0 simulation. In this run **T** climbed from 1.000 to 1.002 and **I** fell from 0.001 to 0.000914 — the largest movements among the focused observables.*

![Babbs2012 - immunotherapy - bar visualization](assets/03-babbs2012-immunotherapy-latest-selected-values.png)

*Endpoint ranking of the focused observables. Top 2 by final value: **T** = 1.002, **I** = 0.000914.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000758`
- License: `CC0`
- Visual scope: Drug/treatment response and tumour-state change
- Caveat: Values are native SBML quantities; the cleanup does not reinterpret source equations.

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `model_state_1` | `oncology_sbml_babbs2012_immunotherapy_biomd0000000758_model.model_state_1` | T observable. |
| `model_state_2` | `oncology_sbml_babbs2012_immunotherapy_biomd0000000758_model.model_state_2` | I observable. |
| `state` | `oncology_sbml_babbs2012_immunotherapy_biomd0000000758_model.state` | Full raw SBML observable record for reproducibility and downstream visualisation. |
| `summary` | `oncology_sbml_babbs2012_immunotherapy_biomd0000000758_model.summary` | Change and peak summary across the simulated SBML observables. |
| `species_labels` | `oncology_sbml_babbs2012_immunotherapy_biomd0000000758_model.species_labels` | Mapping from selected raw SBML observable symbols to display labels. |

## Runtime

- Duration: `10.0`
- Communication step: `1.0`

## Running Locally

```bash
biosimulant labs serve .
```
