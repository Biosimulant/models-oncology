# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Rodrigues2019 - A mathematical model for chemoimmunotherapy of chronic lymphocytic leukemia."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Rodrigues2019AMathematicalModelForChemoimmuBiomd0000000879Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000879'
    _TITLE = 'Rodrigues2019 - A mathematical model for chemoimmunotherapy of chronic lymphocytic leukemia'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['N', 'I', 'Q']
    _SPECIES_LABELS = {'N': 'N', 'I': 'I', 'Q': 'Q'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'chemotherapy_input_level': ('Chemotherapy_Input', 8640.0, 'native SBML value', 'Chemotherapy Input source parameter. Maps to bundled SBML parameter `Chemotherapy_Input`.'), 'immunotherapy_input_level': ('Immunotherapy_Input', 0.0, 'native SBML value', 'Immunotherapy Input source parameter. Maps to bundled SBML parameter `Immunotherapy_Input`.'), 'infusion_dose': ('Infusion_Dose', 1080.0, 'native SBML value', 'Infusion Dose source parameter. Maps to bundled SBML parameter `Infusion_Dose`.')}
    _HEADLINE_OUTPUTS = {'model_state_1': ('N', 'native SBML value', 'N observable. Maps to SBML symbol `N`.'), 'model_state_2': ('I', 'native SBML value', 'I observable. Maps to SBML symbol `I`.'), 'model_state_3': ('Q', 'native SBML value', 'Q observable. Maps to SBML symbol `Q`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000879.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
