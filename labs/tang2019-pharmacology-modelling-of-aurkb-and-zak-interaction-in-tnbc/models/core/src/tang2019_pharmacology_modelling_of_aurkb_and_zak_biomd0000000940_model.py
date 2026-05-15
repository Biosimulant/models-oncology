# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Tang2019 - Pharmacology modelling of AURKB and ZAK interaction in TNBC."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Tang2019PharmacologyModellingOfAurkbAndZakBiomd0000000940Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000940'
    _TITLE = 'Tang2019 - Pharmacology modelling of AURKB and ZAK interaction in TNBC'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['PKN1', 'ZAK', 'MAP2K3', 'MAPK14', 'MAP2K4', 'TP53', 'ATM', 'MAPK13', 'PRKACA', 'SRC', 'BAD', 'PTEN', 'SHC1', 'PIK3R1', 'PARP1', 'AURKB', 'BRCA1', 'YWHAZ', 'TGFBR1', 'CSF1R']
    _SPECIES_LABELS = {'ATM': 'ATM', 'SRC': 'SRC', 'BAD': 'BAD', 'PTEN': 'PTEN', 'SHC1': 'SHC1', 'PKN1': 'PKN1'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'kd_tgfbr1_level': ('kd_tgfbr1', 0.45, 'native SBML value', 'Kd tgfbr1 source parameter. Maps to bundled SBML parameter `kd_tgfbr1`.'), 'k_tgfbr1_level': ('k_tgfbr1', 0.5, 'native SBML value', 'K tgfbr1 source parameter. Maps to bundled SBML parameter `k_tgfbr1`.'), 'initial_atm': ('ATM', 1.0, 'native SBML value', 'Initial ATM. Sets the initial value of bundled SBML symbol `ATM`.'), 'initial_src': ('SRC', 1.0, 'native SBML value', 'Initial SRC. Sets the initial value of bundled SBML symbol `SRC`.'), 'initial_bad': ('BAD', 1.0, 'native SBML value', 'Initial BAD. Sets the initial value of bundled SBML symbol `BAD`.'), 'initial_pten': ('PTEN', 1.0, 'native SBML value', 'Initial PTEN. Sets the initial value of bundled SBML symbol `PTEN`.')}
    _HEADLINE_OUTPUTS = {'atm': ('ATM', 'native SBML value', 'ATM observable. Maps to SBML symbol `ATM`.'), 'src': ('SRC', 'native SBML value', 'SRC observable. Maps to SBML symbol `SRC`.'), 'bad': ('BAD', 'native SBML value', 'BAD observable. Maps to SBML symbol `BAD`.'), 'pten': ('PTEN', 'native SBML value', 'PTEN observable. Maps to SBML symbol `PTEN`.'), 'shc1': ('SHC1', 'native SBML value', 'SHC1 observable. Maps to SBML symbol `SHC1`.'), 'pkn1': ('PKN1', 'native SBML value', 'PKN1 observable. Maps to SBML symbol `PKN1`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000940.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
