# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Kronik2010 - Predicting Outcomes of Prostate Cancer Immunotherapyby Personalized Mathematical Models."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kronik2010PredictingOutcomesOfProstateCanceModel2001130003Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'MODEL2001130003'
    _TITLE = 'Kronik2010 - Predicting Outcomes of Prostate Cancer Immunotherapyby Personalized Mathematical Models'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['V', 'Dm', 'Dc', 'Dr', 'C', 'R', 'P']
    _SPECIES_LABELS = {'V': 'V', 'Dm': 'Dm', 'Dc': 'Dc', 'Dr': 'Dr', 'C': 'C', 'R': 'R'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'model_state_1': ('V', 'native SBML value', 'V observable. Maps to SBML symbol `V`.'), 'model_state_2': ('Dm', 'native SBML value', 'Dm observable. Maps to SBML symbol `Dm`.'), 'model_state_3': ('Dc', 'native SBML value', 'Dc observable. Maps to SBML symbol `Dc`.'), 'model_state_4': ('Dr', 'native SBML value', 'Dr observable. Maps to SBML symbol `Dr`.'), 'model_state_5': ('C', 'native SBML value', 'C observable. Maps to SBML symbol `C`.'), 'model_state_6': ('R', 'native SBML value', 'R observable. Maps to SBML symbol `R`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2001130003.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
