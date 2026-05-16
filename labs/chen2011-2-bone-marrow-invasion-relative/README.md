# Chen2011/2 - bone marrow invasion relative model

This Biosimulant lab wraps `Chen2011/2 - bone marrow invasion relative model` as a runnable oncology model with a companion visualization module.
The paper describes a model of tumor invasion to bone marrow. It can be used to explore treatment-response dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: What oncology-relevant state dominates the bundled SBML simulation over the baseline run? It runs for 10.0 time units with a communication step of 1.0. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on H, and T, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **H** peaked at **0.8737** and **H** moved by **0.3737** native units across 10.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Chen2011/2 - bone marrow invasion relative model - run interpretation](assets/01-chen2011-2-bone-marrow-invasion-relative-model-run-interpretation.png)

*Summary table for Chen2011/2 - bone marrow invasion relative model, reporting the scientific question, observed answer (largest change: **H** at **0.3737** native units), evidence (peak observable: **H**), dominant module, and caveat.*

![Chen2011/2 - bone marrow invasion relative model - timeseries visualization](assets/02-chen2011-2-bone-marrow-invasion-relative-model-selected-oncology-states.png)

*Trajectories of H, and T across the 10.0 simulation. In this run **H** climbed from 0.5000 to 0.8737 — the largest movements among the focused observables.*

![Chen2011/2 - bone marrow invasion relative model - bar visualization](assets/03-chen2011-2-bone-marrow-invasion-relative-model-latest-selected-values.png)

*Endpoint ranking of the focused observables. Top 2 by final value: **H** = 0.8737, **T** = 0.00012.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000795`
- License: `CC0`
- Visual scope: Tumor-system state trajectories and dominant observable changes
- Caveat: Values are native SBML quantities; the cleanup does not reinterpret source equations.

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `model_state_1` | `oncology_sbml_chen2011_2_bone_marrow_invasion_relative_model_biomd0000000795_model.model_state_1` | H observable. |
| `model_state_2` | `oncology_sbml_chen2011_2_bone_marrow_invasion_relative_model_biomd0000000795_model.model_state_2` | T observable. |
| `state` | `oncology_sbml_chen2011_2_bone_marrow_invasion_relative_model_biomd0000000795_model.state` | Full raw SBML observable record for reproducibility and downstream visualisation. |
| `summary` | `oncology_sbml_chen2011_2_bone_marrow_invasion_relative_model_biomd0000000795_model.summary` | Change and peak summary across the simulated SBML observables. |
| `species_labels` | `oncology_sbml_chen2011_2_bone_marrow_invasion_relative_model_biomd0000000795_model.species_labels` | Mapping from selected raw SBML observable symbols to display labels. |

## Runtime

- Duration: `10.0`
- Communication step: `1.0`

## Running Locally

```bash
biosimulant labs serve .
```
