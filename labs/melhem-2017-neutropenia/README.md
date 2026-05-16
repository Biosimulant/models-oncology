# Melhem 2017 - Neutropenia Model

This Biosimulant lab wraps `Melhem 2017 - Neutropenia Model` as a runnable oncology model with a companion visualization module.
The objective of the present study was to use pharmacokinetic–pharmacodynamic modelling to characterize the effects of chemotherapy on the granulopoietic system and to predict the absolute neutrophil. It can be used to explore treatment-response dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: How does the bundled treatment-response model evolve under its baseline source conditions? It runs for 10.0 time units with a communication step of 1.0. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on Chm, Crt, Dt, Mt, Pm1, and Pm2, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **Chm** peaked at **142.5** and **Chm** moved by **0.0258** native units across 10.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Melhem 2017 - Neutropenia Model - run interpretation](assets/01-melhem-2017-neutropenia-model-run-interpretation.png)

*Summary table for Melhem 2017 - Neutropenia Model, reporting the scientific question, observed answer (largest change: **Chm** at **0.0258** native units), evidence (peak observable: **Chm**), dominant module, and caveat.*

![Melhem 2017 - Neutropenia Model - timeseries visualization](assets/02-melhem-2017-neutropenia-model-selected-oncology-states.png)

*Trajectories of Chm, Crt, Dt, Mt, Pm1, and Pm2 across the 10.0 simulation. In this run **Dt** climbed from 0 to 4.9e-12 and **Chm** fell from 142.5 to 142.5 — the largest movements among the focused observables.*

![Melhem 2017 - Neutropenia Model - bar visualization](assets/03-melhem-2017-neutropenia-model-latest-selected-values.png)

*Endpoint ranking of the focused observables. Top 3 by final value: **Chm** = 142.5, **Crt** = 19.990, **Pm2** = 8.36e-10, with 3 more observables below.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:MODEL2211040001`
- License: `CC0`
- Visual scope: Drug/treatment response and tumour-state change
- Caveat: Values are native SBML quantities; the cleanup does not reinterpret source equations.

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Chm | `oncology_sbml_melhem_2017_neutropenia_model_model2211040001_model.initial_chm` | `0.0` | Initial Chm. Sets the initial value of bundled SBML symbol `Chm`. |
| Crt | `oncology_sbml_melhem_2017_neutropenia_model_model2211040001_model.initial_crt` | `0.0` | Initial Crt. Sets the initial value of bundled SBML symbol `Crt`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `chm` | `oncology_sbml_melhem_2017_neutropenia_model_model2211040001_model.chm` | Chm observable. |
| `crt` | `oncology_sbml_melhem_2017_neutropenia_model_model2211040001_model.crt` | Crt observable. |
| `model_state_3` | `oncology_sbml_melhem_2017_neutropenia_model_model2211040001_model.model_state_3` | Dt observable. |
| `model_state_4` | `oncology_sbml_melhem_2017_neutropenia_model_model2211040001_model.model_state_4` | Mt observable. |
| `pm1` | `oncology_sbml_melhem_2017_neutropenia_model_model2211040001_model.pm1` | Pm1 observable. |
| `pm2` | `oncology_sbml_melhem_2017_neutropenia_model_model2211040001_model.pm2` | Pm2 observable. |
| `state` | `oncology_sbml_melhem_2017_neutropenia_model_model2211040001_model.state` | Full raw SBML observable record for reproducibility and downstream visualisation. |
| `summary` | `oncology_sbml_melhem_2017_neutropenia_model_model2211040001_model.summary` | Change and peak summary across the simulated SBML observables. |
| `species_labels` | `oncology_sbml_melhem_2017_neutropenia_model_model2211040001_model.species_labels` | Mapping from selected raw SBML observable symbols to display labels. |

## Runtime

- Duration: `10.0`
- Communication step: `1.0`

## Running Locally

```bash
biosimulant labs serve .
```
