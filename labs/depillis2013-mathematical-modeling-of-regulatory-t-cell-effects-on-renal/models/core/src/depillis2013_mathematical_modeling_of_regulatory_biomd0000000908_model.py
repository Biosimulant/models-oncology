# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for dePillis2013 - Mathematical modeling of regulatory T cell effects on renal cell carcinoma treatment."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Depillis2013MathematicalModelingOfRegulatoryBiomd0000000908Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000908'
    _TITLE = 'dePillis2013 - Mathematical modeling of regulatory T cell effects on renal cell carcinoma treatment'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T', 'N', 'L', 'R', 'C', 'I', 'S']
    _SPECIES_LABELS = {'T': 'Tumor Cells', 'N': 'N', 'L': 'L', 'R': 'R', 'C': 'C', 'I': 'I'}
    _PARAMETER_INPUTS = {'drug_treatment_level': ('D', 9.47552761007735e-06, 'native SBML value', 'Drug Treatment Level. Overrides bundled SBML parameter `D`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_tumor_cells': ('T', 4662000000.0, 'native SBML value', 'Initial Tumor Cells. Sets the initial value of bundled SBML symbol `T`.')}
    _HEADLINE_OUTPUTS = {'tumor_cells': ('T', 'native SBML value', 'Tumor Cells observable. Maps to SBML symbol `T`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000908.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
