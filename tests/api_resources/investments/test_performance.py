# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3
from tests.utils import assert_matches_type
from jocall3.types.investments import PerformanceRetrieveHistoricalResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPerformance:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve_historical(self, client: Jocall3) -> None:
        performance = client.investments.performance.retrieve_historical()
        assert_matches_type(PerformanceRetrieveHistoricalResponse, performance, path=["response"])

    @parametrize
    def test_method_retrieve_historical_with_all_params(self, client: Jocall3) -> None:
        performance = client.investments.performance.retrieve_historical(
            range="1m",
        )
        assert_matches_type(PerformanceRetrieveHistoricalResponse, performance, path=["response"])

    @parametrize
    def test_raw_response_retrieve_historical(self, client: Jocall3) -> None:
        response = client.investments.performance.with_raw_response.retrieve_historical()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        performance = response.parse()
        assert_matches_type(PerformanceRetrieveHistoricalResponse, performance, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_historical(self, client: Jocall3) -> None:
        with client.investments.performance.with_streaming_response.retrieve_historical() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            performance = response.parse()
            assert_matches_type(PerformanceRetrieveHistoricalResponse, performance, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPerformance:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve_historical(self, async_client: AsyncJocall3) -> None:
        performance = await async_client.investments.performance.retrieve_historical()
        assert_matches_type(PerformanceRetrieveHistoricalResponse, performance, path=["response"])

    @parametrize
    async def test_method_retrieve_historical_with_all_params(self, async_client: AsyncJocall3) -> None:
        performance = await async_client.investments.performance.retrieve_historical(
            range="1m",
        )
        assert_matches_type(PerformanceRetrieveHistoricalResponse, performance, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_historical(self, async_client: AsyncJocall3) -> None:
        response = await async_client.investments.performance.with_raw_response.retrieve_historical()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        performance = await response.parse()
        assert_matches_type(PerformanceRetrieveHistoricalResponse, performance, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_historical(self, async_client: AsyncJocall3) -> None:
        async with async_client.investments.performance.with_streaming_response.retrieve_historical() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            performance = await response.parse()
            assert_matches_type(PerformanceRetrieveHistoricalResponse, performance, path=["response"])

        assert cast(Any, response.is_closed) is True
