# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Sun2018 - Instantaneous mutation rate in cancer initiation and progression."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Sun2018InstantaneousMutationRateInCancerInBiomd0000000915Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000915'
    _TITLE = 'Sun2018 - Instantaneous mutation rate in cancer initiation and progression'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['p_0', 'p_1', 'p_2', 'p_3', 'p_4', 'p_5', 'p_6', 'p_7', 'p_8']
    _SPECIES_LABELS = {'p_0': 'Patient 0', 'p_1': 'Patient 1', 'p_2': 'Patient 2', 'p_3': 'Patient 3', 'p_4': 'Patient 4', 'p_5': 'Patient 5'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_patient_0': ('p_0', 1.0, 'native SBML value', 'Initial Patient 0. Sets the initial value of bundled SBML symbol `p_0`.'), 'initial_patient_1': ('p_1', 0.0, 'native SBML value', 'Initial Patient 1. Sets the initial value of bundled SBML symbol `p_1`.'), 'initial_patient_2': ('p_2', 0.0, 'native SBML value', 'Initial Patient 2. Sets the initial value of bundled SBML symbol `p_2`.'), 'initial_patient_3': ('p_3', 0.0, 'native SBML value', 'Initial Patient 3. Sets the initial value of bundled SBML symbol `p_3`.'), 'initial_patient_4': ('p_4', 0.0, 'native SBML value', 'Initial Patient 4. Sets the initial value of bundled SBML symbol `p_4`.'), 'initial_patient_5': ('p_5', 0.0, 'native SBML value', 'Initial Patient 5. Sets the initial value of bundled SBML symbol `p_5`.')}
    _HEADLINE_OUTPUTS = {'patient_0': ('p_0', 'native SBML value', 'Patient 0 observable. Maps to SBML symbol `p_0`.'), 'patient_1': ('p_1', 'native SBML value', 'Patient 1 observable. Maps to SBML symbol `p_1`.'), 'patient_2': ('p_2', 'native SBML value', 'Patient 2 observable. Maps to SBML symbol `p_2`.'), 'patient_3': ('p_3', 'native SBML value', 'Patient 3 observable. Maps to SBML symbol `p_3`.'), 'patient_4': ('p_4', 'native SBML value', 'Patient 4 observable. Maps to SBML symbol `p_4`.'), 'patient_5': ('p_5', 'native SBML value', 'Patient 5 observable. Maps to SBML symbol `p_5`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000915.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
