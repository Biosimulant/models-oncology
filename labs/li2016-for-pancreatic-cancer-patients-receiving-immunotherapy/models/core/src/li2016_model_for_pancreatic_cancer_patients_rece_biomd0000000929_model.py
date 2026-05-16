# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Li2016 - Model for pancreatic cancer patients receiving immunotherapy."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Li2016ModelForPancreaticCancerPatientsReceBiomd0000000929Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000929'
    _TITLE = 'Li2016 - Model for pancreatic cancer patients receiving immunotherapy'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Pancreatic_cancer_cells__C', 'Pancreatic_stellate_cells__P', 'CD8__T_cells__T', 'NK_cells__N', 'helper_T_cells__H']
    _SPECIES_LABELS = {'Pancreatic_cancer_cells__C': 'Pancreatic cancer cells (C)', 'Pancreatic_stellate_cells__P': 'Pancreatic stellate cells (P)', 'CD8__T_cells__T': 'CD8+ T cells (T)', 'NK_cells__N': 'NK cells (N)', 'helper_T_cells__H': 'Helper T cells (H)'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_pancreatic_cancer_cells_c': ('Pancreatic_cancer_cells__C', 1000000000.0, 'native SBML value', 'Initial Pancreatic cancer cells (C). Sets the initial value of bundled SBML symbol `Pancreatic_cancer_cells__C`.'), 'initial_pancreatic_stellate_cells_p': ('Pancreatic_stellate_cells__P', 5600000.0, 'native SBML value', 'Initial Pancreatic stellate cells (P). Sets the initial value of bundled SBML symbol `Pancreatic_stellate_cells__P`.'), 'initial_cd8_t_cells_t': ('CD8__T_cells__T', 700000000.0, 'native SBML value', 'Initial CD8+ T cells (T). Sets the initial value of bundled SBML symbol `CD8__T_cells__T`.'), 'initial_nk_cells_n': ('NK_cells__N', 352800000.0, 'native SBML value', 'Initial NK cells (N). Sets the initial value of bundled SBML symbol `NK_cells__N`.'), 'initial_helper_t_cells_h': ('helper_T_cells__H', 1881600000.0, 'native SBML value', 'Initial Helper T cells (H). Sets the initial value of bundled SBML symbol `helper_T_cells__H`.')}
    _HEADLINE_OUTPUTS = {'pancreatic_cancer_cells_c': ('Pancreatic_cancer_cells__C', 'native SBML value', 'Pancreatic cancer cells (C) observable. Maps to SBML symbol `Pancreatic_cancer_cells__C`.'), 'pancreatic_stellate_cells_p': ('Pancreatic_stellate_cells__P', 'native SBML value', 'Pancreatic stellate cells (P) observable. Maps to SBML symbol `Pancreatic_stellate_cells__P`.'), 'cd8_t_cells_t': ('CD8__T_cells__T', 'native SBML value', 'CD8+ T cells (T) observable. Maps to SBML symbol `CD8__T_cells__T`.'), 'nk_cells_n': ('NK_cells__N', 'native SBML value', 'NK cells (N) observable. Maps to SBML symbol `NK_cells__N`.'), 'helper_t_cells_h': ('helper_T_cells__H', 'native SBML value', 'Helper T cells (H) observable. Maps to SBML symbol `helper_T_cells__H`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000929.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
