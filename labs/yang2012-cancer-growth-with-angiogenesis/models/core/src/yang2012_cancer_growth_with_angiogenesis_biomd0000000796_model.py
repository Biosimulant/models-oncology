# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Yang2012 - cancer growth with angiogenesis."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Yang2012CancerGrowthWithAngiogenesisBiomd0000000796Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000796'
    _TITLE = 'Yang2012 - cancer growth with angiogenesis'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['C', 'E', 'T', 'P', 'A']
    _SPECIES_LABELS = {'C': 'C', 'E': 'E', 'T': 'T', 'P': 'P', 'A': 'A'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'model_state_1': ('C', 'native SBML value', 'C observable. Maps to SBML symbol `C`.'), 'model_state_2': ('E', 'native SBML value', 'E observable. Maps to SBML symbol `E`.'), 'model_state_3': ('T', 'native SBML value', 'T observable. Maps to SBML symbol `T`.'), 'model_state_4': ('P', 'native SBML value', 'P observable. Maps to SBML symbol `P`.'), 'model_state_5': ('A', 'native SBML value', 'A observable. Maps to SBML symbol `A`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000796.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
