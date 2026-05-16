# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Ghaffari2019 - Thrombomodulin Gene Expression after Retinoic Acid Treatment for Cancer Patients with Coagulation Disorders."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Ghaffari2019ThrombomodulinGeneExpressionAfteModel1907140001Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'MODEL1907140001'
    _TITLE = 'Ghaffari2019 - Thrombomodulin Gene Expression after Retinoic Acid Treatment for Cancer Patients with Coagulation Disorders'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['TM_mRNA', 'TM', 'RA', 'REC1t', 'sTM']
    _SPECIES_LABELS = {'TM': 'TM', 'RA': 'RA', 'sTM': 'STM', 'REC1t': 'REC1t', 'TM_mRNA': 'TM mRNA'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_stm': ('sTM', 1.0, 'native SBML value', 'Initial STM. Sets the initial value of bundled SBML symbol `sTM`.'), 'initial_rec1t': ('REC1t', 1e-06, 'native SBML value', 'Initial REC1t. Sets the initial value of bundled SBML symbol `REC1t`.'), 'initial_tm_m_rna': ('TM_mRNA', 0.0, 'native SBML value', 'Initial TM mRNA. Sets the initial value of bundled SBML symbol `TM_mRNA`.')}
    _HEADLINE_OUTPUTS = {'tm': ('TM', 'native SBML value', 'TM observable. Maps to SBML symbol `TM`.'), 'ra': ('RA', 'native SBML value', 'RA observable. Maps to SBML symbol `RA`.'), 'stm': ('sTM', 'native SBML value', 'STM observable. Maps to SBML symbol `sTM`.'), 'rec1t': ('REC1t', 'native SBML value', 'REC1t observable. Maps to SBML symbol `REC1t`.'), 'tm_m_rna': ('TM_mRNA', 'native SBML value', 'TM mRNA observable. Maps to SBML symbol `TM_mRNA`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1907140001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
