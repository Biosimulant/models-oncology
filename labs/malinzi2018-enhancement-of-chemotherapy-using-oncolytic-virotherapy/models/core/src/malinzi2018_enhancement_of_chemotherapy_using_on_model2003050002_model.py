# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Malinzi2018 - Enhancement of chemotherapy using oncolytic virotherapy."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Malinzi2018EnhancementOfChemotherapyUsingOnModel2003050002Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'MODEL2003050002'
    _TITLE = 'Malinzi2018 - Enhancement of chemotherapy using oncolytic virotherapy'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['I', 'T', 'Td', 'C', 'R']
    _SPECIES_LABELS = {'I': 'Infected Tumor Cells', 'T': 'Uninfected Tumor Cells', 'Td': 'Td', 'C': 'Chemotherapy Level', 'R': 'R'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_uninfected_tumor_cells': ('T', 0.8, 'native SBML value', 'Initial Uninfected Tumor Cells. Sets the initial value of bundled SBML symbol `T`.'), 'initial_infected_tumor_cells': ('I', 0.3, 'native SBML value', 'Initial Infected Tumor Cells. Sets the initial value of bundled SBML symbol `I`.'), 'initial_chemotherapy_level': ('C', 1e-06, 'native SBML value', 'Initial Chemotherapy Level. Sets the initial value of bundled SBML symbol `C`.')}
    _HEADLINE_OUTPUTS = {'uninfected_tumor_cells': ('T', 'native SBML value', 'Uninfected Tumor Cells observable. Maps to SBML symbol `T`.'), 'infected_tumor_cells': ('I', 'native SBML value', 'Infected Tumor Cells observable. Maps to SBML symbol `I`.'), 'chemotherapy_level': ('C', 'native SBML value', 'Chemotherapy Level observable. Maps to SBML symbol `C`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2003050002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
