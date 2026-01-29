# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TransactionBridgeChainParams"]


class TransactionBridgeChainParams(TypedDict, total=False):
    token: Required[str]

    amount: Required[str]

    dest_chain: Required[Annotated[str, PropertyInfo(alias="destChain")]]

    source_chain: Required[Annotated[str, PropertyInfo(alias="sourceChain")]]
