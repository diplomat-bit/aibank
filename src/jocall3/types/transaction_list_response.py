# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TransactionListResponse", "Data", "DataMerchantDetails"]


class DataMerchantDetails(BaseModel):
    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)

    name: Optional[str] = None


class Data(BaseModel):
    id: str

    amount: float

    currency: str

    date: datetime.date

    description: str

    account_id: Optional[str] = FieldInfo(alias="accountId", default=None)

    carbon_footprint: Optional[float] = FieldInfo(alias="carbonFootprint", default=None)

    category: Optional[str] = None

    merchant_details: Optional[DataMerchantDetails] = FieldInfo(alias="merchantDetails", default=None)


class TransactionListResponse(BaseModel):
    data: Optional[List[Data]] = None

    next_offset: Optional[int] = FieldInfo(alias="nextOffset", default=None)

    total: Optional[int] = None
