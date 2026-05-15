# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Jenner2019 - Oncolytic virotherapy for tumours following a Gompertz growth law."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Jenner2019OncolyticVirotherapyForTumoursFolBiomd0000000850Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000850'
    _TITLE = 'Jenner2019 - Oncolytic virotherapy for tumours following a Gompertz growth law'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['U', 'I', 'V']
    _SPECIES_LABELS = {'U': 'U', 'I': 'I', 'V': 'V'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'model_state_1': ('U', 'native SBML value', 'U observable. Maps to SBML symbol `U`.'), 'model_state_2': ('I', 'native SBML value', 'I observable. Maps to SBML symbol `I`.'), 'model_state_3': ('V', 'native SBML value', 'V observable. Maps to SBML symbol `V`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000850.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
