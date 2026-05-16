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
    _SPECIES_LABELS = {'T': 'Breast Tumor Cells', 'N': 'N', 'C': 'C', 'E': 'E', 'L': 'L'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_breast_tumor_cells': ('T', 1000000.0, 'native SBML value', 'Initial Breast Tumor Cells. Sets the initial value of bundled SBML symbol `T`.')}
    _HEADLINE_OUTPUTS = {'breast_tumor_cells': ('T', 'native SBML value', 'Breast Tumor Cells observable. Maps to SBML symbol `T`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1909090002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
