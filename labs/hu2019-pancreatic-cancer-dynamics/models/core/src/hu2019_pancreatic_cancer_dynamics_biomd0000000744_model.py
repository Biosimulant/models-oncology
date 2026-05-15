# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Hu2019 - Pancreatic cancer dynamics."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Hu2019PancreaticCancerDynamicsBiomd0000000744Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000744'
    _TITLE = 'Hu2019 - Pancreatic cancer dynamics'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['x', 'y', 'z', 'w', 'v']
    _SPECIES_LABELS = {'x': 'X', 'y': 'Y', 'z': 'Z', 'w': 'W', 'v': 'V'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'model_state_1': ('x', 'native SBML value', 'X observable. Maps to SBML symbol `x`.'), 'model_state_2': ('y', 'native SBML value', 'Y observable. Maps to SBML symbol `y`.'), 'model_state_3': ('z', 'native SBML value', 'Z observable. Maps to SBML symbol `z`.'), 'model_state_4': ('w', 'native SBML value', 'W observable. Maps to SBML symbol `w`.'), 'model_state_5': ('v', 'native SBML value', 'V observable. Maps to SBML symbol `v`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000744.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
