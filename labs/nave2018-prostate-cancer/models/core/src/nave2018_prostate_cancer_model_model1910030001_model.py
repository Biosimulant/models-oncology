# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Nave2018 - prostate cancer model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Nave2018ProstateCancerModelModel1910030001Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'MODEL1910030001'
    _TITLE = 'Nave2018 - prostate cancer model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['N_1', 'T', 'A', 'N_2', 'D', 'I_L']
    _SPECIES_LABELS = {'N_1': 'N 1', 'A': 'A', 'N_2': 'N 2', 'D': 'D', 'T': 'T', 'I_L': 'I L'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'model_state_1': ('N_1', 'native SBML value', 'N 1 observable. Maps to SBML symbol `N_1`.'), 'model_state_2': ('A', 'native SBML value', 'A observable. Maps to SBML symbol `A`.'), 'model_state_3': ('N_2', 'native SBML value', 'N 2 observable. Maps to SBML symbol `N_2`.'), 'model_state_4': ('D', 'native SBML value', 'D observable. Maps to SBML symbol `D`.'), 'model_state_5': ('T', 'native SBML value', 'T observable. Maps to SBML symbol `T`.'), 'model_state_6': ('I_L', 'native SBML value', 'I L observable. Maps to SBML symbol `I_L`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1910030001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
