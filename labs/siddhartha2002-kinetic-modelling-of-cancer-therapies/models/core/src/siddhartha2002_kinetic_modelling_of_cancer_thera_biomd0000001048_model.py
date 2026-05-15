# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Siddhartha2002 - Kinetic modelling of cancer therapies."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Siddhartha2002KineticModellingOfCancerTheraBiomd0000001048Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000001048'
    _TITLE = 'Siddhartha2002 - Kinetic modelling of cancer therapies'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Ttum', 'Tplas', 'Tnew']
    _SPECIES_LABELS = {'Ttum': 'Ttum', 'Tplas': 'Tplas', 'Tnew': 'Tnew'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_ttum': ('Ttum', 1000000.0, 'native SBML value', 'Initial Ttum. Sets the initial value of bundled SBML symbol `Ttum`.'), 'initial_tplas': ('Tplas', 4000000.0, 'native SBML value', 'Initial Tplas. Sets the initial value of bundled SBML symbol `Tplas`.'), 'initial_tnew': ('Tnew', 0.0, 'native SBML value', 'Initial Tnew. Sets the initial value of bundled SBML symbol `Tnew`.')}
    _HEADLINE_OUTPUTS = {'ttum': ('Ttum', 'native SBML value', 'Ttum observable. Maps to SBML symbol `Ttum`.'), 'tplas': ('Tplas', 'native SBML value', 'Tplas observable. Maps to SBML symbol `Tplas`.'), 'tnew': ('Tnew', 'native SBML value', 'Tnew observable. Maps to SBML symbol `Tnew`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000001048.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
