# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Khajanchi2015 - The combined effects of optimal control in cancer remission."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Khajanchi2015TheCombinedEffectsOfOptimalCoBiomd0000000897Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000897'
    _TITLE = 'Khajanchi2015 - The combined effects of optimal control in cancer remission'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['E', 'T']
    _SPECIES_LABELS = {'E': 'Effector Cells', 'T': 'Tumor Cells'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_effector_cells': ('E', 1708110.0, 'native SBML value', 'Initial Effector Cells. Sets the initial value of bundled SBML symbol `E`.'), 'initial_tumor_cells': ('T', 8286380.0, 'native SBML value', 'Initial Tumor Cells. Sets the initial value of bundled SBML symbol `T`.')}
    _HEADLINE_OUTPUTS = {'effector_cells': ('E', 'native SBML value', 'Effector Cells observable. Maps to SBML symbol `E`.'), 'tumor_cells': ('T', 'native SBML value', 'Tumor Cells observable. Maps to SBML symbol `T`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000897.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
