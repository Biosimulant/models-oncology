# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Mpekris2017 - Role of vascular normalization in benefit from metronomic chemotherapy."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Mpekris2017RoleOfVascularNormalizationInBeModel2001200002Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'MODEL2001200002'
    _TITLE = 'Mpekris2017 - Role of vascular normalization in benefit from metronomic chemotherapy'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['C', 'T', 'Csc', 'I', 'N', 'L', 'Treg']
    _SPECIES_LABELS = {'C': 'C', 'T': 'T', 'Csc': 'Csc', 'I': 'I', 'N': 'N', 'L': 'L'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_csc': ('Csc', 1.0, 'native SBML value', 'Initial Csc. Sets the initial value of bundled SBML symbol `Csc`.')}
    _HEADLINE_OUTPUTS = {'model_state_1': ('C', 'native SBML value', 'C observable. Maps to SBML symbol `C`.'), 'model_state_2': ('T', 'native SBML value', 'T observable. Maps to SBML symbol `T`.'), 'csc': ('Csc', 'native SBML value', 'Csc observable. Maps to SBML symbol `Csc`.'), 'model_state_4': ('I', 'native SBML value', 'I observable. Maps to SBML symbol `I`.'), 'model_state_5': ('N', 'native SBML value', 'N observable. Maps to SBML symbol `N`.'), 'model_state_6': ('L', 'native SBML value', 'L observable. Maps to SBML symbol `L`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2001200002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
