# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3
from tests.utils import assert_matches_type
from jocall3.types.web3 import (
    TransactionSendResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTransactions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_bridge_chain(self, client: Jocall3) -> None:
        transaction = client.web3.transactions.bridge_chain(
            token="token",
            amount="amount",
            dest_chain="destChain",
            source_chain="sourceChain",
        )
        assert transaction is None

    @parametrize
    def test_raw_response_bridge_chain(self, client: Jocall3) -> None:
        response = client.web3.transactions.with_raw_response.bridge_chain(
            token="token",
            amount="amount",
            dest_chain="destChain",
            source_chain="sourceChain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert transaction is None

    @parametrize
    def test_streaming_response_bridge_chain(self, client: Jocall3) -> None:
        with client.web3.transactions.with_streaming_response.bridge_chain(
            token="token",
            amount="amount",
            dest_chain="destChain",
            source_chain="sourceChain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert transaction is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_initiate(self, client: Jocall3) -> None:
        transaction = client.web3.transactions.initiate(
            amount=0,
            asset="asset",
            wallet_id="wallet_id",
        )
        assert transaction is None

    @parametrize
    def test_raw_response_initiate(self, client: Jocall3) -> None:
        response = client.web3.transactions.with_raw_response.initiate(
            amount=0,
            asset="asset",
            wallet_id="wallet_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert transaction is None

    @parametrize
    def test_streaming_response_initiate(self, client: Jocall3) -> None:
        with client.web3.transactions.with_streaming_response.initiate(
            amount=0,
            asset="asset",
            wallet_id="wallet_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert transaction is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_send(self, client: Jocall3) -> None:
        transaction = client.web3.transactions.send(
            token="token",
            amount="amount",
            to="to",
        )
        assert_matches_type(TransactionSendResponse, transaction, path=["response"])

    @parametrize
    def test_raw_response_send(self, client: Jocall3) -> None:
        response = client.web3.transactions.with_raw_response.send(
            token="token",
            amount="amount",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(TransactionSendResponse, transaction, path=["response"])

    @parametrize
    def test_streaming_response_send(self, client: Jocall3) -> None:
        with client.web3.transactions.with_streaming_response.send(
            token="token",
            amount="amount",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(TransactionSendResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_swap_tokens(self, client: Jocall3) -> None:
        transaction = client.web3.transactions.swap_tokens(
            amount="amount",
            from_token="fromToken",
            to_token="toToken",
        )
        assert transaction is None

    @parametrize
    def test_raw_response_swap_tokens(self, client: Jocall3) -> None:
        response = client.web3.transactions.with_raw_response.swap_tokens(
            amount="amount",
            from_token="fromToken",
            to_token="toToken",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert transaction is None

    @parametrize
    def test_streaming_response_swap_tokens(self, client: Jocall3) -> None:
        with client.web3.transactions.with_streaming_response.swap_tokens(
            amount="amount",
            from_token="fromToken",
            to_token="toToken",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert transaction is None

        assert cast(Any, response.is_closed) is True


class TestAsyncTransactions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_bridge_chain(self, async_client: AsyncJocall3) -> None:
        transaction = await async_client.web3.transactions.bridge_chain(
            token="token",
            amount="amount",
            dest_chain="destChain",
            source_chain="sourceChain",
        )
        assert transaction is None

    @parametrize
    async def test_raw_response_bridge_chain(self, async_client: AsyncJocall3) -> None:
        response = await async_client.web3.transactions.with_raw_response.bridge_chain(
            token="token",
            amount="amount",
            dest_chain="destChain",
            source_chain="sourceChain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert transaction is None

    @parametrize
    async def test_streaming_response_bridge_chain(self, async_client: AsyncJocall3) -> None:
        async with async_client.web3.transactions.with_streaming_response.bridge_chain(
            token="token",
            amount="amount",
            dest_chain="destChain",
            source_chain="sourceChain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert transaction is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_initiate(self, async_client: AsyncJocall3) -> None:
        transaction = await async_client.web3.transactions.initiate(
            amount=0,
            asset="asset",
            wallet_id="wallet_id",
        )
        assert transaction is None

    @parametrize
    async def test_raw_response_initiate(self, async_client: AsyncJocall3) -> None:
        response = await async_client.web3.transactions.with_raw_response.initiate(
            amount=0,
            asset="asset",
            wallet_id="wallet_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert transaction is None

    @parametrize
    async def test_streaming_response_initiate(self, async_client: AsyncJocall3) -> None:
        async with async_client.web3.transactions.with_streaming_response.initiate(
            amount=0,
            asset="asset",
            wallet_id="wallet_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert transaction is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_send(self, async_client: AsyncJocall3) -> None:
        transaction = await async_client.web3.transactions.send(
            token="token",
            amount="amount",
            to="to",
        )
        assert_matches_type(TransactionSendResponse, transaction, path=["response"])

    @parametrize
    async def test_raw_response_send(self, async_client: AsyncJocall3) -> None:
        response = await async_client.web3.transactions.with_raw_response.send(
            token="token",
            amount="amount",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(TransactionSendResponse, transaction, path=["response"])

    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncJocall3) -> None:
        async with async_client.web3.transactions.with_streaming_response.send(
            token="token",
            amount="amount",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(TransactionSendResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_swap_tokens(self, async_client: AsyncJocall3) -> None:
        transaction = await async_client.web3.transactions.swap_tokens(
            amount="amount",
            from_token="fromToken",
            to_token="toToken",
        )
        assert transaction is None

    @parametrize
    async def test_raw_response_swap_tokens(self, async_client: AsyncJocall3) -> None:
        response = await async_client.web3.transactions.with_raw_response.swap_tokens(
            amount="amount",
            from_token="fromToken",
            to_token="toToken",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert transaction is None

    @parametrize
    async def test_streaming_response_swap_tokens(self, async_client: AsyncJocall3) -> None:
        async with async_client.web3.transactions.with_streaming_response.swap_tokens(
            amount="amount",
            from_token="fromToken",
            to_token="toToken",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert transaction is None

        assert cast(Any, response.is_closed) is True
