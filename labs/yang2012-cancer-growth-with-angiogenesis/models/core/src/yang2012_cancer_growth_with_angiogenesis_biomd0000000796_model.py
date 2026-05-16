# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Yang2012 - cancer growth with angiogenesis."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Yang2012CancerGrowthWithAngiogenesisBiomd0000000796Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000796'
    _TITLE = 'Yang2012 - cancer growth with angiogenesis'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['C', 'E', 'T', 'P', 'A']
    _SPECIES_LABELS = {'C': 'Cancer Cells', 'E': 'Endothelial Cells', 'T': 'T', 'P': 'P', 'A': 'A'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_cancer_cells': ('C', 9.0, 'native SBML value', 'Initial Cancer Cells. Sets the initial value of bundled SBML symbol `C`.'), 'initial_endothelial_cells': ('E', 10.0, 'native SBML value', 'Initial Endothelial Cells. Sets the initial value of bundled SBML symbol `E`.')}
    _HEADLINE_OUTPUTS = {'cancer_cells': ('C', 'native SBML value', 'Cancer Cells observable. Maps to SBML symbol `C`.'), 'endothelial_cells': ('E', 'native SBML value', 'Endothelial Cells observable. Maps to SBML symbol `E`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000796.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
