# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Talemi2015 - Persistent telomere-associated DNA damage foci (TAF), a measure to predict cancer risks."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Talemi2015PersistentTelomereAssociatedDnaDaModel1412200000Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'MODEL1412200000'
    _TITLE = 'Talemi2015 - Persistent telomere-associated DNA damage foci (TAF), a measure to predict cancer risks'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['FAST', 'FASTi', 'SLOWi', 'SLOW', 'RP']
    _SPECIES_LABELS = {'RP': 'RP', 'FAST': 'FAST', 'SLOW': 'SLOW', 'FASTi': 'FASTi', 'SLOWi': 'SLOWi'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'dnadamagefoci_0_source_parameter': ('DNAdamagefoci_0', 750.500039901129, 'native SBML value', 'DNAdamagefoci 0 source parameter. Maps to bundled SBML parameter `DNAdamagefoci_0`.'), 'base_dnadamage_source_parameter': ('BaseDNAdamage', 0.989191113985894, 'native SBML value', 'BaseDNAdamage source parameter. Maps to bundled SBML parameter `BaseDNAdamage`.'), 'initial_fast': ('FAST', 0.0, 'native SBML value', 'Initial FAST. Sets the initial value of bundled SBML symbol `FAST`.'), 'initial_slow': ('SLOW', 0.0, 'native SBML value', 'Initial SLOW. Sets the initial value of bundled SBML symbol `SLOW`.'), 'initial_fasti': ('FASTi', 0.0, 'native SBML value', 'Initial FASTi. Sets the initial value of bundled SBML symbol `FASTi`.'), 'initial_slowi': ('SLOWi', 0.0, 'native SBML value', 'Initial SLOWi. Sets the initial value of bundled SBML symbol `SLOWi`.')}
    _HEADLINE_OUTPUTS = {'rp': ('RP', 'native SBML value', 'RP observable. Maps to SBML symbol `RP`.'), 'fast': ('FAST', 'native SBML value', 'FAST observable. Maps to SBML symbol `FAST`.'), 'slow': ('SLOW', 'native SBML value', 'SLOW observable. Maps to SBML symbol `SLOW`.'), 'fasti': ('FASTi', 'native SBML value', 'FASTi observable. Maps to SBML symbol `FASTi`.'), 'slowi': ('SLOWi', 'native SBML value', 'SLOWi observable. Maps to SBML symbol `SLOWi`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1412200000.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
