# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSweeping:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_configure(self, client: Jocall3) -> None:
        sweeping = client.corporate.treasury.sweeping.configure(
            source_account="sourceAccount",
            target_account="targetAccount",
            threshold=0,
        )
        assert sweeping is None

    @parametrize
    def test_method_configure_with_all_params(self, client: Jocall3) -> None:
        sweeping = client.corporate.treasury.sweeping.configure(
            source_account="sourceAccount",
            target_account="targetAccount",
            threshold=0,
            frequency="daily",
        )
        assert sweeping is None

    @parametrize
    def test_raw_response_configure(self, client: Jocall3) -> None:
        response = client.corporate.treasury.sweeping.with_raw_response.configure(
            source_account="sourceAccount",
            target_account="targetAccount",
            threshold=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sweeping = response.parse()
        assert sweeping is None

    @parametrize
    def test_streaming_response_configure(self, client: Jocall3) -> None:
        with client.corporate.treasury.sweeping.with_streaming_response.configure(
            source_account="sourceAccount",
            target_account="targetAccount",
            threshold=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sweeping = response.parse()
            assert sweeping is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_execute(self, client: Jocall3) -> None:
        sweeping = client.corporate.treasury.sweeping.execute(
            rule_id="ruleId",
        )
        assert sweeping is None

    @parametrize
    def test_raw_response_execute(self, client: Jocall3) -> None:
        response = client.corporate.treasury.sweeping.with_raw_response.execute(
            rule_id="ruleId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sweeping = response.parse()
        assert sweeping is None

    @parametrize
    def test_streaming_response_execute(self, client: Jocall3) -> None:
        with client.corporate.treasury.sweeping.with_streaming_response.execute(
            rule_id="ruleId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sweeping = response.parse()
            assert sweeping is None

        assert cast(Any, response.is_closed) is True


class TestAsyncSweeping:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_configure(self, async_client: AsyncJocall3) -> None:
        sweeping = await async_client.corporate.treasury.sweeping.configure(
            source_account="sourceAccount",
            target_account="targetAccount",
            threshold=0,
        )
        assert sweeping is None

    @parametrize
    async def test_method_configure_with_all_params(self, async_client: AsyncJocall3) -> None:
        sweeping = await async_client.corporate.treasury.sweeping.configure(
            source_account="sourceAccount",
            target_account="targetAccount",
            threshold=0,
            frequency="daily",
        )
        assert sweeping is None

    @parametrize
    async def test_raw_response_configure(self, async_client: AsyncJocall3) -> None:
        response = await async_client.corporate.treasury.sweeping.with_raw_response.configure(
            source_account="sourceAccount",
            target_account="targetAccount",
            threshold=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sweeping = await response.parse()
        assert sweeping is None

    @parametrize
    async def test_streaming_response_configure(self, async_client: AsyncJocall3) -> None:
        async with async_client.corporate.treasury.sweeping.with_streaming_response.configure(
            source_account="sourceAccount",
            target_account="targetAccount",
            threshold=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sweeping = await response.parse()
            assert sweeping is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_execute(self, async_client: AsyncJocall3) -> None:
        sweeping = await async_client.corporate.treasury.sweeping.execute(
            rule_id="ruleId",
        )
        assert sweeping is None

    @parametrize
    async def test_raw_response_execute(self, async_client: AsyncJocall3) -> None:
        response = await async_client.corporate.treasury.sweeping.with_raw_response.execute(
            rule_id="ruleId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sweeping = await response.parse()
        assert sweeping is None

    @parametrize
    async def test_streaming_response_execute(self, async_client: AsyncJocall3) -> None:
        async with async_client.corporate.treasury.sweeping.with_streaming_response.execute(
            rule_id="ruleId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sweeping = await response.parse()
            assert sweeping is None

        assert cast(Any, response.is_closed) is True
