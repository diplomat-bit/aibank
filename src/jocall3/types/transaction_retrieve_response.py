# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TransactionRetrieveResponse", "MerchantDetails"]


class MerchantDetails(BaseModel):
    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)

    name: Optional[str] = None


class TransactionRetrieveResponse(BaseModel):
    id: str

    amount: float

    currency: str

    date: datetime.date

    description: str

    account_id: Optional[str] = FieldInfo(alias="accountId", default=None)

    carbon_footprint: Optional[float] = FieldInfo(alias="carbonFootprint", default=None)

    category: Optional[str] = None

    merchant_details: Optional[MerchantDetails] = FieldInfo(alias="merchantDetails", default=None)
