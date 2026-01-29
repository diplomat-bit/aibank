# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AccountListResponse", "Data", "DataProjectedCashFlow"]


class DataProjectedCashFlow(BaseModel):
    confidence_score: Optional[int] = FieldInfo(alias="confidenceScore", default=None)

    days30: Optional[float] = None


class Data(BaseModel):
    id: str

    currency: str

    current_balance: float = FieldInfo(alias="currentBalance")

    type: str

    available_balance: Optional[float] = FieldInfo(alias="availableBalance", default=None)

    institution_name: Optional[str] = FieldInfo(alias="institutionName", default=None)

    last_updated: Optional[datetime] = FieldInfo(alias="lastUpdated", default=None)

    name: Optional[str] = None

    projected_cash_flow: Optional[DataProjectedCashFlow] = FieldInfo(alias="projectedCashFlow", default=None)


class AccountListResponse(BaseModel):
    data: Optional[List[Data]] = None

    next_offset: Optional[int] = FieldInfo(alias="nextOffset", default=None)

    total: Optional[int] = None
