# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Hayashi2013 - Extended TNF-induced Signaling with Gene Expression Dynamics (Model B)."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Hayashi2013ExtendedTnfInducedSignalingWithModel2502170002Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'MODEL2502170002'
    _TITLE = 'Hayashi2013 - Extended TNF-induced Signaling with Gene Expression Dynamics (Model B)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['species_1', 'species_2', 'species_3', 'species_4', 'species_5', 'species_6', 'species_7', 'species_8', 'species_9', 'species_10', 'species_11', 'species_12', 'species_15', 'species_18', 'species_19', 'species_20', 'species_21', 'species_24', 'species_13', 'species_14', 'species_16', 'species_17', 'species_22', 'species_23', 'species_52', 'species_53']
    _SPECIES_LABELS = {'species_3': 'TNFR1', 'species_1': 'IkBa NFkb', 'species_13': 'MAPK', 'species_2': 'NFkBc', 'species_6': 'TRAF6', 'species_7': 'TRAF5'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_tnfr1': ('species_3', 1.0, 'native SBML value', 'Initial TNFR1. Sets the initial value of bundled SBML symbol `species_3`.'), 'initial_ikba_nfkb': ('species_1', 5.0, 'native SBML value', 'Initial IkBa NFkb. Sets the initial value of bundled SBML symbol `species_1`.'), 'initial_mapk': ('species_13', 46.0, 'native SBML value', 'Initial MAPK. Sets the initial value of bundled SBML symbol `species_13`.'), 'initial_nfkbc': ('species_2', 0.0, 'native SBML value', 'Initial NFkBc. Sets the initial value of bundled SBML symbol `species_2`.'), 'initial_traf6': ('species_6', 0.0, 'native SBML value', 'Initial TRAF6. Sets the initial value of bundled SBML symbol `species_6`.'), 'initial_traf5': ('species_7', 0.0, 'native SBML value', 'Initial TRAF5. Sets the initial value of bundled SBML symbol `species_7`.')}
    _HEADLINE_OUTPUTS = {'tnfr1': ('species_3', 'native SBML value', 'TNFR1 observable. Maps to SBML symbol `species_3`.'), 'ikba_nfkb': ('species_1', 'native SBML value', 'IkBa NFkb observable. Maps to SBML symbol `species_1`.'), 'mapk': ('species_13', 'native SBML value', 'MAPK observable. Maps to SBML symbol `species_13`.'), 'nfkbc': ('species_2', 'native SBML value', 'NFkBc observable. Maps to SBML symbol `species_2`.'), 'traf6': ('species_6', 'native SBML value', 'TRAF6 observable. Maps to SBML symbol `species_6`.'), 'traf5': ('species_7', 'native SBML value', 'TRAF5 observable. Maps to SBML symbol `species_7`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2502170002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
