# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Perez-Garcia19 - Computational design of improved standardized chemotherapy protocols for grade 2 oligodendrogliomas."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class PerezGarcia19ComputationalDesignOfImprovedBiomd0000000814Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000814'
    _TITLE = 'Perez-Garcia19 - Computational design of improved standardized chemotherapy protocols for grade 2 oligodendrogliomas'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Drug_Concentration_C', 'Tumor_Cell_Population_P', 'Damaged_Tumor_Cells_D']
    _SPECIES_LABELS = {'Damaged_Tumor_Cells_D': 'Damaged Tumor Cells D', 'Tumor_Cell_Population_P': 'Tumor Cell Population P', 'Drug_Concentration_C': 'Drug Concentration C'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'dose_5': ('dose_5', 0.0, 'native SBML value', 'Dose 5 source parameter. Maps to bundled SBML parameter `dose_5`.'), 'dose_4': ('dose_4', 0.0, 'native SBML value', 'Dose 4 source parameter. Maps to bundled SBML parameter `dose_4`.'), 'dose3': ('dose3', 0.0, 'native SBML value', 'Dose3 source parameter. Maps to bundled SBML parameter `dose3`.'), 'dose2': ('dose2', 0.0, 'native SBML value', 'Dose2 source parameter. Maps to bundled SBML parameter `dose2`.'), 'initial_damaged_tumor_cells_d': ('Damaged_Tumor_Cells_D', 0.0, 'native SBML value', 'Initial Damaged Tumor Cells D. Sets the initial value of bundled SBML symbol `Damaged_Tumor_Cells_D`.'), 'initial_tumor_cell_population_p': ('Tumor_Cell_Population_P', 144.952075141053, 'native SBML value', 'Initial Tumor Cell Population P. Sets the initial value of bundled SBML symbol `Tumor_Cell_Population_P`.')}
    _HEADLINE_OUTPUTS = {'damaged_tumor_cells_d': ('Damaged_Tumor_Cells_D', 'native SBML value', 'Damaged Tumor Cells D observable. Maps to SBML symbol `Damaged_Tumor_Cells_D`.'), 'tumor_cell_population_p': ('Tumor_Cell_Population_P', 'native SBML value', 'Tumor Cell Population P observable. Maps to SBML symbol `Tumor_Cell_Population_P`.'), 'drug_concentration_c': ('Drug_Concentration_C', 'native SBML value', 'Drug Concentration C observable. Maps to SBML symbol `Drug_Concentration_C`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000814.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
