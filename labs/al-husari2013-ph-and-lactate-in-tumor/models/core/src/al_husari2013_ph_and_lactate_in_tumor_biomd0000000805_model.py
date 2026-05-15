# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Al-Husari2013 - pH and lactate in tumor."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class AlHusari2013PhAndLactateInTumorBiomd0000000805Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000805'
    _TITLE = 'Al-Husari2013 - pH and lactate in tumor'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Hi', 'He', 'Li', 'Le']
    _SPECIES_LABELS = {'Hi': 'Hi', 'He': 'He', 'Li': 'Li', 'Le': 'Le'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'model_state_1': ('Hi', 'native SBML value', 'Hi observable. Maps to SBML symbol `Hi`.'), 'model_state_2': ('He', 'native SBML value', 'He observable. Maps to SBML symbol `He`.'), 'model_state_3': ('Li', 'native SBML value', 'Li observable. Maps to SBML symbol `Li`.'), 'model_state_4': ('Le', 'native SBML value', 'Le observable. Maps to SBML symbol `Le`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000805.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
