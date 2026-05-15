# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Chakrabarty2010 - A control theory approach to cancer remission aided by an optimal therapy."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Chakrabarty2010AControlTheoryApproachToCanBiomd0000000777Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000777'
    _TITLE = 'Chakrabarty2010 - A control theory approach to cancer remission aided by an optimal therapy'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['M_Tumor_Cells', 'N_CTL', 'Z_THL']
    _SPECIES_LABELS = {'M_Tumor_Cells': 'M Tumor Cells', 'N_CTL': 'N CTL', 'Z_THL': 'Z THL'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_m_tumor_cells': ('M_Tumor_Cells', 2750000.0, 'native SBML value', 'Initial M Tumor Cells. Sets the initial value of bundled SBML symbol `M_Tumor_Cells`.'), 'initial_n_ctl': ('N_CTL', 200000.0, 'native SBML value', 'Initial N CTL. Sets the initial value of bundled SBML symbol `N_CTL`.'), 'initial_z_thl': ('Z_THL', 7200000.0, 'native SBML value', 'Initial Z THL. Sets the initial value of bundled SBML symbol `Z_THL`.')}
    _HEADLINE_OUTPUTS = {'m_tumor_cells': ('M_Tumor_Cells', 'native SBML value', 'M Tumor Cells observable. Maps to SBML symbol `M_Tumor_Cells`.'), 'n_ctl': ('N_CTL', 'native SBML value', 'N CTL observable. Maps to SBML symbol `N_CTL`.'), 'z_thl': ('Z_THL', 'native SBML value', 'Z THL observable. Maps to SBML symbol `Z_THL`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000777.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
