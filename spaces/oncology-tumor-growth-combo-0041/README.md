# COMBO_0041 - Oncology Tumor Growth

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
- `oncology-sbml-tang2019-pharmacology-modelling-of-aurkb-and-zak-biomd0000000940-model`: Oncology: Tang2019PharmacologyModellingOfAurkbAndZakBiomd0000000940Model
- `oncology-sbml-taoma2024-the-ssa-based-boolean-model-of-cell-cy-model2405030001-model`: Oncology: Taoma2024TheSsaBasedBooleanModelOfCellCyModel2405030001Model
- `oncology-sbml-terfve2012-signalling-in-liver-cancer-logical-mo-model1506260000-model`: Oncology: Terfve2012SignallingInLiverCancerLogicalMoModel1506260000Model

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
- oncology-sbml-tang2019-pharmacology-modelling-of-aurkb-and-zak-biomd0000000940-model :: biomodels_ebi:BIOMD0000000940 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000940
- oncology-sbml-taoma2024-the-ssa-based-boolean-model-of-cell-cy-model2405030001-model :: biomodels_ebi:MODEL2405030001 :: https://www.ebi.ac.uk/biomodels/MODEL2405030001
- oncology-sbml-terfve2012-signalling-in-liver-cancer-logical-mo-model1506260000-model :: biomodels_ebi:MODEL1506260000 :: https://www.ebi.ac.uk/biomodels/MODEL1506260000

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
