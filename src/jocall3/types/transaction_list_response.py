# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.transaction import Transaction

__all__ = ["TransactionListResponse"]


class TransactionListResponse(BaseModel):
    data: List[Transaction]

    total: int

    next_offset: Optional[int] = FieldInfo(alias="nextOffset", default=None)
