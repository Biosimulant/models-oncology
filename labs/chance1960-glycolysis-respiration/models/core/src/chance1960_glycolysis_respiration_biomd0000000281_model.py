# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Chance1960_Glycolysis_Respiration."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Chance1960GlycolysisRespirationBiomd0000000281Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled SBML source file."""

    _SBML_ID = 'BIOMD0000000281'
    _TITLE = 'Chance1960_Glycolysis_Respiration'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['GLU', 'ENZ', 'ENG', 'TP1', 'ADP', 'GLP', 'ETZ', 'ETG', 'GPP', 'GAP', 'DHA', 'DPN', 'DPH', 'PID', 'DGA', 'PGA', 'PYR', 'LAC', 'DIN', 'DIH', 'XI', 'XSI', 'OXY', 'XSP', 'TP2', 'DBP', 'PUE', 'PPP', 'AGP', 'MOD', 'MOB', 'MOX']
    _SPECIES_LABELS = {'LAC': '(LAC) lactate', 'PUE': '(PUE) enzyme concerned in ATP utilization', 'PPP': '(PPP) enzyme intermediate concerned in ATP utilization', 'GLU': '(GLU) glucose', 'ENG': '(ENG) hexokinase glucose intermediate', 'GLP': '(GLP) glucose 6 phosphate'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_lac_lactate': ('LAC', 0.001, 'native SBML value', 'Initial (LAC) lactate. Sets the initial value of bundled SBML symbol `LAC`.'), 'initial_pue_enzyme_concerned_in_atp_utilization': ('PUE', 2e-06, 'native SBML value', 'Initial (PUE) enzyme concerned in ATP utilization. Sets the initial value of bundled SBML symbol `PUE`.'), 'initial_ppp_enzyme_intermediate_concerned_in_atp_utilization': ('PPP', 1e-06, 'native SBML value', 'Initial (PPP) enzyme intermediate concerned in ATP utilization. Sets the initial value of bundled SBML symbol `PPP`.'), 'initial_glu_glucose': ('GLU', 0.0, 'native SBML value', 'Initial (GLU) glucose. Sets the initial value of bundled SBML symbol `GLU`.'), 'initial_eng_hexokinase_glucose_intermediate': ('ENG', 0.0, 'native SBML value', 'Initial (ENG) hexokinase glucose intermediate. Sets the initial value of bundled SBML symbol `ENG`.'), 'initial_glp_glucose_6_phosphate': ('GLP', 0.0, 'native SBML value', 'Initial (GLP) glucose 6 phosphate. Sets the initial value of bundled SBML symbol `GLP`.')}
    _HEADLINE_OUTPUTS = {'lac_lactate': ('LAC', 'native SBML value', '(LAC) lactate observable. Maps to SBML symbol `LAC`.'), 'pue_enzyme_concerned_in_atp_utilization': ('PUE', 'native SBML value', '(PUE) enzyme concerned in ATP utilization observable. Maps to SBML symbol `PUE`.'), 'ppp_enzyme_intermediate_concerned_in_atp_utilization': ('PPP', 'native SBML value', '(PPP) enzyme intermediate concerned in ATP utilization observable. Maps to SBML symbol `PPP`.'), 'glu_glucose': ('GLU', 'native SBML value', '(GLU) glucose observable. Maps to SBML symbol `GLU`.'), 'eng_hexokinase_glucose_intermediate': ('ENG', 'native SBML value', '(ENG) hexokinase glucose intermediate observable. Maps to SBML symbol `ENG`.'), 'glp_glucose_6_phosphate': ('GLP', 'native SBML value', '(GLP) glucose 6 phosphate observable. Maps to SBML symbol `GLP`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000281.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
