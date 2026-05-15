# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Capuani2015 - Human Core Catabolic Network."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Capuani2015HumanCoreCatabolicNetworkModel1506170000Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'MODEL1506170000'
    _TITLE = 'Capuani2015 - Human Core Catabolic Network'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['M_13dpg_e', 'M_23dpg_e', 'M_2pg_e', 'M_3pg_e', 'M_6pgc_e', 'M_6pgl_e', 'M_accoa_e', 'M_adp_e', 'M_akg_e', 'M_atp_e', 'M_cit_e', 'M_co2_e', 'M_coa_e', 'M_dhap_e', 'M_e4p_e', 'M_f6p_e', 'M_fad_e', 'M_fadh2_e', 'M_fdp_e', 'M_ficytC_e', 'M_focytC_e', 'M_fum_e', 'M_g3p_e', 'M_g6p_e', 'M_glc_DASH_D_e', 'M_h2o_e', 'M_h_c', 'M_h_e', 'M_icit_e', 'M_lac_DASH_L_e', 'M_mal_DASH_L_e', 'M_nad_e', 'M_nadh_e', 'M_nadp_e', 'M_nadph_e', 'M_o2_e', 'M_o2s_e', 'M_oaa_e', 'M_pep_e', 'M_pi_e', 'M_pyr_e', 'M_q10_e', 'M_q10h2_e', 'M_r5p_e', 'M_ru5p_DASH_D_e', 'M_s7p_e', 'M_succ_e', 'M_succoa_e', 'M_xu5p_DASH_D_e', 'M_gln_DASH_L_e', 'M_glu_DASH_L_e', 'M_nh4_e', 'M_ch3_e', 'M_asp_DASH_L_e', 'M_ala_DASH_L_e', 'M_asn_DASH_L_e', 'M_pro_DASH_L_e', 'M_ser_DASH_L_e', 'M_gly_e', 'M_arg_DASH_L_e', 'M_cys_DASH_L_e', 'M_met_DASH_L_e', 'M_tyr_DASH_L_e', 'M_phe_DASH_L_e', 'M_hdca_e']
    _SPECIES_LABELS = {'M_atp_e': 'ATP', 'M_g6p_e': 'D Glucose 6 phosphate', 'M_glc_DASH_D_e': 'D Glucose', 'M_lac_DASH_L_e': 'L Lactate', 'M_nad_e': 'Nicotinamide adenine dinucleotide', 'M_nadh_e': 'Nicotinamide adenine dinucleotide reduced'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'atp': ('M_atp_e', 'native SBML value', 'ATP observable. Maps to SBML symbol `M_atp_e`.'), 'd_glucose_6_phosphate': ('M_g6p_e', 'native SBML value', 'D Glucose 6 phosphate observable. Maps to SBML symbol `M_g6p_e`.'), 'd_glucose': ('M_glc_DASH_D_e', 'native SBML value', 'D Glucose observable. Maps to SBML symbol `M_glc_DASH_D_e`.'), 'l_lactate': ('M_lac_DASH_L_e', 'native SBML value', 'L Lactate observable. Maps to SBML symbol `M_lac_DASH_L_e`.'), 'nicotinamide_adenine_dinucleotide': ('M_nad_e', 'native SBML value', 'Nicotinamide adenine dinucleotide observable. Maps to SBML symbol `M_nad_e`.'), 'nicotinamide_adenine_dinucleotide_reduced': ('M_nadh_e', 'native SBML value', 'Nicotinamide adenine dinucleotide reduced observable. Maps to SBML symbol `M_nadh_e`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1506170000.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
