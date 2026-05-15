# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Shariatpanahi2018 - Mathematical modeling of tumor-induced immunosuppression by myeloid-derived suppressor cells."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Shariatpanahi2018MathematicalModelingOfTumorModel1909090003Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'MODEL1909090003'
    _TITLE = 'Shariatpanahi2018 - Mathematical modeling of tumor-induced immunosuppression by myeloid-derived suppressor cells'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['C', 'N', 'T', 'M']
    _SPECIES_LABELS = {'C': 'C', 'N': 'N', 'T': 'T', 'M': 'M'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'model_state_1': ('C', 'native SBML value', 'C observable. Maps to SBML symbol `C`.'), 'model_state_2': ('N', 'native SBML value', 'N observable. Maps to SBML symbol `N`.'), 'model_state_3': ('T', 'native SBML value', 'T observable. Maps to SBML symbol `T`.'), 'model_state_4': ('M', 'native SBML value', 'M observable. Maps to SBML symbol `M`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1909090003.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
