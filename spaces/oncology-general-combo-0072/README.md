# COMBO_0072 - Oncology General

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
- `oncology-sbml-jiao2018-feedback-regulation-in-a-stem-cell-mode-biomd0000000898-model`: Oncology: Jiao2018FeedbackRegulationInAStemCellModeBiomd0000000898Model
- `oncology-sbml-lolas2016-tumour-induced-neoneurogenesis-and-per-biomd0000000750-model`: Oncology: Lolas2016TumourInducedNeoneurogenesisAndPerBiomd0000000750Model
- `oncology-sbml-moore-2004-mathematical-model-for-cml-and-t-cell-biomd0000000733-model`: Oncology: Moore2004MathematicalModelForCmlAndTCellBiomd0000000733Model
- `oncology-sbml-nikolaev2019-immunobiochemical-reconstruction-of-biomd0000000865-model`: Oncology: Nikolaev2019ImmunobiochemicalReconstructionOfBiomd0000000865Model

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
- oncology-sbml-jiao2018-feedback-regulation-in-a-stem-cell-mode-biomd0000000898-model :: biomodels_ebi:BIOMD0000000898 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000898
- oncology-sbml-lolas2016-tumour-induced-neoneurogenesis-and-per-biomd0000000750-model :: biomodels_ebi:BIOMD0000000750 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000750
- oncology-sbml-moore-2004-mathematical-model-for-cml-and-t-cell-biomd0000000733-model :: biomodels_ebi:BIOMD0000000733 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000733
- oncology-sbml-nikolaev2019-immunobiochemical-reconstruction-of-biomd0000000865-model :: biomodels_ebi:BIOMD0000000865 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000865

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
