# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Alharbi2019 - Tumor-normal model (TNM) of the development of tumor cells and their impact on normal cell dynamics."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Alharbi2019TumorNormalModelTnmOfTheDeveloBiomd0000001037Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000001037'
    _TITLE = 'Alharbi2019 - Tumor-normal model (TNM) of the development of tumor cells and their impact on normal cell dynamics'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Normal_cells', 'Tumor_cells']
    _SPECIES_LABELS = {'Tumor_cells': 'Tumor cells', 'Normal_cells': 'Normal cells'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_tumor_cells': ('Tumor_cells', 1.0, 'native SBML value', 'Initial Tumor cells. Sets the initial value of bundled SBML symbol `Tumor_cells`.'), 'initial_normal_cells': ('Normal_cells', 1.0, 'native SBML value', 'Initial Normal cells. Sets the initial value of bundled SBML symbol `Normal_cells`.')}
    _HEADLINE_OUTPUTS = {'tumor_cells': ('Tumor_cells', 'native SBML value', 'Tumor cells observable. Maps to SBML symbol `Tumor_cells`.'), 'normal_cells': ('Normal_cells', 'native SBML value', 'Normal cells observable. Maps to SBML symbol `Normal_cells`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000001037.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
