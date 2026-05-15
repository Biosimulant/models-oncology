# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Orton2009 - Modelling cancerous mutations in the EGFR/ERK pathway - EGF Model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Orton2009ModellingCancerousMutationsInTheEBiomd0000000623Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000623'
    _TITLE = 'Orton2009 - Modelling cancerous mutations in the EGFR/ERK pathway - EGF Model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['species_0', 'species_1', 'species_2', 'species_3', 'species_4', 'species_5', 'species_6', 'species_7', 'species_8', 'species_9', 'species_10', 'species_11', 'species_12', 'species_13', 'species_14', 'species_15', 'species_16', 'species_17', 'species_18', 'species_19', 'species_20', 'species_21', 'species_22', 'species_23', 'species_24']
    _SPECIES_LABELS = {'species_1': 'FreeEGFReceptor', 'species_0': 'BoundEGFReceptor', 'species_18': 'DegradedEGFReceptor', 'species_5': 'RasInactive', 'species_7': 'Raf1Inactive', 'species_11': 'ErkInactive'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_freeegfreceptor': ('species_1', 80000.0, 'native SBML value', 'Initial FreeEGFReceptor. Sets the initial value of bundled SBML symbol `species_1`.'), 'initial_boundegfreceptor': ('species_0', 0.0, 'native SBML value', 'Initial BoundEGFReceptor. Sets the initial value of bundled SBML symbol `species_0`.'), 'initial_degradedegfreceptor': ('species_18', 0.0, 'native SBML value', 'Initial DegradedEGFReceptor. Sets the initial value of bundled SBML symbol `species_18`.'), 'initial_rasinactive': ('species_5', 120000.0, 'native SBML value', 'Initial RasInactive. Sets the initial value of bundled SBML symbol `species_5`.'), 'initial_raf1inactive': ('species_7', 120000.0, 'native SBML value', 'Initial Raf1Inactive. Sets the initial value of bundled SBML symbol `species_7`.'), 'initial_erkinactive': ('species_11', 600000.0, 'native SBML value', 'Initial ErkInactive. Sets the initial value of bundled SBML symbol `species_11`.')}
    _HEADLINE_OUTPUTS = {'freeegfreceptor': ('species_1', 'native SBML value', 'FreeEGFReceptor observable. Maps to SBML symbol `species_1`.'), 'boundegfreceptor': ('species_0', 'native SBML value', 'BoundEGFReceptor observable. Maps to SBML symbol `species_0`.'), 'degradedegfreceptor': ('species_18', 'native SBML value', 'DegradedEGFReceptor observable. Maps to SBML symbol `species_18`.'), 'rasinactive': ('species_5', 'native SBML value', 'RasInactive observable. Maps to SBML symbol `species_5`.'), 'raf1inactive': ('species_7', 'native SBML value', 'Raf1Inactive observable. Maps to SBML symbol `species_7`.'), 'erkinactive': ('species_11', 'native SBML value', 'ErkInactive observable. Maps to SBML symbol `species_11`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000623.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
