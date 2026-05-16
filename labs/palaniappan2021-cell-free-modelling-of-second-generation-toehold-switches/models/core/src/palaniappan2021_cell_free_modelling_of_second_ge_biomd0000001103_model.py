# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Palaniappan2021 - Cell free modelling of second generation Toehold switches."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Palaniappan2021CellFreeModellingOfSecondGeBiomd0000001103Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000001103'
    _TITLE = 'Palaniappan2021 - Cell free modelling of second generation Toehold switches'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['miR', 'antimiR', 'Toehold_DNA', 'Toehold_RNA_CTS', 'miR_antimiR', 'GFP', 'Toehold_RNA_OTS', 'Mat_GFP']
    _SPECIES_LABELS = {'miR': 'MiR', 'antimiR': 'AntimiR', 'Toehold_DNA': 'Toehold DNA', 'GFP': 'GFP', 'Toehold_RNA_CTS': 'Toehold RNA CTS', 'miR_antimiR': 'MiR antimiR'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_mi_r': ('miR', 1.2e-07, 'native SBML value', 'Initial MiR. Sets the initial value of bundled SBML symbol `miR`.'), 'initial_antimi_r': ('antimiR', 1.2e-07, 'native SBML value', 'Initial AntimiR. Sets the initial value of bundled SBML symbol `antimiR`.'), 'initial_toehold_dna': ('Toehold_DNA', 2.35e-07, 'native SBML value', 'Initial Toehold DNA. Sets the initial value of bundled SBML symbol `Toehold_DNA`.'), 'initial_gfp': ('GFP', 0.0, 'native SBML value', 'Initial GFP. Sets the initial value of bundled SBML symbol `GFP`.'), 'initial_toehold_rna_cts': ('Toehold_RNA_CTS', 0.0, 'native SBML value', 'Initial Toehold RNA CTS. Sets the initial value of bundled SBML symbol `Toehold_RNA_CTS`.'), 'initial_mi_r_antimi_r': ('miR_antimiR', 0.0, 'native SBML value', 'Initial MiR antimiR. Sets the initial value of bundled SBML symbol `miR_antimiR`.')}
    _HEADLINE_OUTPUTS = {'mi_r': ('miR', 'native SBML value', 'MiR observable. Maps to SBML symbol `miR`.'), 'antimi_r': ('antimiR', 'native SBML value', 'AntimiR observable. Maps to SBML symbol `antimiR`.'), 'toehold_dna': ('Toehold_DNA', 'native SBML value', 'Toehold DNA observable. Maps to SBML symbol `Toehold_DNA`.'), 'gfp': ('GFP', 'native SBML value', 'GFP observable. Maps to SBML symbol `GFP`.'), 'toehold_rna_cts': ('Toehold_RNA_CTS', 'native SBML value', 'Toehold RNA CTS observable. Maps to SBML symbol `Toehold_RNA_CTS`.'), 'mi_r_antimi_r': ('miR_antimiR', 'native SBML value', 'MiR antimiR observable. Maps to SBML symbol `miR_antimiR`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000001103.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
