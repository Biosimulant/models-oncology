# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Morrison1989 - Folate Cycle."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Morrison1989FolateCycleBiomd0000000018Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000018'
    _TITLE = 'Morrison1989 - Folate Cycle'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['FH2f', 'DHFRf', 'FH4', 'CH2FH4', 'CH3FH4', 'CHOFH4', 'FFH2', 'HCHO', 'FGAR', 'AICAR', 'MTX1', 'MTX2', 'MTX3', 'MTX4', 'MTX5', 'MTX1b', 'MTX2b', 'MTX3b', 'MTX4b', 'MTX5b']
    _SPECIES_LABELS = {'FH2f': 'Dihydrofolate free', 'FH4': 'Tetrahydrofolate', 'FFH2': '10 formyl dihydrofolate', 'DHFRf': 'Dihydrofolate reductase free', 'CH2FH4': '5,10 methylene tetrahydrofolate', 'CH3FH4': '5 methyl tetrahydrofolate'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_dihydrofolate_free': ('FH2f', 0.0012, 'native SBML value', 'Initial Dihydrofolate free. Sets the initial value of bundled SBML symbol `FH2f`.'), 'initial_tetrahydrofolate': ('FH4', 0.46, 'native SBML value', 'Initial Tetrahydrofolate. Sets the initial value of bundled SBML symbol `FH4`.'), 'initial_dihydrofolate_reductase_free': ('DHFRf', 0.64, 'native SBML value', 'Initial Dihydrofolate reductase free. Sets the initial value of bundled SBML symbol `DHFRf`.')}
    _HEADLINE_OUTPUTS = {'dihydrofolate_free': ('FH2f', 'native SBML value', 'Dihydrofolate free observable. Maps to SBML symbol `FH2f`.'), 'tetrahydrofolate': ('FH4', 'native SBML value', 'Tetrahydrofolate observable. Maps to SBML symbol `FH4`.'), 'model_state_3': ('FFH2', 'native SBML value', '10 formyl dihydrofolate observable. Maps to SBML symbol `FFH2`.'), 'dihydrofolate_reductase_free': ('DHFRf', 'native SBML value', 'Dihydrofolate reductase free observable. Maps to SBML symbol `DHFRf`.'), 'model_state_5': ('CH2FH4', 'native SBML value', '5,10 methylene tetrahydrofolate observable. Maps to SBML symbol `CH2FH4`.'), 'model_state_6': ('CH3FH4', 'native SBML value', '5 methyl tetrahydrofolate observable. Maps to SBML symbol `CH3FH4`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000018.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
