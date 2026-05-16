# Alharbi2019 - Tumor-normal model (TNM) of the development of tumor cells and their impact on normal cell dynamics

This Biosimulant lab wraps `Alharbi2019 - Tumor-normal model (TNM) of the development of tumor cells and their impact on normal cell dynamics` as a runnable oncology model with a companion visualization module.
This ordinary differential equation model of the interactions between tumor and normal cells is based on the publication:S. It can be used to explore treatment-response dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: How does the bundled treatment-response model evolve under its baseline source conditions? It runs for 10.0 time units with a communication step of 1.0. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on Tumor cells, and Normal cells, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **Tumor_cells** carried the largest peak and **Tumor_cells** moved by **1.514** native units across 10.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Alharbi2019 - Tumor-normal model (TNM) of the development of tumor cells and their impact on normal cell dynamics - run interpretation](assets/01-alharbi2019-tumor-normal-model-tnm-of-the-development-of-tumor-cells-and-their-i.png)

*Summary table for Alharbi2019 - Tumor-normal model (TNM) of the development of tumor cells and their impact on normal cell dynamics, reporting the scientific question, observed answer (largest change: **Tumor_cells** at **1.514** native units), evidence (peak observable: **Tumor_cells**), dominant module, and caveat.*

![Alharbi2019 - Tumor-normal model (TNM) of the development of tumor cells and their impact on normal cell dynamics - timeseries visualization](assets/02-alharbi2019-tumor-normal-model-tnm-of-the-development-of-tumor-cells-and-their-i.png)

*Trajectories of Tumor cells, and Normal cells across the 10.0 simulation. In this run **Tumor cells** climbed from 1.000 to 2.514 and **Normal cells** fell from 1.000 to 3.46e-08 — the largest movements among the focused observables.*

![Alharbi2019 - Tumor-normal model (TNM) of the development of tumor cells and their impact on normal cell dynamics - bar visualization](assets/03-alharbi2019-tumor-normal-model-tnm-of-the-development-of-tumor-cells-and-their-i.png)

*Endpoint ranking of the focused observables. Top 2 by final value: **Tumor cells** = 2.514, **Normal cells** = 3.46e-08.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000001037`
- License: `CC0`
- Visual scope: Drug/treatment response and tumour-state change
- Caveat: Values are native SBML quantities; the cleanup does not reinterpret source equations.

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Tumor cells | `oncology_sbml_alharbi2019_tumor_normal_model_tnm_of_the_develo_biomd0000001037_model.initial_tumor_cells` | `1.0` | Initial Tumor cells. Sets the initial value of bundled SBML symbol `Tumor_cells`. |
| Normal cells | `oncology_sbml_alharbi2019_tumor_normal_model_tnm_of_the_develo_biomd0000001037_model.initial_normal_cells` | `1.0` | Initial Normal cells. Sets the initial value of bundled SBML symbol `Normal_cells`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `tumor_cells` | `oncology_sbml_alharbi2019_tumor_normal_model_tnm_of_the_develo_biomd0000001037_model.tumor_cells` | Tumor cells observable. |
| `normal_cells` | `oncology_sbml_alharbi2019_tumor_normal_model_tnm_of_the_develo_biomd0000001037_model.normal_cells` | Normal cells observable. |
| `state` | `oncology_sbml_alharbi2019_tumor_normal_model_tnm_of_the_develo_biomd0000001037_model.state` | Full raw SBML observable record for reproducibility and downstream visualisation. |
| `summary` | `oncology_sbml_alharbi2019_tumor_normal_model_tnm_of_the_develo_biomd0000001037_model.summary` | Change and peak summary across the simulated SBML observables. |
| `species_labels` | `oncology_sbml_alharbi2019_tumor_normal_model_tnm_of_the_develo_biomd0000001037_model.species_labels` | Mapping from selected raw SBML observable symbols to display labels. |

## Runtime

- Duration: `10.0`
- Communication step: `1.0`

## Running Locally

```bash
biosimulant labs serve .
```
