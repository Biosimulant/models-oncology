# Shariatpanahi2018 - Mathematical modeling of tumor-induced immunosuppression by myeloid-derived suppressor cells

This Biosimulant lab wraps `Shariatpanahi2018 - Mathematical modeling of tumor-induced immunosuppression by myeloid-derived suppressor cells` as a runnable oncology model with a companion visualization module.
This is a ODE-based mathematical model featuring equations describing the dynamics of tumor cells, cytotoxic T cells, natural killer cells, and myeloid-derived suppressor cells (MDSCs) that together d. It can be used to explore treatment-response dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: How does the bundled treatment-response model evolve under its baseline source conditions? It runs for 10.0 time units with a communication step of 1.0. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on C, N, T, and M, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **M** peaked at **5e+06** and **N** moved by **1.05e+05** native units across 10.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Shariatpanahi2018 - Mathematical modeling of tumor-induced immunosuppression by myeloid-derived suppressor cells - run interpretation](assets/01-shariatpanahi2018-mathematical-modeling-of-tumor-induced-immunosuppression-by-my.png)

*Summary table for Shariatpanahi2018 - Mathematical modeling of tumor-induced immunosuppression by myeloid-derived suppressor cells, reporting the scientific question, observed answer (largest change: **N** at **1.05e+05** native units), evidence (peak observable: **M**), dominant module, and caveat.*

![Shariatpanahi2018 - Mathematical modeling of tumor-induced immunosuppression by myeloid-derived suppressor cells - timeseries visualization](assets/02-shariatpanahi2018-mathematical-modeling-of-tumor-induced-immunosuppression-by-my.png)

*Trajectories of C, N, T, and M across the 10.0 simulation. In this run **N** climbed from 1.000 to 1.05e+05 — the largest movements among the focused observables.*

![Shariatpanahi2018 - Mathematical modeling of tumor-induced immunosuppression by myeloid-derived suppressor cells - bar visualization](assets/03-shariatpanahi2018-mathematical-modeling-of-tumor-induced-immunosuppression-by-my.png)

*Endpoint ranking of the focused observables. Top 3 by final value: **M** = 5e+06, **N** = 1.05e+05, **C** = 65.284, with 1 more observable below.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:MODEL1909090003`
- License: `CC0`
- Visual scope: Drug/treatment response and tumour-state change
- Caveat: Values are native SBML quantities; the cleanup does not reinterpret source equations.

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `model_state_1` | `oncology_sbml_shariatpanahi2018_mathematical_modeling_of_tumor_model1909090003_model.model_state_1` | C observable. |
| `model_state_2` | `oncology_sbml_shariatpanahi2018_mathematical_modeling_of_tumor_model1909090003_model.model_state_2` | N observable. |
| `model_state_3` | `oncology_sbml_shariatpanahi2018_mathematical_modeling_of_tumor_model1909090003_model.model_state_3` | T observable. |
| `model_state_4` | `oncology_sbml_shariatpanahi2018_mathematical_modeling_of_tumor_model1909090003_model.model_state_4` | M observable. |
| `state` | `oncology_sbml_shariatpanahi2018_mathematical_modeling_of_tumor_model1909090003_model.state` | Full raw SBML observable record for reproducibility and downstream visualisation. |
| `summary` | `oncology_sbml_shariatpanahi2018_mathematical_modeling_of_tumor_model1909090003_model.summary` | Change and peak summary across the simulated SBML observables. |
| `species_labels` | `oncology_sbml_shariatpanahi2018_mathematical_modeling_of_tumor_model1909090003_model.species_labels` | Mapping from selected raw SBML observable symbols to display labels. |

## Runtime

- Duration: `10.0`
- Communication step: `1.0`

## Running Locally

```bash
biosimulant labs serve .
```
