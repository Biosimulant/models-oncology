# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Owen1998 - tumour growth model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Owen1998TumourGrowthModelBiomd0000000670Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000670'
    _TITLE = 'Owen1998 - tumour growth model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rateRule'
    _OBSERVABLES = ['l', 'n', 'm']
    _SPECIES_LABELS = {'l': 'Macrophage', 'n': 'Normal Cells', 'm': 'Mutated Cells'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_macrophage': ('l', 0.0999999999999985, 'native SBML value', 'Initial Macrophage. Sets the initial value of bundled SBML symbol `l`.'), 'initial_normal_cells': ('n', 0.899999999999988, 'native SBML value', 'Initial Normal Cells. Sets the initial value of bundled SBML symbol `n`.'), 'initial_mutated_cells': ('m', 0.899999999999988, 'native SBML value', 'Initial Mutated Cells. Sets the initial value of bundled SBML symbol `m`.')}
    _HEADLINE_OUTPUTS = {'macrophage': ('l', 'native SBML value', 'Macrophage observable. Maps to SBML symbol `l`.'), 'normal_cells': ('n', 'native SBML value', 'Normal Cells observable. Maps to SBML symbol `n`.'), 'mutated_cells': ('m', 'native SBML value', 'Mutated Cells observable. Maps to SBML symbol `m`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000670.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
