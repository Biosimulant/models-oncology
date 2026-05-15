# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Giani2019 - Computational modeling to predict MAP3K8 effects as mediator of resistance to vemurafenib in thyroid cancer stem cells."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Giani2019ComputationalModelingToPredictMap3Biomd0000000883Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000883'
    _TITLE = 'Giani2019 - Computational modeling to predict MAP3K8 effects as mediator of resistance to vemurafenib in thyroid cancer stem cells'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['species_0', 'species_1', 'species_2', 'species_3', 'species_4', 'species_5', 'species_6', 'species_7', 'species_8', 'species_9', 'species_10', 'species_11', 'species_14', 'species_15', 'species_16', 'species_17', 'PIP3Active', 'PIP3Inactive', 'PDK1Inactive', 'PDK1Active', 'mTORC2Active', 'mTORC1Active', 'mTORC1Inactive', 'bRafMutated', 'PLX4032', 'Grb2Active', 'Grb2Inactive', 'freeFGFR', 'pFGFR', 'freeTNFR1', 'pTNFR1', 'freeTNFR2', 'pTNFR2', 'TRADD_TRAF2_TRAF5_RIP1_Active', 'TRADD_TRAF2_TRAF5_RIP1_Inactive', 'TRAF1_TRAF2_TRAF3_Active', 'TRAF1_TRAF2_TRAF3_Inactive', 'NIKActive', 'NIKInactive', 'IKKbeta_IKKalfa_IKKgamma_Active', 'IKKbeta_IKKalfa_IKKgamma_Inactive', 'TAB1_TAB2_TAB3_TAK1_Active', 'TAB1_TAB2_TAB3_TAK1_Inactive', 'Tpl2_NF_kB_Active', 'Tpl2_NF_kB_Inactive', 'bRafMutatedInactive', 'TRADD_TRAF2_TRAF5_RIP1_bRafINH_Active', 'TRADD_TRAF2_TRAF5_RIP1_bRafINH_Inactive', 'TAB1_TAB2_TAB3_TAK1_bRafINH_Inactive', 'TAB1_TAB2_TAB3_TAK1_bRafINH_Active', 'NIK_bRafINH_Active', 'NIK_bRafINH_Inactive', 'IKKbeta_IKKalfa_IKKgamma_bRafINH_Active', 'IKKbeta_IKKalfa_IKKgamma_bRafINH_Inactive', 'Tpl2_NF_kB_bRafINH_Active', 'Tpl2_NF_kB_bRafINH_Inactive', 'TRAF1_TRAF2_TRAF3_bRafINH_Active', 'TRAF1_TRAF2_TRAF3_bRafINH_Inactive', 'Tpl2_NF_kB_RasINH_Active', 'Tpl2_NF_kB_RasINH_Inactive', 'mTORC2Inactive', 'MAP3K8_inhibitor', 'MAP3K8_NF_kB_inhibited']
    _SPECIES_LABELS = {'species_1': 'Free EGFR', 'species_3': 'Sos Inactive', 'species_5': 'Ras Inactive', 'species_7': 'Raf1 Inactive', 'species_9': 'Mek Inactive', 'species_11': 'ERK'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_free_egfr': ('species_1', 10.0, 'native SBML value', 'Initial Free EGFR. Sets the initial value of bundled SBML symbol `species_1`.'), 'initial_sos_inactive': ('species_3', 10.0, 'native SBML value', 'Initial Sos Inactive. Sets the initial value of bundled SBML symbol `species_3`.'), 'initial_ras_inactive': ('species_5', 10.0, 'native SBML value', 'Initial Ras Inactive. Sets the initial value of bundled SBML symbol `species_5`.'), 'initial_raf1_inactive': ('species_7', 10.0, 'native SBML value', 'Initial Raf1 Inactive. Sets the initial value of bundled SBML symbol `species_7`.'), 'initial_mek_inactive': ('species_9', 10.0, 'native SBML value', 'Initial Mek Inactive. Sets the initial value of bundled SBML symbol `species_9`.'), 'initial_erk': ('species_11', 10.0, 'native SBML value', 'Initial ERK. Sets the initial value of bundled SBML symbol `species_11`.')}
    _HEADLINE_OUTPUTS = {'free_egfr': ('species_1', 'native SBML value', 'Free EGFR observable. Maps to SBML symbol `species_1`.'), 'sos_inactive': ('species_3', 'native SBML value', 'Sos Inactive observable. Maps to SBML symbol `species_3`.'), 'ras_inactive': ('species_5', 'native SBML value', 'Ras Inactive observable. Maps to SBML symbol `species_5`.'), 'raf1_inactive': ('species_7', 'native SBML value', 'Raf1 Inactive observable. Maps to SBML symbol `species_7`.'), 'mek_inactive': ('species_9', 'native SBML value', 'Mek Inactive observable. Maps to SBML symbol `species_9`.'), 'erk': ('species_11', 'native SBML value', 'ERK observable. Maps to SBML symbol `species_11`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000883.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
