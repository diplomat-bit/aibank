# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TreasuryForecastCashFlowParams"]


class TreasuryForecastCashFlowParams(TypedDict, total=False):
    horizon_days: Annotated[int, PropertyInfo(alias="horizonDays")]
