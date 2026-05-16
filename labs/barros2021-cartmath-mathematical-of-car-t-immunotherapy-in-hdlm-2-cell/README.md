# Barros2021 - CARTmath, Mathematical Model of CAR-T Immunotherapy in HDLM-2 cell line

This Biosimulant lab wraps `Barros2021 - CARTmath, Mathematical Model of CAR-T Immunotherapy in HDLM-2 cell line` as a runnable oncology model with a companion visualization module.
A mathematical model (CART-math) studying the impact of CAR-T cells therapy on haematological cancer cell line which in this case is HDLM-2. It can be used to explore treatment-response dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: How does the bundled treatment-response model evolve under its baseline source conditions? It runs for 10.0 time units with a communication step of 1.0. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on T, Cm, and Ct, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **T** peaked at **3.33e+06** and **T** moved by **1.33e+06** native units across 10.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Barros2021 - CARTmath, Mathematical Model of CAR-T Immunotherapy in HDLM-2 cell line - run interpretation](assets/01-barros2021-cartmath-mathematical-model-of-car-t-immunotherapy-in-hdlm-2-cell-lin.png)

*Summary table for Barros2021 - CARTmath, Mathematical Model of CAR-T Immunotherapy in HDLM-2 cell line, reporting the scientific question, observed answer (largest change: **T** at **1.33e+06** native units), evidence (peak observable: **T**), dominant module, and caveat.*

![Barros2021 - CARTmath, Mathematical Model of CAR-T Immunotherapy in HDLM-2 cell line - timeseries visualization](assets/02-barros2021-cartmath-mathematical-model-of-car-t-immunotherapy-in-hdlm-2-cell-lin.png)

*Trajectories of T, Cm, and Ct across the 10.0 simulation. In this run **T** climbed from 2e+06 to 3.33e+06 — the largest movements among the focused observables.*

![Barros2021 - CARTmath, Mathematical Model of CAR-T Immunotherapy in HDLM-2 cell line - bar visualization](assets/03-barros2021-cartmath-mathematical-model-of-car-t-immunotherapy-in-hdlm-2-cell-lin.png)

*Endpoint ranking of the focused observables. Top 3 by final value: **T** = 3.33e+06, **Cm** = 0, **Ct** = 0.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000001019`
- License: `CC0`
- Visual scope: Drug/treatment response and tumour-state change
- Caveat: Logical/qualitative SBML semantics must be validated carefully; do not treat numeric trajectories as mechanistic ODEs without source support.

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Epsilon source parameter | `oncology_sbml_barros2021_cartmath_mathematical_model_of_car_t_biomd0000001019_model.epsilon_level` | `0.15` | Epsilon source parameter. Maps to bundled SBML parameter `epsilon`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `model_state_1` | `oncology_sbml_barros2021_cartmath_mathematical_model_of_car_t_biomd0000001019_model.model_state_1` | T observable. |
| `model_state_2` | `oncology_sbml_barros2021_cartmath_mathematical_model_of_car_t_biomd0000001019_model.model_state_2` | Cm observable. |
| `model_state_3` | `oncology_sbml_barros2021_cartmath_mathematical_model_of_car_t_biomd0000001019_model.model_state_3` | Ct observable. |
| `state` | `oncology_sbml_barros2021_cartmath_mathematical_model_of_car_t_biomd0000001019_model.state` | Full raw SBML observable record for reproducibility and downstream visualisation. |
| `summary` | `oncology_sbml_barros2021_cartmath_mathematical_model_of_car_t_biomd0000001019_model.summary` | Change and peak summary across the simulated SBML observables. |
| `species_labels` | `oncology_sbml_barros2021_cartmath_mathematical_model_of_car_t_biomd0000001019_model.species_labels` | Mapping from selected raw SBML observable symbols to display labels. |

## Runtime

- Duration: `10.0`
- Communication step: `1.0`

## Running Locally

```bash
biosimulant labs serve .
```
