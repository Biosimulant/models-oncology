# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Hutchinson2016 - Vascular phenotype identification and anti-angiogenic treatment recommendation."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Hutchinson2016VascularPhenotypeIdentificationModel1911130007Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'MODEL1911130007'
    _TITLE = 'Hutchinson2016 - Vascular phenotype identification and anti-angiogenic treatment recommendation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['v', 'rv', 'bv', 'a1', 'aw', 'a2', 'ra', 'ba1', 'ba2', 'p', 'rp', 'bp', 'Ei', 'Em', 'P', 'EP']
    _SPECIES_LABELS = {'v': 'V', 'rv': 'Rv', 'bv': 'Bv', 'a1': 'A1', 'aw': 'Aw', 'a2': 'A2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'epsilon_source_parameter': ('epsilon', 0.04, 'native SBML value', 'Epsilon source parameter. Maps to bundled SBML parameter `epsilon`.')}
    _HEADLINE_OUTPUTS = {'v': ('v', 'native SBML value', 'V observable. Maps to SBML symbol `v`.'), 'rv': ('rv', 'native SBML value', 'Rv observable. Maps to SBML symbol `rv`.'), 'bv': ('bv', 'native SBML value', 'Bv observable. Maps to SBML symbol `bv`.'), 'a1': ('a1', 'native SBML value', 'A1 observable. Maps to SBML symbol `a1`.'), 'aw': ('aw', 'native SBML value', 'Aw observable. Maps to SBML symbol `aw`.'), 'a2': ('a2', 'native SBML value', 'A2 observable. Maps to SBML symbol `a2`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1911130007.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
