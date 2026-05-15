# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Tham2008 - PDmodel, Tumour shrinkage by gemcitabine and carboplatin."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Tham2008PdmodelTumourShrinkageByGemcitabineBiomd0000000234Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000234'
    _TITLE = 'Tham2008 - PDmodel, Tumour shrinkage by gemcitabine and carboplatin'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rateRule'
    _OBSERVABLES = ['Ce', 'TumorSize']
    _SPECIES_LABELS = {'TumorSize': 'TumorSize', 'Ce': 'Ce'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'dose_int2': ('Dose_Int2', -2.0, 'native SBML value', 'Dose Int2 source parameter. Maps to bundled SBML parameter `Dose_Int2`.'), 'dose_int1': ('Dose_Int1', 0.0, 'native SBML value', 'Dose Int1 source parameter. Maps to bundled SBML parameter `Dose_Int1`.'), 'dose': ('Dose', 5203.84, 'native SBML value', 'Dose source parameter. Maps to bundled SBML parameter `Dose`.'), 'initial_tumorsize': ('TumorSize', 6.66, 'native SBML value', 'Initial TumorSize. Sets the initial value of bundled SBML symbol `TumorSize`.')}
    _HEADLINE_OUTPUTS = {'tumorsize': ('TumorSize', 'native SBML value', 'TumorSize observable. Maps to SBML symbol `TumorSize`.'), 'model_state_2': ('Ce', 'native SBML value', 'Ce observable. Maps to SBML symbol `Ce`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000234.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
