# Copyright [yyyy] [name of copyright owner]
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

"""
Instructions:
 - Fill in [yyyy] and [name of copyright owner] in the copyright (top line)
 - Add demo code below
 - Format code so that it conforms with PEP 8
"""

from __future__ import annotations

from collections import defaultdict
from operator import itemgetter
from pathlib import Path
from typing import NamedTuple, Union

import dash
import diskcache
from dash import MATCH, DiskcacheManager, callback_context, ctx
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from app_configs import APP_TITLE, DEBUG, THEME_COLOR, THEME_COLOR_SECONDARY
from dash_html import SAMPLER_TYPES, set_html

from solver.solver import ProblemParameters, SamplerType, Solver

cache = diskcache.Cache("./cache")
background_callback_manager = DiskcacheManager(cache)

# Fix Dash long callbacks crashing on macOS 10.13+ (also potentially not working
# on other POSIX systems), caused by https://bugs.python.org/issue33725
# (aka "beware of multithreaded process forking").
#
# Note: default start method has already been changed to "spawn" on darwin in
# the `multiprocessing` library, but its fork, `multiprocess` still hasn't caught up.
# (see docs: https://docs.python.org/3/library/multiprocessing.html#contexts-and-start-methods)
import multiprocess
if multiprocess.get_start_method(allow_none=True) is None:
    multiprocess.set_start_method('spawn')

app = dash.Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    prevent_initial_callbacks="initial_duplicate",
    background_callback_manager=background_callback_manager,
)
app.title = APP_TITLE

server = app.server
app.config.suppress_callback_exceptions = True

BASE_PATH = Path(__file__).parent.resolve()
DATA_PATH = BASE_PATH.joinpath("input").resolve()

# Generates css file and variable using THEME_COLOR and THEME_COLOR_SECONDARY settings
css = f"""/* Generated theme settings css file, see app.py */
:root {{
    --theme: {THEME_COLOR};
    --theme-secondary: {THEME_COLOR_SECONDARY};
}}
"""
with open("assets/theme.css", "w") as f:
    f.write(css)


@app.callback(
    Output({"type": "to-collapse-class", "index": MATCH}, "className"),
    inputs=[
        Input({"type": "collapse-trigger", "index": MATCH}, "n_clicks"),
        State({"type": "to-collapse-class", "index": MATCH}, "className"),
    ],
    prevent_initial_call=True,
)
def toggle_left_column(collapse_trigger: int, to_collapse_class: str) -> str:
    """Toggles a 'collapsed' class that hides and shows some aspect of the UI.

    Args:
        collapse_trigger (int): The (total) number of times a collapse button has been clicked.
        to_collapse_class (str): Current class name of the thing to collapse, 'collapsed' if not visible, empty string if visible

    Returns:
        str: The new class name of the thing to collapse.
    """

    classes = to_collapse_class.split(" ") if to_collapse_class else []
    if "collapsed" in classes:
        classes.remove("collapsed")
        return " ".join(classes)
    return to_collapse_class + " collapsed" if to_collapse_class else "collapsed"


@app.callback(
    Output("solution-map", "srcDoc", allow_duplicate=True),
    inputs=[
        Input("run-button", "n_clicks"),
    ],
)
def render_initial_state(_) -> str:
    """Generates and saves and HTML version of the initial map.

    Note that 'run-button' is required as an Input to reload the map each time
    a run is started. This resets the solution map to the initial map but does
    NOT regenerate the initial map unless 'num-clients-select' is changed.

    Args:
        num_clients: Number of locations.

    Returns:
        str: Initial map shown on the map tab as HTML.
    """

    # only regenerate map if num_clients is changed (i.e., if run buttons is NOT clicked)
    if ctx.triggered_id != "run-button":
        return

    return


