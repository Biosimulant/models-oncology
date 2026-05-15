# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Ribba2012 - Low-grade gliomas, tumour growth inhibition model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Ribba2012LowGradeGliomasTumourGrowthInhibiBiomd0000000521Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000521'
    _TITLE = 'Ribba2012 - Low-grade gliomas, tumour growth inhibition model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['C', 'P', 'Q', 'Qp']
    _SPECIES_LABELS = {'Qp': 'Damaged quiescent cells', 'C': 'PCV plasma', 'P': 'Proliferative tissue', 'Q': 'Nonproliferative quiescent tissue'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_damaged_quiescent_cells': ('Qp', 0.0, 'native SBML value', 'Initial Damaged quiescent cells. Sets the initial value of bundled SBML symbol `Qp`.'), 'initial_pcv_plasma': ('C', 1.0, 'native SBML value', 'Initial PCV plasma. Sets the initial value of bundled SBML symbol `C`.'), 'initial_proliferative_tissue': ('P', 7.13, 'native SBML value', 'Initial Proliferative tissue. Sets the initial value of bundled SBML symbol `P`.'), 'initial_nonproliferative_quiescent_tissue': ('Q', 41.2, 'native SBML value', 'Initial Nonproliferative quiescent tissue. Sets the initial value of bundled SBML symbol `Q`.')}
    _HEADLINE_OUTPUTS = {'damaged_quiescent_cells': ('Qp', 'native SBML value', 'Damaged quiescent cells observable. Maps to SBML symbol `Qp`.'), 'pcv_plasma': ('C', 'native SBML value', 'PCV plasma observable. Maps to SBML symbol `C`.'), 'proliferative_tissue': ('P', 'native SBML value', 'Proliferative tissue observable. Maps to SBML symbol `P`.'), 'nonproliferative_quiescent_tissue': ('Q', 'native SBML value', 'Nonproliferative quiescent tissue observable. Maps to SBML symbol `Q`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000521.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
