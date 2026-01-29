# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UserRegisterParams", "Address"]


class UserRegisterParams(TypedDict, total=False):
    email: Required[str]
    """Primary login email"""

    name: Required[str]
    """Full legal name"""

    password: Required[str]
    """Secure hashable string"""

    address: Address

    phone: str
    """International format phone number"""


class Address(TypedDict, total=False):
    city: str

    country: str

    state: str

    street: str

    zip: str
