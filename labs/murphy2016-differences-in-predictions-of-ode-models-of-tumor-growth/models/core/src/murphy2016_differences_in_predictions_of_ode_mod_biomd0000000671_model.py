# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Murphy2016 - Differences in predictions of ODE models of tumor growth."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Murphy2016DifferencesInPredictionsOfOdeModBiomd0000000671Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000671'
    _TITLE = 'Murphy2016 - Differences in predictions of ODE models of tumor growth'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rateRule'
    _OBSERVABLES = ['V_exp', 'V_mend', 'V_log', 'V_lin', 'V_surf', 'V_gomp', 'V_bert']
    _SPECIES_LABELS = {'V_exp': 'V exp', 'V_mend': 'V mend', 'V_log': 'V log', 'V_lin': 'V lin', 'V_surf': 'V surf', 'V_gomp': 'V gomp'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'v_exp': ('V_exp', 'native SBML value', 'V exp observable. Maps to SBML symbol `V_exp`.'), 'v_mend': ('V_mend', 'native SBML value', 'V mend observable. Maps to SBML symbol `V_mend`.'), 'v_log': ('V_log', 'native SBML value', 'V log observable. Maps to SBML symbol `V_log`.'), 'v_lin': ('V_lin', 'native SBML value', 'V lin observable. Maps to SBML symbol `V_lin`.'), 'v_surf': ('V_surf', 'native SBML value', 'V surf observable. Maps to SBML symbol `V_surf`.'), 'v_gomp': ('V_gomp', 'native SBML value', 'V gomp observable. Maps to SBML symbol `V_gomp`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000671.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
