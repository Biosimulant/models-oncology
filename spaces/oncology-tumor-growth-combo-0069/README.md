# COMBO_0069 - Oncology Tumor Growth

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
- `oncology-sbml-bayleyegn2016-interactions-of-cyce-cdk2-cdc25a-a-model2003180002-model`: Oncology: Bayleyegn2016InteractionsOfCyceCdk2Cdc25aAModel2003180002Model
- `oncology-sbml-bianconi2012-egfr-and-igf1r-pathway-in-lung-canc-biomd0000000427-model`: Oncology: Bianconi2012EgfrAndIgf1rPathwayInLungCancBiomd0000000427Model
- `oncology-sbml-boer1986-interactions-between-macrophages-and-t-model1912110001-model`: Oncology: Boer1986InteractionsBetweenMacrophagesAndTModel1912110001Model
- `oncology-sbml-bordel2018-gsmm-for-human-metabolic-reactions-hm-model1707250000-model`: Oncology: Bordel2018GsmmForHumanMetabolicReactionsHmModel1707250000Model

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
- oncology-sbml-bayleyegn2016-interactions-of-cyce-cdk2-cdc25a-a-model2003180002-model :: biomodels_ebi:MODEL2003180002 :: https://www.ebi.ac.uk/biomodels/MODEL2003180002
- oncology-sbml-bianconi2012-egfr-and-igf1r-pathway-in-lung-canc-biomd0000000427-model :: biomodels_ebi:BIOMD0000000427 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000427
- oncology-sbml-boer1986-interactions-between-macrophages-and-t-model1912110001-model :: biomodels_ebi:MODEL1912110001 :: https://www.ebi.ac.uk/biomodels/MODEL1912110001
- oncology-sbml-bordel2018-gsmm-for-human-metabolic-reactions-hm-model1707250000-model :: biomodels_ebi:MODEL1707250000 :: https://www.ebi.ac.uk/biomodels/MODEL1707250000

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
