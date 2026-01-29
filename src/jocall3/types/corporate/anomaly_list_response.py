# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AnomalyListResponse", "Data"]


class Data(BaseModel):
    id: str

    severity: Literal["low", "medium", "high", "critical"]

    type: str

    description: Optional[str] = None

    detected_at: Optional[datetime] = FieldInfo(alias="detectedAt", default=None)


class AnomalyListResponse(BaseModel):
    data: Optional[List[Data]] = None
