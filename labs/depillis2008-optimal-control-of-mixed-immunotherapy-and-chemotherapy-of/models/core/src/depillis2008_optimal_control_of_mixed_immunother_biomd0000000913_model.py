# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for dePillis2008 - Optimal control of mixed immunotherapy and chemotherapy of tumors."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Depillis2008OptimalControlOfMixedImmunotherBiomd0000000913Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000913'
    _TITLE = 'dePillis2008 - Optimal control of mixed immunotherapy and chemotherapy of tumors'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T', 'L', 'N', 'C', 'I', 'M']
    _SPECIES_LABELS = {'T': 'Tumor Cells', 'L': 'L', 'N': 'N', 'C': 'C', 'I': 'I', 'M': 'M'}
    _PARAMETER_INPUTS = {'chemotherapy_drug_level': ('D', 6.6666657777779e-07, 'native SBML value', 'Chemotherapy Drug Level. Overrides bundled SBML parameter `D`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_tumor_cells': ('T', 10000000.0, 'native SBML value', 'Initial Tumor Cells. Sets the initial value of bundled SBML symbol `T`.')}
    _HEADLINE_OUTPUTS = {'tumor_cells': ('T', 'native SBML value', 'Tumor Cells observable. Maps to SBML symbol `T`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000913.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
