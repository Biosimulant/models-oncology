# COMBO_0080 - Oncology Tumor Growth

## Scientific Question
How do tumor growth mechanisms compare across these models?

## Biological Context
Tumor growth, treatment response, and cell fate interactions.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `oncology-sbml-chen2011-2-bone-marrow-invasion-relative-model-biomd0000000795-model`: Oncology: Chen20112BoneMarrowInvasionRelativeModelBiomd0000000795Model
- `oncology-sbml-claret2009-predicting-phase-iii-overall-survival-model1708310001-model`: Oncology: Claret2009PredictingPhaseIiiOverallSurvivalModel1708310001Model
- `oncology-sbml-coletti2020-qsp-model-of-prostate-cancer-immunot-model2109110002-model`: Oncology: Coletti2020QspModelOfProstateCancerImmunotModel2109110002Model
- `oncology-sbml-depillis2003-the-dynamics-of-an-optimally-contro-biomd0000000909-model`: Oncology: Depillis2003TheDynamicsOfAnOptimallyControBiomd0000000909Model

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
- oncology-sbml-chen2011-2-bone-marrow-invasion-relative-model-biomd0000000795-model :: biomodels_ebi:BIOMD0000000795 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000795
- oncology-sbml-claret2009-predicting-phase-iii-overall-survival-model1708310001-model :: biomodels_ebi:MODEL1708310001 :: https://www.ebi.ac.uk/biomodels/MODEL1708310001
- oncology-sbml-coletti2020-qsp-model-of-prostate-cancer-immunot-model2109110002-model :: biomodels_ebi:MODEL2109110002 :: https://www.ebi.ac.uk/biomodels/MODEL2109110002
- oncology-sbml-depillis2003-the-dynamics-of-an-optimally-contro-biomd0000000909-model :: biomodels_ebi:BIOMD0000000909 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000909

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
