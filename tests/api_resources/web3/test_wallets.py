# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3
from tests.utils import assert_matches_type
from jocall3.types.web3 import (
    WalletListResponse,
    WalletCreateResponse,
    WalletGetBalanceResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWallets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Jocall3) -> None:
        wallet = client.web3.wallets.create(
            network="ETH",
        )
        assert_matches_type(WalletCreateResponse, wallet, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Jocall3) -> None:
        response = client.web3.wallets.with_raw_response.create(
            network="ETH",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = response.parse()
        assert_matches_type(WalletCreateResponse, wallet, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Jocall3) -> None:
        with client.web3.wallets.with_streaming_response.create(
            network="ETH",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = response.parse()
            assert_matches_type(WalletCreateResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Jocall3) -> None:
        wallet = client.web3.wallets.list()
        assert_matches_type(WalletListResponse, wallet, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Jocall3) -> None:
        response = client.web3.wallets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = response.parse()
        assert_matches_type(WalletListResponse, wallet, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Jocall3) -> None:
        with client.web3.wallets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = response.parse()
            assert_matches_type(WalletListResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_connect(self, client: Jocall3) -> None:
        wallet = client.web3.wallets.connect(
            address="address",
            provider="provider",
            signature="signature",
        )
        assert wallet is None

    @parametrize
    def test_raw_response_connect(self, client: Jocall3) -> None:
        response = client.web3.wallets.with_raw_response.connect(
            address="address",
            provider="provider",
            signature="signature",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = response.parse()
        assert wallet is None

    @parametrize
    def test_streaming_response_connect(self, client: Jocall3) -> None:
        with client.web3.wallets.with_streaming_response.connect(
            address="address",
            provider="provider",
            signature="signature",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = response.parse()
            assert wallet is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_balance(self, client: Jocall3) -> None:
        wallet = client.web3.wallets.get_balance(
            "walletId",
        )
        assert_matches_type(WalletGetBalanceResponse, wallet, path=["response"])

    @parametrize
    def test_raw_response_get_balance(self, client: Jocall3) -> None:
        response = client.web3.wallets.with_raw_response.get_balance(
            "walletId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = response.parse()
        assert_matches_type(WalletGetBalanceResponse, wallet, path=["response"])

    @parametrize
    def test_streaming_response_get_balance(self, client: Jocall3) -> None:
        with client.web3.wallets.with_streaming_response.get_balance(
            "walletId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = response.parse()
            assert_matches_type(WalletGetBalanceResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_balance(self, client: Jocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            client.web3.wallets.with_raw_response.get_balance(
                "",
            )


class TestAsyncWallets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncJocall3) -> None:
        wallet = await async_client.web3.wallets.create(
            network="ETH",
        )
        assert_matches_type(WalletCreateResponse, wallet, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncJocall3) -> None:
        response = await async_client.web3.wallets.with_raw_response.create(
            network="ETH",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = await response.parse()
        assert_matches_type(WalletCreateResponse, wallet, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncJocall3) -> None:
        async with async_client.web3.wallets.with_streaming_response.create(
            network="ETH",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = await response.parse()
            assert_matches_type(WalletCreateResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncJocall3) -> None:
        wallet = await async_client.web3.wallets.list()
        assert_matches_type(WalletListResponse, wallet, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJocall3) -> None:
        response = await async_client.web3.wallets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = await response.parse()
        assert_matches_type(WalletListResponse, wallet, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJocall3) -> None:
        async with async_client.web3.wallets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = await response.parse()
            assert_matches_type(WalletListResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_connect(self, async_client: AsyncJocall3) -> None:
        wallet = await async_client.web3.wallets.connect(
            address="address",
            provider="provider",
            signature="signature",
        )
        assert wallet is None

    @parametrize
    async def test_raw_response_connect(self, async_client: AsyncJocall3) -> None:
        response = await async_client.web3.wallets.with_raw_response.connect(
            address="address",
            provider="provider",
            signature="signature",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = await response.parse()
        assert wallet is None

    @parametrize
    async def test_streaming_response_connect(self, async_client: AsyncJocall3) -> None:
        async with async_client.web3.wallets.with_streaming_response.connect(
            address="address",
            provider="provider",
            signature="signature",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = await response.parse()
            assert wallet is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_balance(self, async_client: AsyncJocall3) -> None:
        wallet = await async_client.web3.wallets.get_balance(
            "walletId",
        )
        assert_matches_type(WalletGetBalanceResponse, wallet, path=["response"])

    @parametrize
    async def test_raw_response_get_balance(self, async_client: AsyncJocall3) -> None:
        response = await async_client.web3.wallets.with_raw_response.get_balance(
            "walletId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = await response.parse()
        assert_matches_type(WalletGetBalanceResponse, wallet, path=["response"])

    @parametrize
    async def test_streaming_response_get_balance(self, async_client: AsyncJocall3) -> None:
        async with async_client.web3.wallets.with_streaming_response.get_balance(
            "walletId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = await response.parse()
            assert_matches_type(WalletGetBalanceResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_balance(self, async_client: AsyncJocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            await async_client.web3.wallets.with_raw_response.get_balance(
                "",
            )
