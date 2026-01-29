# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPooling:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_configure(self, client: Jocall3) -> None:
        pooling = client.corporate.treasury.pooling.configure()
        assert pooling is None

    @parametrize
    def test_method_configure_with_all_params(self, client: Jocall3) -> None:
        pooling = client.corporate.treasury.pooling.configure(
            source_account_ids=["string"],
            target_account_id="target_account_id",
        )
        assert pooling is None

    @parametrize
    def test_raw_response_configure(self, client: Jocall3) -> None:
        response = client.corporate.treasury.pooling.with_raw_response.configure()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pooling = response.parse()
        assert pooling is None

    @parametrize
    def test_streaming_response_configure(self, client: Jocall3) -> None:
        with client.corporate.treasury.pooling.with_streaming_response.configure() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pooling = response.parse()
            assert pooling is None

        assert cast(Any, response.is_closed) is True


class TestAsyncPooling:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_configure(self, async_client: AsyncJocall3) -> None:
        pooling = await async_client.corporate.treasury.pooling.configure()
        assert pooling is None

    @parametrize
    async def test_method_configure_with_all_params(self, async_client: AsyncJocall3) -> None:
        pooling = await async_client.corporate.treasury.pooling.configure(
            source_account_ids=["string"],
            target_account_id="target_account_id",
        )
        assert pooling is None

    @parametrize
    async def test_raw_response_configure(self, async_client: AsyncJocall3) -> None:
        response = await async_client.corporate.treasury.pooling.with_raw_response.configure()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pooling = await response.parse()
        assert pooling is None

    @parametrize
    async def test_streaming_response_configure(self, async_client: AsyncJocall3) -> None:
        async with async_client.corporate.treasury.pooling.with_streaming_response.configure() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pooling = await response.parse()
            assert pooling is None

        assert cast(Any, response.is_closed) is True