def get_updated_wall_clock_times(
    wall_clock_time: float, sampler_type: Union[SamplerType, int], reset_results: bool
) -> tuple[str, str]:
    """Determine which wall clock times to update in the UI.

    Args:
        wall_clock_time: Total run time.
        sampler_type: The sampler that was run. Either Either Quantum Hybrid (DQM) (``0`` or ``SamplerType.DQM``),
            Quantum Hybrid (NL) (``1`` or ``SamplerType.NL``), or Classical (K-Means) (``2`` or ``SamplerType.KMEANS``).
        reset_results: Whether or not to reset wall clock times.

    Returns:
        wall_clock_time_kmeans: Updated kmeans wall clock time.
        wall_clock_time_quantum: Updated quantum wall clock time.
    """
    wall_clock_time_kmeans = ""
    wall_clock_time_quantum = ""
    if sampler_type is SamplerType.KMEANS:
        wall_clock_time_kmeans = f"{wall_clock_time:.3f}s"
        if not reset_results:
            wall_clock_time_quantum = dash.no_update
    else:
        wall_clock_time_quantum = f"{wall_clock_time:.3f}s"
        if not reset_results:
            wall_clock_time_kmeans = dash.no_update
    return wall_clock_time_kmeans, wall_clock_time_quantum


class RunOptimizationReturn(NamedTuple):
    """Return type for the ``run_optimization`` callback function."""
    solution_map: str
    cost_table: tuple
    hybrid_table_label: str
    sampler_type: str
    reset_results: bool
    parameter_hash: str
    cost_comparison: dict
    problem_size: int
    search_space: str
    wall_clock_time_classical: str
    wall_clock_time_quantum: str
    num_locations: int
    vehicles_deployed: int

