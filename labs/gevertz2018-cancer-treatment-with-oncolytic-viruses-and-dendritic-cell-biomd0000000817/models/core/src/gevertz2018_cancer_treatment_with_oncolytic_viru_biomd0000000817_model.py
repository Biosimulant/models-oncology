# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Gevertz2018 - cancer treatment with oncolytic viruses and dendritic cell injections minimal model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Gevertz2018CancerTreatmentWithOncolyticViruBiomd0000000817Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000817'
    _TITLE = 'Gevertz2018 - cancer treatment with oncolytic viruses and dendritic cell injections minimal model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Uninfected_Tumor_Cell_U', 'Infected_Cancer_Cell_I', 'Oncolytic_Adenovirus_V', 'Tumor_targeting_T_cells_T', 'Naive_T_cells_A', 'Dendritic_Cells_D']
    _SPECIES_LABELS = {'Uninfected_Tumor_Cell_U': 'Uninfected Tumor Cell U', 'Tumor_targeting_T_cells_T': 'Tumor targeting T cells T', 'Infected_Cancer_Cell_I': 'Infected Cancer Cell I', 'Naive_T_cells_A': 'Naive T cells A', 'Dendritic_Cells_D': 'Dendritic Cells D', 'Oncolytic_Adenovirus_V': 'Oncolytic Adenovirus V'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'c_kill_source_parameter': ('c_kill', 0.623397, 'native SBML value', 'C kill source parameter. Maps to bundled SBML parameter `c_kill`.'), 'ov_dose_source_parameter': ('OV_dose', 2.5, 'native SBML value', 'OV dose source parameter. Maps to bundled SBML parameter `OV_dose`.'), 'initial_uninfected_tumor_cell_u': ('Uninfected_Tumor_Cell_U', 57.414042, 'native SBML value', 'Initial Uninfected Tumor Cell U. Sets the initial value of bundled SBML symbol `Uninfected_Tumor_Cell_U`.'), 'initial_tumor_targeting_t_cells_t': ('Tumor_targeting_T_cells_T', 0.0, 'native SBML value', 'Initial Tumor targeting T cells T. Sets the initial value of bundled SBML symbol `Tumor_targeting_T_cells_T`.'), 'initial_infected_cancer_cell_i': ('Infected_Cancer_Cell_I', 0.0, 'native SBML value', 'Initial Infected Cancer Cell I. Sets the initial value of bundled SBML symbol `Infected_Cancer_Cell_I`.'), 'initial_naive_t_cells_a': ('Naive_T_cells_A', 0.0, 'native SBML value', 'Initial Naive T cells A. Sets the initial value of bundled SBML symbol `Naive_T_cells_A`.')}
    _HEADLINE_OUTPUTS = {'uninfected_tumor_cell_u': ('Uninfected_Tumor_Cell_U', 'native SBML value', 'Uninfected Tumor Cell U observable. Maps to SBML symbol `Uninfected_Tumor_Cell_U`.'), 'tumor_targeting_t_cells_t': ('Tumor_targeting_T_cells_T', 'native SBML value', 'Tumor targeting T cells T observable. Maps to SBML symbol `Tumor_targeting_T_cells_T`.'), 'infected_cancer_cell_i': ('Infected_Cancer_Cell_I', 'native SBML value', 'Infected Cancer Cell I observable. Maps to SBML symbol `Infected_Cancer_Cell_I`.'), 'naive_t_cells_a': ('Naive_T_cells_A', 'native SBML value', 'Naive T cells A observable. Maps to SBML symbol `Naive_T_cells_A`.'), 'dendritic_cells_d': ('Dendritic_Cells_D', 'native SBML value', 'Dendritic Cells D observable. Maps to SBML symbol `Dendritic_Cells_D`.'), 'oncolytic_adenovirus_v': ('Oncolytic_Adenovirus_V', 'native SBML value', 'Oncolytic Adenovirus V observable. Maps to SBML symbol `Oncolytic_Adenovirus_V`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000817.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
