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
    _SPECIES_LABELS = {'T': 'T', 'Th': 'Th', 'Cs': 'Cs', 'Cp': 'Cp', 'C': 'C'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'model_state_1': ('T', 'native SBML value', 'T observable. Maps to SBML symbol `T`.'), 'model_state_2': ('Th', 'native SBML value', 'Th observable. Maps to SBML symbol `Th`.'), 'model_state_3': ('Cs', 'native SBML value', 'Cs observable. Maps to SBML symbol `Cs`.'), 'model_state_4': ('Cp', 'native SBML value', 'Cp observable. Maps to SBML symbol `Cp`.'), 'model_state_5': ('C', 'native SBML value', 'C observable. Maps to SBML symbol `C`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000768.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
