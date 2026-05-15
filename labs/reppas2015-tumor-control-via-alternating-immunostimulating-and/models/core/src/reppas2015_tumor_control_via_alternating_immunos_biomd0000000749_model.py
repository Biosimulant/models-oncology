# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Reppas2015 - tumor control via alternating immunostimulating and immunosuppressive phases."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Reppas2015TumorControlViaAlternatingImmunosBiomd0000000749Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000749'
    _TITLE = 'Reppas2015 - tumor control via alternating immunostimulating and immunosuppressive phases'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['E', 'R']
    _SPECIES_LABELS = {'E': 'E', 'R': 'R'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'model_state_1': ('E', 'native SBML value', 'E observable. Maps to SBML symbol `E`.'), 'model_state_2': ('R', 'native SBML value', 'R observable. Maps to SBML symbol `R`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000749.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
