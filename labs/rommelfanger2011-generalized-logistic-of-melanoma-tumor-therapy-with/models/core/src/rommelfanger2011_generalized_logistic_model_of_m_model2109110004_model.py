# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Rommelfanger2011 - Generalized logistic model of melanoma tumor therapy with vesicular stomatitis virus."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Rommelfanger2011GeneralizedLogisticModelOfMModel2109110004Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'MODEL2109110004'
    _TITLE = 'Rommelfanger2011 - Generalized logistic model of melanoma tumor therapy with vesicular stomatitis virus'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['x', 'y', 'z', 'v', 'v_i']
    _SPECIES_LABELS = {'y': 'Y', 'v': 'V', 'v_i': 'V i', 'x': 'X', 'z': 'Z'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'epsilon_level': ('epsilon', 3.0, 'native SBML value', 'Epsilon source parameter. Maps to bundled SBML parameter `epsilon`.')}
    _HEADLINE_OUTPUTS = {'model_state_1': ('y', 'native SBML value', 'Y observable. Maps to SBML symbol `y`.'), 'model_state_2': ('v', 'native SBML value', 'V observable. Maps to SBML symbol `v`.'), 'model_state_3': ('v_i', 'native SBML value', 'V i observable. Maps to SBML symbol `v_i`.'), 'model_state_4': ('x', 'native SBML value', 'X observable. Maps to SBML symbol `x`.'), 'model_state_5': ('z', 'native SBML value', 'Z observable. Maps to SBML symbol `z`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2109110004.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
