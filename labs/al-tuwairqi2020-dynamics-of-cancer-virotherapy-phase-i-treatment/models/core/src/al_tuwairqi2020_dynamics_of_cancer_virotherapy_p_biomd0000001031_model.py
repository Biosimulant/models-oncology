# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Al-Tuwairqi2020 - Dynamics of cancer virotherapy - Phase I treatment."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class AlTuwairqi2020DynamicsOfCancerVirotherapyPBiomd0000001031Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000001031'
    _TITLE = 'Al-Tuwairqi2020 - Dynamics of cancer virotherapy - Phase I treatment'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['uninfected_cancer_cells', 'infected_cancer_cells', 'free_virus']
    _SPECIES_LABELS = {'uninfected_cancer_cells': 'Uninfected cancer cells', 'infected_cancer_cells': 'Infected cancer cells', 'free_virus': 'Free virus'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_uninfected_cancer_cells': ('uninfected_cancer_cells', 0.6, 'native SBML value', 'Initial Uninfected cancer cells. Sets the initial value of bundled SBML symbol `uninfected_cancer_cells`.'), 'initial_infected_cancer_cells': ('infected_cancer_cells', 0.0, 'native SBML value', 'Initial Infected cancer cells. Sets the initial value of bundled SBML symbol `infected_cancer_cells`.'), 'initial_free_virus': ('free_virus', 0.5, 'native SBML value', 'Initial Free virus. Sets the initial value of bundled SBML symbol `free_virus`.')}
    _HEADLINE_OUTPUTS = {'uninfected_cancer_cells': ('uninfected_cancer_cells', 'native SBML value', 'Uninfected cancer cells observable. Maps to SBML symbol `uninfected_cancer_cells`.'), 'infected_cancer_cells': ('infected_cancer_cells', 'native SBML value', 'Infected cancer cells observable. Maps to SBML symbol `infected_cancer_cells`.'), 'free_virus': ('free_virus', 'native SBML value', 'Free virus observable. Maps to SBML symbol `free_virus`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000001031.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
