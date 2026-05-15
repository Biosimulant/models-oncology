# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Barros2021 - CARTmath, Mathematical Model of CAR-T Immunotherapy in HDLM-2 cell line."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Barros2021CartmathMathematicalModelOfCarTBiomd0000001019Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000001019'
    _TITLE = 'Barros2021 - CARTmath, Mathematical Model of CAR-T Immunotherapy in HDLM-2 cell line'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Cm', 'Ct', 'T']
    _SPECIES_LABELS = {'T': 'T', 'Cm': 'Cm', 'Ct': 'Ct'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'epsilon_level': ('epsilon', 0.15, 'native SBML value', 'Epsilon source parameter. Maps to bundled SBML parameter `epsilon`.')}
    _HEADLINE_OUTPUTS = {'model_state_1': ('T', 'native SBML value', 'T observable. Maps to SBML symbol `T`.'), 'model_state_2': ('Cm', 'native SBML value', 'Cm observable. Maps to SBML symbol `Cm`.'), 'model_state_3': ('Ct', 'native SBML value', 'Ct observable. Maps to SBML symbol `Ct`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000001019.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
