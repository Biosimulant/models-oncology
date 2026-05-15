# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Kosinsky2018 - Radiation and PD-(L)1 treatment combinations."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kosinsky2018RadiationAndPdL1TreatmentCombBiomd0000000863Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000863'
    _TITLE = 'Kosinsky2018 - Radiation and PD-(L)1 treatment combinations'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['TV', 'U', 'nTeff', 'dTeff', 'PDL1', 'TVd']
    _SPECIES_LABELS = {'TV': 'TV', 'U': 'DSB', 'PDL1': 'PDL1', 'TVd': 'TVD', 'nTeff': 'TC ND', 'dTeff': 'TC D'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'radiation_dose': ('radiation_Dose', 0.0, 'native SBML value', 'Radiation Dose source parameter. Maps to bundled SBML parameter `radiation_Dose`.'), 'initial_dsb': ('U', 0.0, 'native SBML value', 'Initial DSB. Sets the initial value of bundled SBML symbol `U`.'), 'initial_pdl1': ('PDL1', 0.0, 'native SBML value', 'Initial PDL1. Sets the initial value of bundled SBML symbol `PDL1`.'), 'initial_tvd': ('TVd', 0.0, 'native SBML value', 'Initial TVD. Sets the initial value of bundled SBML symbol `TVd`.'), 'initial_tc_nd': ('nTeff', 0.0, 'native SBML value', 'Initial TC ND. Sets the initial value of bundled SBML symbol `nTeff`.'), 'initial_tc_d': ('dTeff', 0.0, 'native SBML value', 'Initial TC D. Sets the initial value of bundled SBML symbol `dTeff`.')}
    _HEADLINE_OUTPUTS = {'model_state_1': ('TV', 'native SBML value', 'TV observable. Maps to SBML symbol `TV`.'), 'dsb': ('U', 'native SBML value', 'DSB observable. Maps to SBML symbol `U`.'), 'pdl1': ('PDL1', 'native SBML value', 'PDL1 observable. Maps to SBML symbol `PDL1`.'), 'tvd': ('TVd', 'native SBML value', 'TVD observable. Maps to SBML symbol `TVd`.'), 'tc_nd': ('nTeff', 'native SBML value', 'TC ND observable. Maps to SBML symbol `nTeff`.'), 'tc_d': ('dTeff', 'native SBML value', 'TC D observable. Maps to SBML symbol `dTeff`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000863.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
