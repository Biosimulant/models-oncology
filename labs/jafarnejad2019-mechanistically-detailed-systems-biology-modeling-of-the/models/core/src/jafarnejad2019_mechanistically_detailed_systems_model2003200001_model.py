# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Jafarnejad2019 - Mechanistically detailed systems biology modeling of the HGF/Met pathway in hepatocellular carcinoma."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Jafarnejad2019MechanisticallyDetailedSystemsModel2003200001Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'MODEL2003200001'
    _TITLE = 'Jafarnejad2019 - Mechanistically detailed systems biology modeling of the HGF/Met pathway in hepatocellular carcinoma'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Itg', 'Met_Itg', 'pMet', 'pMet_i', 'pMet_Itg', 'pMet_Itg_i', 'pMet_total', 'pMet_i_total', 'Met_pMet_s_total', 'pMet_s_total', 'Gab1', 'Gab1_pMet', 'PI3K', 'PI3K_active', 'Akt', 'pAkt', 'Rac', 'Rac_active', 'PAK1', 'pPAK1', 'SOS', 'mSOS_pMet', 'Ras', 'Ras_active', 'Raf', 'pRaf', 'MEK', 'pMEK', 'ERK', 'pERK', 'RSK', 'pRSK', 'ppRSK', 'PDK1', 'Peptide_Itg', 'Sorafenib_Raf', 'Cabozantinib_Met', 'Cabozantinib_Met_Itg', 'Met_max', 'Itg_max', 'Akt_max', 'Raf_max', 'MEK_max', 'ERK_max', 'RSK_max', 'Peptide', 'Sorafenib', 'Cabozantinib', 'Met']
    _SPECIES_LABELS = {'PI3K': 'PI3K', 'Akt': 'AKT', 'Ras': 'Ras', 'Raf': 'Raf', 'ERK': 'ERK', 'pAkt': 'PAkt'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'kd_rilotumumab_level': ('KD_Rilotumumab', 0.22, 'native SBML value', 'KD Rilotumumab source parameter. Maps to bundled SBML parameter `KD_Rilotumumab`.'), 'initial_pi3k': ('PI3K', 1976.0, 'native SBML value', 'Initial PI3K. Sets the initial value of bundled SBML symbol `PI3K`.'), 'initial_akt': ('Akt', 32983.0, 'native SBML value', 'Initial AKT. Sets the initial value of bundled SBML symbol `Akt`.'), 'initial_ras': ('Ras', 30826.0, 'native SBML value', 'Initial Ras. Sets the initial value of bundled SBML symbol `Ras`.'), 'initial_raf': ('Raf', 89608.0, 'native SBML value', 'Initial Raf. Sets the initial value of bundled SBML symbol `Raf`.'), 'initial_erk': ('ERK', 232907.0, 'native SBML value', 'Initial ERK. Sets the initial value of bundled SBML symbol `ERK`.')}
    _HEADLINE_OUTPUTS = {'pi3k': ('PI3K', 'native SBML value', 'PI3K observable. Maps to SBML symbol `PI3K`.'), 'akt': ('Akt', 'native SBML value', 'AKT observable. Maps to SBML symbol `Akt`.'), 'ras': ('Ras', 'native SBML value', 'Ras observable. Maps to SBML symbol `Ras`.'), 'raf': ('Raf', 'native SBML value', 'Raf observable. Maps to SBML symbol `Raf`.'), 'erk': ('ERK', 'native SBML value', 'ERK observable. Maps to SBML symbol `ERK`.'), 'pakt': ('pAkt', 'native SBML value', 'PAkt observable. Maps to SBML symbol `pAkt`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2003200001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
