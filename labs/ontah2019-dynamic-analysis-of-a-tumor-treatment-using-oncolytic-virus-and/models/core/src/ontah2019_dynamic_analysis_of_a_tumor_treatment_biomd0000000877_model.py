# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Ontah2019 - Dynamic analysis of a tumor treatment model using oncolytic virus and chemotherapy with saturated infection rate."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Ontah2019DynamicAnalysisOfATumorTreatmentBiomd0000000877Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000877'
    _TITLE = 'Ontah2019 - Dynamic analysis of a tumor treatment model using oncolytic virus and chemotherapy with saturated infection rate'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['U', 'I', 'V', 'C']
    _SPECIES_LABELS = {'U': 'U', 'I': 'I', 'V': 'V', 'C': 'C'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'model_state_1': ('U', 'native SBML value', 'U observable. Maps to SBML symbol `U`.'), 'model_state_2': ('I', 'native SBML value', 'I observable. Maps to SBML symbol `I`.'), 'model_state_3': ('V', 'native SBML value', 'V observable. Maps to SBML symbol `V`.'), 'model_state_4': ('C', 'native SBML value', 'C observable. Maps to SBML symbol `C`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000877.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
