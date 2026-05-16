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
    _SPECIES_LABELS = {'T': 'Tumor Cells', 'N': 'N', 'D': 'Drug Level', 'L': 'L'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_tumor_cells': ('T', 100.0, 'native SBML value', 'Initial Tumor Cells. Sets the initial value of bundled SBML symbol `T`.'), 'initial_drug_level': ('D', 1.0, 'native SBML value', 'Initial Drug Level. Sets the initial value of bundled SBML symbol `D`.')}
    _HEADLINE_OUTPUTS = {'tumor_cells': ('T', 'native SBML value', 'Tumor Cells observable. Maps to SBML symbol `T`.'), 'drug_level': ('D', 'native SBML value', 'Drug Level observable. Maps to SBML symbol `D`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000888.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
