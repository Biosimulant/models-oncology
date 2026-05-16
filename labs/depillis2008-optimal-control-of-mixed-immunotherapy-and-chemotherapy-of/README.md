# dePillis2008 - Optimal control of mixed immunotherapy and chemotherapy of tumors

This Biosimulant lab wraps `dePillis2008 - Optimal control of mixed immunotherapy and chemotherapy of tumors` as a runnable oncology model with a companion visualization module.
&amp;lt;notes xmlns=&amp;quot;http://www.sbml.org/sbml/level2/version4&amp;quot;&amp;gt; &amp;lt;body xmlns=&amp;quot;http://www.w3.org/1999/xhtml&amp;quot;&amp;gt; &amp;lt;pre&amp;gt;Optimal control. It can be used to explore treatment-response dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: How does the bundled treatment-response model evolve under its baseline source conditions? It runs for 10.0 time units with a communication step of 1.0. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on T, L, N, C, I, and M, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **C** peaked at **4.17e+10** and **C** moved by **3.41e+06** native units across 10.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![dePillis2008 - Optimal control of mixed immunotherapy and chemotherapy of tumors - run interpretation](assets/01-depillis2008-optimal-control-of-mixed-immunotherapy-and-chemotherapy-of-tumors-r.png)

*Summary table for dePillis2008 - Optimal control of mixed immunotherapy and chemotherapy of tumors, reporting the scientific question, observed answer (largest change: **C** at **3.41e+06** native units), evidence (peak observable: **C**), dominant module, and caveat.*

![dePillis2008 - Optimal control of mixed immunotherapy and chemotherapy of tumors - timeseries visualization](assets/02-depillis2008-optimal-control-of-mixed-immunotherapy-and-chemotherapy-of-tumors-s.png)

*Trajectories of T, L, N, C, I, and M across the 10.0 simulation. In this run **C** fell from 4.17e+10 to 4.17e+10 — the largest movements among the focused observables.*

![dePillis2008 - Optimal control of mixed immunotherapy and chemotherapy of tumors - bar visualization](assets/03-depillis2008-optimal-control-of-mixed-immunotherapy-and-chemotherapy-of-tumors-l.png)

*Endpoint ranking of the focused observables. Top 3 by final value: **C** = 4.17e+10, **T** = 8.24e+06, **N** = 1.56e+04, with 3 more observables below.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000913`
- License: `CC0`
- Visual scope: Drug/treatment response and tumour-state change
- Caveat: Values are native SBML quantities; the cleanup does not reinterpret source equations.

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `model_state_1` | `oncology_sbml_depillis2008_optimal_control_of_mixed_immunother_biomd0000000913_model.model_state_1` | T observable. |
| `model_state_2` | `oncology_sbml_depillis2008_optimal_control_of_mixed_immunother_biomd0000000913_model.model_state_2` | L observable. |
| `model_state_3` | `oncology_sbml_depillis2008_optimal_control_of_mixed_immunother_biomd0000000913_model.model_state_3` | N observable. |
| `model_state_4` | `oncology_sbml_depillis2008_optimal_control_of_mixed_immunother_biomd0000000913_model.model_state_4` | C observable. |
| `model_state_5` | `oncology_sbml_depillis2008_optimal_control_of_mixed_immunother_biomd0000000913_model.model_state_5` | I observable. |
| `model_state_6` | `oncology_sbml_depillis2008_optimal_control_of_mixed_immunother_biomd0000000913_model.model_state_6` | M observable. |
| `state` | `oncology_sbml_depillis2008_optimal_control_of_mixed_immunother_biomd0000000913_model.state` | Full raw SBML observable record for reproducibility and downstream visualisation. |
| `summary` | `oncology_sbml_depillis2008_optimal_control_of_mixed_immunother_biomd0000000913_model.summary` | Change and peak summary across the simulated SBML observables. |
| `species_labels` | `oncology_sbml_depillis2008_optimal_control_of_mixed_immunother_biomd0000000913_model.species_labels` | Mapping from selected raw SBML observable symbols to display labels. |

## Runtime

- Duration: `10.0`
- Communication step: `1.0`

## Running Locally

```bash
biosimulant labs serve .
```
