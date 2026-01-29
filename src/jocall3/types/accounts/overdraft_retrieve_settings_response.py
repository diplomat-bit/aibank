# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["OverdraftRetrieveSettingsResponse"]


class OverdraftRetrieveSettingsResponse(BaseModel):
    enabled: Optional[bool] = None

    fee_preference: Optional[str] = FieldInfo(alias="feePreference", default=None)

    limit: Optional[float] = None
