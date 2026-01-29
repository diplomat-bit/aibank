# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["SimulateRunMonteCarloParams"]


class SimulateRunMonteCarloParams(TypedDict, total=False):
    iterations: Required[int]

    variables: Required[SequenceNotStr[str]]

    confidence_interval: Annotated[float, PropertyInfo(alias="confidenceInterval")]
