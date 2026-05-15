# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Hu2019 - Modeling Pancreatic Cancer Dynamics with Immunotherapy."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Hu2019ModelingPancreaticCancerDynamicsWithBiomd0000000792Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000792'
    _TITLE = 'Hu2019 - Modeling Pancreatic Cancer Dynamics with Immunotherapy'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['x_PCC', 'y_PSC', 'z_Effector_Cells', 'w_TPC', 'v_TSC', 'R_siRNA']
    _SPECIES_LABELS = {'z_Effector_Cells': 'Z Effector Cells', 'x_PCC': 'X PCC', 'y_PSC': 'Y PSC', 'w_TPC': 'W TPC', 'v_TSC': 'V TSC', 'R_siRNA': 'R siRNA'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_z_effector_cells': ('z_Effector_Cells', 190000000.0, 'native SBML value', 'Initial Z Effector Cells. Sets the initial value of bundled SBML symbol `z_Effector_Cells`.'), 'initial_x_pcc': ('x_PCC', 1000000000.0, 'native SBML value', 'Initial X PCC. Sets the initial value of bundled SBML symbol `x_PCC`.'), 'initial_y_psc': ('y_PSC', 5600000.0, 'native SBML value', 'Initial Y PSC. Sets the initial value of bundled SBML symbol `y_PSC`.'), 'initial_w_tpc': ('w_TPC', 50000.0, 'native SBML value', 'Initial W TPC. Sets the initial value of bundled SBML symbol `w_TPC`.'), 'initial_v_tsc': ('v_TSC', 9.4, 'native SBML value', 'Initial V TSC. Sets the initial value of bundled SBML symbol `v_TSC`.'), 'initial_r_sirna': ('R_siRNA', 1.0, 'native SBML value', 'Initial R siRNA. Sets the initial value of bundled SBML symbol `R_siRNA`.')}
    _HEADLINE_OUTPUTS = {'z_effector_cells': ('z_Effector_Cells', 'native SBML value', 'Z Effector Cells observable. Maps to SBML symbol `z_Effector_Cells`.'), 'x_pcc': ('x_PCC', 'native SBML value', 'X PCC observable. Maps to SBML symbol `x_PCC`.'), 'y_psc': ('y_PSC', 'native SBML value', 'Y PSC observable. Maps to SBML symbol `y_PSC`.'), 'w_tpc': ('w_TPC', 'native SBML value', 'W TPC observable. Maps to SBML symbol `w_TPC`.'), 'v_tsc': ('v_TSC', 'native SBML value', 'V TSC observable. Maps to SBML symbol `v_TSC`.'), 'r_sirna': ('R_siRNA', 'native SBML value', 'R siRNA observable. Maps to SBML symbol `R_siRNA`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000792.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
