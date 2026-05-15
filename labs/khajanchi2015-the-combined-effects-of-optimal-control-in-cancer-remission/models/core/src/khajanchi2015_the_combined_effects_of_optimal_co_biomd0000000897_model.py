# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Khajanchi2015 - The combined effects of optimal control in cancer remission."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Khajanchi2015TheCombinedEffectsOfOptimalCoBiomd0000000897Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000897'
    _TITLE = 'Khajanchi2015 - The combined effects of optimal control in cancer remission'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['E', 'T']
    _SPECIES_LABELS = {'E': 'E', 'T': 'T'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'model_state_1': ('E', 'native SBML value', 'E observable. Maps to SBML symbol `E`.'), 'model_state_2': ('T', 'native SBML value', 'T observable. Maps to SBML symbol `T`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000897.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
