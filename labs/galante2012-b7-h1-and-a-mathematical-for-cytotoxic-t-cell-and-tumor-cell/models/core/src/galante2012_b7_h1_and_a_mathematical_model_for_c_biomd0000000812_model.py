# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Galante2012 - B7-H1 and a Mathematical Model for Cytotoxic T Cell and Tumor Cell Interaction."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Galante2012B7H1AndAMathematicalModelForCBiomd0000000812Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000812'
    _TITLE = 'Galante2012 - B7-H1 and a Mathematical Model for Cytotoxic T Cell and Tumor Cell Interaction'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['X_Complex', 'P_Perforin', 'C_Cancer_Uncomplexed', 'T_ast']
    _SPECIES_LABELS = {'P_Perforin': 'P Perforin', 'C_Cancer_Uncomplexed': 'C Cancer Uncomplexed', 'T_ast': 'T ast', 'X_Complex': 'X Complex'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_p_perforin': ('P_Perforin', 0.315, 'native SBML value', 'Initial P Perforin. Sets the initial value of bundled SBML symbol `P_Perforin`.'), 'initial_c_cancer_uncomplexed': ('C_Cancer_Uncomplexed', 1.0, 'native SBML value', 'Initial C Cancer Uncomplexed. Sets the initial value of bundled SBML symbol `C_Cancer_Uncomplexed`.'), 'initial_t_ast': ('T_ast', 1.0, 'native SBML value', 'Initial T ast. Sets the initial value of bundled SBML symbol `T_ast`.'), 'initial_x_complex': ('X_Complex', 0.0, 'native SBML value', 'Initial X Complex. Sets the initial value of bundled SBML symbol `X_Complex`.')}
    _HEADLINE_OUTPUTS = {'p_perforin': ('P_Perforin', 'native SBML value', 'P Perforin observable. Maps to SBML symbol `P_Perforin`.'), 'c_cancer_uncomplexed': ('C_Cancer_Uncomplexed', 'native SBML value', 'C Cancer Uncomplexed observable. Maps to SBML symbol `C_Cancer_Uncomplexed`.'), 't_ast': ('T_ast', 'native SBML value', 'T ast observable. Maps to SBML symbol `T_ast`.'), 'x_complex': ('X_Complex', 'native SBML value', 'X Complex observable. Maps to SBML symbol `X_Complex`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000812.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
