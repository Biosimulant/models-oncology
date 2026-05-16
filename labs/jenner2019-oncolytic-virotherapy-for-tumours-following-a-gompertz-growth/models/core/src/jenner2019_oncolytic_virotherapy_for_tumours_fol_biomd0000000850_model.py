# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Jenner2019 - Oncolytic virotherapy for tumours following a Gompertz growth law."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Jenner2019OncolyticVirotherapyForTumoursFolBiomd0000000850Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000850'
    _TITLE = 'Jenner2019 - Oncolytic virotherapy for tumours following a Gompertz growth law'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['U', 'I', 'V']
    _SPECIES_LABELS = {'U': 'Uninfected Tumor Cells', 'I': 'Infected Tumor Cells', 'V': 'Virus Load'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_uninfected_tumor_cells': ('U', 75.0, 'native SBML value', 'Initial Uninfected Tumor Cells. Sets the initial value of bundled SBML symbol `U`.'), 'initial_infected_tumor_cells': ('I', 100.0, 'native SBML value', 'Initial Infected Tumor Cells. Sets the initial value of bundled SBML symbol `I`.'), 'initial_virus_load': ('V', 10.0, 'native SBML value', 'Initial Virus Load. Sets the initial value of bundled SBML symbol `V`.')}
    _HEADLINE_OUTPUTS = {'uninfected_tumor_cells': ('U', 'native SBML value', 'Uninfected Tumor Cells observable. Maps to SBML symbol `U`.'), 'infected_tumor_cells': ('I', 'native SBML value', 'Infected Tumor Cells observable. Maps to SBML symbol `I`.'), 'virus_load': ('V', 'native SBML value', 'Virus Load observable. Maps to SBML symbol `V`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000850.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
