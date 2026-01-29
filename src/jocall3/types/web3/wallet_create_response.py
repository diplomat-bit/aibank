# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["WalletCreateResponse"]


class WalletCreateResponse(BaseModel):
    id: str

    blockchain_network: str = FieldInfo(alias="blockchainNetwork")

    status: str

    wallet_address: str = FieldInfo(alias="walletAddress")

    last_synced: Optional[datetime] = FieldInfo(alias="lastSynced", default=None)

    wallet_provider: Optional[str] = FieldInfo(alias="walletProvider", default=None)
