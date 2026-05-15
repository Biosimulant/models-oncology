# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Kim2007 - Crosstalk between Wnt and ERK pathways."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kim2007CrosstalkBetweenWntAndErkPathwaysBiomd0000000149Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000149'
    _TITLE = 'Kim2007 - Crosstalk between Wnt and ERK pathways'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10', 'X11', 'X12', 'X13', 'X14', 'X15', 'X16', 'X17', 'X18', 'X19', 'X20', 'X21', 'X22', 'X23', 'X24', 'X25', 'X26', 'X27', 'X28']
    _SPECIES_LABELS = {'X16': 'Rasi', 'X18': 'Raf 1', 'X19': 'Raf 1 ast', 'X22': 'ERK', 'X23': 'ERK ast', 'X24': 'Raf1/RKIP'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_rasi': ('X16', 200.0, 'native SBML value', 'Initial Rasi. Sets the initial value of bundled SBML symbol `X16`.'), 'initial_raf_1': ('X18', 112.5585, 'native SBML value', 'Initial Raf 1. Sets the initial value of bundled SBML symbol `X18`.'), 'initial_raf_1_ast': ('X19', 6.486, 'native SBML value', 'Initial Raf 1 ast. Sets the initial value of bundled SBML symbol `X19`.'), 'initial_erk': ('X22', 297.8897, 'native SBML value', 'Initial ERK. Sets the initial value of bundled SBML symbol `X22`.'), 'initial_erk_ast': ('X23', 2.1103, 'native SBML value', 'Initial ERK ast. Sets the initial value of bundled SBML symbol `X23`.'), 'initial_raf1_rkip': ('X24', 180.9595, 'native SBML value', 'Initial Raf1/RKIP. Sets the initial value of bundled SBML symbol `X24`.')}
    _HEADLINE_OUTPUTS = {'rasi': ('X16', 'native SBML value', 'Rasi observable. Maps to SBML symbol `X16`.'), 'raf_1': ('X18', 'native SBML value', 'Raf 1 observable. Maps to SBML symbol `X18`.'), 'raf_1_ast': ('X19', 'native SBML value', 'Raf 1 ast observable. Maps to SBML symbol `X19`.'), 'erk': ('X22', 'native SBML value', 'ERK observable. Maps to SBML symbol `X22`.'), 'erk_ast': ('X23', 'native SBML value', 'ERK ast observable. Maps to SBML symbol `X23`.'), 'raf1_rkip': ('X24', 'native SBML value', 'Raf1/RKIP observable. Maps to SBML symbol `X24`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000149.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
