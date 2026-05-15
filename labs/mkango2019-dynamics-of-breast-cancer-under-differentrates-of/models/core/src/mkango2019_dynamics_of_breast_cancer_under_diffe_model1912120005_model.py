# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Mkango2019 - Dynamics of Breast Cancer under DifferentRates of Chemoradiotherapy."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Mkango2019DynamicsOfBreastCancerUnderDiffeModel1912120005Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'MODEL1912120005'
    _TITLE = 'Mkango2019 - Dynamics of Breast Cancer under DifferentRates of Chemoradiotherapy'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T', 'TR', 'N', 'I', 'M', 'R']
    _SPECIES_LABELS = {'T': 'T', 'TR': 'TR', 'N': 'N', 'I': 'I', 'M': 'M', 'R': 'R'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'model_state_1': ('T', 'native SBML value', 'T observable. Maps to SBML symbol `T`.'), 'model_state_2': ('TR', 'native SBML value', 'TR observable. Maps to SBML symbol `TR`.'), 'model_state_3': ('N', 'native SBML value', 'N observable. Maps to SBML symbol `N`.'), 'model_state_4': ('I', 'native SBML value', 'I observable. Maps to SBML symbol `I`.'), 'model_state_5': ('M', 'native SBML value', 'M observable. Maps to SBML symbol `M`.'), 'model_state_6': ('R', 'native SBML value', 'R observable. Maps to SBML symbol `R`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1912120005.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
