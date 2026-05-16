# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Andersen2017 - Mathematical modelling as a proof of concept for MPNs as a human inflammation model for cancer development."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Andersen2017MathematicalModellingAsAProofOBiomd0000000852Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000852'
    _TITLE = 'Andersen2017 - Mathematical modelling as a proof of concept for MPNs as a human inflammation model for cancer development'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['x0', 'x1', 'y0', 'y1', 'a', 's']
    _SPECIES_LABELS = {'x0': 'X0', 'x1': 'X1', 'a': 'A', 's': 'S', 'y0': 'Y0', 'y1': 'Y1'}
    _PARAMETER_INPUTS = {'inflammation_level': ('inflammation', 7.0, 'native SBML value', 'Inflammation Level. Overrides bundled SBML parameter `inflammation`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'x0': ('x0', 'native SBML value', 'X0 observable. Maps to SBML symbol `x0`.'), 'x1': ('x1', 'native SBML value', 'X1 observable. Maps to SBML symbol `x1`.'), 'a': ('a', 'native SBML value', 'A observable. Maps to SBML symbol `a`.'), 's': ('s', 'native SBML value', 'S observable. Maps to SBML symbol `s`.'), 'y0': ('y0', 'native SBML value', 'Y0 observable. Maps to SBML symbol `y0`.'), 'y1': ('y1', 'native SBML value', 'Y1 observable. Maps to SBML symbol `y1`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000852.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
