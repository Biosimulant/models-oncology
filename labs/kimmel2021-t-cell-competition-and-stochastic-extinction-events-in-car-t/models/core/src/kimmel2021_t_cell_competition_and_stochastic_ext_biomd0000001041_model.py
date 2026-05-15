# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Kimmel2021 - T cell competition and stochastic extinction events in CAR T cell therapy."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kimmel2021TCellCompetitionAndStochasticExtBiomd0000001041Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000001041'
    _TITLE = 'Kimmel2021 - T cell competition and stochastic extinction events in CAR T cell therapy'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Normal_T_cells', 'CAR_T_cells', 'Antigen_presenting_tumour_cells']
    _SPECIES_LABELS = {'Antigen_presenting_tumour_cells': 'Antigen presenting tumour cells', 'Normal_T_cells': 'Normal T cells', 'CAR_T_cells': 'CAR T cells'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_antigen_presenting_tumour_cells': ('Antigen_presenting_tumour_cells', 94.86, 'native SBML value', 'Initial Antigen presenting tumour cells. Sets the initial value of bundled SBML symbol `Antigen_presenting_tumour_cells`.'), 'initial_normal_t_cells': ('Normal_T_cells', 6.0, 'native SBML value', 'Initial Normal T cells. Sets the initial value of bundled SBML symbol `Normal_T_cells`.'), 'initial_car_t_cells': ('CAR_T_cells', 0.36, 'native SBML value', 'Initial CAR T cells. Sets the initial value of bundled SBML symbol `CAR_T_cells`.')}
    _HEADLINE_OUTPUTS = {'antigen_presenting_tumour_cells': ('Antigen_presenting_tumour_cells', 'native SBML value', 'Antigen presenting tumour cells observable. Maps to SBML symbol `Antigen_presenting_tumour_cells`.'), 'normal_t_cells': ('Normal_T_cells', 'native SBML value', 'Normal T cells observable. Maps to SBML symbol `Normal_T_cells`.'), 'car_t_cells': ('CAR_T_cells', 'native SBML value', 'CAR T cells observable. Maps to SBML symbol `CAR_T_cells`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000001041.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
