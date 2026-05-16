# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Ontah2019 - Dynamic analysis of a tumor treatment model using oncolytic virus and chemotherapy with saturated infection rate."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Ontah2019DynamicAnalysisOfATumorTreatmentBiomd0000000877Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000877'
    _TITLE = 'Ontah2019 - Dynamic analysis of a tumor treatment model using oncolytic virus and chemotherapy with saturated infection rate'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['U', 'I', 'V', 'C']
    _SPECIES_LABELS = {'U': 'Uninfected Tumor Cells', 'I': 'Infected Tumor Cells', 'V': 'Virus Load', 'C': 'Chemotherapy Level'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_uninfected_tumor_cells': ('U', 100.0, 'native SBML value', 'Initial Uninfected Tumor Cells. Sets the initial value of bundled SBML symbol `U`.'), 'initial_infected_tumor_cells': ('I', 10.0, 'native SBML value', 'Initial Infected Tumor Cells. Sets the initial value of bundled SBML symbol `I`.'), 'initial_virus_load': ('V', 10.0, 'native SBML value', 'Initial Virus Load. Sets the initial value of bundled SBML symbol `V`.'), 'initial_chemotherapy_level': ('C', 30.0, 'native SBML value', 'Initial Chemotherapy Level. Sets the initial value of bundled SBML symbol `C`.')}
    _HEADLINE_OUTPUTS = {'uninfected_tumor_cells': ('U', 'native SBML value', 'Uninfected Tumor Cells observable. Maps to SBML symbol `U`.'), 'infected_tumor_cells': ('I', 'native SBML value', 'Infected Tumor Cells observable. Maps to SBML symbol `I`.'), 'virus_load': ('V', 'native SBML value', 'Virus Load observable. Maps to SBML symbol `V`.'), 'chemotherapy_level': ('C', 'native SBML value', 'Chemotherapy Level observable. Maps to SBML symbol `C`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000877.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
