# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Yazdjer2019 - reinforcement learning-based control of tumor growth under anti-angiogenic therapy."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Yazdjer2019ReinforcementLearningBasedControlBiomd0000000821Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000821'
    _TITLE = 'Yazdjer2019 - reinforcement learning-based control of tumor growth under anti-angiogenic therapy'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['tumor_volume_x_1', 'endothelial_volume_x_2', 'concentration_of_administrated_inhibitor_x_3']
    _SPECIES_LABELS = {'tumor_volume_x_1': 'Tumor volume x 1', 'endothelial_volume_x_2': 'Endothelial volume x 2', 'concentration_of_administrated_inhibitor_x_3': 'Concentration of administrated inhibitor x 3'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_tumor_volume_x_1': ('tumor_volume_x_1', 1.0, 'native SBML value', 'Initial Tumor volume x 1. Sets the initial value of bundled SBML symbol `tumor_volume_x_1`.'), 'initial_endothelial_volume_x_2': ('endothelial_volume_x_2', 1.0, 'native SBML value', 'Initial Endothelial volume x 2. Sets the initial value of bundled SBML symbol `endothelial_volume_x_2`.'), 'initial_concentration_of_administrated_inhibitor_x_3': ('concentration_of_administrated_inhibitor_x_3', 0.0, 'native SBML value', 'Initial Concentration of administrated inhibitor x 3. Sets the initial value of bundled SBML symbol `concentration_of_administrated_inhibitor_x_3`.')}
    _HEADLINE_OUTPUTS = {'tumor_volume_x_1': ('tumor_volume_x_1', 'native SBML value', 'Tumor volume x 1 observable. Maps to SBML symbol `tumor_volume_x_1`.'), 'endothelial_volume_x_2': ('endothelial_volume_x_2', 'native SBML value', 'Endothelial volume x 2 observable. Maps to SBML symbol `endothelial_volume_x_2`.'), 'concentration_of_administrated_inhibitor_x_3': ('concentration_of_administrated_inhibitor_x_3', 'native SBML value', 'Concentration of administrated inhibitor x 3 observable. Maps to SBML symbol `concentration_of_administrated_inhibitor_x_3`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000821.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
