# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Dritschel2018 - A mathematical model of cytotoxic and helper T cell interactions in a tumour microenvironment."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Dritschel2018AMathematicalModelOfCytotoxicBiomd0000000763Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000763'
    _TITLE = 'Dritschel2018 - A mathematical model of cytotoxic and helper T cell interactions in a tumour microenvironment'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['N_Tumour', 'T_H', 'T_C']
    _SPECIES_LABELS = {'N_Tumour': 'N Tumour', 'T_H': 'T H', 'T_C': 'T C'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'ntilde_level': ('Ntilde', 0.04, 'native SBML value', 'Ntilde source parameter. Maps to bundled SBML parameter `Ntilde`.'), 'initial_n_tumour': ('N_Tumour', 0.01, 'native SBML value', 'Initial N Tumour. Sets the initial value of bundled SBML symbol `N_Tumour`.')}
    _HEADLINE_OUTPUTS = {'n_tumour': ('N_Tumour', 'native SBML value', 'N Tumour observable. Maps to SBML symbol `N_Tumour`.'), 'model_state_2': ('T_H', 'native SBML value', 'T H observable. Maps to SBML symbol `T_H`.'), 'model_state_3': ('T_C', 'native SBML value', 'T C observable. Maps to SBML symbol `T_C`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000763.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
