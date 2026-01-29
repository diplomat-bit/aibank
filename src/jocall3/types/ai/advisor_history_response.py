# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["AdvisorHistoryResponse"]


class AdvisorHistoryResponse(BaseModel):
    messages: Optional[List[object]] = None
