# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Monro2008 - chemotherapy resistance."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Monro2008ChemotherapyResistanceBiomd0000000776Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000776'
    _TITLE = 'Monro2008 - chemotherapy resistance'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['S', 'R']
    _SPECIES_LABELS = {'S': 'Chemo-Sensitive Cells', 'R': 'Chemo-Resistant Cells'}
    _PARAMETER_INPUTS = {'chemotherapy_concentration': ('C0', 2.0, 'native SBML value', 'Chemotherapy Concentration. Overrides bundled SBML parameter `C0`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_chemo_sensitive_cells': ('S', 10000000000.0, 'native SBML value', 'Initial Chemo-Sensitive Cells. Sets the initial value of bundled SBML symbol `S`.'), 'initial_chemo_resistant_cells': ('R', 200000.0, 'native SBML value', 'Initial Chemo-Resistant Cells. Sets the initial value of bundled SBML symbol `R`.')}
    _HEADLINE_OUTPUTS = {'chemo_sensitive_cells': ('S', 'native SBML value', 'Chemo-Sensitive Cells observable. Maps to SBML symbol `S`.'), 'chemo_resistant_cells': ('R', 'native SBML value', 'Chemo-Resistant Cells observable. Maps to SBML symbol `R`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000776.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
