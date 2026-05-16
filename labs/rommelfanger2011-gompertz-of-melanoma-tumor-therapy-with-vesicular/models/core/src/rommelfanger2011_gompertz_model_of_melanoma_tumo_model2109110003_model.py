# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Rommelfanger2011 - Gompertz model of melanoma tumor therapy with vesicular stomatitis virus."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Rommelfanger2011GompertzModelOfMelanomaTumoModel2109110003Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'MODEL2109110003'
    _TITLE = 'Rommelfanger2011 - Gompertz model of melanoma tumor therapy with vesicular stomatitis virus'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['x', 'y', 'z', 'v_i']
    _SPECIES_LABELS = {'y': 'Y', 'v_i': 'Injected Virus', 'x': 'X', 'z': 'Z'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_injected_virus': ('v_i', 500000000.0, 'native SBML value', 'Initial Injected Virus. Sets the initial value of bundled SBML symbol `v_i`.')}
    _HEADLINE_OUTPUTS = {'injected_virus': ('v_i', 'native SBML value', 'Injected Virus observable. Maps to SBML symbol `v_i`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2109110003.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
