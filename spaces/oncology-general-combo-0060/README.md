# COMBO_0060 - Oncology General

## Scientific Question
How do general mechanisms compare across these models?

## Biological Context
Tumor growth, treatment response, and cell fate interactions.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `oncology-sbml-depillis2008-optimal-control-of-mixed-immunother-biomd0000000913-model`: Oncology: Depillis2008OptimalControlOfMixedImmunotherBiomd0000000913Model
- `oncology-sbml-dritschel2018-a-mathematical-model-of-cytotoxic-biomd0000000763-model`: Oncology: Dritschel2018AMathematicalModelOfCytotoxicBiomd0000000763Model
- `oncology-sbml-ghaffari2019-thrombomodulin-gene-expression-afte-model1907140001-model`: Oncology: Ghaffari2019ThrombomodulinGeneExpressionAfteModel1907140001Model
- `oncology-sbml-hesse2021-interplay-between-core-clock-and-cance-model2109140001-model`: Oncology: Hesse2021InterplayBetweenCoreClockAndCanceModel2109140001Model

## Wiring Rationale
- Comparative (non-causal) mode: no direct causal links were created.

## Visualization Strategy
- Monitor-driven visualization is required for this space.
- State streams are routed into explicit monitor ports (`state_a..state_d`) to avoid signal overwrite.
- At minimum, monitor visuals include one timeseries panel and one summary table.
- Rationale: A dedicated monitor model receives all participating model state streams (`state_a..state_d`) so trajectories can be compared in one place without claiming causal coupling when IO semantics are incomplete.

## Expected Behaviors
- Model output trajectories under shared runtime settings.
- Cross-model agreement/divergence in key state or metric signals.
- Relative behavior comparison without causal linkage claims.

## Known Limitations
- No new biology is introduced beyond what upstream models encode.
- Cross-model semantic matching is rule-based and may under-connect uncertain routes.

## Source Provenance
- oncology-sbml-depillis2008-optimal-control-of-mixed-immunother-biomd0000000913-model :: biomodels_ebi:BIOMD0000000913 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000913
- oncology-sbml-dritschel2018-a-mathematical-model-of-cytotoxic-biomd0000000763-model :: biomodels_ebi:BIOMD0000000763 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000763
- oncology-sbml-ghaffari2019-thrombomodulin-gene-expression-afte-model1907140001-model :: biomodels_ebi:MODEL1907140001 :: https://www.ebi.ac.uk/biomodels/MODEL1907140001
- oncology-sbml-hesse2021-interplay-between-core-clock-and-cance-model2109140001-model :: biomodels_ebi:MODEL2109140001 :: https://www.ebi.ac.uk/biomodels/MODEL2109140001

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
