# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["InternationalRetrieveStatusResponse"]


class InternationalRetrieveStatusResponse(BaseModel):
    fx_rate: Optional[float] = None

    status: Optional[str] = None
