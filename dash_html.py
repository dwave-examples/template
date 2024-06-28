# Copyright 2024 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This file stores the HTML layout for the app."""
from __future__ import annotations

from dash import dcc, html

from app_configs import (
    CHECKLIST,
    DESCRIPTION,
    DROPDOWN,
    MAIN_HEADER,
    SLIDER,
    SOLVER_TIME,
    THEME_COLOR_SECONDARY,
    THUMBNAIL,
)
from solver.solver import SamplerType


SAMPLER_TYPES = {SamplerType.NL: "Quantum Hybrid (NL)", SamplerType.CLASSIC: "Classical"}


def description_card():
    """A Div containing dashboard title & descriptions."""
    return html.Div(
        id="description-card",
        children=[html.H1(MAIN_HEADER), html.P(DESCRIPTION)],
    )


def slider(label: str, id: str, config: dict) -> html.Div:
    """Slider element for value selection."""
    return html.Div(
        children=[
            html.Label(label),
            dcc.Slider(
                id=id,
                className="slider",
                **config,
                marks={
                    config["min"]: str(config["min"]),
                    config["max"]: str(config["max"]),
                },
                tooltip={
                    "placement": "bottom",
                    "always_visible": True,
                },
            ),
        ],
    )


def dropdown(label: str, id: str, options: list) -> html.Div:
    """Slider element for value selection."""
    return html.Div(
        children=[
            html.Label(label),
            dcc.Dropdown(
                id=id,
                options=options,
                value=options[0]["value"],
                clearable=False,
                searchable=False,
            ),
        ],
    )


def checklist(label: str, id: str, options: list, value: list) -> html.Div:
    """Checklist element for value selection."""
    return html.Div(
        children=[
            html.Label(label),
            dcc.Checklist(
                id=id,
                options=options,
                value=value,
            ),
        ],
    )


def generate_control_card() -> html.Div:
    """
    This function generates the control card for the dashboard, which
    contains the dropdowns for selecting the scenario, model, and solver.

    Returns:
        html.Div: A Div containing the dropdowns for selecting the scenario,
        model, and solver.
    """
    # calculate dropdown options
    dropdown_options = [
        {"label": label, "value": i}
        for i, label in enumerate(DROPDOWN)
    ]
    # calculate checklist options
    checklist_options = [
        {"label": label, "value": i}
        for i, label in enumerate(CHECKLIST)
    ]

    sampler_options = [
        {"label": label, "value": sampler_type.value}
        for sampler_type, label in SAMPLER_TYPES.items()
    ]

    return html.Div(
        id="control-card",
        children=[
            slider(
                "Example Slider",
                "slider-id",
                SLIDER,
            ),
            dropdown(
                "Example Dropdown",
                "dropdown-id",
                sorted(dropdown_options, key=lambda op: op["value"]),
            ),
            checklist(
                "Example Checklist",
                "checklist-id",
                sorted(checklist_options, key=lambda op: op["value"]),
                [0],
            ),
            dropdown(
                "Solver",
                "sampler-type-select",
                sorted(sampler_options, key=lambda op: op["value"]),
            ),
            html.Label("Solver Time Limit (seconds)"),
            dcc.Input(
                id="solver-time-limit",
                type="number",
                **SOLVER_TIME,
            ),
            html.Div(
                id="button-group",
                children=[
                    html.Button(
                        id="run-button", children="Run Optimization", n_clicks=0, disabled=False
                    ),
                    html.Button(
                        id="cancel-button",
                        children="Cancel Optimization",
                        n_clicks=0,
                        className="display-none",
                    ),
                ],
            ),
        ],
    )


def set_html(app):
    """Set the application HTML."""
    app.layout = html.Div(
        id="app-container",
        children=[
            # Banner
            html.Div(id="banner", children=[html.Img(src=THUMBNAIL)]),
            html.Div(
                id="columns",
                children=[
                    # Left column
                    html.Div(
                        id={"type": "to-collapse-class", "index": 0},
                        className="left-column",
                        children=[
                            html.Div(
                                [  # Fixed width Div to collapse
                                    html.Div(
                                        [  # Padding and content wrapper
                                            description_card(),
                                            generate_control_card(),
                                        ]
                                    )
                                ]
                            ),
                            html.Div(
                                html.Button(
                                    id={"type": "collapse-trigger", "index": 0},
                                    className="left-column-collapse",
                                    children=[html.Div(className="collapse-arrow")],
                                ),
                            ),
                        ],
                    ),
                    # Right column
                    html.Div(
                        id="right-column",
                        children=[
                            dcc.Tabs(
                                id="tabs",
                                value="input-tab",
                                mobile_breakpoint=0,
                                children=[
                                    dcc.Tab(
                                        label="Input",
                                        id="input-tab",
                                        value="input-tab",  # used for switching to programatically
                                        className="tab",
                                        children=[
                                            dcc.Loading(
                                                id="loading",
                                                type="circle",
                                                color=THEME_COLOR_SECONDARY,
                                                children="Problem set up here",
                                            ),
                                        ],
                                    ),
                                    dcc.Tab(
                                        label="Results",
                                        id="results-tab",
                                        className="tab",
                                        disabled=True,
                                        children=[
                                            html.Div(
                                                className="tab-content--results",
                                                children=[
                                                    html.Div(
                                                        "Results go here"
                                                    ),
                                                    html.Div(
                                                        [
                                                            html.Hr(),
                                                            html.Div(
                                                                id={
                                                                    "type": "to-collapse-class",
                                                                    "index": 1,
                                                                },
                                                                className="details-collapse-wrapper collapsed",
                                                                children=[
                                                                    html.Button(
                                                                        id={
                                                                            "type": "collapse-trigger",
                                                                            "index": 1,
                                                                        },
                                                                        className="details-collapse",
                                                                        children=[
                                                                            html.H5(
                                                                                "Problem Details"
                                                                            ),
                                                                            html.Div(
                                                                                className="collapse-arrow"
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    html.Div(
                                                                        className="details-to-collapse",
                                                                        children=[
                                                                            html.Table(
                                                                                id="solution-stats-table",
                                                                                children=[
                                                                                    html.Thead(
                                                                                        [
                                                                                            html.Tr(
                                                                                                [
                                                                                                    html.Th(
                                                                                                        colSpan=2,
                                                                                                        children=[
                                                                                                            "Problem Specifics"
                                                                                                        ],
                                                                                                    ),
                                                                                                    html.Th(
                                                                                                        colSpan=2,
                                                                                                        children=[
                                                                                                            "Wall Clock Time"
                                                                                                        ],
                                                                                                    ),
                                                                                                ]
                                                                                            )
                                                                                        ]
                                                                                    ),
                                                                                    html.Tbody(
                                                                                        id="problem-details",
                                                                                        children=[
                                                                                            html.Tr(
                                                                                                [
                                                                                                    html.Td(
                                                                                                        "Locations"
                                                                                                    ),
                                                                                                    html.Td(
                                                                                                        id="num-locations"
                                                                                                    ),
                                                                                                    html.Td(
                                                                                                        "Quantum Hybrid"
                                                                                                    ),
                                                                                                    html.Td(
                                                                                                        id="wall-clock-time-quantum"
                                                                                                    ),
                                                                                                ]
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                            ),
                                                        ]
                                                    ),
                                                ],
                                            )
                                        ],
                                    ),
                                ],
                            )
                        ],
                    ),
                ],
            ),
        ],
    )
