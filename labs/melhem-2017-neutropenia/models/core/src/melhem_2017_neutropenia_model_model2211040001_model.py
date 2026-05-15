# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Melhem 2017 - Neutropenia Model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Melhem2017NeutropeniaModelModel2211040001Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'MODEL2211040001'
    _TITLE = 'Melhem 2017 - Neutropenia Model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rateRule'
    _OBSERVABLES = ['Chm', 'Crt', 'Dt', 'Mt', 'Pm1', 'Pm2', 'Rb', 'Sc', 'Sm']
    _SPECIES_LABELS = {'Chm': 'Chm', 'Crt': 'Crt', 'Dt': 'Dt', 'Mt': 'Mt', 'Pm1': 'Pm1', 'Pm2': 'Pm2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_chm': ('Chm', 0.0, 'native SBML value', 'Initial Chm. Sets the initial value of bundled SBML symbol `Chm`.'), 'initial_crt': ('Crt', 0.0, 'native SBML value', 'Initial Crt. Sets the initial value of bundled SBML symbol `Crt`.')}
    _HEADLINE_OUTPUTS = {'chm': ('Chm', 'native SBML value', 'Chm observable. Maps to SBML symbol `Chm`.'), 'crt': ('Crt', 'native SBML value', 'Crt observable. Maps to SBML symbol `Crt`.'), 'model_state_3': ('Dt', 'native SBML value', 'Dt observable. Maps to SBML symbol `Dt`.'), 'model_state_4': ('Mt', 'native SBML value', 'Mt observable. Maps to SBML symbol `Mt`.'), 'pm1': ('Pm1', 'native SBML value', 'Pm1 observable. Maps to SBML symbol `Pm1`.'), 'pm2': ('Pm2', 'native SBML value', 'Pm2 observable. Maps to SBML symbol `Pm2`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2211040001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
