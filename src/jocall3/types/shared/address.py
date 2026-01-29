# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Address"]


class Address(BaseModel):
    city: str

    country: str

    street: str

    state: Optional[str] = None

    zip: Optional[str] = None
