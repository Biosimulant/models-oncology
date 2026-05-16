# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Pappalardo2016 - PI3K/AKT and MAPK Signaling Pathways in Melanoma Cancer."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Pappalardo2016Pi3kAktAndMapkSignalingPathwBiomd0000000666Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000666'
    _TITLE = 'Pappalardo2016 - PI3K/AKT and MAPK Signaling Pathways in Melanoma Cancer'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['species_0', 'species_1', 'species_2', 'species_3', 'species_4', 'species_5', 'species_6', 'species_7', 'species_8', 'species_9', 'species_10', 'species_11', 'species_12', 'species_13', 'species_14', 'species_15', 'species_16', 'species_17', 'species_19', 'species_20', 'species_21', 'species_22', 'PIP3Active', 'PIP3Inactive', 'IRS1Active', 'IRS1Inactive', 'PDK1Inactive', 'PDK1Active', 'mTORC1Active', 'mTORC1Inactive', 'S6K1Active', 'S6K1Inactive', 'bRafMutated', 'Dabrafenib', 'bRafMutatedInactive']
    _SPECIES_LABELS = {'species_5': 'RasInactive', 'species_7': 'Raf1Inactive', 'species_11': 'ErkInactive', 'species_15': 'PI3KInactive', 'species_17': 'AktInactive', 'bRafMutated': 'BRafMutated'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_ras_inactive': ('species_5', 120000.0, 'native SBML value', 'Initial RasInactive. Sets the initial value of bundled SBML symbol `species_5`.'), 'initial_raf1_inactive': ('species_7', 120000.0, 'native SBML value', 'Initial Raf1Inactive. Sets the initial value of bundled SBML symbol `species_7`.'), 'initial_erk_inactive': ('species_11', 600000.0, 'native SBML value', 'Initial ErkInactive. Sets the initial value of bundled SBML symbol `species_11`.'), 'initial_pi3_kinactive': ('species_15', 120000.0, 'native SBML value', 'Initial PI3KInactive. Sets the initial value of bundled SBML symbol `species_15`.'), 'initial_akt_inactive': ('species_17', 120000.0, 'native SBML value', 'Initial AktInactive. Sets the initial value of bundled SBML symbol `species_17`.'), 'initial_braf_mutated': ('bRafMutated', 120000.0, 'native SBML value', 'Initial BRafMutated. Sets the initial value of bundled SBML symbol `bRafMutated`.')}
    _HEADLINE_OUTPUTS = {'ras_inactive': ('species_5', 'native SBML value', 'RasInactive observable. Maps to SBML symbol `species_5`.'), 'raf1_inactive': ('species_7', 'native SBML value', 'Raf1Inactive observable. Maps to SBML symbol `species_7`.'), 'erk_inactive': ('species_11', 'native SBML value', 'ErkInactive observable. Maps to SBML symbol `species_11`.'), 'pi3_kinactive': ('species_15', 'native SBML value', 'PI3KInactive observable. Maps to SBML symbol `species_15`.'), 'akt_inactive': ('species_17', 'native SBML value', 'AktInactive observable. Maps to SBML symbol `species_17`.'), 'braf_mutated': ('bRafMutated', 'native SBML value', 'BRafMutated observable. Maps to SBML symbol `bRafMutated`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000666.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
