# Chen2011/1 - bone marrow invasion absolute model

This Biosimulant lab wraps `Chen2011/1 - bone marrow invasion absolute model` as a runnable oncology model with a companion visualization module.
The paper describes a model of tumor invasion to bone marrow. It can be used to explore treatment-response dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: What oncology-relevant state dominates the bundled SBML simulation over the baseline run? It runs for 10.0 time units with a communication step of 1.0. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on H, and T, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **H** peaked at **0.6000** and **H** moved by **0.0637** native units across 10.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Chen2011/1 - bone marrow invasion absolute model - run interpretation](assets/01-chen2011-1-bone-marrow-invasion-absolute-model-run-interpretation.png)

*Summary table for Chen2011/1 - bone marrow invasion absolute model, reporting the scientific question, observed answer (largest change: **H** at **0.0637** native units), evidence (peak observable: **H**), dominant module, and caveat.*

![Chen2011/1 - bone marrow invasion absolute model - timeseries visualization](assets/02-chen2011-1-bone-marrow-invasion-absolute-model-selected-oncology-states.png)

*Trajectories of H, and T across the 10.0 simulation. In this run **T** climbed from 0.0001 to 0.000345 and **H** fell from 0.6000 to 0.5363 — the largest movements among the focused observables.*

![Chen2011/1 - bone marrow invasion absolute model - bar visualization](assets/03-chen2011-1-bone-marrow-invasion-absolute-model-latest-selected-values.png)

*Endpoint ranking of the focused observables. Top 2 by final value: **H** = 0.5363, **T** = 0.000345.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000793`
- License: `CC0`
- Visual scope: Tumor-system state trajectories and dominant observable changes
- Caveat: Values are native SBML quantities; the cleanup does not reinterpret source equations.

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `model_state_1` | `oncology_sbml_chen2011_1_bone_marrow_invasion_absolute_model_biomd0000000793_model.model_state_1` | H observable. |
| `model_state_2` | `oncology_sbml_chen2011_1_bone_marrow_invasion_absolute_model_biomd0000000793_model.model_state_2` | T observable. |
| `state` | `oncology_sbml_chen2011_1_bone_marrow_invasion_absolute_model_biomd0000000793_model.state` | Full raw SBML observable record for reproducibility and downstream visualisation. |
| `summary` | `oncology_sbml_chen2011_1_bone_marrow_invasion_absolute_model_biomd0000000793_model.summary` | Change and peak summary across the simulated SBML observables. |
| `species_labels` | `oncology_sbml_chen2011_1_bone_marrow_invasion_absolute_model_biomd0000000793_model.species_labels` | Mapping from selected raw SBML observable symbols to display labels. |

## Runtime

- Duration: `10.0`
- Communication step: `1.0`

## Running Locally

```bash
biosimulant labs serve .
```
