# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Moore_2004_Mathematical model for CML and T cell interaction."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Moore2004MathematicalModelForCmlAndTCellBiomd0000000733Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000733'
    _TITLE = 'Moore_2004_Mathematical model for CML and T cell interaction'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['naive_Tcells', 'eff_Tcells', 'tumor_cells']
    _SPECIES_LABELS = {'tumor_cells': 'Tumor cells', 'naive_Tcells': 'Naive Tcells', 'eff_Tcells': 'Eff Tcells'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_tumor_cells': ('tumor_cells', 10000.0, 'native SBML value', 'Initial Tumor cells. Sets the initial value of bundled SBML symbol `tumor_cells`.'), 'initial_naive_tcells': ('naive_Tcells', 1510.0, 'native SBML value', 'Initial Naive Tcells. Sets the initial value of bundled SBML symbol `naive_Tcells`.'), 'initial_eff_tcells': ('eff_Tcells', 20.0, 'native SBML value', 'Initial Eff Tcells. Sets the initial value of bundled SBML symbol `eff_Tcells`.')}
    _HEADLINE_OUTPUTS = {'tumor_cells': ('tumor_cells', 'native SBML value', 'Tumor cells observable. Maps to SBML symbol `tumor_cells`.'), 'naive_tcells': ('naive_Tcells', 'native SBML value', 'Naive Tcells observable. Maps to SBML symbol `naive_Tcells`.'), 'eff_tcells': ('eff_Tcells', 'native SBML value', 'Eff Tcells observable. Maps to SBML symbol `eff_Tcells`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000733.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
