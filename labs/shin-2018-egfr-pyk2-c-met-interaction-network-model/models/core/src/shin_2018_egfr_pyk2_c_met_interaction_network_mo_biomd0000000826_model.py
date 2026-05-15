# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Shin_2018_EGFR-PYK2-c-Met interaction network_model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Shin2018EgfrPyk2CMetInteractionNetworkMoBiomd0000000826Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000826'
    _TITLE = 'Shin_2018_EGFR-PYK2-c-Met interaction network_model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['pEGFR', 'EGFRub', 'PYK2m', 'PYK2', 'pPYK2', 'pSTAT3', 'cMETm', 'cMET', 'pcMET', 'pCbl', 'aPTP', 'pERK', 'STAT3uStattic']
    _SPECIES_LABELS = {'pEGFR': 'PEGFR', 'EGFRub': 'EGFRub', 'pERK': 'PERK', 'pSTAT3': 'PSTAT3', 'STAT3uStattic': 'STAT3uStattic', 'PYK2': 'PYK2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'egfrtot_level': ('EGFRtot', 398.107, 'native SBML value', 'EGFRtot source parameter. Maps to bundled SBML parameter `EGFRtot`.'), 'caegf_level': ('caEGF', 0.0891251, 'native SBML value', 'CaEGF source parameter. Maps to bundled SBML parameter `caEGF`.'), 'egf_level': ('EGF', 10.0, 'native SBML value', 'EGF source parameter. Maps to bundled SBML parameter `EGF`.'), 'initial_pegfr': ('pEGFR', 0.109014, 'native SBML value', 'Initial PEGFR. Sets the initial value of bundled SBML symbol `pEGFR`.'), 'initial_egfrub': ('EGFRub', 6.93991, 'native SBML value', 'Initial EGFRub. Sets the initial value of bundled SBML symbol `EGFRub`.'), 'initial_perk': ('pERK', 0.669043, 'native SBML value', 'Initial PERK. Sets the initial value of bundled SBML symbol `pERK`.')}
    _HEADLINE_OUTPUTS = {'pegfr': ('pEGFR', 'native SBML value', 'PEGFR observable. Maps to SBML symbol `pEGFR`.'), 'egfrub': ('EGFRub', 'native SBML value', 'EGFRub observable. Maps to SBML symbol `EGFRub`.'), 'perk': ('pERK', 'native SBML value', 'PERK observable. Maps to SBML symbol `pERK`.'), 'pstat3': ('pSTAT3', 'native SBML value', 'PSTAT3 observable. Maps to SBML symbol `pSTAT3`.'), 'stat3ustattic': ('STAT3uStattic', 'native SBML value', 'STAT3uStattic observable. Maps to SBML symbol `STAT3uStattic`.'), 'pyk2': ('PYK2', 'native SBML value', 'PYK2 observable. Maps to SBML symbol `PYK2`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000826.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
