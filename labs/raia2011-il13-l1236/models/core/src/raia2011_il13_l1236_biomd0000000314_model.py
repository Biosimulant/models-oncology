# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Raia2011 - IL13 L1236."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Raia2011Il13L1236Biomd0000000314Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000314'
    _TITLE = 'Raia2011 - IL13 L1236'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Rec', 'Rec_i', 'IL13_Rec', 'p_IL13_Rec', 'p_IL13_Rec_i', 'JAK2', 'pJAK2', 'SHP1', 'STAT5', 'pSTAT5', 'CD274mRNA']
    _SPECIES_LABELS = {'STAT5': 'STAT5', 'pSTAT5': 'PSTAT5', 'Rec': 'Rec', 'JAK2': 'JAK2', 'SHP1': 'SHP1', 'Rec_i': 'Rec i'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'kon_il13rec_level': ('Kon_IL13Rec', 0.00174087, 'native SBML value', 'Kon IL13Rec source parameter. Maps to bundled SBML parameter `Kon_IL13Rec`.'), 'il13stimulation_level': ('IL13stimulation', 1.0, 'native SBML value', 'IL13stimulation source parameter. Maps to bundled SBML parameter `IL13stimulation`.'), 'initial_stat5': ('STAT5', 209.0, 'native SBML value', 'Initial STAT5. Sets the initial value of bundled SBML symbol `STAT5`.'), 'initial_pstat5': ('pSTAT5', 0.0, 'native SBML value', 'Initial PSTAT5. Sets the initial value of bundled SBML symbol `pSTAT5`.'), 'initial_rec': ('Rec', 1.8, 'native SBML value', 'Initial Rec. Sets the initial value of bundled SBML symbol `Rec`.'), 'initial_jak2': ('JAK2', 24.0, 'native SBML value', 'Initial JAK2. Sets the initial value of bundled SBML symbol `JAK2`.')}
    _HEADLINE_OUTPUTS = {'stat5': ('STAT5', 'native SBML value', 'STAT5 observable. Maps to SBML symbol `STAT5`.'), 'pstat5': ('pSTAT5', 'native SBML value', 'PSTAT5 observable. Maps to SBML symbol `pSTAT5`.'), 'rec': ('Rec', 'native SBML value', 'Rec observable. Maps to SBML symbol `Rec`.'), 'jak2': ('JAK2', 'native SBML value', 'JAK2 observable. Maps to SBML symbol `JAK2`.'), 'shp1': ('SHP1', 'native SBML value', 'SHP1 observable. Maps to SBML symbol `SHP1`.'), 'rec_i': ('Rec_i', 'native SBML value', 'Rec i observable. Maps to SBML symbol `Rec_i`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000314.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
