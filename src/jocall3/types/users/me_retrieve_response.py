# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.address import Address

__all__ = ["MeRetrieveResponse", "SecurityStatus"]


class SecurityStatus(BaseModel):
    last_login: Optional[datetime] = FieldInfo(alias="lastLogin", default=None)

    two_factor_enabled: Optional[bool] = FieldInfo(alias="twoFactorEnabled", default=None)


class MeRetrieveResponse(BaseModel):
    id: str

    email: str

    identity_verified: bool = FieldInfo(alias="identityVerified")

    name: str

    address: Optional[Address] = None

    preferences: Optional[Dict[str, object]] = None

    security_status: Optional[SecurityStatus] = FieldInfo(alias="securityStatus", default=None)
