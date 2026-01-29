# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AccountRetrieveResponse"]


class AccountRetrieveResponse(BaseModel):
    id: str

    currency: str

    current_balance: float = FieldInfo(alias="currentBalance")

    institution_name: str = FieldInfo(alias="institutionName")

    type: str

    available_balance: Optional[float] = FieldInfo(alias="availableBalance", default=None)

    last_updated: Optional[datetime] = FieldInfo(alias="lastUpdated", default=None)

    name: Optional[str] = None
