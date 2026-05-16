# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Shariatpanahi2018 - Mathematical modeling of tumor-induced immunosuppression by myeloid-derived suppressor cells."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Shariatpanahi2018MathematicalModelingOfTumorModel1909090003Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'MODEL1909090003'
    _TITLE = 'Shariatpanahi2018 - Mathematical modeling of tumor-induced immunosuppression by myeloid-derived suppressor cells'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['C', 'N', 'T', 'M']
    _SPECIES_LABELS = {'C': 'C', 'N': 'N', 'T': 'Tumor Cells', 'M': 'Myeloid-Derived Suppressor Cells'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_tumor_cells': ('T', 1.0, 'native SBML value', 'Initial Tumor Cells. Sets the initial value of bundled SBML symbol `T`.'), 'initial_myeloid_derived_suppressor_cells': ('M', 5000000.0, 'native SBML value', 'Initial Myeloid-Derived Suppressor Cells. Sets the initial value of bundled SBML symbol `M`.')}
    _HEADLINE_OUTPUTS = {'tumor_cells': ('T', 'native SBML value', 'Tumor Cells observable. Maps to SBML symbol `T`.'), 'myeloid_derived_suppressor_cells': ('M', 'native SBML value', 'Myeloid-Derived Suppressor Cells observable. Maps to SBML symbol `M`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1909090003.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
