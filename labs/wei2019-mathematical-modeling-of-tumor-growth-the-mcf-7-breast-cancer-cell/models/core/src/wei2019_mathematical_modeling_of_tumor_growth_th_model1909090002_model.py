# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Wei2019 - Mathematical modeling of tumor growth The MCF-7 breast cancer cell line."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Wei2019MathematicalModelingOfTumorGrowthThModel1909090002Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'MODEL1909090002'
    _TITLE = 'Wei2019 - Mathematical modeling of tumor growth The MCF-7 breast cancer cell line'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T', 'N', 'L', 'C', 'E']
    _SPECIES_LABELS = {'T': 'T', 'N': 'N', 'C': 'C', 'E': 'E', 'L': 'L'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'model_state_1': ('T', 'native SBML value', 'T observable. Maps to SBML symbol `T`.'), 'model_state_2': ('N', 'native SBML value', 'N observable. Maps to SBML symbol `N`.'), 'model_state_3': ('C', 'native SBML value', 'C observable. Maps to SBML symbol `C`.'), 'model_state_4': ('E', 'native SBML value', 'E observable. Maps to SBML symbol `E`.'), 'model_state_5': ('L', 'native SBML value', 'L observable. Maps to SBML symbol `L`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1909090002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
