# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOffsets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_purchase(self, client: Jocall3) -> None:
        offset = client.sustainability.offsets.purchase(
            project_id="projectId",
            tonnes=0,
        )
        assert offset is None

    @parametrize
    def test_method_purchase_with_all_params(self, client: Jocall3) -> None:
        offset = client.sustainability.offsets.purchase(
            project_id="projectId",
            tonnes=0,
            payment_source_id="paymentSourceId",
        )
        assert offset is None

    @parametrize
    def test_raw_response_purchase(self, client: Jocall3) -> None:
        response = client.sustainability.offsets.with_raw_response.purchase(
            project_id="projectId",
            tonnes=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        offset = response.parse()
        assert offset is None

    @parametrize
    def test_streaming_response_purchase(self, client: Jocall3) -> None:
        with client.sustainability.offsets.with_streaming_response.purchase(
            project_id="projectId",
            tonnes=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            offset = response.parse()
            assert offset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retire(self, client: Jocall3) -> None:
        offset = client.sustainability.offsets.retire(
            certificate_id="certificateId",
        )
        assert offset is None

    @parametrize
    def test_raw_response_retire(self, client: Jocall3) -> None:
        response = client.sustainability.offsets.with_raw_response.retire(
            certificate_id="certificateId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        offset = response.parse()
        assert offset is None

    @parametrize
    def test_streaming_response_retire(self, client: Jocall3) -> None:
        with client.sustainability.offsets.with_streaming_response.retire(
            certificate_id="certificateId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            offset = response.parse()
            assert offset is None

        assert cast(Any, response.is_closed) is True


class TestAsyncOffsets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_purchase(self, async_client: AsyncJocall3) -> None:
        offset = await async_client.sustainability.offsets.purchase(
            project_id="projectId",
            tonnes=0,
        )
        assert offset is None

    @parametrize
    async def test_method_purchase_with_all_params(self, async_client: AsyncJocall3) -> None:
        offset = await async_client.sustainability.offsets.purchase(
            project_id="projectId",
            tonnes=0,
            payment_source_id="paymentSourceId",
        )
        assert offset is None

    @parametrize
    async def test_raw_response_purchase(self, async_client: AsyncJocall3) -> None:
        response = await async_client.sustainability.offsets.with_raw_response.purchase(
            project_id="projectId",
            tonnes=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        offset = await response.parse()
        assert offset is None

    @parametrize
    async def test_streaming_response_purchase(self, async_client: AsyncJocall3) -> None:
        async with async_client.sustainability.offsets.with_streaming_response.purchase(
            project_id="projectId",
            tonnes=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            offset = await response.parse()
            assert offset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retire(self, async_client: AsyncJocall3) -> None:
        offset = await async_client.sustainability.offsets.retire(
            certificate_id="certificateId",
        )
        assert offset is None

    @parametrize
    async def test_raw_response_retire(self, async_client: AsyncJocall3) -> None:
        response = await async_client.sustainability.offsets.with_raw_response.retire(
            certificate_id="certificateId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        offset = await response.parse()
        assert offset is None

    @parametrize
    async def test_streaming_response_retire(self, async_client: AsyncJocall3) -> None:
        async with async_client.sustainability.offsets.with_streaming_response.retire(
            certificate_id="certificateId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            offset = await response.parse()
            assert offset is None

        assert cast(Any, response.is_closed) is True