@app.callback(
    # store the solver used, whether or not to reset results tabs and the
    # parameter hash value used to detect parameter changes
    Output("sampler-type", "data"),
    Output("reset-results", "data"),
    Output("parameter-hash", "data"),
    Output("cost-comparison", "data"),
    # updates problem details table
    Output("problem-size", "children"),
    Output("search-space", "children"),
    Output("wall-clock-time-classical", "children"),
    Output("wall-clock-time-quantum", "children"),
    Output("num-locations", "children"),
    Output("vehicles-deployed", "children"),
    background=True,
    inputs=[
        Input("run-button", "n_clicks"),
        State("sampler-type-select", "value"),
        State("num-vehicles-select", "value"),
        State("solver-time-limit", "value"),
        State("num-clients-select", "value"),
        State("parameter-hash", "data"),
        State("cost-comparison", "data"),
    ],
    running=[
        # show cancel button and hide run button, and disable and animate results tab
        (Output("cancel-button", "className"), "", "display-none"),
        (Output("run-button", "className"), "display-none", ""),
        (Output("results-tab", "disabled"), True, False),
        (Output("results-tab", "label"), "Loading...", "Results"),
        # switch to map tab while running
        (Output("tabs", "value"), "map-tab", "map-tab"),
        # block certain callbacks from running until this is done
        (Output("run-in-progress", "data"), True, False),
    ],
    cancel=[Input("cancel-button", "n_clicks")],
    prevent_initial_call=True,
)
def run_optimization(
    run_click: int,
    sampler_type: Union[SamplerType, int],
    num_vehicles: int,
    time_limit: float,
    num_clients: int,
    previous_parameter_hash: str,
    cost_comparison: dict,
) -> RunOptimizationReturn:
    """Run the optimization and update map and results tables.

    This is the main optimization function which is called when the Run optimization button is
    clicked. It used all inputs from the drop-down lists, sliders and text entries and runs the
    optimization, updates the run/cancel buttons, animates (and deactivates) the results tab,
    moves focus to the map tab and updates all relevant HTML entries.

    Args:
        run_click: The (total) number of times the run button has been clicked.
        vehicle_type: Either Trucks (``0`` or ``VehicleType.TRUCKS``) or
            Delivery Drones (``1`` or ``VehicleType.DELIVERY_DRONES``).
        sampler_type: Either Quantum Hybrid (DQM) (``0`` or ``SamplerType.DQM``),
            Quantum Hybrid (NL) (``1`` or ``SamplerType.NL``), or Classical (K-Means)
            (``2`` or ``SamplerType.KMEANS``).
        num_vehicles: The number of vehicles.
        time_limit: The solver time limit.
        num_clients: The number of locations.
        cost_table: The html 'Solution cost' table. Used to update it dynamically.
        previous_parameter_hash: Previous hash string to detect changed parameters
        cost_comparison: Dictionary with solver keys and run cost values.

    Returns:
        A NamedTuple (RunOptimizationReturn) containing all outputs to be used when updating the HTML
        template (in ``dash_html.py``). These are:

            solution-map: Updates the 'srcDoc' entry for the 'solution-map' Iframe in the map tab.
                This is the map (initial and solution map).
            stored-results: Stores the Solution cost table in the results tab.
            hybrid-table-label: Label for the hybrid results table (either NL or DQM).
            sampler-type: The sampler used (``"quantum"`` or ``"classical"``).
            reset-results: Whether or not to reset the results tables before applying the new one.
            parameter-hash: Hash string to detect changed parameters.
            performance-improvement-quantum: Updates quantum performance improvement message.
            cost-comparison: Keeps track of the difference between classical and hybrid run costs.
            problem-size: Updates the problem-size entry in the problem details table.
            search-space: Updates the search-space entry in the problem details table.
            wall-clock-time-classical: Updates the wall clock time in the Classical table header.
            wall-clock-time-quantum: Updates the wall clock time in the Hybrid Quantum table header.
            num-locations: Updates the number of locations in the problem details table.
            vehicles-deployed: Updates the vehicles-deployed entry in the problem details table.
    """
    if run_click == 0 or ctx.triggered_id != "run-button":
        raise PreventUpdate

    if isinstance(sampler_type, int):
        sampler_type = SamplerType(sampler_type)

    if ctx.triggered_id == "run-button":
        routing_problem_parameters = ProblemParameters(
            sampler_type=sampler_type,
            time_limit=time_limit,
        )
        routing_problem_solver = Solver(routing_problem_parameters)

        # run problem and generate solution (stored in Solver)
        wall_clock_time = routing_problem_solver.generate()

        problem_size = num_vehicles * num_clients
        search_space = f"{num_vehicles**num_clients:.2e}"

        solution_cost = dict(sorted(solution_cost.items()))
        total_cost = defaultdict(int)
        for cost_info_dict in solution_cost.values():
            for key, value in cost_info_dict.items():
                total_cost[key] += value

        parameter_hash = _get_parameter_hash(**callback_context.states)
        reset_results = parameter_hash != previous_parameter_hash

        wall_clock_time_kmeans, wall_clock_time_quantum = get_updated_wall_clock_times(
            wall_clock_time, sampler_type, reset_results
        )

        return RunOptimizationReturn(
            sampler_type = "classical" if sampler_type is SamplerType.KMEANS else "quantum",
            reset_results = reset_results,
            parameter_hash = str(parameter_hash),
            cost_comparison = cost_comparison,
            problem_size = problem_size,
            search_space = search_space,
            wall_clock_time_classical = wall_clock_time_kmeans,
            wall_clock_time_quantum = wall_clock_time_quantum,
            num_locations = num_clients,
            vehicles_deployed = num_vehicles,
        )

    raise PreventUpdate


def _get_parameter_hash(**states) -> str:
    """Calculate a hash string for parameters which reset the results tables."""
    # list of parameter values that will reset the results tables
    # when changed in the app; must be hashable
    items = [
        "vehicle-type-select.value",
        "num-vehicles-select.value",
        "num-clients-select.value",
        "solver-time-limit.value",
    ]
    try:
        return str(hash(itemgetter(*items)(states)))
    except TypeError as e:
        raise TypeError("unhashable problem parameter value") from e


# import the html code and sets it in the app
# creates the visual layout and app (see `dash_html.py`)
set_html(app)

# Run the server
if __name__ == "__main__":
    app.run_server(debug=DEBUG)
