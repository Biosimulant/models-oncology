# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Oncology visualisation module for cleaned SBML labs."""

from __future__ import annotations

from typing import Any, Mapping, Optional

from biosim import BioModule
from biosim.signals import BioSignal, SignalSpec


SUMMARY_SCHEMA = {
    "duration_simulated": "float",
    "observable_count": "int",
    "largest_change_observable": "str",
    "largest_change_magnitude": "float",
    "peak_observable": "str",
    "peak_value": "float",
}


class OncologyVisualisationModel(BioModule):
    def __init__(
        self,
        *,
        lab_title: str,
        question: str,
        answer_focus: str,
        visual_scope: str,
        caveat: str,
        sources: list[dict[str, Any]],
        integration_step: float = 1.0,
    ) -> None:
        self.lab_title = lab_title
        self.question = question
        self.answer_focus = answer_focus
        self.visual_scope = visual_scope
        self.caveat = caveat
        self.sources = list(sources)
        self.integration_step = float(integration_step)
        self._inputs: dict[str, BioSignal] = {}
        self._history: dict[str, list[dict[str, float]]] = {}
        self._summaries: dict[str, Mapping[str, Any]] = {}
        self._labels: dict[str, dict[str, str]] = {}

    def inputs(self) -> dict[str, SignalSpec]:
        specs: dict[str, SignalSpec] = {}
        for source in self.sources:
            alias = str(source["alias"])
            observable_ids = [str(item["id"]) for item in source.get("observables", [])]
            state_ids = [str(item) for item in source.get("state_observables", [])] or observable_ids
            specs[f"{alias}_state"] = SignalSpec.record(schema={name: "float" for name in state_ids} or {"payload": "json"})
            specs[f"{alias}_summary"] = SignalSpec.record(schema=SUMMARY_SCHEMA)
            specs[f"{alias}_species_labels"] = SignalSpec.record(schema={name: "str" for name in observable_ids} or {"payload": "json"})
        return specs

    def outputs(self) -> dict[str, SignalSpec]:
        return {}

    def setup(self, config: Optional[dict[str, Any]] = None) -> None:
        self._history = {str(source["alias"]): [] for source in self.sources}
        self._summaries = {}
        self._labels = {}

    def set_inputs(self, inputs: dict[str, BioSignal]) -> None:
        self._inputs = dict(inputs or {})

    def advance_window(self, start: float, end: float) -> None:
        for source in self.sources:
            alias = str(source["alias"])
            state = self._payload(self._inputs.get(f"{alias}_state"))
            summary = self._payload(self._inputs.get(f"{alias}_summary"))
            labels = self._payload(self._inputs.get(f"{alias}_species_labels"))
            if isinstance(summary, Mapping):
                self._summaries[alias] = dict(summary)
            if isinstance(labels, Mapping):
                self._labels[alias] = {str(k): str(v) for k, v in labels.items()}
            if isinstance(state, Mapping):
                row = {"t": float(end)}
                for item in source.get("observables", []):
                    raw_id = str(item["id"])
                    value = state.get(raw_id)
                    if isinstance(value, (int, float)):
                        row[raw_id] = float(value)
                if len(row) > 1:
                    self._history.setdefault(alias, []).append(row)

    def get_outputs(self) -> dict[str, BioSignal]:
        return {}

    def visualize(self) -> Optional[list[dict[str, Any]]]:
        visuals: list[dict[str, Any]] = []
        for source in self.sources:
            alias = str(source["alias"])
            rows = self._history.get(alias, [])
            summary = self._summaries.get(alias, {})
            observables = list(source.get("observables", []))
            visuals.append(self._qa_visual(alias, rows, summary, observables))
            timeseries = self._timeseries_visual(alias, rows, observables)
            if timeseries is not None:
                visuals.append(timeseries)
            bars = self._bar_visual(alias, rows, observables)
            if bars is not None:
                visuals.append(bars)
        return [item for item in visuals if self._has_renderable_data(item)] or None

    def _payload(self, signal: BioSignal | None) -> Any:
        if signal is None:
            return None
        value = getattr(signal, "value", signal)
        if isinstance(value, Mapping) and set(value) == {"payload"}:
            return value["payload"]
        return value

    def _label(self, item: Mapping[str, Any]) -> str:
        return str(item.get("label") or item.get("id") or "Observable")

    def _qa_visual(
        self,
        alias: str,
        rows: list[dict[str, float]],
        summary: Mapping[str, Any],
        observables: list[Mapping[str, Any]],
    ) -> dict[str, Any]:
        largest = summary.get("largest_change_observable") or "no dominant change detected"
        magnitude = summary.get("largest_change_magnitude")
        peak = summary.get("peak_observable") or "no peak detected"
        observed = f"Largest change: {largest}"
        if isinstance(magnitude, (int, float)):
            observed += f" ({float(magnitude):.4g} native units)"
        evidence = f"Peak observable: {peak}; tracked {len(observables)} selected source observables across {len(rows)} captured windows."
        if not rows:
            evidence = "No dynamic window was captured; use the core state and summary outputs as baseline evidence."
        return {
            "render": "table",
            "description": "Direct scientific answer for this oncology lab run.",
            "data": {
                "title": f"{self.lab_title} - run interpretation",
                "columns": ["Prompt", "Answer"],
                "rows": [
                    ["Scientific question", self.question],
                    ["Observed answer", observed],
                    ["Evidence", evidence],
                    ["Dominant module", self.visual_scope],
                    ["Caveat", self.caveat],
                ],
            },
        }

    def _timeseries_visual(
        self,
        alias: str,
        rows: list[dict[str, float]],
        observables: list[Mapping[str, Any]],
    ) -> dict[str, Any] | None:
        if not rows:
            return None
        series = []
        for item in observables:
            raw_id = str(item["id"])
            points = [[row["t"], row[raw_id]] for row in rows if raw_id in row]
            if points:
                series.append({"name": self._label(item), "points": points})
        if not series:
            return None
        return {
            "render": "timeseries",
            "description": self.visual_scope,
            "data": {
                "title": f"{self.lab_title} - selected oncology states",
                "x_label": "Model time",
                "y_label": "Native SBML value",
                "series": series,
            },
        }

    def _bar_visual(
        self,
        alias: str,
        rows: list[dict[str, float]],
        observables: list[Mapping[str, Any]],
    ) -> dict[str, Any] | None:
        if not rows:
            return None
        latest = rows[-1]
        items = []
        for item in observables:
            raw_id = str(item["id"])
            value = latest.get(raw_id)
            if isinstance(value, (int, float)):
                items.append({"label": self._label(item), "value": float(value)})
        if not items:
            return None
        return {
            "render": "bar",
            "description": "Latest selected source-state values.",
            "data": {
                "title": f"{self.lab_title} - latest selected values",
                "x_label": "Observable",
                "y_label": "Native SBML value",
                "items": items,
            },
        }

    def _has_renderable_data(self, visual: Mapping[str, Any]) -> bool:
        data = visual.get("data")
        if not isinstance(data, Mapping):
            return False
        render = visual.get("render")
        if render == "table":
            return bool(data.get("rows"))
        if render == "timeseries":
            return bool(data.get("series"))
        if render == "bar":
            return bool(data.get("items"))
        if render == "scatter":
            return bool(data.get("points"))
        return False
