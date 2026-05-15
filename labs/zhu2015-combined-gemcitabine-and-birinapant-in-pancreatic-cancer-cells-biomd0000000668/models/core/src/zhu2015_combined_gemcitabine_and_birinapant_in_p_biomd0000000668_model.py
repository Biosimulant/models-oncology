# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Zhu2015 - Combined gemcitabine and birinapant in pancreatic cancer cells - basic PD model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Zhu2015CombinedGemcitabineAndBirinapantInPBiomd0000000668Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000668'
    _TITLE = 'Zhu2015 - Combined gemcitabine and birinapant in pancreatic cancer cells - basic PD model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Sti_g1', 'Sti_g2', 'Sti_g3', 'Sti_g4', 'Sti_b1', 'Sti_b2', 'Sti_b3', 'Sti_b4']
    _SPECIES_LABELS = {'Sti_g1': 'Sti g1', 'Sti_g2': 'Sti g2', 'Sti_g3': 'Sti g3', 'Sti_g4': 'Sti g4', 'Sti_b1': 'Sti b1', 'Sti_b2': 'Sti b2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_sti_g1': ('Sti_g1', 0.0, 'native SBML value', 'Initial Sti g1. Sets the initial value of bundled SBML symbol `Sti_g1`.'), 'initial_sti_g2': ('Sti_g2', 0.0, 'native SBML value', 'Initial Sti g2. Sets the initial value of bundled SBML symbol `Sti_g2`.'), 'initial_sti_g3': ('Sti_g3', 0.0, 'native SBML value', 'Initial Sti g3. Sets the initial value of bundled SBML symbol `Sti_g3`.'), 'initial_sti_g4': ('Sti_g4', 0.0, 'native SBML value', 'Initial Sti g4. Sets the initial value of bundled SBML symbol `Sti_g4`.'), 'initial_sti_b1': ('Sti_b1', 0.0, 'native SBML value', 'Initial Sti b1. Sets the initial value of bundled SBML symbol `Sti_b1`.'), 'initial_sti_b2': ('Sti_b2', 0.0, 'native SBML value', 'Initial Sti b2. Sets the initial value of bundled SBML symbol `Sti_b2`.')}
    _HEADLINE_OUTPUTS = {'sti_g1': ('Sti_g1', 'native SBML value', 'Sti g1 observable. Maps to SBML symbol `Sti_g1`.'), 'sti_g2': ('Sti_g2', 'native SBML value', 'Sti g2 observable. Maps to SBML symbol `Sti_g2`.'), 'sti_g3': ('Sti_g3', 'native SBML value', 'Sti g3 observable. Maps to SBML symbol `Sti_g3`.'), 'sti_g4': ('Sti_g4', 'native SBML value', 'Sti g4 observable. Maps to SBML symbol `Sti_g4`.'), 'sti_b1': ('Sti_b1', 'native SBML value', 'Sti b1 observable. Maps to SBML symbol `Sti_b1`.'), 'sti_b2': ('Sti_b2', 'native SBML value', 'Sti b2 observable. Maps to SBML symbol `Sti_b2`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000668.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
