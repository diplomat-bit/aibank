# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CardIssueVirtualResponse", "Controls"]


class Controls(BaseModel):
    categories: Optional[List[str]] = None

    monthly_limit: Optional[float] = FieldInfo(alias="monthlyLimit", default=None)


class CardIssueVirtualResponse(BaseModel):
    id: str

    card_number_mask: str = FieldInfo(alias="cardNumberMask")

    holder_name: str = FieldInfo(alias="holderName")

    status: str

    controls: Optional[Controls] = None

    expiration_date: Optional[date] = FieldInfo(alias="expirationDate", default=None)

    frozen: Optional[bool] = None
