# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["AnomalyListResponse", "Data"]


class Data(BaseModel):
    id: str

    severity: str

    type: str


class AnomalyListResponse(BaseModel):
    data: Optional[List[Data]] = None
