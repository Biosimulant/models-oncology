# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Greene2019 - Differentiate Spontaneous and Induced Evolution to Drug Resistance During Cancer Treatment."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Greene2019DifferentiateSpontaneousAndInducedBiomd0000000825Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000825'
    _TITLE = 'Greene2019 - Differentiate Spontaneous and Induced Evolution to Drug Resistance During Cancer Treatment'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Resistant_tumor_R', 'Sensitive_tumor_S']
    _SPECIES_LABELS = {'Sensitive_tumor_S': 'Sensitive tumor S', 'Resistant_tumor_R': 'Resistant tumor R'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'epsilon_source_parameter': ('epsilon', 1e-06, 'native SBML value', 'Epsilon source parameter. Maps to bundled SBML parameter `epsilon`.'), 'initial_sensitive_tumor_s': ('Sensitive_tumor_S', 0.01, 'native SBML value', 'Initial Sensitive tumor S. Sets the initial value of bundled SBML symbol `Sensitive_tumor_S`.'), 'initial_resistant_tumor_r': ('Resistant_tumor_R', 0.0, 'native SBML value', 'Initial Resistant tumor R. Sets the initial value of bundled SBML symbol `Resistant_tumor_R`.')}
    _HEADLINE_OUTPUTS = {'sensitive_tumor_s': ('Sensitive_tumor_S', 'native SBML value', 'Sensitive tumor S observable. Maps to SBML symbol `Sensitive_tumor_S`.'), 'resistant_tumor_r': ('Resistant_tumor_R', 'native SBML value', 'Resistant tumor R observable. Maps to SBML symbol `Resistant_tumor_R`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000825.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
