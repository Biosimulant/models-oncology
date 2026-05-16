# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Wodarz2018/1 - simple model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Wodarz20181SimpleModelBiomd0000000774Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000774'
    _TITLE = 'Wodarz2018/1 - simple model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['S', 'D']
    _SPECIES_LABELS = {'S': 'Stem-Like Cells', 'D': 'Differentiated Cells'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_stem_like_cells': ('S', 1.0, 'native SBML value', 'Initial Stem-Like Cells. Sets the initial value of bundled SBML symbol `S`.'), 'initial_differentiated_cells': ('D', 0.0, 'native SBML value', 'Initial Differentiated Cells. Sets the initial value of bundled SBML symbol `D`.')}
    _HEADLINE_OUTPUTS = {'stem_like_cells': ('S', 'native SBML value', 'Stem-Like Cells observable. Maps to SBML symbol `S`.'), 'differentiated_cells': ('D', 'native SBML value', 'Differentiated Cells observable. Maps to SBML symbol `D`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000774.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
