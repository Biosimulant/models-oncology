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
    _SPECIES_LABELS = {'G1': 'G1 Cells', 'S': 'S-Phase Cells', 'G2': 'G2 Cells', 'R_apo': 'Apoptotic Response', 'R_other': 'Other Response'}
    _PARAMETER_INPUTS = {'gemcitabine_concentration': ('C_g', 20.0, 'native SBML value', 'Gemcitabine Concentration. Overrides bundled SBML parameter `C_g`.'), 'birinapant_concentration': ('C_b', 500.0, 'native SBML value', 'Birinapant Concentration. Overrides bundled SBML parameter `C_b`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_g1_cells': ('G1', 113516.0, 'native SBML value', 'Initial G1 Cells. Sets the initial value of bundled SBML symbol `G1`.'), 'initial_g2_cells': ('G2', 81656.0, 'native SBML value', 'Initial G2 Cells. Sets the initial value of bundled SBML symbol `G2`.')}
    _HEADLINE_OUTPUTS = {'g1_cells': ('G1', 'native SBML value', 'G1 Cells observable. Maps to SBML symbol `G1`.'), 's_phase_cells': ('S', 'native SBML value', 'S-Phase Cells observable. Maps to SBML symbol `S`.'), 'g2_cells': ('G2', 'native SBML value', 'G2 Cells observable. Maps to SBML symbol `G2`.'), 'apoptotic_response': ('R_apo', 'native SBML value', 'Apoptotic Response observable. Maps to SBML symbol `R_apo`.'), 'other_response': ('R_other', 'native SBML value', 'Other Response observable. Maps to SBML symbol `R_other`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000669.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
