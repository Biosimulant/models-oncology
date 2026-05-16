# Monro2008 - chemotherapy resistance

This Biosimulant lab wraps `Monro2008 - chemotherapy resistance` as a runnable oncology model with a companion visualization module.
The paper describes a model of resistance of cancer to chemotherapy. It can be used to explore treatment-response dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: How does the bundled treatment-response model evolve under its baseline source conditions? It runs for 10.0 time units with a communication step of 1.0. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on S, and R, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **S** peaked at **1e+10** and **S** moved by **2.52e+09** native units across 10.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Monro2008 - chemotherapy resistance - run interpretation](assets/01-monro2008-chemotherapy-resistance-run-interpretation.png)

*Summary table for Monro2008 - chemotherapy resistance, reporting the scientific question, observed answer (largest change: **S** at **2.52e+09** native units), evidence (peak observable: **S**), dominant module, and caveat.*

![Monro2008 - chemotherapy resistance - timeseries visualization](assets/02-monro2008-chemotherapy-resistance-selected-oncology-states.png)

*Trajectories of S, and R across the 10.0 simulation. In this run **R** climbed from 2e+05 to 2.7e+05 and **S** fell from 1e+10 to 7.48e+09 — the largest movements among the focused observables.*

![Monro2008 - chemotherapy resistance - bar visualization](assets/03-monro2008-chemotherapy-resistance-latest-selected-values.png)

*Endpoint ranking of the focused observables. Top 2 by final value: **S** = 7.48e+09, **R** = 2.7e+05.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000776`
- License: `CC0`
- Visual scope: Drug/treatment response and tumour-state change
- Caveat: Values are native SBML quantities; the cleanup does not reinterpret source equations.

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `model_state_1` | `oncology_sbml_monro2008_chemotherapy_resistance_biomd0000000776_model.model_state_1` | S observable. |
| `model_state_2` | `oncology_sbml_monro2008_chemotherapy_resistance_biomd0000000776_model.model_state_2` | R observable. |
| `state` | `oncology_sbml_monro2008_chemotherapy_resistance_biomd0000000776_model.state` | Full raw SBML observable record for reproducibility and downstream visualisation. |
| `summary` | `oncology_sbml_monro2008_chemotherapy_resistance_biomd0000000776_model.summary` | Change and peak summary across the simulated SBML observables. |
| `species_labels` | `oncology_sbml_monro2008_chemotherapy_resistance_biomd0000000776_model.species_labels` | Mapping from selected raw SBML observable symbols to display labels. |

## Runtime

- Duration: `10.0`
- Communication step: `1.0`

## Running Locally

```bash
biosimulant labs serve .
```
