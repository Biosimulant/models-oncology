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
    _SPECIES_LABELS = {'H': 'Healthy Bone Marrow', 'T': 'Tumor Burden'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_healthy_bone_marrow': ('H', 0.6, 'native SBML value', 'Initial Healthy Bone Marrow. Sets the initial value of bundled SBML symbol `H`.'), 'initial_tumor_burden': ('T', 0.0001, 'native SBML value', 'Initial Tumor Burden. Sets the initial value of bundled SBML symbol `T`.')}
    _HEADLINE_OUTPUTS = {'healthy_bone_marrow': ('H', 'native SBML value', 'Healthy Bone Marrow observable. Maps to SBML symbol `H`.'), 'tumor_burden': ('T', 'native SBML value', 'Tumor Burden observable. Maps to SBML symbol `T`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000793.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
