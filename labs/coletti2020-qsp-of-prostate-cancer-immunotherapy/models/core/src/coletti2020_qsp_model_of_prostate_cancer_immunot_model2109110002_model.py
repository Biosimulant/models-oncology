# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Coletti2020 - QSP model of prostate cancer immunotherapy."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Coletti2020QspModelOfProstateCancerImmunotModel2109110002Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'MODEL2109110002'
    _TITLE = 'Coletti2020 - QSP model of prostate cancer immunotherapy'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['X_1', 'X_2', 'A', 'D_m', 'V', 'C_2', 'I_2', 'N', 'R_2', 'M', 'D_f', 'D_r', 'C_1', 'R_1', 'I_1', 'AI', 'AR', 'AM', 'ICB']
    _SPECIES_LABELS = {'X_1': 'X 1', 'A': 'A', 'D_m': 'D m', 'C_2': 'C 2', 'I_2': 'I 2', 'N': 'N'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'k_antiil_level': ('k_antiIl', 0.714, 'native SBML value', 'K antiIl source parameter. Maps to bundled SBML parameter `k_antiIl`.')}
    _HEADLINE_OUTPUTS = {'model_state_1': ('X_1', 'native SBML value', 'X 1 observable. Maps to SBML symbol `X_1`.'), 'model_state_2': ('A', 'native SBML value', 'A observable. Maps to SBML symbol `A`.'), 'model_state_3': ('D_m', 'native SBML value', 'D m observable. Maps to SBML symbol `D_m`.'), 'model_state_4': ('C_2', 'native SBML value', 'C 2 observable. Maps to SBML symbol `C_2`.'), 'model_state_5': ('I_2', 'native SBML value', 'I 2 observable. Maps to SBML symbol `I_2`.'), 'model_state_6': ('N', 'native SBML value', 'N observable. Maps to SBML symbol `N`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2109110002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
