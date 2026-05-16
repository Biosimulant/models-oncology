# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Nguyen2016 - Feedback regulation in cell signalling: Lessons for cancer therapeutics."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Nguyen2016FeedbackRegulationInCellSignallinBiomd0000000651Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000651'
    _TITLE = 'Nguyen2016 - Feedback regulation in cell signalling: Lessons for cancer therapeutics'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['IRS', 'aIRS', 'iIRS', 'PI3K', 'aPI3K', 'Akt', 'aAkt', 'mTORC1', 'amTORC1', 'S6K', 'aS6K', 'FOXO', 'iFOXO', 'RTK', 'aRTK', 'iRTK', 'RasGDP', 'RasGTP', 'Raf', 'aRaf', 'iRaf', 'MEK', 'aMEK', 'ERK', 'aERK', 'AktI', 'iAkt', 'MEKI', 'iMEK']
    _SPECIES_LABELS = {'PI3K': 'PI3K', 'Akt': 'AKT', 'Raf': 'Raf', 'ERK': 'ERK', 'aAkt': 'AAkt', 'RasGDP': 'RasGDP'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_pi3_k': ('PI3K', 100.0, 'native SBML value', 'Initial PI3K. Sets the initial value of bundled SBML symbol `PI3K`.'), 'initial_akt': ('Akt', 100.0, 'native SBML value', 'Initial AKT. Sets the initial value of bundled SBML symbol `Akt`.'), 'initial_raf': ('Raf', 100.0, 'native SBML value', 'Initial Raf. Sets the initial value of bundled SBML symbol `Raf`.'), 'initial_erk': ('ERK', 899.999999999996, 'native SBML value', 'Initial ERK. Sets the initial value of bundled SBML symbol `ERK`.'), 'initial_aakt': ('aAkt', 0.0, 'native SBML value', 'Initial AAkt. Sets the initial value of bundled SBML symbol `aAkt`.'), 'initial_ras_gdp': ('RasGDP', 100.0, 'native SBML value', 'Initial RasGDP. Sets the initial value of bundled SBML symbol `RasGDP`.')}
    _HEADLINE_OUTPUTS = {'pi3_k': ('PI3K', 'native SBML value', 'PI3K observable. Maps to SBML symbol `PI3K`.'), 'akt': ('Akt', 'native SBML value', 'AKT observable. Maps to SBML symbol `Akt`.'), 'raf': ('Raf', 'native SBML value', 'Raf observable. Maps to SBML symbol `Raf`.'), 'erk': ('ERK', 'native SBML value', 'ERK observable. Maps to SBML symbol `ERK`.'), 'aakt': ('aAkt', 'native SBML value', 'AAkt observable. Maps to SBML symbol `aAkt`.'), 'ras_gdp': ('RasGDP', 'native SBML value', 'RasGDP observable. Maps to SBML symbol `RasGDP`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000651.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
