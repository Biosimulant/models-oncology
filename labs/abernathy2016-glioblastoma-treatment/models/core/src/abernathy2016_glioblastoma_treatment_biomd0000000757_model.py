# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Abernathy2016 - glioblastoma treatment."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Abernathy2016GlioblastomaTreatmentBiomd0000000757Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000757'
    _TITLE = 'Abernathy2016 - glioblastoma treatment'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Tumor', 'CancerStemCell', 'CytotoxicTcell', 'TGFb', 'IFNy', 'MHC1', 'MHC2']
    _SPECIES_LABELS = {'Tumor': 'Tumor', 'CancerStemCell': 'CancerStemCell', 'CytotoxicTcell': 'CytotoxicTcell', 'TGFb': 'TGFb', 'IFNy': 'IFNy', 'MHC1': 'MHC1'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_tumor': ('Tumor', 70.0, 'native SBML value', 'Initial Tumor. Sets the initial value of bundled SBML symbol `Tumor`.'), 'initial_cancerstemcell': ('CancerStemCell', 30.0, 'native SBML value', 'Initial CancerStemCell. Sets the initial value of bundled SBML symbol `CancerStemCell`.'), 'initial_cytotoxictcell': ('CytotoxicTcell', 250.0, 'native SBML value', 'Initial CytotoxicTcell. Sets the initial value of bundled SBML symbol `CytotoxicTcell`.'), 'initial_tgfb': ('TGFb', 50.0, 'native SBML value', 'Initial TGFb. Sets the initial value of bundled SBML symbol `TGFb`.'), 'initial_ifny': ('IFNy', 50.0, 'native SBML value', 'Initial IFNy. Sets the initial value of bundled SBML symbol `IFNy`.'), 'initial_mhc1': ('MHC1', 50.0, 'native SBML value', 'Initial MHC1. Sets the initial value of bundled SBML symbol `MHC1`.')}
    _HEADLINE_OUTPUTS = {'tumor': ('Tumor', 'native SBML value', 'Tumor observable. Maps to SBML symbol `Tumor`.'), 'cancerstemcell': ('CancerStemCell', 'native SBML value', 'CancerStemCell observable. Maps to SBML symbol `CancerStemCell`.'), 'cytotoxictcell': ('CytotoxicTcell', 'native SBML value', 'CytotoxicTcell observable. Maps to SBML symbol `CytotoxicTcell`.'), 'tgfb': ('TGFb', 'native SBML value', 'TGFb observable. Maps to SBML symbol `TGFb`.'), 'ifny': ('IFNy', 'native SBML value', 'IFNy observable. Maps to SBML symbol `IFNy`.'), 'mhc1': ('MHC1', 'native SBML value', 'MHC1 observable. Maps to SBML symbol `MHC1`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000757.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
