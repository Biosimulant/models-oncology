# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Zhu2015 - Combined gemcitabine and birinapant in pancreatic cancer cells - mechanistic PD model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Zhu2015CombinedGemcitabineAndBirinapantInPBiomd0000000669Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000669'
    _TITLE = 'Zhu2015 - Combined gemcitabine and birinapant in pancreatic cancer cells - mechanistic PD model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rateRule'
    _OBSERVABLES = ['G1', 'S', 'G2', 'R_apo', 'R_other']
    _SPECIES_LABELS = {'G1': 'G1', 'S': 'S', 'G2': 'G2', 'R_apo': 'R apo', 'R_other': 'R other'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'g1': ('G1', 'native SBML value', 'G1 observable. Maps to SBML symbol `G1`.'), 'model_state_2': ('S', 'native SBML value', 'S observable. Maps to SBML symbol `S`.'), 'g2': ('G2', 'native SBML value', 'G2 observable. Maps to SBML symbol `G2`.'), 'r_apo': ('R_apo', 'native SBML value', 'R apo observable. Maps to SBML symbol `R_apo`.'), 'r_other': ('R_other', 'native SBML value', 'R other observable. Maps to SBML symbol `R_other`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000669.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
