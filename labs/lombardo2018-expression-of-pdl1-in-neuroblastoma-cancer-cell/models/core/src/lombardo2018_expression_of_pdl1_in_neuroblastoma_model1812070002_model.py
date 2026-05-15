# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Lombardo2018 - Expression of PDL1 in Neuroblastoma Cancer Cell."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Lombardo2018ExpressionOfPdl1InNeuroblastomaModel1812070002Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'MODEL1812070002'
    _TITLE = 'Lombardo2018 - Expression of PDL1 in Neuroblastoma Cancer Cell'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['EGFR_f', 'EGFR_di_p', 'SOS_active', 'SOS_inactive', 'bNGFR', 'NGFR', 'P90Rsk_active', 'P90Rsk_inactive', 'RAS_active', 'RAS_inactive', 'PTENActive', 'S6K1Inactive', 'mTORC1Inactive', 'PDK1Inactive', 'IRS1Inactive', 'PDK1Active', 'mTORC1Active', 'S6K1Active', 'IRS1Active', 'AktInactive', 'C3GInactive', 'Raf1Inactive', 'degradedEGFR', 'AktActive', 'C3GActive', 'Rap1Active', 'Rap1Inactive', 'bRafActive', 'PP2AActive', 'MekActive', 'bRafInactive', 'ERK_inactive', 'PI3KActive', 'PI3KInactive', 'ERK_active', 'Raf1Active', 'MekInactive', 'degradedNGFR', 'STAT1', 'STAT1_p', 'STAT3', 'STAT3_ac', 'STAT3_ac_p', 'STAT3_p', 'PDL1_mRNA', 'degraded_PDL1_mRNA', 'ASK_MLK_active', 'ASK_MLK_inactive', 'JNK_active', 'MKK3_6_active', 'MKK3_6_inactive', 'p38_active', 'p38_inactive', 'PP2A_inactive', 'DUSP4_6_active', 'DUSP4_6_inactive', 'JNK_inactive', 'MKK4_7_active', 'MKK4_7_inactive', 'DUSP2_active', 'DUSP2_inactive', 'MYCN_mRNA', 'GSK3b_active', 'GSK3b_inactive', 'N_MYC', 'MYCN_mRNA_degraded', 'N_MYC_pp', 'ALK_Mutated', 'Akt_Thr308', 'Akt_conformational_change', 'PIP3', 'PIP2', 'AMPK_active', 'AMPK_inactive', 'PTEN_inactive', 'Crizotinib', 'EGFR_inhibited', 'Gefitinib']
    _SPECIES_LABELS = {'NGFR': 'NGFR', 'PIP3': 'PIP3', 'EGFR_f': 'EGFR free', 'SOS_inactive': 'SOS inactive', 'P90Rsk_inactive': 'P90Rsk inactive', 'RAS_inactive': 'RAS inactive'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'kmegf_level': ('KmEGF', 6086070.0, 'native SBML value', 'KmEGF source parameter. Maps to bundled SBML parameter `KmEGF`.'), 'kcategf_level': ('KcatEGF', 694.731, 'native SBML value', 'KcatEGF source parameter. Maps to bundled SBML parameter `KcatEGF`.'), 'initial_ngfr': ('NGFR', 14737.0, 'native SBML value', 'Initial NGFR. Sets the initial value of bundled SBML symbol `NGFR`.'), 'initial_pip3': ('PIP3', 100000.0, 'native SBML value', 'Initial PIP3. Sets the initial value of bundled SBML symbol `PIP3`.'), 'initial_egfr_free': ('EGFR_f', 618.0, 'native SBML value', 'Initial EGFR free. Sets the initial value of bundled SBML symbol `EGFR_f`.'), 'initial_sos_inactive': ('SOS_inactive', 9456.0, 'native SBML value', 'Initial SOS inactive. Sets the initial value of bundled SBML symbol `SOS_inactive`.')}
    _HEADLINE_OUTPUTS = {'ngfr': ('NGFR', 'native SBML value', 'NGFR observable. Maps to SBML symbol `NGFR`.'), 'pip3': ('PIP3', 'native SBML value', 'PIP3 observable. Maps to SBML symbol `PIP3`.'), 'egfr_free': ('EGFR_f', 'native SBML value', 'EGFR free observable. Maps to SBML symbol `EGFR_f`.'), 'sos_inactive': ('SOS_inactive', 'native SBML value', 'SOS inactive observable. Maps to SBML symbol `SOS_inactive`.'), 'p90rsk_inactive': ('P90Rsk_inactive', 'native SBML value', 'P90Rsk inactive observable. Maps to SBML symbol `P90Rsk_inactive`.'), 'ras_inactive': ('RAS_inactive', 'native SBML value', 'RAS inactive observable. Maps to SBML symbol `RAS_inactive`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1812070002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
