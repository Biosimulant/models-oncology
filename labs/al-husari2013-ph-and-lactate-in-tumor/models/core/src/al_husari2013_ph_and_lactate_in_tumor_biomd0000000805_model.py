# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Al-Husari2013 - pH and lactate in tumor."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class AlHusari2013PhAndLactateInTumorBiomd0000000805Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000805'
    _TITLE = 'Al-Husari2013 - pH and lactate in tumor'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Hi', 'He', 'Li', 'Le']
    _SPECIES_LABELS = {'Hi': 'Intracellular Hydrogen Ion', 'He': 'Extracellular Hydrogen Ion', 'Li': 'Intracellular Lactate', 'Le': 'Extracellular Lactate'}
    _PARAMETER_INPUTS = {'intracellular_ph': ('pHi', 7.3, 'native SBML value', 'Intracellular pH. Overrides bundled SBML parameter `pHi`.'), 'extracellular_ph': ('pHe', 7.0, 'native SBML value', 'Extracellular pH. Overrides bundled SBML parameter `pHe`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'intracellular_hydrogen_ion': ('Hi', 'native SBML value', 'Intracellular Hydrogen Ion observable. Maps to SBML symbol `Hi`.'), 'extracellular_hydrogen_ion': ('He', 'native SBML value', 'Extracellular Hydrogen Ion observable. Maps to SBML symbol `He`.'), 'intracellular_lactate': ('Li', 'native SBML value', 'Intracellular Lactate observable. Maps to SBML symbol `Li`.'), 'extracellular_lactate': ('Le', 'native SBML value', 'Extracellular Lactate observable. Maps to SBML symbol `Le`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000805.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
