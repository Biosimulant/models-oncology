# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Hayashi2013 - TNF-induced Signaling Dynamics (Model A)."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Hayashi2013TnfInducedSignalingDynamicsModelModel2502170001Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'MODEL2502170001'
    _TITLE = 'Hayashi2013 - TNF-induced Signaling Dynamics (Model A)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['species_1', 'species_2', 'species_3', 'species_4', 'species_5', 'species_6', 'species_7', 'species_8', 'species_9', 'species_10', 'species_11', 'species_12', 'species_13', 'species_14', 'species_15', 'species_16', 'species_17', 'species_18', 'species_19', 'species_20', 'species_21', 'species_22', 'species_23', 'species_24', 'species_25', 'species_26', 'species_27', 'species_28', 'species_29', 'species_30', 'species_31', 'species_32', 'species_33', 'species_34', 'species_35', 'species_36', 'species_37', 'species_38', 'species_39', 'species_40', 'species_41', 'species_42', 'species_43', 'species_44', 'species_45', 'species_46', 'species_47', 'species_48', 'species_49', 'species_50', 'species_51']
    _SPECIES_LABELS = {'species_3': 'TNFR1', 'species_2': 'NFkBc', 'species_6': 'TRAF6', 'species_7': 'TRAF5', 'species_9': 'TRAF2', 'species_16': 'ERKc'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_tnfr1': ('species_3', 1.0, 'native SBML value', 'Initial TNFR1. Sets the initial value of bundled SBML symbol `species_3`.'), 'initial_nfkbc': ('species_2', 0.0, 'native SBML value', 'Initial NFkBc. Sets the initial value of bundled SBML symbol `species_2`.'), 'initial_traf6': ('species_6', 0.0, 'native SBML value', 'Initial TRAF6. Sets the initial value of bundled SBML symbol `species_6`.'), 'initial_traf5': ('species_7', 0.0, 'native SBML value', 'Initial TRAF5. Sets the initial value of bundled SBML symbol `species_7`.'), 'initial_traf2': ('species_9', 0.0, 'native SBML value', 'Initial TRAF2. Sets the initial value of bundled SBML symbol `species_9`.'), 'initial_erkc': ('species_16', 0.0, 'native SBML value', 'Initial ERKc. Sets the initial value of bundled SBML symbol `species_16`.')}
    _HEADLINE_OUTPUTS = {'tnfr1': ('species_3', 'native SBML value', 'TNFR1 observable. Maps to SBML symbol `species_3`.'), 'nfkbc': ('species_2', 'native SBML value', 'NFkBc observable. Maps to SBML symbol `species_2`.'), 'traf6': ('species_6', 'native SBML value', 'TRAF6 observable. Maps to SBML symbol `species_6`.'), 'traf5': ('species_7', 'native SBML value', 'TRAF5 observable. Maps to SBML symbol `species_7`.'), 'traf2': ('species_9', 'native SBML value', 'TRAF2 observable. Maps to SBML symbol `species_9`.'), 'erkc': ('species_16', 'native SBML value', 'ERKc observable. Maps to SBML symbol `species_16`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2502170001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
