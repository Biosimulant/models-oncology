# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Wodarz2001 - Viruses as antitumor weapons."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Wodarz2001VirusesAsAntitumorWeaponsBiomd0000001043Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000001043'
    _TITLE = 'Wodarz2001 - Viruses as antitumor weapons'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['uninfected_tumor_cells', 'infected_tumor_cells', 'virus_specific_CTLs']
    _SPECIES_LABELS = {'uninfected_tumor_cells': 'Uninfected tumor cells', 'infected_tumor_cells': 'Infected tumor cells', 'virus_specific_CTLs': 'Virus specific CTLs'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_uninfected_tumor_cells': ('uninfected_tumor_cells', 0.01, 'native SBML value', 'Initial Uninfected tumor cells. Sets the initial value of bundled SBML symbol `uninfected_tumor_cells`.'), 'initial_infected_tumor_cells': ('infected_tumor_cells', 0.0001, 'native SBML value', 'Initial Infected tumor cells. Sets the initial value of bundled SBML symbol `infected_tumor_cells`.'), 'initial_virus_specific_ctls': ('virus_specific_CTLs', 0.0, 'native SBML value', 'Initial Virus specific CTLs. Sets the initial value of bundled SBML symbol `virus_specific_CTLs`.')}
    _HEADLINE_OUTPUTS = {'uninfected_tumor_cells': ('uninfected_tumor_cells', 'native SBML value', 'Uninfected tumor cells observable. Maps to SBML symbol `uninfected_tumor_cells`.'), 'infected_tumor_cells': ('infected_tumor_cells', 'native SBML value', 'Infected tumor cells observable. Maps to SBML symbol `infected_tumor_cells`.'), 'virus_specific_ctls': ('virus_specific_CTLs', 'native SBML value', 'Virus specific CTLs observable. Maps to SBML symbol `virus_specific_CTLs`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000001043.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
