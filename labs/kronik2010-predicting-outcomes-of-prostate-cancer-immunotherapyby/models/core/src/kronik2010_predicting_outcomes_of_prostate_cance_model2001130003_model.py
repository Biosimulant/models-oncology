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
    _SPECIES_LABELS = {'V': 'Tumor Volume', 'Dm': 'Dm', 'Dc': 'Dc', 'Dr': 'Dr', 'C': 'C', 'R': 'R'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_tumor_volume': ('V', 1000000.0, 'native SBML value', 'Initial Tumor Volume. Sets the initial value of bundled SBML symbol `V`.')}
    _HEADLINE_OUTPUTS = {'tumor_volume': ('V', 'native SBML value', 'Tumor Volume observable. Maps to SBML symbol `V`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2001130003.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
