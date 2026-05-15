# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Chaudhury2020 - EC50 expansion and killing mathematical model of CAR-T cell and tumour kinetics."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Chaudhury2020Ec50ExpansionAndKillingMathemaBiomd0000001025Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000001025'
    _TITLE = 'Chaudhury2020 - EC50 expansion and killing mathematical model of CAR-T cell and tumour kinetics'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Tumor_cells']
    _SPECIES_LABELS = {'Tumor_cells': 'Tumor cells'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_tumor_cells': ('Tumor_cells', 900.0, 'native SBML value', 'Initial Tumor cells. Sets the initial value of bundled SBML symbol `Tumor_cells`.')}
    _HEADLINE_OUTPUTS = {'tumor_cells': ('Tumor_cells', 'native SBML value', 'Tumor cells observable. Maps to SBML symbol `Tumor_cells`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000001025.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
