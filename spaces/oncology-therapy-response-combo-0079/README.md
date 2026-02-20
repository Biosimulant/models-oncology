# COMBO_0079 - Oncology Therapy Response

## Scientific Question
How do therapy response mechanisms compare across these models?

## Biological Context
Tumor growth, treatment response, and cell fate interactions.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `oncology-sbml-melhem-2017-neutropenia-model-model2211040001-model`: Oncology: Melhem2017NeutropeniaModelModel2211040001Model
- `oncology-sbml-mpekris2017-role-of-vascular-normalization-in-be-model2001200002-model`: Oncology: Mpekris2017RoleOfVascularNormalizationInBeModel2001200002Model
- `oncology-sbml-perez-garcia19-computational-design-of-improved-biomd0000000814-model`: Oncology: PerezGarcia19ComputationalDesignOfImprovedBiomd0000000814Model
- `oncology-sbml-rodrigues2019-a-mathematical-model-for-chemoimmu-biomd0000000879-model`: Oncology: Rodrigues2019AMathematicalModelForChemoimmuBiomd0000000879Model

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
- oncology-sbml-melhem-2017-neutropenia-model-model2211040001-model :: biomodels_ebi:MODEL2211040001 :: https://www.ebi.ac.uk/biomodels/MODEL2211040001
- oncology-sbml-mpekris2017-role-of-vascular-normalization-in-be-model2001200002-model :: biomodels_ebi:MODEL2001200002 :: https://www.ebi.ac.uk/biomodels/MODEL2001200002
- oncology-sbml-perez-garcia19-computational-design-of-improved-biomd0000000814-model :: biomodels_ebi:BIOMD0000000814 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000814
- oncology-sbml-rodrigues2019-a-mathematical-model-for-chemoimmu-biomd0000000879-model :: biomodels_ebi:BIOMD0000000879 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000879

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
