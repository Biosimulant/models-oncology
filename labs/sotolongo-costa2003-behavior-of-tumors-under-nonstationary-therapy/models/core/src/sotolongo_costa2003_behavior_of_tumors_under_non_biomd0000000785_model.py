# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Sotolongo-Costa2003 - Behavior of tumors under nonstationary therapy."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SotolongoCosta2003BehaviorOfTumorsUnderNonBiomd0000000785Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000785'
    _TITLE = 'Sotolongo-Costa2003 - Behavior of tumors under nonstationary therapy'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['x_Malignant_Cells', 'y_Lymphocytes']
    _SPECIES_LABELS = {'x_Malignant_Cells': 'X Malignant Cells', 'y_Lymphocytes': 'Y Lymphocytes'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_x_malignant_cells': ('x_Malignant_Cells', 5.3, 'native SBML value', 'Initial X Malignant Cells. Sets the initial value of bundled SBML symbol `x_Malignant_Cells`.'), 'initial_y_lymphocytes': ('y_Lymphocytes', 6.7, 'native SBML value', 'Initial Y Lymphocytes. Sets the initial value of bundled SBML symbol `y_Lymphocytes`.')}
    _HEADLINE_OUTPUTS = {'x_malignant_cells': ('x_Malignant_Cells', 'native SBML value', 'X Malignant Cells observable. Maps to SBML symbol `x_Malignant_Cells`.'), 'y_lymphocytes': ('y_Lymphocytes', 'native SBML value', 'Y Lymphocytes observable. Maps to SBML symbol `y_Lymphocytes`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000785.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
