# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Iwamoto2010 - Cell cycle reponse to DNA damage."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Iwamoto2010CellCycleReponseToDnaDamageBiomd0000000939Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000939'
    _TITLE = 'Iwamoto2010 - Cell cycle reponse to DNA damage'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Cyclin_D', 'Cdk4', 'Cyclin_D_Cdk4', 'Cyclin_E', 'E2F', 'Cdk2', 'Cyclin_E_Cdk2_inactive_phosphorylated', 'Cyclin_A', 'B_Myb_active', 'Cyclin_A_Cdk2_inactive', 'Cyclin_A_Cdk2_active', 'APC_Ccdc20_active', 'APC_Ccdh1_active', 'Cyclin_E_Cdk2_active_unphosphorylated', 'p21', 'p21_CyclinD_Cdk4', 'p27', 'p27_CyclinD_Cdk4', 'Cdc25A_active', 'p27_CyclinE_Cdk2', 'p21_CyclinE_Cdk2', 'p27_CyclinA_Cdk2', 'p21_CyclinA_Cdk2', 'p53', 'p16', 'Rb', 'Rb_E2F', 'Rb_PP_E2F', 'Rb_PPP', 'ATM_ATR', 'Mdm2', 'Intermediate', 'NF_Y', 'Cdc25A_inactive', 'Chk1_active', 'Chk1_inactive', 'Cyclin_B', 'Cdk1', 'Cyclin_B_Cdk1_inactive_unphosphorylated_cytoplasm', 'Cyclin_B_Cdk1_active_phosphorylated_cytoplasm', 'Cdc25C_active', '_14_3_3_sigma', 'Cdc25C_Ps216_phosphorylated_active', 'Wee1', 'Wee1_phosphorylated', 'Cyclin_B_Cdk1_nuclear', 'p21_CyclinB_Cdk1', 'B_Myb_inactive', 'Cdc25C_inactive', 'Cdc25C_Ps216_phosphorylated_inactive', '_14_3_3_sigma_iCdc25C_PS216_phosphorylated', 'APC_Ccdc20_inactive', 'APC_Ccdh1_inactive', 'Cyclin_B_Cdk1_nuclear_inactive']
    _SPECIES_LABELS = {'p27_CyclinD_Cdk4': 'P27/CyclinD/Cdk4', 'p27_CyclinE_Cdk2': 'P27/CyclinE/Cdk2', 'p27_CyclinA_Cdk2': 'P27/CyclinA/Cdk2', 'p21_CyclinD_Cdk4': 'P21/CyclinD/Cdk4', 'p21_CyclinE_Cdk2': 'P21/CyclinE/Cdk2', 'p21_CyclinA_Cdk2': 'P21/CyclinA/Cdk2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'dna_damage_signal': ('DNA_damage_signal', 0.0, 'native SBML value', 'DNA damage signal source parameter. Maps to bundled SBML parameter `DNA_damage_signal`.'), 'initial_p27_cyclind_cdk4': ('p27_CyclinD_Cdk4', 0.001, 'native SBML value', 'Initial P27/CyclinD/Cdk4. Sets the initial value of bundled SBML symbol `p27_CyclinD_Cdk4`.'), 'initial_p27_cycline_cdk2': ('p27_CyclinE_Cdk2', 1.0, 'native SBML value', 'Initial P27/CyclinE/Cdk2. Sets the initial value of bundled SBML symbol `p27_CyclinE_Cdk2`.'), 'initial_p27_cyclina_cdk2': ('p27_CyclinA_Cdk2', 0.0001, 'native SBML value', 'Initial P27/CyclinA/Cdk2. Sets the initial value of bundled SBML symbol `p27_CyclinA_Cdk2`.'), 'initial_p21_cyclind_cdk4': ('p21_CyclinD_Cdk4', 0.0, 'native SBML value', 'Initial P21/CyclinD/Cdk4. Sets the initial value of bundled SBML symbol `p21_CyclinD_Cdk4`.'), 'initial_p21_cycline_cdk2': ('p21_CyclinE_Cdk2', 0.0, 'native SBML value', 'Initial P21/CyclinE/Cdk2. Sets the initial value of bundled SBML symbol `p21_CyclinE_Cdk2`.')}
    _HEADLINE_OUTPUTS = {'p27_cyclind_cdk4': ('p27_CyclinD_Cdk4', 'native SBML value', 'P27/CyclinD/Cdk4 observable. Maps to SBML symbol `p27_CyclinD_Cdk4`.'), 'p27_cycline_cdk2': ('p27_CyclinE_Cdk2', 'native SBML value', 'P27/CyclinE/Cdk2 observable. Maps to SBML symbol `p27_CyclinE_Cdk2`.'), 'p27_cyclina_cdk2': ('p27_CyclinA_Cdk2', 'native SBML value', 'P27/CyclinA/Cdk2 observable. Maps to SBML symbol `p27_CyclinA_Cdk2`.'), 'p21_cyclind_cdk4': ('p21_CyclinD_Cdk4', 'native SBML value', 'P21/CyclinD/Cdk4 observable. Maps to SBML symbol `p21_CyclinD_Cdk4`.'), 'p21_cycline_cdk2': ('p21_CyclinE_Cdk2', 'native SBML value', 'P21/CyclinE/Cdk2 observable. Maps to SBML symbol `p21_CyclinE_Cdk2`.'), 'p21_cyclina_cdk2': ('p21_CyclinA_Cdk2', 'native SBML value', 'P21/CyclinA/Cdk2 observable. Maps to SBML symbol `p21_CyclinA_Cdk2`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000939.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
