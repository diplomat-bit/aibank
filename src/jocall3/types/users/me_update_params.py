# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MeUpdateParams", "Address"]


class MeUpdateParams(TypedDict, total=False):
    address: Address

    name: str

    phone: str


class Address(TypedDict, total=False):
    city: Required[str]

    country: Required[str]

    street: Required[str]

    state: str

    zip: str
