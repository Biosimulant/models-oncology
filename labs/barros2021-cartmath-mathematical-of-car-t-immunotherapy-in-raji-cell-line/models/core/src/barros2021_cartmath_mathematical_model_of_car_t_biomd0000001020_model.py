# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Barros2021 - CARTmath, Mathematical Model of CAR-T Immunotherapy in Raji Cell Line."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Barros2021CartmathMathematicalModelOfCarTBiomd0000001020Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000001020'
    _TITLE = 'Barros2021 - CARTmath, Mathematical Model of CAR-T Immunotherapy in Raji Cell Line'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Cm', 'Ct', 'T']
    _SPECIES_LABELS = {'T': 'T', 'Cm': 'Cm', 'Ct': 'Ct'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'epsilon_level': ('epsilon', 1.59795, 'native SBML value', 'Epsilon source parameter. Maps to bundled SBML parameter `epsilon`.'), 'raji_ido_positive_cart_19_positive_1mt_level': ('Raji_IDO_CART_19_1MT', 0.0, 'native SBML value', 'Raji IDO+CART 19+1MT source parameter. Maps to bundled SBML parameter `Raji_IDO_CART_19_1MT`.'), 'initial_for_raji_ido_positive_cart_19_positive_1mt': ('ModelValue_10', 0.0, 'native SBML value', 'Initial for Raji IDO+CART 19+1MT source parameter. Maps to bundled SBML parameter `ModelValue_10`.')}
    _HEADLINE_OUTPUTS = {'model_state_1': ('T', 'native SBML value', 'T observable. Maps to SBML symbol `T`.'), 'model_state_2': ('Cm', 'native SBML value', 'Cm observable. Maps to SBML symbol `Cm`.'), 'model_state_3': ('Ct', 'native SBML value', 'Ct observable. Maps to SBML symbol `Ct`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000001020.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
