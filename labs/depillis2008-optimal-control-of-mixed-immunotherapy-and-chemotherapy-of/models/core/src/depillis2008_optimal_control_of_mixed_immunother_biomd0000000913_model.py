# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for dePillis2008 - Optimal control of mixed immunotherapy and chemotherapy of tumors."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Depillis2008OptimalControlOfMixedImmunotherBiomd0000000913Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000913'
    _TITLE = 'dePillis2008 - Optimal control of mixed immunotherapy and chemotherapy of tumors'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T', 'L', 'N', 'C', 'I', 'M']
    _SPECIES_LABELS = {'T': 'T', 'L': 'L', 'N': 'N', 'C': 'C', 'I': 'I', 'M': 'M'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'model_state_1': ('T', 'native SBML value', 'T observable. Maps to SBML symbol `T`.'), 'model_state_2': ('L', 'native SBML value', 'L observable. Maps to SBML symbol `L`.'), 'model_state_3': ('N', 'native SBML value', 'N observable. Maps to SBML symbol `N`.'), 'model_state_4': ('C', 'native SBML value', 'C observable. Maps to SBML symbol `C`.'), 'model_state_5': ('I', 'native SBML value', 'I observable. Maps to SBML symbol `I`.'), 'model_state_6': ('M', 'native SBML value', 'M observable. Maps to SBML symbol `M`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000913.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
