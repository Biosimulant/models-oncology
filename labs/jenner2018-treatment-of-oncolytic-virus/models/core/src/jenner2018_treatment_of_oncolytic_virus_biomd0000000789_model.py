# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Jenner2018 - treatment of oncolytic virus."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Jenner2018TreatmentOfOncolyticVirusBiomd0000000789Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000789'
    _TITLE = 'Jenner2018 - treatment of oncolytic virus'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['V', 'S', 'I']
    _SPECIES_LABELS = {'S': 'S', 'V': 'V', 'I': 'I'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'model_state_1': ('S', 'native SBML value', 'S observable. Maps to SBML symbol `S`.'), 'model_state_2': ('V', 'native SBML value', 'V observable. Maps to SBML symbol `V`.'), 'model_state_3': ('I', 'native SBML value', 'I observable. Maps to SBML symbol `I`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000789.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
