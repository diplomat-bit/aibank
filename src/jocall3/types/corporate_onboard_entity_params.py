# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared_params.address import Address

__all__ = ["CorporateOnboardEntityParams", "BeneficialOwner", "BeneficialOwnerSecurityStatus"]


class CorporateOnboardEntityParams(TypedDict, total=False):
    entity_type: Required[Annotated[Literal["LLC", "CORP", "NGO", "PARTNERSHIP"], PropertyInfo(alias="entityType")]]

    jurisdiction: Required[str]

    legal_name: Required[Annotated[str, PropertyInfo(alias="legalName")]]
    """Registered business name"""

    tax_id: Required[Annotated[str, PropertyInfo(alias="taxId")]]
    """EIN, VAT, or local tax ID"""

    beneficial_owners: Annotated[Iterable[BeneficialOwner], PropertyInfo(alias="beneficialOwners")]


class BeneficialOwnerSecurityStatus(TypedDict, total=False):
    last_login: Annotated[Union[str, datetime], PropertyInfo(alias="lastLogin", format="iso8601")]

    two_factor_enabled: Annotated[bool, PropertyInfo(alias="twoFactorEnabled")]


class BeneficialOwner(TypedDict, total=False):
    id: Required[str]

    email: Required[str]

    identity_verified: Required[Annotated[bool, PropertyInfo(alias="identityVerified")]]

    name: Required[str]

    address: Address

    preferences: Dict[str, object]

    security_status: Annotated[BeneficialOwnerSecurityStatus, PropertyInfo(alias="securityStatus")]
