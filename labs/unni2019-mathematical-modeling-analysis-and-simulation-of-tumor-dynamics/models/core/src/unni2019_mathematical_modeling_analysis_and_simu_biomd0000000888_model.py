# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Unni2019 - Mathematical Modeling, Analysis, and Simulation of Tumor Dynamics with Drug Interventions."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Unni2019MathematicalModelingAnalysisAndSimuBiomd0000000888Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000888'
    _TITLE = 'Unni2019 - Mathematical Modeling, Analysis, and Simulation of Tumor Dynamics with Drug Interventions'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T', 'N', 'D', 'L']
    _SPECIES_LABELS = {'T': 'T', 'N': 'N', 'D': 'D', 'L': 'L'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'model_state_1': ('T', 'native SBML value', 'T observable. Maps to SBML symbol `T`.'), 'model_state_2': ('N', 'native SBML value', 'N observable. Maps to SBML symbol `N`.'), 'model_state_3': ('D', 'native SBML value', 'D observable. Maps to SBML symbol `D`.'), 'model_state_4': ('L', 'native SBML value', 'L observable. Maps to SBML symbol `L`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000888.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
