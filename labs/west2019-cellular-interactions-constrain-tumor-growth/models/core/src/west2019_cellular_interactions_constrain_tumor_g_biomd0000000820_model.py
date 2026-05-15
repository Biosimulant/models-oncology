# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for West2019 - Cellular interactions constrain tumor growth."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class West2019CellularInteractionsConstrainTumorGBiomd0000000820Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000820'
    _TITLE = 'West2019 - Cellular interactions constrain tumor growth'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['tumor_at_Exp_Lin_growth', 'tumor_at_Gen__logistic_growth', 'tumor_at_Gomp__growth', 'tumor_at_Power_growth', 'tumor_at_Von_Bert__growth', 'tumor_at_Exp_growth', 'tumor_at_Logistic_growth']
    _SPECIES_LABELS = {'tumor_at_Exp_Lin_growth': 'Tumor at Exp Lin growth', 'tumor_at_Gen__logistic_growth': 'Tumor at Gen. logistic growth', 'tumor_at_Gomp__growth': 'Tumor at Gomp. growth', 'tumor_at_Power_growth': 'Tumor at Power growth', 'tumor_at_Von_Bert__growth': 'Tumor at Von Bert. growth', 'tumor_at_Exp_growth': 'Tumor at Exp growth'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_tumor_at_exp_lin_growth': ('tumor_at_Exp_Lin_growth', 1.0, 'native SBML value', 'Initial Tumor at Exp Lin growth. Sets the initial value of bundled SBML symbol `tumor_at_Exp_Lin_growth`.'), 'initial_tumor_at_gen_logistic_growth': ('tumor_at_Gen__logistic_growth', 1.0, 'native SBML value', 'Initial Tumor at Gen. logistic growth. Sets the initial value of bundled SBML symbol `tumor_at_Gen__logistic_growth`.'), 'initial_tumor_at_gomp_growth': ('tumor_at_Gomp__growth', 1.0, 'native SBML value', 'Initial Tumor at Gomp. growth. Sets the initial value of bundled SBML symbol `tumor_at_Gomp__growth`.'), 'initial_tumor_at_power_growth': ('tumor_at_Power_growth', 1.0, 'native SBML value', 'Initial Tumor at Power growth. Sets the initial value of bundled SBML symbol `tumor_at_Power_growth`.'), 'initial_tumor_at_von_bert_growth': ('tumor_at_Von_Bert__growth', 1.0, 'native SBML value', 'Initial Tumor at Von Bert. growth. Sets the initial value of bundled SBML symbol `tumor_at_Von_Bert__growth`.'), 'initial_tumor_at_exp_growth': ('tumor_at_Exp_growth', 1.0, 'native SBML value', 'Initial Tumor at Exp growth. Sets the initial value of bundled SBML symbol `tumor_at_Exp_growth`.')}
    _HEADLINE_OUTPUTS = {'tumor_at_exp_lin_growth': ('tumor_at_Exp_Lin_growth', 'native SBML value', 'Tumor at Exp Lin growth observable. Maps to SBML symbol `tumor_at_Exp_Lin_growth`.'), 'tumor_at_gen_logistic_growth': ('tumor_at_Gen__logistic_growth', 'native SBML value', 'Tumor at Gen. logistic growth observable. Maps to SBML symbol `tumor_at_Gen__logistic_growth`.'), 'tumor_at_gomp_growth': ('tumor_at_Gomp__growth', 'native SBML value', 'Tumor at Gomp. growth observable. Maps to SBML symbol `tumor_at_Gomp__growth`.'), 'tumor_at_power_growth': ('tumor_at_Power_growth', 'native SBML value', 'Tumor at Power growth observable. Maps to SBML symbol `tumor_at_Power_growth`.'), 'tumor_at_von_bert_growth': ('tumor_at_Von_Bert__growth', 'native SBML value', 'Tumor at Von Bert. growth observable. Maps to SBML symbol `tumor_at_Von_Bert__growth`.'), 'tumor_at_exp_growth': ('tumor_at_Exp_growth', 'native SBML value', 'Tumor at Exp growth observable. Maps to SBML symbol `tumor_at_Exp_growth`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000820.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
