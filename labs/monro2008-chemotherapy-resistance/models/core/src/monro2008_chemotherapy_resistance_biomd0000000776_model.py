# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Monro2008 - chemotherapy resistance."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Monro2008ChemotherapyResistanceBiomd0000000776Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000776'
    _TITLE = 'Monro2008 - chemotherapy resistance'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['S', 'R']
    _SPECIES_LABELS = {'S': 'S', 'R': 'R'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'model_state_1': ('S', 'native SBML value', 'S observable. Maps to SBML symbol `S`.'), 'model_state_2': ('R', 'native SBML value', 'R observable. Maps to SBML symbol `R`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000776.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
