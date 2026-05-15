# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Dorvash2019 - Dynamic modeling of signal transduction by mTOR complexes in cancer."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Dorvash2019DynamicModelingOfSignalTransductBiomd0000000822Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000822'
    _TITLE = 'Dorvash2019 - Dynamic modeling of signal transduction by mTOR complexes in cancer'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Cytosolic_Rapamycin', 'mTOR', 'Raptor', 'Rictor', 'mTORC1', 'mTORC2', 'mTOR_Rapamycin', 'mTORC1_Rapamycin']
    _SPECIES_LABELS = {'mTOR': 'MTOR', 'Raptor': 'Raptor', 'Rictor': 'Rictor', 'Cytosolic_Rapamycin': 'Cytosolic Rapamycin', 'mTORC1': 'MTORC1', 'mTORC2': 'MTORC2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'rapamycin_dose': ('Rapamycin_Dose', 0.0, 'native SBML value', 'Rapamycin Dose source parameter. Maps to bundled SBML parameter `Rapamycin_Dose`.'), 'initial_mtor': ('mTOR', 3.756228e-07, 'native SBML value', 'Initial MTOR. Sets the initial value of bundled SBML symbol `mTOR`.'), 'initial_raptor': ('Raptor', 3.201594e-07, 'native SBML value', 'Initial Raptor. Sets the initial value of bundled SBML symbol `Raptor`.'), 'initial_rictor': ('Rictor', 8.834274e-08, 'native SBML value', 'Initial Rictor. Sets the initial value of bundled SBML symbol `Rictor`.'), 'initial_cytosolic_rapamycin': ('Cytosolic_Rapamycin', 0.0, 'native SBML value', 'Initial Cytosolic Rapamycin. Sets the initial value of bundled SBML symbol `Cytosolic_Rapamycin`.'), 'initial_mtorc1': ('mTORC1', 0.0, 'native SBML value', 'Initial MTORC1. Sets the initial value of bundled SBML symbol `mTORC1`.')}
    _HEADLINE_OUTPUTS = {'mtor': ('mTOR', 'native SBML value', 'MTOR observable. Maps to SBML symbol `mTOR`.'), 'raptor': ('Raptor', 'native SBML value', 'Raptor observable. Maps to SBML symbol `Raptor`.'), 'rictor': ('Rictor', 'native SBML value', 'Rictor observable. Maps to SBML symbol `Rictor`.'), 'cytosolic_rapamycin': ('Cytosolic_Rapamycin', 'native SBML value', 'Cytosolic Rapamycin observable. Maps to SBML symbol `Cytosolic_Rapamycin`.'), 'mtorc1': ('mTORC1', 'native SBML value', 'MTORC1 observable. Maps to SBML symbol `mTORC1`.'), 'mtorc2': ('mTORC2', 'native SBML value', 'MTORC2 observable. Maps to SBML symbol `mTORC2`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000822.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
