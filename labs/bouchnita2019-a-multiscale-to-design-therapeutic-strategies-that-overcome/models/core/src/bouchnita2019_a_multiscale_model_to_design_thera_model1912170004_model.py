# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Bouchnita2019 - A multiscale model to design therapeutic strategies that overcome drug resistance to tyrosine kinase inhibitors in multiple myeloma."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bouchnita2019AMultiscaleModelToDesignTheraModel1912170004Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'MODEL1912170004'
    _TITLE = 'Bouchnita2019 - A multiscale model to design therapeutic strategies that overcome drug resistance to tyrosine kinase inhibitors in multiple myeloma'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Ei', 'Ti', 'Ni', 'Di', 'Ai', 'Gf', 'GF', 'Ie', 'I0', 'Ae']
    _SPECIES_LABELS = {'Ei': 'Ei', 'Ti': 'Ti', 'Ni': 'Ni', 'Di': 'Di', 'Ai': 'Ai', 'Gf': 'Gf'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'model_state_1': ('Ei', 'native SBML value', 'Ei observable. Maps to SBML symbol `Ei`.'), 'model_state_2': ('Ti', 'native SBML value', 'Ti observable. Maps to SBML symbol `Ti`.'), 'model_state_3': ('Ni', 'native SBML value', 'Ni observable. Maps to SBML symbol `Ni`.'), 'model_state_4': ('Di', 'native SBML value', 'Di observable. Maps to SBML symbol `Di`.'), 'model_state_5': ('Ai', 'native SBML value', 'Ai observable. Maps to SBML symbol `Ai`.'), 'model_state_6': ('Gf', 'native SBML value', 'Gf observable. Maps to SBML symbol `Gf`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1912170004.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
