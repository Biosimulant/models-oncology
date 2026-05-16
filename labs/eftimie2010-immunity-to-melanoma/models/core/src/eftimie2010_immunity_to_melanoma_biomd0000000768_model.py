# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Eftimie2010 - immunity to melanoma."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Eftimie2010ImmunityToMelanomaBiomd0000000768Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000768'
    _TITLE = 'Eftimie2010 - immunity to melanoma'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Th', 'T', 'Cs', 'Cp', 'C']
    _SPECIES_LABELS = {'T': 'Melanoma Cells', 'Th': 'Helper T Cells', 'Cs': 'Cs', 'Cp': 'Cp', 'C': 'C'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_melanoma_cells': ('T', 100000.0, 'native SBML value', 'Initial Melanoma Cells. Sets the initial value of bundled SBML symbol `T`.'), 'initial_helper_t_cells': ('Th', 0.0, 'native SBML value', 'Initial Helper T Cells. Sets the initial value of bundled SBML symbol `Th`.')}
    _HEADLINE_OUTPUTS = {'melanoma_cells': ('T', 'native SBML value', 'Melanoma Cells observable. Maps to SBML symbol `T`.'), 'helper_t_cells': ('Th', 'native SBML value', 'Helper T Cells observable. Maps to SBML symbol `Th`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000768.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
