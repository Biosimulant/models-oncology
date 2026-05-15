# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Kuznetsov1994 - Nonlinear dynamics of immunogenic tumors."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kuznetsov1994NonlinearDynamicsOfImmunogenicBiomd0000000762Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000762'
    _TITLE = 'Kuznetsov1994 - Nonlinear dynamics of immunogenic tumors'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['E', 'T']
    _SPECIES_LABELS = {'T': 'Tumor Cells', 'E': 'Effector Cells'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_tumor_cells': ('T', 5000000.0, 'native SBML value', 'Initial Tumor Cells. Sets the initial value of bundled SBML symbol `T`.'), 'initial_effector_cells': ('E', 320000.0, 'native SBML value', 'Initial Effector Cells. Sets the initial value of bundled SBML symbol `E`.')}
    _HEADLINE_OUTPUTS = {'tumor_cells': ('T', 'native SBML value', 'Tumor Cells observable. Maps to SBML symbol `T`.'), 'effector_cells': ('E', 'native SBML value', 'Effector Cells observable. Maps to SBML symbol `E`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000762.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
