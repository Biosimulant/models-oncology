# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Boer1986 - Interactions between Macrophages and T-lymphocytes: Tumor Sneaking Through Intrinsic to Helper T cell Dynamics."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Boer1986InteractionsBetweenMacrophagesAndTModel1912110001Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'MODEL1912110001'
    _TITLE = 'Boer1986 - Interactions between Macrophages and T-lymphocytes: Tumor Sneaking Through Intrinsic to Helper T cell Dynamics'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['CTLP', 'HTLP', 'MPH', 'CTL', 'HTL', 'ANGRY', 'TUMOR', 'DEBRIS']
    _SPECIES_LABELS = {'TUMOR': 'TUMOR', 'CTLP': 'CTLP', 'HTLP': 'HTLP', 'MPH': 'MPH', 'CTL': 'CTL', 'HTL': 'HTL'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'kill_level': ('KILL', 10.0, 'native SBML value', 'KILL source parameter. Maps to bundled SBML parameter `KILL`.'), 'initial_tumor': ('TUMOR', 1000.0, 'native SBML value', 'Initial TUMOR. Sets the initial value of bundled SBML symbol `TUMOR`.'), 'initial_ctlp': ('CTLP', 1.0, 'native SBML value', 'Initial CTLP. Sets the initial value of bundled SBML symbol `CTLP`.'), 'initial_htlp': ('HTLP', 15.0, 'native SBML value', 'Initial HTLP. Sets the initial value of bundled SBML symbol `HTLP`.'), 'initial_mph': ('MPH', 3000000.0, 'native SBML value', 'Initial MPH. Sets the initial value of bundled SBML symbol `MPH`.'), 'initial_ctl': ('CTL', 3909.0, 'native SBML value', 'Initial CTL. Sets the initial value of bundled SBML symbol `CTL`.')}
    _HEADLINE_OUTPUTS = {'tumor': ('TUMOR', 'native SBML value', 'TUMOR observable. Maps to SBML symbol `TUMOR`.'), 'ctlp': ('CTLP', 'native SBML value', 'CTLP observable. Maps to SBML symbol `CTLP`.'), 'htlp': ('HTLP', 'native SBML value', 'HTLP observable. Maps to SBML symbol `HTLP`.'), 'mph': ('MPH', 'native SBML value', 'MPH observable. Maps to SBML symbol `MPH`.'), 'ctl': ('CTL', 'native SBML value', 'CTL observable. Maps to SBML symbol `CTL`.'), 'htl': ('HTL', 'native SBML value', 'HTL observable. Maps to SBML symbol `HTL`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1912110001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
