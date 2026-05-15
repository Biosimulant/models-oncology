# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Lopes2025 - NFkB model in Breast Cancer."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Lopes2025NfkbModelInBreastCancerModel2508260001Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'MODEL2508260001'
    _TITLE = 'Lopes2025 - NFkB model in Breast Cancer'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['NFkB', 'SLUG', 'TWIST1', 'N0TWIST1', 'SIP1', 'N0SIP1', 'N0SLUG', 'p65', 'p50', 'RNAp50', 'RNAp65', 'RNASLUG', 'RNASIP1', 'RNATWIST1', 'N0p50', 'N0p65', 'N1p50', 'N1p65', 'N1SIP1', 'N1SLUG', 'N1TWIST1']
    _SPECIES_LABELS = {'NFkB': 'NF-kB', 'SLUG': 'SLUG', 'SIP1': 'SIP1', 'p65': 'P65', 'p50': 'P50', 'TWIST1': 'TWIST1'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_nf_kb': ('NFkB', 5893.41991828698, 'native SBML value', 'Initial NF-kB. Sets the initial value of bundled SBML symbol `NFkB`.'), 'initial_slug': ('SLUG', 7789508.97608121, 'native SBML value', 'Initial SLUG. Sets the initial value of bundled SBML symbol `SLUG`.'), 'initial_sip1': ('SIP1', 23581097.7152633, 'native SBML value', 'Initial SIP1. Sets the initial value of bundled SBML symbol `SIP1`.'), 'initial_twist1': ('TWIST1', 200834985.025365, 'native SBML value', 'Initial TWIST1. Sets the initial value of bundled SBML symbol `TWIST1`.')}
    _HEADLINE_OUTPUTS = {'nf_kb': ('NFkB', 'native SBML value', 'NF-kB observable. Maps to SBML symbol `NFkB`.'), 'slug': ('SLUG', 'native SBML value', 'SLUG observable. Maps to SBML symbol `SLUG`.'), 'sip1': ('SIP1', 'native SBML value', 'SIP1 observable. Maps to SBML symbol `SIP1`.'), 'p65': ('p65', 'native SBML value', 'P65 observable. Maps to SBML symbol `p65`.'), 'p50': ('p50', 'native SBML value', 'P50 observable. Maps to SBML symbol `p50`.'), 'twist1': ('TWIST1', 'native SBML value', 'TWIST1 observable. Maps to SBML symbol `TWIST1`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2508260001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
