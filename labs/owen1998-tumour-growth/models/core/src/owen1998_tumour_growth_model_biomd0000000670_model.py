# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Owen1998 - tumour growth model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Owen1998TumourGrowthModelBiomd0000000670Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000670'
    _TITLE = 'Owen1998 - tumour growth model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rateRule'
    _OBSERVABLES = ['l', 'n', 'm']
    _SPECIES_LABELS = {'l': 'L', 'n': 'N', 'm': 'M'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'model_state_1': ('l', 'native SBML value', 'L observable. Maps to SBML symbol `l`.'), 'model_state_2': ('n', 'native SBML value', 'N observable. Maps to SBML symbol `n`.'), 'model_state_3': ('m', 'native SBML value', 'M observable. Maps to SBML symbol `m`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000670.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
