# Chaudhury2020 - EC50 expansion and killing mathematical model of CAR-T cell and tumour kinetics

This Biosimulant lab wraps `Chaudhury2020 - EC50 expansion and killing mathematical model of CAR-T cell and tumour kinetics` as a runnable oncology model with a companion visualization module.
This ordinary differential equation model of the cellular kinetics and pharmacodynamics of CAR-T cell therapy is described in the publication:Chaudhury, A., Zhu, X., Chu, L., Goliaei, A., June, C., Ke. It can be used to explore treatment-response dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: How does the bundled treatment-response model evolve under its baseline source conditions? It runs for 10.0 time units with a communication step of 1.0. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on Tumor cells, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **Tumor_cells** carried the largest peak and **Tumor_cells** moved by **826.3** native units across 10.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Chaudhury2020 - EC50 expansion and killing mathematical model of CAR-T cell and tumour kinetics - run interpretation](assets/01-chaudhury2020-ec50-expansion-and-killing-mathematical-model-of-car-t-cell-and-tu.png)

*Summary table for Chaudhury2020 - EC50 expansion and killing mathematical model of CAR-T cell and tumour kinetics, reporting the scientific question, observed answer (largest change: **Tumor_cells** at **826.3** native units), evidence (peak observable: **Tumor_cells**), dominant module, and caveat.*

![Chaudhury2020 - EC50 expansion and killing mathematical model of CAR-T cell and tumour kinetics - timeseries visualization](assets/02-chaudhury2020-ec50-expansion-and-killing-mathematical-model-of-car-t-cell-and-tu.png)

*Trajectories of Tumor cells across the 10.0 simulation. In this run **Tumor cells** fell from 900.0 to 73.681 — the largest movements among the focused observables.*

![Chaudhury2020 - EC50 expansion and killing mathematical model of CAR-T cell and tumour kinetics - bar visualization](assets/03-chaudhury2020-ec50-expansion-and-killing-mathematical-model-of-car-t-cell-and-tu.png)

*Endpoint ranking of the focused observables. Top 1 by final value: **Tumor cells** = 73.681.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000001025`
- License: `CC0`
- Visual scope: Drug/treatment response and tumour-state change
- Caveat: Values are native SBML quantities; the cleanup does not reinterpret source equations.

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Tumor cells | `oncology_sbml_chaudhury2020_ec50_expansion_and_killing_mathema_biomd0000001025_model.initial_tumor_cells` | `900.0` | Initial Tumor cells. Sets the initial value of bundled SBML symbol `Tumor_cells`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `tumor_cells` | `oncology_sbml_chaudhury2020_ec50_expansion_and_killing_mathema_biomd0000001025_model.tumor_cells` | Tumor cells observable. |
| `state` | `oncology_sbml_chaudhury2020_ec50_expansion_and_killing_mathema_biomd0000001025_model.state` | Full raw SBML observable record for reproducibility and downstream visualisation. |
| `summary` | `oncology_sbml_chaudhury2020_ec50_expansion_and_killing_mathema_biomd0000001025_model.summary` | Change and peak summary across the simulated SBML observables. |
| `species_labels` | `oncology_sbml_chaudhury2020_ec50_expansion_and_killing_mathema_biomd0000001025_model.species_labels` | Mapping from selected raw SBML observable symbols to display labels. |

## Runtime

- Duration: `10.0`
- Communication step: `1.0`

## Running Locally

```bash
biosimulant labs serve .
```
