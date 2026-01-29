# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MeRetrieveResponse", "Address", "Preferences", "SecurityStatus"]


class Address(BaseModel):
    city: Optional[str] = None

    country: Optional[str] = None

    state: Optional[str] = None

    street: Optional[str] = None

    zip: Optional[str] = None


class Preferences(BaseModel):
    notification_channels: Optional[object] = FieldInfo(alias="notificationChannels", default=None)

    theme: Optional[str] = None


class SecurityStatus(BaseModel):
    last_login: Optional[datetime] = FieldInfo(alias="lastLogin", default=None)

    two_factor_enabled: Optional[bool] = FieldInfo(alias="twoFactorEnabled", default=None)


class MeRetrieveResponse(BaseModel):
    id: str

    email: str

    identity_verified: bool = FieldInfo(alias="identityVerified")

    name: str

    address: Optional[Address] = None

    phone: Optional[str] = None

    preferences: Optional[Preferences] = None

    security_status: Optional[SecurityStatus] = FieldInfo(alias="securityStatus", default=None)
