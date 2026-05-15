# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Fassoni2019 - Oncogenesis encompassing mutations and genetic instability."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Fassoni2019OncogenesisEncompassingMutationsABiomd0000000807Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000807'
    _TITLE = 'Fassoni2019 - Oncogenesis encompassing mutations and genetic instability'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['normalized_normal_cell_n', 'normalized_pre_cancer_cell_g', 'normalized_cancer_cell_a']
    _SPECIES_LABELS = {'normalized_normal_cell_n': 'Normalized normal cell n', 'normalized_pre_cancer_cell_g': 'Normalized pre cancer cell g', 'normalized_cancer_cell_a': 'Normalized cancer cell a'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_normalized_normal_cell_n': ('normalized_normal_cell_n', 0.99999999, 'native SBML value', 'Initial Normalized normal cell n. Sets the initial value of bundled SBML symbol `normalized_normal_cell_n`.'), 'initial_normalized_pre_cancer_cell_g': ('normalized_pre_cancer_cell_g', 1e-08, 'native SBML value', 'Initial Normalized pre cancer cell g. Sets the initial value of bundled SBML symbol `normalized_pre_cancer_cell_g`.'), 'initial_normalized_cancer_cell_a': ('normalized_cancer_cell_a', 0.0, 'native SBML value', 'Initial Normalized cancer cell a. Sets the initial value of bundled SBML symbol `normalized_cancer_cell_a`.')}
    _HEADLINE_OUTPUTS = {'normalized_normal_cell_n': ('normalized_normal_cell_n', 'native SBML value', 'Normalized normal cell n observable. Maps to SBML symbol `normalized_normal_cell_n`.'), 'normalized_pre_cancer_cell_g': ('normalized_pre_cancer_cell_g', 'native SBML value', 'Normalized pre cancer cell g observable. Maps to SBML symbol `normalized_pre_cancer_cell_g`.'), 'normalized_cancer_cell_a': ('normalized_cancer_cell_a', 'native SBML value', 'Normalized cancer cell a observable. Maps to SBML symbol `normalized_cancer_cell_a`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000807.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
