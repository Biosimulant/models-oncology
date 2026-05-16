# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Jenner2018 - treatment of oncolytic virus."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Jenner2018TreatmentOfOncolyticVirusBiomd0000000789Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000789'
    _TITLE = 'Jenner2018 - treatment of oncolytic virus'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['V', 'S', 'I']
    _SPECIES_LABELS = {'S': 'Susceptible Tumor Cells', 'V': 'Virus Load', 'I': 'Infected Tumor Cells'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_virus_load': ('V', 0.0, 'native SBML value', 'Initial Virus Load. Sets the initial value of bundled SBML symbol `V`.'), 'initial_susceptible_tumor_cells': ('S', 251000000.0, 'native SBML value', 'Initial Susceptible Tumor Cells. Sets the initial value of bundled SBML symbol `S`.'), 'initial_infected_tumor_cells': ('I', 0.0, 'native SBML value', 'Initial Infected Tumor Cells. Sets the initial value of bundled SBML symbol `I`.')}
    _HEADLINE_OUTPUTS = {'virus_load': ('V', 'native SBML value', 'Virus Load observable. Maps to SBML symbol `V`.'), 'susceptible_tumor_cells': ('S', 'native SBML value', 'Susceptible Tumor Cells observable. Maps to SBML symbol `S`.'), 'infected_tumor_cells': ('I', 'native SBML value', 'Infected Tumor Cells observable. Maps to SBML symbol `I`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000789.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
