# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Merola2008 - An insight into tumor dormancy equilibrium via the analysis of its domain of attraction."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Merola2008AnInsightIntoTumorDormancyEquiliBiomd0000000911Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000911'
    _TITLE = 'Merola2008 - An insight into tumor dormancy equilibrium via the analysis of its domain of attraction'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['M', 'N', 'Z']
    _SPECIES_LABELS = {'M': 'M', 'N': 'N', 'Z': 'Z'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'model_state_1': ('M', 'native SBML value', 'M observable. Maps to SBML symbol `M`.'), 'model_state_2': ('N', 'native SBML value', 'N observable. Maps to SBML symbol `N`.'), 'model_state_3': ('Z', 'native SBML value', 'Z observable. Maps to SBML symbol `Z`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000911.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
