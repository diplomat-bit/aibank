# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "CorporateOnboardEntityParams",
    "BeneficialOwner",
    "BeneficialOwnerAddress",
    "BeneficialOwnerPreferences",
    "BeneficialOwnerSecurityStatus",
]


class CorporateOnboardEntityParams(TypedDict, total=False):
    entity_type: Required[Annotated[Literal["LLC", "CORP", "NGO", "PARTNERSHIP"], PropertyInfo(alias="entityType")]]

    jurisdiction: Required[str]

    legal_name: Required[Annotated[str, PropertyInfo(alias="legalName")]]
    """Registered business name"""

    tax_id: Required[Annotated[str, PropertyInfo(alias="taxId")]]
    """EIN, VAT, or local tax ID"""

    beneficial_owners: Annotated[Iterable[BeneficialOwner], PropertyInfo(alias="beneficialOwners")]


class BeneficialOwnerAddress(TypedDict, total=False):
    city: str

    country: str

    state: str

    street: str

    zip: str


class BeneficialOwnerPreferences(TypedDict, total=False):
    notification_channels: Annotated[object, PropertyInfo(alias="notificationChannels")]

    theme: str


class BeneficialOwnerSecurityStatus(TypedDict, total=False):
    last_login: Annotated[Union[str, datetime], PropertyInfo(alias="lastLogin", format="iso8601")]

    two_factor_enabled: Annotated[bool, PropertyInfo(alias="twoFactorEnabled")]


class BeneficialOwner(TypedDict, total=False):
    id: Required[str]

    email: Required[str]

    identity_verified: Required[Annotated[bool, PropertyInfo(alias="identityVerified")]]

    name: Required[str]

    address: BeneficialOwnerAddress

    phone: str

    preferences: BeneficialOwnerPreferences

    security_status: Annotated[BeneficialOwnerSecurityStatus, PropertyInfo(alias="securityStatus")]
