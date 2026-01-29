# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.transaction import Transaction

__all__ = ["CardListTransactionsResponse"]


class CardListTransactionsResponse(BaseModel):
    data: Optional[List[Transaction]] = None
