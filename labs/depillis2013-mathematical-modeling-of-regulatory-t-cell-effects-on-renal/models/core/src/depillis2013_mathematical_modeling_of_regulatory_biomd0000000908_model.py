# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for dePillis2013 - Mathematical modeling of regulatory T cell effects on renal cell carcinoma treatment."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Depillis2013MathematicalModelingOfRegulatoryBiomd0000000908Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000908'
    _TITLE = 'dePillis2013 - Mathematical modeling of regulatory T cell effects on renal cell carcinoma treatment'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T', 'N', 'L', 'R', 'C', 'I', 'S']
    _SPECIES_LABELS = {'T': 'T', 'N': 'N', 'L': 'L', 'R': 'R', 'C': 'C', 'I': 'I'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'model_state_1': ('T', 'native SBML value', 'T observable. Maps to SBML symbol `T`.'), 'model_state_2': ('N', 'native SBML value', 'N observable. Maps to SBML symbol `N`.'), 'model_state_3': ('L', 'native SBML value', 'L observable. Maps to SBML symbol `L`.'), 'model_state_4': ('R', 'native SBML value', 'R observable. Maps to SBML symbol `R`.'), 'model_state_5': ('C', 'native SBML value', 'C observable. Maps to SBML symbol `C`.'), 'model_state_6': ('I', 'native SBML value', 'I observable. Maps to SBML symbol `I`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000908.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
