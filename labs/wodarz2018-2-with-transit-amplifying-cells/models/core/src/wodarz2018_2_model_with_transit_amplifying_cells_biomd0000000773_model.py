# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Wodarz2018/2 - model with transit amplifying cells."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Wodarz20182ModelWithTransitAmplifyingCellsBiomd0000000773Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000773'
    _TITLE = 'Wodarz2018/2 - model with transit amplifying cells'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['S', 'T', 'D']
    _SPECIES_LABELS = {'S': 'Stem-Like Cells', 'T': 'Transit-Amplifying Cells', 'D': 'Differentiated Cells'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_stem_like_cells': ('S', 1.0, 'native SBML value', 'Initial Stem-Like Cells. Sets the initial value of bundled SBML symbol `S`.'), 'initial_transit_amplifying_cells': ('T', 0.0, 'native SBML value', 'Initial Transit-Amplifying Cells. Sets the initial value of bundled SBML symbol `T`.'), 'initial_differentiated_cells': ('D', 0.0, 'native SBML value', 'Initial Differentiated Cells. Sets the initial value of bundled SBML symbol `D`.')}
    _HEADLINE_OUTPUTS = {'stem_like_cells': ('S', 'native SBML value', 'Stem-Like Cells observable. Maps to SBML symbol `S`.'), 'transit_amplifying_cells': ('T', 'native SBML value', 'Transit-Amplifying Cells observable. Maps to SBML symbol `T`.'), 'differentiated_cells': ('D', 'native SBML value', 'Differentiated Cells observable. Maps to SBML symbol `D`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000773.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
