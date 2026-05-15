# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Bianconi2012 - EGFR and IGF1R pathway in lung cancer."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bianconi2012EgfrAndIgf1rPathwayInLungCancBiomd0000000427Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000427'
    _TITLE = 'Bianconi2012 - EGFR and IGF1R pathway in lung cancer'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['EGFR_active', 'D_SOS', 'A_SOS', 'Raf', 'Ras_active', 'Mek_active', 'ERK', 'ERK_active', 'IGFR_active', 'PI3KCA', 'PI3KCA_active', 'AKT_active', 'AKT', 'PP2A', 'Ras', 'Raf_active', 'Mek', 'RasGapActive', 'RafPP', 'P90RskInactive', 'P90Rsk_Active']
    _SPECIES_LABELS = {'EGFR_active': 'EGFR active', 'Raf': 'Raf', 'ERK': 'ERK', 'AKT': 'AKT', 'Ras': 'Ras', 'PI3KCA': 'PI3KCA'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'gamma_egfr_level': ('gamma_EGFR', 0.02, 'native SBML value', 'Gamma EGFR source parameter. Maps to bundled SBML parameter `gamma_EGFR`.'), 'initial_egfr_active': ('EGFR_active', 8000.0, 'native SBML value', 'Initial EGFR active. Sets the initial value of bundled SBML symbol `EGFR_active`.'), 'initial_raf': ('Raf', 120000.0, 'native SBML value', 'Initial Raf. Sets the initial value of bundled SBML symbol `Raf`.'), 'initial_erk': ('ERK', 600000.0, 'native SBML value', 'Initial ERK. Sets the initial value of bundled SBML symbol `ERK`.'), 'initial_akt': ('AKT', 600000.0, 'native SBML value', 'Initial AKT. Sets the initial value of bundled SBML symbol `AKT`.'), 'initial_ras': ('Ras', 120000.0, 'native SBML value', 'Initial Ras. Sets the initial value of bundled SBML symbol `Ras`.')}
    _HEADLINE_OUTPUTS = {'egfr_active': ('EGFR_active', 'native SBML value', 'EGFR active observable. Maps to SBML symbol `EGFR_active`.'), 'raf': ('Raf', 'native SBML value', 'Raf observable. Maps to SBML symbol `Raf`.'), 'erk': ('ERK', 'native SBML value', 'ERK observable. Maps to SBML symbol `ERK`.'), 'akt': ('AKT', 'native SBML value', 'AKT observable. Maps to SBML symbol `AKT`.'), 'ras': ('Ras', 'native SBML value', 'Ras observable. Maps to SBML symbol `Ras`.'), 'pi3kca': ('PI3KCA', 'native SBML value', 'PI3KCA observable. Maps to SBML symbol `PI3KCA`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000427.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
