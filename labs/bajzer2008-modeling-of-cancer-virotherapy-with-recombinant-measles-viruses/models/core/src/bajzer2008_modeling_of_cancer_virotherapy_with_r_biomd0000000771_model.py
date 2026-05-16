# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Bajzer2008 - Modeling of cancer virotherapy with recombinant measles viruses."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bajzer2008ModelingOfCancerVirotherapyWithRBiomd0000000771Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000771'
    _TITLE = 'Bajzer2008 - Modeling of cancer virotherapy with recombinant measles viruses'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['y_Tumor_Cell', 'v_Virus', 'x_Infected_Cell']
    _SPECIES_LABELS = {'y_Tumor_Cell': 'Y Tumor Cell', 'x_Infected_Cell': 'X Infected Cell', 'v_Virus': 'V Virus'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'epsilon_source_parameter': ('epsilon', 1.648773, 'native SBML value', 'Epsilon source parameter. Maps to bundled SBML parameter `epsilon`.'), 'initial_y_tumor_cell': ('y_Tumor_Cell', 126.237, 'native SBML value', 'Initial Y Tumor Cell. Sets the initial value of bundled SBML symbol `y_Tumor_Cell`.'), 'initial_x_infected_cell': ('x_Infected_Cell', 0.0, 'native SBML value', 'Initial X Infected Cell. Sets the initial value of bundled SBML symbol `x_Infected_Cell`.'), 'initial_v_virus': ('v_Virus', 2.0, 'native SBML value', 'Initial V Virus. Sets the initial value of bundled SBML symbol `v_Virus`.')}
    _HEADLINE_OUTPUTS = {'y_tumor_cell': ('y_Tumor_Cell', 'native SBML value', 'Y Tumor Cell observable. Maps to SBML symbol `y_Tumor_Cell`.'), 'x_infected_cell': ('x_Infected_Cell', 'native SBML value', 'X Infected Cell observable. Maps to SBML symbol `x_Infected_Cell`.'), 'v_virus': ('v_Virus', 'native SBML value', 'V Virus observable. Maps to SBML symbol `v_Virus`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000771.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
