# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Claret2009 - Predicting phase III overall survival in colorectal cancer."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Claret2009PredictingPhaseIiiOverallSurvivalModel1708310001Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'MODEL1708310001'
    _TITLE = 'Claret2009 - Predicting phase III overall survival in colorectal cancer'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rateRule'
    _OBSERVABLES = ['y']
    _SPECIES_LABELS = {'y': 'Y'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'treatment_int_source_parameter': ('treatment_int', 14.0, 'native SBML value', 'Treatment int source parameter. Maps to bundled SBML parameter `treatment_int`.'), 'treatment_day_source_parameter': ('treatment_day', 1.0, 'native SBML value', 'Treatment day source parameter. Maps to bundled SBML parameter `treatment_day`.'), 'dose_length_source_parameter': ('dose_length', 0.0625, 'native SBML value', 'Dose length source parameter. Maps to bundled SBML parameter `dose_length`.'), 'dose_int2_source_parameter': ('Dose_int2', 0.5, 'native SBML value', 'Dose int2 source parameter. Maps to bundled SBML parameter `Dose_int2`.')}
    _HEADLINE_OUTPUTS = {'y': ('y', 'native SBML value', 'Y observable. Maps to SBML symbol `y`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1708310001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
