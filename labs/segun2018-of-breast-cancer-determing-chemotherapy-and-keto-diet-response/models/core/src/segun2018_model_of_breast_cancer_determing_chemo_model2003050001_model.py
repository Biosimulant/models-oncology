# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Segun2018 - model of breast cancer determing Chemotherapy and Keto diet response."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Segun2018ModelOfBreastCancerDetermingChemoModel2003050001Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'MODEL2003050001'
    _TITLE = 'Segun2018 - model of breast cancer determing Chemotherapy and Keto diet response'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['N', 'T', 'M', 'E']
    _SPECIES_LABELS = {'N': 'N', 'T': 'T', 'M': 'M', 'E': 'E'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'model_state_1': ('N', 'native SBML value', 'N observable. Maps to SBML symbol `N`.'), 'model_state_2': ('T', 'native SBML value', 'T observable. Maps to SBML symbol `T`.'), 'model_state_3': ('M', 'native SBML value', 'M observable. Maps to SBML symbol `M`.'), 'model_state_4': ('E', 'native SBML value', 'E observable. Maps to SBML symbol `E`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2003050001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
