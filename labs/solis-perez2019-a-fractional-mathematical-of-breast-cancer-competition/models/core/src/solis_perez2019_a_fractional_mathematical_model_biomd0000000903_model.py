# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Solis-perez2019 - A fractional mathematical model of breast cancer competition model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SolisPerez2019AFractionalMathematicalModelBiomd0000000903Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000903'
    _TITLE = 'Solis-perez2019 - A fractional mathematical model of breast cancer competition model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['C', 'T', 'H', 'I', 'E']
    _SPECIES_LABELS = {'C': 'C', 'T': 'T', 'H': 'H', 'I': 'I', 'E': 'E'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'model_state_1': ('C', 'native SBML value', 'C observable. Maps to SBML symbol `C`.'), 'model_state_2': ('T', 'native SBML value', 'T observable. Maps to SBML symbol `T`.'), 'model_state_3': ('H', 'native SBML value', 'H observable. Maps to SBML symbol `H`.'), 'model_state_4': ('I', 'native SBML value', 'I observable. Maps to SBML symbol `I`.'), 'model_state_5': ('E', 'native SBML value', 'E observable. Maps to SBML symbol `E`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000903.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
