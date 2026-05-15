# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Lolas2016 - tumour-induced neoneurogenesis and perineural tumour growth."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Lolas2016TumourInducedNeoneurogenesisAndPerBiomd0000000750Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000750'
    _TITLE = 'Lolas2016 - tumour-induced neoneurogenesis and perineural tumour growth'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Tp', 'Tm', 'G', 'A', 'S', 'P', 'Nn', 'Na']
    _SPECIES_LABELS = {'Tp': 'Tp', 'S': 'S', 'P': 'P', 'Nn': 'Nn', 'Na': 'Na', 'Tm': 'Tm'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'model_state_1': ('Tp', 'native SBML value', 'Tp observable. Maps to SBML symbol `Tp`.'), 'model_state_2': ('S', 'native SBML value', 'S observable. Maps to SBML symbol `S`.'), 'model_state_3': ('P', 'native SBML value', 'P observable. Maps to SBML symbol `P`.'), 'model_state_4': ('Nn', 'native SBML value', 'Nn observable. Maps to SBML symbol `Nn`.'), 'model_state_5': ('Na', 'native SBML value', 'Na observable. Maps to SBML symbol `Na`.'), 'model_state_6': ('Tm', 'native SBML value', 'Tm observable. Maps to SBML symbol `Tm`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000750.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
