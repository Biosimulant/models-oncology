# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Park2019 - Cetuximab resistance in colorectal cancer."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Park2019CetuximabResistanceInColorectalCancModel1909300004Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'MODEL1909300004'
    _TITLE = 'Park2019 - Cetuximab resistance in colorectal cancer'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Cetuximab', 'EGF', 'EGFRa', 'EGFRi', 'GNB5', 'KRASa', 'KRASi', 'MEKa', 'MEKi', 'ERKa', 'ERKi', 'PI3Ka', 'PI3Ki', 'AKTa', 'AKTi']
    _SPECIES_LABELS = {'EGF': 'EGF', 'GNB5': 'GNB5', 'MEKi': 'MEKi', 'ERKi': 'ERKi', 'AKTi': 'AKTi', 'EGFRi': 'EGFRi'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_egf': ('EGF', 1.0, 'native SBML value', 'Initial EGF. Sets the initial value of bundled SBML symbol `EGF`.'), 'initial_gnb5': ('GNB5', 0.5, 'native SBML value', 'Initial GNB5. Sets the initial value of bundled SBML symbol `GNB5`.'), 'initial_meki': ('MEKi', 1.0, 'native SBML value', 'Initial MEKi. Sets the initial value of bundled SBML symbol `MEKi`.'), 'initial_erki': ('ERKi', 1.0, 'native SBML value', 'Initial ERKi. Sets the initial value of bundled SBML symbol `ERKi`.'), 'initial_akti': ('AKTi', 1.0, 'native SBML value', 'Initial AKTi. Sets the initial value of bundled SBML symbol `AKTi`.'), 'initial_egfri': ('EGFRi', 1.0, 'native SBML value', 'Initial EGFRi. Sets the initial value of bundled SBML symbol `EGFRi`.')}
    _HEADLINE_OUTPUTS = {'egf': ('EGF', 'native SBML value', 'EGF observable. Maps to SBML symbol `EGF`.'), 'gnb5': ('GNB5', 'native SBML value', 'GNB5 observable. Maps to SBML symbol `GNB5`.'), 'meki': ('MEKi', 'native SBML value', 'MEKi observable. Maps to SBML symbol `MEKi`.'), 'erki': ('ERKi', 'native SBML value', 'ERKi observable. Maps to SBML symbol `ERKi`.'), 'akti': ('AKTi', 'native SBML value', 'AKTi observable. Maps to SBML symbol `AKTi`.'), 'egfri': ('EGFRi', 'native SBML value', 'EGFRi observable. Maps to SBML symbol `EGFRi`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1909300004.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
