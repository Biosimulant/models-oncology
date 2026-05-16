# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Mkango2019 - Dynamics of Breast Cancer under DifferentRates of Chemoradiotherapy."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Mkango2019DynamicsOfBreastCancerUnderDiffeModel1912120005Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'MODEL1912120005'
    _TITLE = 'Mkango2019 - Dynamics of Breast Cancer under DifferentRates of Chemoradiotherapy'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T', 'TR', 'N', 'I', 'M', 'R']
    _SPECIES_LABELS = {'T': 'Breast Tumor Cells', 'TR': 'TR', 'N': 'N', 'I': 'I', 'M': 'M', 'R': 'R'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_breast_tumor_cells': ('T', 3500000.0, 'native SBML value', 'Initial Breast Tumor Cells. Sets the initial value of bundled SBML symbol `T`.')}
    _HEADLINE_OUTPUTS = {'breast_tumor_cells': ('T', 'native SBML value', 'Breast Tumor Cells observable. Maps to SBML symbol `T`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1912120005.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
