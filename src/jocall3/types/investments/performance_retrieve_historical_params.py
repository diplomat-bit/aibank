# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["PerformanceRetrieveHistoricalParams"]


class PerformanceRetrieveHistoricalParams(TypedDict, total=False):
    range: Literal["1m", "3m", "1y", "5y", "max"]
