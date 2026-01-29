# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3
from tests.utils import assert_matches_type
from jocall3.types import Web3RetrieveNetworkStatusResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWeb3:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve_network_status(self, client: Jocall3) -> None:
        web3 = client.web3.retrieve_network_status()
        assert_matches_type(Web3RetrieveNetworkStatusResponse, web3, path=["response"])

    @parametrize
    def test_raw_response_retrieve_network_status(self, client: Jocall3) -> None:
        response = client.web3.with_raw_response.retrieve_network_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web3 = response.parse()
        assert_matches_type(Web3RetrieveNetworkStatusResponse, web3, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_network_status(self, client: Jocall3) -> None:
        with client.web3.with_streaming_response.retrieve_network_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web3 = response.parse()
            assert_matches_type(Web3RetrieveNetworkStatusResponse, web3, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWeb3:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve_network_status(self, async_client: AsyncJocall3) -> None:
        web3 = await async_client.web3.retrieve_network_status()
        assert_matches_type(Web3RetrieveNetworkStatusResponse, web3, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_network_status(self, async_client: AsyncJocall3) -> None:
        response = await async_client.web3.with_raw_response.retrieve_network_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web3 = await response.parse()
        assert_matches_type(Web3RetrieveNetworkStatusResponse, web3, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_network_status(self, async_client: AsyncJocall3) -> None:
        async with async_client.web3.with_streaming_response.retrieve_network_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web3 = await response.parse()
            assert_matches_type(Web3RetrieveNetworkStatusResponse, web3, path=["response"])

        assert cast(Any, response.is_closed) is True
