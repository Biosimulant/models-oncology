# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Zeilfelder2025 - Model for human liver cancer cell line HepG2."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Zeilfelder2025ModelForHumanLiverCancerCellModel2503270001Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'MODEL2503270001'
    _TITLE = 'Zeilfelder2025 - Model for human liver cancer cell line HepG2'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['BMPR', 'BMPR_delay1', 'BMPR_delay2', 'BMPR_delay3', 'BMPR_delay4', 'BMPR_delay5', 'BMPR_delay6', 'SMAD6RNA1', 'SMAD6RNA2', 'SMAD6RNA', 'ID3RNA', 'JAK1_gp130', 'pJAK1_pgp130', 'STAT3', 'cpSTAT3', 'npSTAT3', 'nSOCS3RNA1', 'nSOCS3RNA2', 'nSOCS3RNA3', 'nSOCS3RNA4', 'nSOCS3RNA5', 'SOCS3RNA', 'SOCS3', 'nHAMPRNA1', 'nHAMPRNA2', 'nHAMPRNA3', 'nHAMPRNA4', 'nHAMPRNA5', 'nHAMPRNA6', 'nHAMPRNA7', 'HAMPRNA']
    _SPECIES_LABELS = {'STAT3': 'Unphosphorylated STAT3', 'cpSTAT3': 'Active cytoplasmic STAT3', 'npSTAT3': 'Active nuclear STAT3', 'BMPR': 'Total BMP receptor', 'BMPR_delay1': 'Cofactor activated by BMP receptor', 'BMPR_delay2': 'Cofactor activated by BMP receptor 2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'input_il6_source_parameter': ('input_il6', 10.0, 'native SBML value', 'Input il6 source parameter. Maps to bundled SBML parameter `input_il6`.'), 'il6_basal_source_parameter': ('il6_basal', 0.00957067090828757, 'native SBML value', 'Il6 basal source parameter. Maps to bundled SBML parameter `il6_basal`.'), 'il6_act_source_parameter': ('il6_act', 0.0226985677410744, 'native SBML value', 'Il6 act source parameter. Maps to bundled SBML parameter `il6_act`.'), 'dcf_il6_basal_source_parameter': ('dcf_il6_basal', 0.835096746625705, 'native SBML value', 'Dcf il6 basal source parameter. Maps to bundled SBML parameter `dcf_il6_basal`.'), 'initial_unphosphorylated_stat3': ('STAT3', 1237.76392668883, 'native SBML value', 'Initial Unphosphorylated STAT3. Sets the initial value of bundled SBML symbol `STAT3`.'), 'initial_active_cytoplasmic_stat3': ('cpSTAT3', 24.1373740148803, 'native SBML value', 'Initial Active cytoplasmic STAT3. Sets the initial value of bundled SBML symbol `cpSTAT3`.')}
    _HEADLINE_OUTPUTS = {'unphosphorylated_stat3': ('STAT3', 'native SBML value', 'Unphosphorylated STAT3 observable. Maps to SBML symbol `STAT3`.'), 'active_cytoplasmic_stat3': ('cpSTAT3', 'native SBML value', 'Active cytoplasmic STAT3 observable. Maps to SBML symbol `cpSTAT3`.'), 'active_nuclear_stat3': ('npSTAT3', 'native SBML value', 'Active nuclear STAT3 observable. Maps to SBML symbol `npSTAT3`.'), 'total_bmp_receptor': ('BMPR', 'native SBML value', 'Total BMP receptor observable. Maps to SBML symbol `BMPR`.'), 'cofactor_activated_by_bmp_receptor': ('BMPR_delay1', 'native SBML value', 'Cofactor activated by BMP receptor observable. Maps to SBML symbol `BMPR_delay1`.'), 'cofactor_activated_by_bmp_receptor_2': ('BMPR_delay2', 'native SBML value', 'Cofactor activated by BMP receptor 2 observable. Maps to SBML symbol `BMPR_delay2`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2503270001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
