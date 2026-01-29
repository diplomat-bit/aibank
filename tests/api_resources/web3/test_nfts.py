# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3
from tests.utils import assert_matches_type
from jocall3.types.web3 import NFTListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNFTs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Jocall3) -> None:
        nft = client.web3.nfts.list()
        assert_matches_type(NFTListResponse, nft, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Jocall3) -> None:
        response = client.web3.nfts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nft = response.parse()
        assert_matches_type(NFTListResponse, nft, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Jocall3) -> None:
        with client.web3.nfts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nft = response.parse()
            assert_matches_type(NFTListResponse, nft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_mint(self, client: Jocall3) -> None:
        nft = client.web3.nfts.mint(
            metadata_uri="metadataUri",
        )
        assert nft is None

    @parametrize
    def test_raw_response_mint(self, client: Jocall3) -> None:
        response = client.web3.nfts.with_raw_response.mint(
            metadata_uri="metadataUri",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nft = response.parse()
        assert nft is None

    @parametrize
    def test_streaming_response_mint(self, client: Jocall3) -> None:
        with client.web3.nfts.with_streaming_response.mint(
            metadata_uri="metadataUri",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nft = response.parse()
            assert nft is None

        assert cast(Any, response.is_closed) is True


class TestAsyncNFTs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncJocall3) -> None:
        nft = await async_client.web3.nfts.list()
        assert_matches_type(NFTListResponse, nft, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJocall3) -> None:
        response = await async_client.web3.nfts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nft = await response.parse()
        assert_matches_type(NFTListResponse, nft, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJocall3) -> None:
        async with async_client.web3.nfts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nft = await response.parse()
            assert_matches_type(NFTListResponse, nft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_mint(self, async_client: AsyncJocall3) -> None:
        nft = await async_client.web3.nfts.mint(
            metadata_uri="metadataUri",
        )
        assert nft is None

    @parametrize
    async def test_raw_response_mint(self, async_client: AsyncJocall3) -> None:
        response = await async_client.web3.nfts.with_raw_response.mint(
            metadata_uri="metadataUri",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nft = await response.parse()
        assert nft is None

    @parametrize
    async def test_streaming_response_mint(self, async_client: AsyncJocall3) -> None:
        async with async_client.web3.nfts.with_streaming_response.mint(
            metadata_uri="metadataUri",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nft = await response.parse()
            assert nft is None

        assert cast(Any, response.is_closed) is True
