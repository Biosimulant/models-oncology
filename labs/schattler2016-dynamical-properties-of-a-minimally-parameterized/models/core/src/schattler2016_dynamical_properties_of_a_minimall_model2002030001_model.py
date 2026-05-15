# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Schattler2016 - Dynamical properties of a minimally parameterized mathematical model for metronomic chemotherapy."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Schattler2016DynamicalPropertiesOfAMinimallModel2002030001Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'MODEL2002030001'
    _TITLE = 'Schattler2016 - Dynamical properties of a minimally parameterized mathematical model for metronomic chemotherapy'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['p', 'q', 'r']
    _SPECIES_LABELS = {'p': 'P', 'q': 'Q', 'r': 'R'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'model_state_1': ('p', 'native SBML value', 'P observable. Maps to SBML symbol `p`.'), 'model_state_2': ('q', 'native SBML value', 'Q observable. Maps to SBML symbol `q`.'), 'model_state_3': ('r', 'native SBML value', 'R observable. Maps to SBML symbol `r`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2002030001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
