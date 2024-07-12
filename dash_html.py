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
    RADIO,
    SLIDER,
    SOLVER_TIME,
    THEME_COLOR_SECONDARY,
    THUMBNAIL,
)
from src.enums import SamplerType


SAMPLER_TYPES = {SamplerType.HYBRID: "Quantum Hybrid", SamplerType.CLASSICAL: "Classical"}


def description_card():
    """A Div containing dashboard title & descriptions."""
    return html.Div(
        className="description-card",
        children=[html.H1(MAIN_HEADER), html.P(DESCRIPTION)],
    )


def slider(label: str, id: str, config: dict) -> html.Div:
    """Slider element for value selection."""
    return html.Div(
        className="slider-wrapper",
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
        className="dropdown-wrapper",
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


def checklist(label: str, id: str, options: list, value: list, inline: bool = True) -> html.Div:
    """Checklist element for value selection."""
    return html.Div(
        className="checklist-wrapper",
        children=[
            html.Label(label),
            dcc.Checklist(
                id=id,
                className=f"checklist{' checklist--inline' if inline else ''}",
                inline=inline,
                options=options,
                value=value,
            ),
        ],
    )


def radio(label: str, id: str, options: list, value: int, inline: bool = True) -> html.Div:
    """Radio element for value selection."""
    return html.Div(
        className="radio-wrapper",
        children=[
            html.Label(label),
            dcc.RadioItems(
                id=id,
                className=f"radio{' radio--inline' if inline else ''}",
                inline=inline,
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

    # calculate radio options
    radio_options = [
        {"label": label, "value": i}
        for i, label in enumerate(RADIO)
    ]

    sampler_options = [
        {"label": label, "value": sampler_type.value}
        for sampler_type, label in SAMPLER_TYPES.items()
    ]

    return html.Div(
        id="control-card",
        children=[
            html.Div(
                className="settings",
                children=[
                    slider(
                        "Example Slider",
                        "slider",
                        SLIDER,
                    ),
                    dropdown(
                        "Example Dropdown",
                        "dropdown",
                        sorted(dropdown_options, key=lambda op: op["value"]),
                    ),
                    checklist(
                        "Example Checklist",
                        "checklist",
                        sorted(checklist_options, key=lambda op: op["value"]),
                        [0],
                    ),
                    radio(
                        "Example Radio",
                        "radio",
                        sorted(radio_options, key=lambda op: op["value"]),
                        0,
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
                ]
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


def generate_problem_details_table(
    solver: str,
    time_limit: int,
    total_time: float,
    variable_1: int, 
    variable_2: int,
) -> list[html.Tr]:
    """Generate the problem details table.

    Args:
        solver: The solver used for optimization.
        time_limit: The solver time limit.
        total_time: The overall time to optimize the scenario.
        variable_1: Variable 1.
        variable_2: Variable 2.

    Returns:
        list[html.Tr]: List of table rows for problem details.
    """

    table_rows = (
        ("Variable 1", variable_1, "Solver", solver),
        ("Variable 2", variable_2, "Time Limit", f"{time_limit}s"),
        ("Problem Size", variable_1 * variable_2, "Total Time", f"{round(total_time, 2)}s"),
        ("Search Space", f"{variable_1**variable_2:.2e}"),
    )

    return [html.Tr([html.Td(cell) for cell in row]) for row in table_rows]


def problem_details(index: int) -> html.Div:
    """Generate the problem details section.

    Args:
        index: Unique element id to differentiate matching elements.

    Returns:
        html.Div: Div containing a collapsable table.
    """
    return html.Div(
        id={"type": "to-collapse-class", "index": index},
        className="details-collapse-wrapper collapsed",
        children=[
            html.Button(
                id={"type": "collapse-trigger", "index": index},
                className="details-collapse",
                children=[
                    html.H5("Problem Details"),
                    html.Div(className="collapse-arrow"),
                ],
            ),
            html.Div(
                className="details-to-collapse",
                children=[
                    html.Table(
                        className="solution-stats-table",
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
                                                    "Run Time Specifics"
                                                ],
                                            ),
                                        ]
                                    )
                                ]
                            ),
                            html.Tbody(id="problem-details")
                        ]
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
            # Below are any temporary storage items, e.g., for sharing data between callbacks.
            dcc.Store(id="sampler-type"),  # solver type used for latest run
            dcc.Store(
                id="reset-results"
            ),  # whether to reset the results tables before displaying the latest run
            dcc.Store(
                id="run-in-progress", data=False
            ),  # callback blocker to signal that the run is complete
            dcc.Store(id="parameter-hash"),  # hash string to detect changed parameters
            # Header brand banner
            html.Div(className="banner", children=[html.Img(src=THUMBNAIL)]),
            # Settings and results columns
            html.Div(
                className="columns-main",
                children=[
                    # Left column
                    html.Div(
                        id={"type": "to-collapse-class", "index": 0},
                        className="left-column",
                        children=[
                            html.Div(
                                className="left-column-layer-1",
                                children=[  # Fixed width Div to collapse
                                    html.Div(
                                        className="left-column-layer-2",
                                        children=[  # Padding and content wrapper
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
                        className="right-column",
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
                                                parent_className="input",
                                                type="circle",
                                                color=THEME_COLOR_SECONDARY,
                                                children=html.Div(id="input"),
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
                                                    dcc.Loading(
                                                        parent_className="results",
                                                        type="circle",
                                                        color=THEME_COLOR_SECONDARY,
                                                        children=html.Div(id="results"),
                                                    ),
                                                    html.Div(
                                                        [
                                                            html.Hr(),
                                                            problem_details(1)
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
