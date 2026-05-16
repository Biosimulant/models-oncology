# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Babbs2012 - immunotherapy."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Babbs2012ImmunotherapyBiomd0000000758Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000758'
    _TITLE = 'Babbs2012 - immunotherapy'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T', 'I']
    _SPECIES_LABELS = {'T': 'Tumor Burden', 'I': 'Immune Response'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_tumor_burden': ('T', 1.0, 'native SBML value', 'Initial Tumor Burden. Sets the initial value of bundled SBML symbol `T`.'), 'initial_immune_response': ('I', 0.001, 'native SBML value', 'Initial Immune Response. Sets the initial value of bundled SBML symbol `I`.')}
    _HEADLINE_OUTPUTS = {'tumor_burden': ('T', 'native SBML value', 'Tumor Burden observable. Maps to SBML symbol `T`.'), 'immune_response': ('I', 'native SBML value', 'Immune Response observable. Maps to SBML symbol `I`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000758.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
