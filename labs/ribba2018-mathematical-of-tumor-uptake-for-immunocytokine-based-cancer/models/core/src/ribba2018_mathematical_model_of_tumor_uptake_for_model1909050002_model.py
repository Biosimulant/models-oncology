# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Ribba2018 - Mathematical Model of Tumor Uptake for Immunocytokine-Based Cancer Immunotherapy."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Ribba2018MathematicalModelOfTumorUptakeForModel1909050002Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'MODEL1909050002'
    _TITLE = 'Ribba2018 - Mathematical Model of Tumor Uptake for Immunocytokine-Based Cancer Immunotherapy'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['A_1_b', 'C_4_T']
    _SPECIES_LABELS = {'A_1_b': 'A 1 b', 'C_4_T': 'C 4 T'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'epsilon_level': ('epsilon', 0.25, 'native SBML value', 'Epsilon source parameter. Maps to bundled SBML parameter `epsilon`.'), 'initial_for_epsilon': ('ModelValue_2', 0.25, 'native SBML value', 'Initial for epsilon source parameter. Maps to bundled SBML parameter `ModelValue_2`.'), 'initial_a_1_b': ('A_1_b', 8.0, 'native SBML value', 'Initial A 1 b. Sets the initial value of bundled SBML symbol `A_1_b`.'), 'initial_c_4_t': ('C_4_T', 0.0, 'native SBML value', 'Initial C 4 T. Sets the initial value of bundled SBML symbol `C_4_T`.')}
    _HEADLINE_OUTPUTS = {'a_1_b': ('A_1_b', 'native SBML value', 'A 1 b observable. Maps to SBML symbol `A_1_b`.'), 'c_4_t': ('C_4_T', 'native SBML value', 'C 4 T observable. Maps to SBML symbol `C_4_T`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1909050002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
