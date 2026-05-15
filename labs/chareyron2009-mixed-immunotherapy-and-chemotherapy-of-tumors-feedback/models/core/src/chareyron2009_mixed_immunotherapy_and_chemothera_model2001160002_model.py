# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Chareyron2009 - Mixed immunotherapy and chemotherapy of tumors Feedback design and model updating schemes."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Chareyron2009MixedImmunotherapyAndChemotheraModel2001160002Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'MODEL2001160002'
    _TITLE = 'Chareyron2009 - Mixed immunotherapy and chemotherapy of tumors Feedback design and model updating schemes'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T', 'N', 'L', 'C', 'M', 'I']
    _SPECIES_LABELS = {'T': 'T', 'N': 'N', 'L': 'L', 'C': 'C', 'M': 'M', 'I': 'I'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'model_state_1': ('T', 'native SBML value', 'T observable. Maps to SBML symbol `T`.'), 'model_state_2': ('N', 'native SBML value', 'N observable. Maps to SBML symbol `N`.'), 'model_state_3': ('L', 'native SBML value', 'L observable. Maps to SBML symbol `L`.'), 'model_state_4': ('C', 'native SBML value', 'C observable. Maps to SBML symbol `C`.'), 'model_state_5': ('M', 'native SBML value', 'M observable. Maps to SBML symbol `M`.'), 'model_state_6': ('I', 'native SBML value', 'I observable. Maps to SBML symbol `I`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2001160002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
