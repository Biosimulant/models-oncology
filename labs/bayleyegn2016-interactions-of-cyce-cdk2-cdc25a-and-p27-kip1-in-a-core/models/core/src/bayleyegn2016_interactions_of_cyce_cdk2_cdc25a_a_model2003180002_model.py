# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Bayleyegn2016 - interactions of CycE/Cdk2, Cdc25A, and P27 Kip1 in a core cancer subnetwork."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bayleyegn2016InteractionsOfCyceCdk2Cdc25aAModel2003180002Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'MODEL2003180002'
    _TITLE = 'Bayleyegn2016 - interactions of CycE/Cdk2, Cdc25A, and P27 Kip1 in a core cancer subnetwork'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rateRule'
    _OBSERVABLES = ['Cdc25A', 'CycE_CDK2', 'p27_kip1']
    _SPECIES_LABELS = {'CycE_CDK2': 'CycE CDK2', 'p27_kip1': 'P27 kip1', 'Cdc25A': 'Cdc25A'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'cyce_cdk2': ('CycE_CDK2', 'native SBML value', 'CycE CDK2 observable. Maps to SBML symbol `CycE_CDK2`.'), 'p27_kip1': ('p27_kip1', 'native SBML value', 'P27 kip1 observable. Maps to SBML symbol `p27_kip1`.'), 'cdc25a': ('Cdc25A', 'native SBML value', 'Cdc25A observable. Maps to SBML symbol `Cdc25A`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2003180002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
