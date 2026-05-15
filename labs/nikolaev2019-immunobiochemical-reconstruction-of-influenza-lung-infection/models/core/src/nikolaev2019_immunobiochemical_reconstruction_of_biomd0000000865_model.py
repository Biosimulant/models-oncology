# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Nikolaev2019 - Immunobiochemical reconstruction of influenza lung infection-melanoma skin cancer interactions."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Nikolaev2019ImmunobiochemicalReconstructionOfBiomd0000000865Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000865'
    _TITLE = 'Nikolaev2019 - Immunobiochemical reconstruction of influenza lung infection-melanoma skin cancer interactions'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['C', 'P', 'I', 'B']
    _SPECIES_LABELS = {'C': 'C', 'P': 'P', 'I': 'I', 'B': 'B'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'sigma_p_tilde_level': ('sigma_p_tilde', 0.1, 'native SBML value', 'Sigma p tilde source parameter. Maps to bundled SBML parameter `sigma_p_tilde`.')}
    _HEADLINE_OUTPUTS = {'model_state_1': ('C', 'native SBML value', 'C observable. Maps to SBML symbol `C`.'), 'model_state_2': ('P', 'native SBML value', 'P observable. Maps to SBML symbol `P`.'), 'model_state_3': ('I', 'native SBML value', 'I observable. Maps to SBML symbol `I`.'), 'model_state_4': ('B', 'native SBML value', 'B observable. Maps to SBML symbol `B`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000865.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
