# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for dePillis2003 - The dynamics of an optimally controlled tumor model: A case study."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Depillis2003TheDynamicsOfAnOptimallyControBiomd0000000909Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000909'
    _TITLE = 'dePillis2003 - The dynamics of an optimally controlled tumor model: A case study'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['N', 'T', 'I', 'u']
    _SPECIES_LABELS = {'N': 'N', 'T': 'T', 'I': 'I', 'u': 'U'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'model_state_1': ('N', 'native SBML value', 'N observable. Maps to SBML symbol `N`.'), 'model_state_2': ('T', 'native SBML value', 'T observable. Maps to SBML symbol `T`.'), 'model_state_3': ('I', 'native SBML value', 'I observable. Maps to SBML symbol `I`.'), 'model_state_4': ('u', 'native SBML value', 'U observable. Maps to SBML symbol `u`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000909.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
