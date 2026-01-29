# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TransactionListPendingResponse", "Data"]


class Data(BaseModel):
    id: str

    amount: float

    currency: str

    date: datetime.date

    description: str

    category: Optional[str] = None

    notes: Optional[str] = None


class TransactionListPendingResponse(BaseModel):
    data: List[Data]

    total: int

    next_offset: Optional[int] = FieldInfo(alias="nextOffset", default=None)
