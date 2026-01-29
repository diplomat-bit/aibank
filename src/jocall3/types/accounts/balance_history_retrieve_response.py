# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["BalanceHistoryRetrieveResponse", "History"]


class History(BaseModel):
    balance: Optional[float] = None

    timestamp: Optional[datetime] = None


class BalanceHistoryRetrieveResponse(BaseModel):
    history: Optional[List[History]] = None
