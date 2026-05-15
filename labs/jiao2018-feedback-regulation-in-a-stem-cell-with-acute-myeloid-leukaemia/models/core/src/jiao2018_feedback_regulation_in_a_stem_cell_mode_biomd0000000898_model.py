# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Jiao2018 - Feedback regulation in a stem cell model with acute myeloid leukaemia."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Jiao2018FeedbackRegulationInAStemCellModeBiomd0000000898Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000898'
    _TITLE = 'Jiao2018 - Feedback regulation in a stem cell model with acute myeloid leukaemia'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['S_HSC', 'A_PC', 'D_TDSC', 'L_LSC', 'T_TDLC']
    _SPECIES_LABELS = {'S_HSC': 'S HSC', 'A_PC': 'A PC', 'L_LSC': 'L LSC', 'D_TDSC': 'D TDSC', 'T_TDLC': 'T TDLC'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_s_hsc': ('S_HSC', 10.0, 'native SBML value', 'Initial S HSC. Sets the initial value of bundled SBML symbol `S_HSC`.'), 'initial_a_pc': ('A_PC', 0.0, 'native SBML value', 'Initial A PC. Sets the initial value of bundled SBML symbol `A_PC`.'), 'initial_l_lsc': ('L_LSC', 10.0, 'native SBML value', 'Initial L LSC. Sets the initial value of bundled SBML symbol `L_LSC`.'), 'initial_d_tdsc': ('D_TDSC', 0.0, 'native SBML value', 'Initial D TDSC. Sets the initial value of bundled SBML symbol `D_TDSC`.'), 'initial_t_tdlc': ('T_TDLC', 0.0, 'native SBML value', 'Initial T TDLC. Sets the initial value of bundled SBML symbol `T_TDLC`.')}
    _HEADLINE_OUTPUTS = {'s_hsc': ('S_HSC', 'native SBML value', 'S HSC observable. Maps to SBML symbol `S_HSC`.'), 'a_pc': ('A_PC', 'native SBML value', 'A PC observable. Maps to SBML symbol `A_PC`.'), 'l_lsc': ('L_LSC', 'native SBML value', 'L LSC observable. Maps to SBML symbol `L_LSC`.'), 'd_tdsc': ('D_TDSC', 'native SBML value', 'D TDSC observable. Maps to SBML symbol `D_TDSC`.'), 't_tdlc': ('T_TDLC', 'native SBML value', 'T TDLC observable. Maps to SBML symbol `T_TDLC`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000898.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
