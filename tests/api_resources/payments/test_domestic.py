# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDomestic:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_ach(self, client: Jocall3) -> None:
        domestic = client.payments.domestic.ach(
            account="account",
            amount=0,
            routing="routing",
        )
        assert domestic is None

    @parametrize
    def test_raw_response_ach(self, client: Jocall3) -> None:
        response = client.payments.domestic.with_raw_response.ach(
            account="account",
            amount=0,
            routing="routing",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domestic = response.parse()
        assert domestic is None

    @parametrize
    def test_streaming_response_ach(self, client: Jocall3) -> None:
        with client.payments.domestic.with_streaming_response.ach(
            account="account",
            amount=0,
            routing="routing",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domestic = response.parse()
            assert domestic is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_rtp(self, client: Jocall3) -> None:
        domestic = client.payments.domestic.rtp(
            amount=0,
            recipient_id="recipientId",
        )
        assert domestic is None

    @parametrize
    def test_raw_response_rtp(self, client: Jocall3) -> None:
        response = client.payments.domestic.with_raw_response.rtp(
            amount=0,
            recipient_id="recipientId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domestic = response.parse()
        assert domestic is None

    @parametrize
    def test_streaming_response_rtp(self, client: Jocall3) -> None:
        with client.payments.domestic.with_streaming_response.rtp(
            amount=0,
            recipient_id="recipientId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domestic = response.parse()
            assert domestic is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_wire(self, client: Jocall3) -> None:
        domestic = client.payments.domestic.wire(
            account="account",
            amount=0,
            routing="routing",
        )
        assert domestic is None

    @parametrize
    def test_raw_response_wire(self, client: Jocall3) -> None:
        response = client.payments.domestic.with_raw_response.wire(
            account="account",
            amount=0,
            routing="routing",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domestic = response.parse()
        assert domestic is None

    @parametrize
    def test_streaming_response_wire(self, client: Jocall3) -> None:
        with client.payments.domestic.with_streaming_response.wire(
            account="account",
            amount=0,
            routing="routing",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domestic = response.parse()
            assert domestic is None

        assert cast(Any, response.is_closed) is True


class TestAsyncDomestic:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_ach(self, async_client: AsyncJocall3) -> None:
        domestic = await async_client.payments.domestic.ach(
            account="account",
            amount=0,
            routing="routing",
        )
        assert domestic is None

    @parametrize
    async def test_raw_response_ach(self, async_client: AsyncJocall3) -> None:
        response = await async_client.payments.domestic.with_raw_response.ach(
            account="account",
            amount=0,
            routing="routing",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domestic = await response.parse()
        assert domestic is None

    @parametrize
    async def test_streaming_response_ach(self, async_client: AsyncJocall3) -> None:
        async with async_client.payments.domestic.with_streaming_response.ach(
            account="account",
            amount=0,
            routing="routing",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domestic = await response.parse()
            assert domestic is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_rtp(self, async_client: AsyncJocall3) -> None:
        domestic = await async_client.payments.domestic.rtp(
            amount=0,
            recipient_id="recipientId",
        )
        assert domestic is None

    @parametrize
    async def test_raw_response_rtp(self, async_client: AsyncJocall3) -> None:
        response = await async_client.payments.domestic.with_raw_response.rtp(
            amount=0,
            recipient_id="recipientId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domestic = await response.parse()
        assert domestic is None

    @parametrize
    async def test_streaming_response_rtp(self, async_client: AsyncJocall3) -> None:
        async with async_client.payments.domestic.with_streaming_response.rtp(
            amount=0,
            recipient_id="recipientId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domestic = await response.parse()
            assert domestic is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_wire(self, async_client: AsyncJocall3) -> None:
        domestic = await async_client.payments.domestic.wire(
            account="account",
            amount=0,
            routing="routing",
        )
        assert domestic is None

    @parametrize
    async def test_raw_response_wire(self, async_client: AsyncJocall3) -> None:
        response = await async_client.payments.domestic.with_raw_response.wire(
            account="account",
            amount=0,
            routing="routing",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domestic = await response.parse()
        assert domestic is None

    @parametrize
    async def test_streaming_response_wire(self, async_client: AsyncJocall3) -> None:
        async with async_client.payments.domestic.with_streaming_response.wire(
            account="account",
            amount=0,
            routing="routing",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domestic = await response.parse()
            assert domestic is None

        assert cast(Any, response.is_closed) is True
