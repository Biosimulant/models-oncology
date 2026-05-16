# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Chareyron2009 - Mixed immunotherapy and chemotherapy of tumors Feedback design and model updating schemes."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Chareyron2009MixedImmunotherapyAndChemotheraModel2001160002Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'MODEL2001160002'
    _TITLE = 'Chareyron2009 - Mixed immunotherapy and chemotherapy of tumors Feedback design and model updating schemes'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T', 'N', 'L', 'C', 'M', 'I']
    _SPECIES_LABELS = {'T': 'Tumor Cells', 'N': 'N', 'L': 'L', 'C': 'C', 'M': 'M', 'I': 'I'}
    _PARAMETER_INPUTS = {'chemotherapy_drug_level': ('D', 2.34000000000344, 'native SBML value', 'Chemotherapy Drug Level. Overrides bundled SBML parameter `D`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_tumor_cells': ('T', 50000000.0, 'native SBML value', 'Initial Tumor Cells. Sets the initial value of bundled SBML symbol `T`.')}
    _HEADLINE_OUTPUTS = {'tumor_cells': ('T', 'native SBML value', 'Tumor Cells observable. Maps to SBML symbol `T`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2001160002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
