# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Segun2018 - model of breast cancer determing Chemotherapy and Keto diet response."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Segun2018ModelOfBreastCancerDetermingChemoModel2003050001Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'MODEL2003050001'
    _TITLE = 'Segun2018 - model of breast cancer determing Chemotherapy and Keto diet response'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['N', 'T', 'M', 'E']
    _SPECIES_LABELS = {'N': 'Normal Cells', 'T': 'Breast Tumor Cells', 'M': 'M', 'E': 'E'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_breast_tumor_cells': ('T', 800.0, 'native SBML value', 'Initial Breast Tumor Cells. Sets the initial value of bundled SBML symbol `T`.'), 'initial_normal_cells': ('N', 2000.0, 'native SBML value', 'Initial Normal Cells. Sets the initial value of bundled SBML symbol `N`.')}
    _HEADLINE_OUTPUTS = {'breast_tumor_cells': ('T', 'native SBML value', 'Breast Tumor Cells observable. Maps to SBML symbol `T`.'), 'normal_cells': ('N', 'native SBML value', 'Normal Cells observable. Maps to SBML symbol `N`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2003050001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
