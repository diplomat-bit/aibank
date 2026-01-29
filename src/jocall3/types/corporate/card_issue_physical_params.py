# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared_params.address import Address

__all__ = ["CardIssuePhysicalParams"]


class CardIssuePhysicalParams(TypedDict, total=False):
    holder_name: Required[Annotated[str, PropertyInfo(alias="holderName")]]

    shipping_address: Required[Annotated[Address, PropertyInfo(alias="shippingAddress")]]
