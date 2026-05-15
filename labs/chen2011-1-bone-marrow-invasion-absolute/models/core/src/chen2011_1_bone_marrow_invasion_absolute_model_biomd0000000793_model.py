# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Chen2011/1 - bone marrow invasion absolute model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Chen20111BoneMarrowInvasionAbsoluteModelBiomd0000000793Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000793'
    _TITLE = 'Chen2011/1 - bone marrow invasion absolute model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['H', 'T']
    _SPECIES_LABELS = {'H': 'H', 'T': 'T'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'model_state_1': ('H', 'native SBML value', 'H observable. Maps to SBML symbol `H`.'), 'model_state_2': ('T', 'native SBML value', 'T observable. Maps to SBML symbol `T`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000793.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
