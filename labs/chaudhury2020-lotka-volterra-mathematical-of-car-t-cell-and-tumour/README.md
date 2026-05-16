# Chaudhury2020 - Lotka-Volterra mathematical model of CAR-T cell and tumour kinetics

This Biosimulant lab wraps `Chaudhury2020 - Lotka-Volterra mathematical model of CAR-T cell and tumour kinetics` as a runnable oncology model with a companion visualization module.
This ordinary differential equation model of the cellular kinetics and pharmacodynamics of CAR-T cell therapy is described in the publication:Chaudhury, A., Zhu, X., Chu, L., Goliaei, A., June, C., Ke. It can be used to explore treatment-response dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: How does the bundled treatment-response model evolve under its baseline source conditions? It runs for 10.0 time units with a communication step of 1.0. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on Tumor cells, and Expanding CAR T cells, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **Expanding_CAR_T_cells** carried the largest peak and **Expanding_CAR_T_cells** moved by **8313.0** native units across 10.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Chaudhury2020 - Lotka-Volterra mathematical model of CAR-T cell and tumour kinetics - run interpretation](assets/01-chaudhury2020-lotka-volterra-mathematical-model-of-car-t-cell-and-tumour-kinetic.png)

*Summary table for Chaudhury2020 - Lotka-Volterra mathematical model of CAR-T cell and tumour kinetics, reporting the scientific question, observed answer (largest change: **Expanding_CAR_T_cells** at **8313.0** native units), evidence (peak observable: **Expanding_CAR_T_cells**), dominant module, and caveat.*

![Chaudhury2020 - Lotka-Volterra mathematical model of CAR-T cell and tumour kinetics - timeseries visualization](assets/02-chaudhury2020-lotka-volterra-mathematical-model-of-car-t-cell-and-tumour-kinetic.png)

*Trajectories of Tumor cells, and Expanding CAR T cells across the 10.0 simulation. In this run **Expanding CAR T cells** climbed from 10.000 to 8323.4 and **Tumor cells** fell from 900.0 to 0.1603 — the largest movements among the focused observables.*

![Chaudhury2020 - Lotka-Volterra mathematical model of CAR-T cell and tumour kinetics - bar visualization](assets/03-chaudhury2020-lotka-volterra-mathematical-model-of-car-t-cell-and-tumour-kinetic.png)

*Endpoint ranking of the focused observables. Top 2 by final value: **Expanding CAR T cells** = 8323.4, **Tumor cells** = 0.1603.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000001024`
- License: `CC0`
- Visual scope: Drug/treatment response and tumour-state change
- Caveat: Values are native SBML quantities; the cleanup does not reinterpret source equations.

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Tumor cells | `oncology_sbml_chaudhury2020_lotka_volterra_mathematical_model_biomd0000001024_model.initial_tumor_cells` | `900.0` | Initial Tumor cells. Sets the initial value of bundled SBML symbol `Tumor_cells`. |
| Expanding CAR T cells | `oncology_sbml_chaudhury2020_lotka_volterra_mathematical_model_biomd0000001024_model.initial_expanding_car_t_cells` | `10.0` | Initial Expanding CAR T cells. Sets the initial value of bundled SBML symbol `Expanding_CAR_T_cells`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `tumor_cells` | `oncology_sbml_chaudhury2020_lotka_volterra_mathematical_model_biomd0000001024_model.tumor_cells` | Tumor cells observable. |
| `expanding_car_t_cells` | `oncology_sbml_chaudhury2020_lotka_volterra_mathematical_model_biomd0000001024_model.expanding_car_t_cells` | Expanding CAR T cells observable. |
| `state` | `oncology_sbml_chaudhury2020_lotka_volterra_mathematical_model_biomd0000001024_model.state` | Full raw SBML observable record for reproducibility and downstream visualisation. |
| `summary` | `oncology_sbml_chaudhury2020_lotka_volterra_mathematical_model_biomd0000001024_model.summary` | Change and peak summary across the simulated SBML observables. |
| `species_labels` | `oncology_sbml_chaudhury2020_lotka_volterra_mathematical_model_biomd0000001024_model.species_labels` | Mapping from selected raw SBML observable symbols to display labels. |

## Runtime

- Duration: `10.0`
- Communication step: `1.0`

## Running Locally

```bash
biosimulant labs serve .
```
