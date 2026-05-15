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
    _SPECIES_LABELS = {'I': 'I', 'T': 'T', 'Td': 'Td', 'C': 'C', 'R': 'R'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'model_state_1': ('I', 'native SBML value', 'I observable. Maps to SBML symbol `I`.'), 'model_state_2': ('T', 'native SBML value', 'T observable. Maps to SBML symbol `T`.'), 'model_state_3': ('Td', 'native SBML value', 'Td observable. Maps to SBML symbol `Td`.'), 'model_state_4': ('C', 'native SBML value', 'C observable. Maps to SBML symbol `C`.'), 'model_state_5': ('R', 'native SBML value', 'R observable. Maps to SBML symbol `R`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2003050002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
