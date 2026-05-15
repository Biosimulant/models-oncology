# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Evans2005 - Compartmental model for antineoplastic drug topotecan in breast cancer cells."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Evans2005CompartmentalModelForAntineoplasticBiomd0000000946Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000946'
    _TITLE = 'Evans2005 - Compartmental model for antineoplastic drug topotecan in breast cancer cells'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rateRule'
    _OBSERVABLES = ['L_m', 'H_m', 'L_e', 'H_e', 'L_c', 'H_c', 'L_n']
    _SPECIES_LABELS = {'L_m': 'L m', 'H_m': 'H m', 'L_e': 'L e', 'H_e': 'H e', 'L_c': 'L c', 'H_c': 'H c'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'model_state_1': ('L_m', 'native SBML value', 'L m observable. Maps to SBML symbol `L_m`.'), 'model_state_2': ('H_m', 'native SBML value', 'H m observable. Maps to SBML symbol `H_m`.'), 'model_state_3': ('L_e', 'native SBML value', 'L e observable. Maps to SBML symbol `L_e`.'), 'model_state_4': ('H_e', 'native SBML value', 'H e observable. Maps to SBML symbol `H_e`.'), 'model_state_5': ('L_c', 'native SBML value', 'L c observable. Maps to SBML symbol `L_c`.'), 'model_state_6': ('H_c', 'native SBML value', 'H c observable. Maps to SBML symbol `H_c`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000946.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
