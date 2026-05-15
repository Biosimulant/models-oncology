# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Nazari2018 - IL6 mediated stem cell driven tumor growth and targeted treatment."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Nazari2018Il6MediatedStemCellDrivenTumorGBiomd0000000819Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000819'
    _TITLE = 'Nazari2018 - IL6 mediated stem cell driven tumor growth and targeted treatment'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Cancer_Stem_Cell_S', 'IL_6__Cell_bound_IL_6R_complex_on_S', 'Progenitor_tumor_cell_E', 'Differentiated_tumor_cell_D', 'IL_6__Cell_bound_IL_6R_complex_on_E', 'IL_6__Cell_bound_IL_6R_complex_on_D', 'IL_6__L', 'IL_6R_on_S', 'IL_6R_on_E', 'IL_6R_on_D']
    _SPECIES_LABELS = {'Progenitor_tumor_cell_E': 'Progenitor tumor cell E', 'Differentiated_tumor_cell_D': 'Differentiated tumor cell D', 'Cancer_Stem_Cell_S': 'Cancer Stem Cell S', 'IL_6__Cell_bound_IL_6R_complex_on_S': 'IL 6, Cell bound IL 6R complex on S', 'IL_6__Cell_bound_IL_6R_complex_on_E': 'IL 6, Cell bound IL 6R complex on E', 'IL_6__Cell_bound_IL_6R_complex_on_D': 'IL 6, Cell bound IL 6R complex on D'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_progenitor_tumor_cell_e': ('Progenitor_tumor_cell_E', 0.01, 'native SBML value', 'Initial Progenitor tumor cell E. Sets the initial value of bundled SBML symbol `Progenitor_tumor_cell_E`.'), 'initial_differentiated_tumor_cell_d': ('Differentiated_tumor_cell_D', 0.01, 'native SBML value', 'Initial Differentiated tumor cell D. Sets the initial value of bundled SBML symbol `Differentiated_tumor_cell_D`.'), 'initial_cancer_stem_cell_s': ('Cancer_Stem_Cell_S', 1000.0, 'native SBML value', 'Initial Cancer Stem Cell S. Sets the initial value of bundled SBML symbol `Cancer_Stem_Cell_S`.'), 'initial_il_6_cell_bound_il_6r_complex_on_s': ('IL_6__Cell_bound_IL_6R_complex_on_S', 0.0, 'native SBML value', 'Initial IL 6, Cell bound IL 6R complex on S. Sets the initial value of bundled SBML symbol `IL_6__Cell_bound_IL_6R_complex_on_S`.'), 'initial_il_6_cell_bound_il_6r_complex_on_e': ('IL_6__Cell_bound_IL_6R_complex_on_E', 0.0, 'native SBML value', 'Initial IL 6, Cell bound IL 6R complex on E. Sets the initial value of bundled SBML symbol `IL_6__Cell_bound_IL_6R_complex_on_E`.'), 'initial_il_6_cell_bound_il_6r_complex_on_d': ('IL_6__Cell_bound_IL_6R_complex_on_D', 0.0, 'native SBML value', 'Initial IL 6, Cell bound IL 6R complex on D. Sets the initial value of bundled SBML symbol `IL_6__Cell_bound_IL_6R_complex_on_D`.')}
    _HEADLINE_OUTPUTS = {'progenitor_tumor_cell_e': ('Progenitor_tumor_cell_E', 'native SBML value', 'Progenitor tumor cell E observable. Maps to SBML symbol `Progenitor_tumor_cell_E`.'), 'differentiated_tumor_cell_d': ('Differentiated_tumor_cell_D', 'native SBML value', 'Differentiated tumor cell D observable. Maps to SBML symbol `Differentiated_tumor_cell_D`.'), 'cancer_stem_cell_s': ('Cancer_Stem_Cell_S', 'native SBML value', 'Cancer Stem Cell S observable. Maps to SBML symbol `Cancer_Stem_Cell_S`.'), 'il_6_cell_bound_il_6r_complex_on_s': ('IL_6__Cell_bound_IL_6R_complex_on_S', 'native SBML value', 'IL 6, Cell bound IL 6R complex on S observable. Maps to SBML symbol `IL_6__Cell_bound_IL_6R_complex_on_S`.'), 'il_6_cell_bound_il_6r_complex_on_e': ('IL_6__Cell_bound_IL_6R_complex_on_E', 'native SBML value', 'IL 6, Cell bound IL 6R complex on E observable. Maps to SBML symbol `IL_6__Cell_bound_IL_6R_complex_on_E`.'), 'il_6_cell_bound_il_6r_complex_on_d': ('IL_6__Cell_bound_IL_6R_complex_on_D', 'native SBML value', 'IL 6, Cell bound IL 6R complex on D observable. Maps to SBML symbol `IL_6__Cell_bound_IL_6R_complex_on_D`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000819.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
