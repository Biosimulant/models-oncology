# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Chaudhury2020 - First order expansion model of CAR-T cell and tumour kinetics."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Chaudhury2020FirstOrderExpansionModelOfCarModel2109110005Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'MODEL2109110005'
    _TITLE = 'Chaudhury2020 - First order expansion model of CAR-T cell and tumour kinetics'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['U']
    _SPECIES_LABELS = {'U': 'Tumor Burden'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_car_t_cells': ('CAR_T_cells', 10.0, 'native SBML value', 'Initial CAR-T Cells. Sets the initial value of bundled SBML symbol `CAR_T_cells`.'), 'initial_tumor_burden': ('U', 900.000000000001, 'native SBML value', 'Initial Tumor Burden. Sets the initial value of bundled SBML symbol `U`.')}
    _HEADLINE_OUTPUTS = {'car_t_cells': ('CAR_T_cells', 'native SBML value', 'CAR-T Cells observable. Maps to SBML symbol `CAR_T_cells`.'), 'tumor_burden': ('U', 'native SBML value', 'Tumor Burden observable. Maps to SBML symbol `U`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2109110005.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
