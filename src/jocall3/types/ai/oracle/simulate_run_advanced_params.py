# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["SimulateRunAdvancedParams", "Scenario"]


class SimulateRunAdvancedParams(TypedDict, total=False):
    prompt: Required[str]

    scenarios: Required[Iterable[Scenario]]

    global_economic_factors: Annotated[object, PropertyInfo(alias="globalEconomicFactors")]

    personal_assumptions: Annotated[object, PropertyInfo(alias="personalAssumptions")]


class Scenario(TypedDict, total=False):
    name: Required[str]

    description: str

    variables: Dict[str, object]
