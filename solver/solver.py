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
from __future__ import annotations

import time
from enum import Enum
from typing import Any, NamedTuple


class SamplerType(Enum):
    HYBRID = 0
    CLASSICAL = 1


class ProblemParameters(NamedTuple):
    """Structure to hold all provided problem parameters.

    Args:
        sampler_type: Either Quantum Hybrid (``0`` or ``SamplerType.HYBRID``),
            or Classical (``1`` or ``SamplerType.CLASSICAL``).
        time_limit: Time limit in seconds to run optimization for.
    """

    sampler_type: SamplerType
    time_limit: float
    # Add more problem parameters here.


class Solver:
    """Solver class to run the routing problem and store the solution.

    Args:
        parameters: NamedTuple that specifies all problem details.
    """

    def __init__(self, parameters: ProblemParameters) -> None:
        self._parameters = parameters
        self._solution = None

    def __getattr__(self, name: str) -> Any:
        """Get problem parameters."""
        # checks for attributes in 'self._parameters' if not found in class
        return object.__getattribute__(self._parameters, name)

    @property
    def solution(self) -> dict:
        """Solution for the problem."""
        return self._solution

    def generate(self) -> float:
        """Generates solution.

        Returns:
            float: The wall clock time for finding the solution.
        """
        start_time = time.perf_counter()

        if self.sampler_type is SamplerType.HYBRID:
            print("Implement Hybrid solver solution here.")
        else:
            print("Implement Classical solver solution here.")

        total_run_time = time.perf_counter() - start_time

        return total_run_time
