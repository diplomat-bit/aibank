# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3
from tests.utils import assert_matches_type
from jocall3.types.ai.oracle import (
    PredictionInflationResponse,
    PredictionMarketCrashResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPredictions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_inflation(self, client: Jocall3) -> None:
        prediction = client.ai.oracle.predictions.inflation()
        assert_matches_type(PredictionInflationResponse, prediction, path=["response"])

    @parametrize
    def test_method_inflation_with_all_params(self, client: Jocall3) -> None:
        prediction = client.ai.oracle.predictions.inflation(
            region="region",
        )
        assert_matches_type(PredictionInflationResponse, prediction, path=["response"])

    @parametrize
    def test_raw_response_inflation(self, client: Jocall3) -> None:
        response = client.ai.oracle.predictions.with_raw_response.inflation()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prediction = response.parse()
        assert_matches_type(PredictionInflationResponse, prediction, path=["response"])

    @parametrize
    def test_streaming_response_inflation(self, client: Jocall3) -> None:
        with client.ai.oracle.predictions.with_streaming_response.inflation() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prediction = response.parse()
            assert_matches_type(PredictionInflationResponse, prediction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_market_crash(self, client: Jocall3) -> None:
        prediction = client.ai.oracle.predictions.market_crash()
        assert_matches_type(PredictionMarketCrashResponse, prediction, path=["response"])

    @parametrize
    def test_raw_response_market_crash(self, client: Jocall3) -> None:
        response = client.ai.oracle.predictions.with_raw_response.market_crash()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prediction = response.parse()
        assert_matches_type(PredictionMarketCrashResponse, prediction, path=["response"])

    @parametrize
    def test_streaming_response_market_crash(self, client: Jocall3) -> None:
        with client.ai.oracle.predictions.with_streaming_response.market_crash() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prediction = response.parse()
            assert_matches_type(PredictionMarketCrashResponse, prediction, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPredictions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_inflation(self, async_client: AsyncJocall3) -> None:
        prediction = await async_client.ai.oracle.predictions.inflation()
        assert_matches_type(PredictionInflationResponse, prediction, path=["response"])

    @parametrize
    async def test_method_inflation_with_all_params(self, async_client: AsyncJocall3) -> None:
        prediction = await async_client.ai.oracle.predictions.inflation(
            region="region",
        )
        assert_matches_type(PredictionInflationResponse, prediction, path=["response"])

    @parametrize
    async def test_raw_response_inflation(self, async_client: AsyncJocall3) -> None:
        response = await async_client.ai.oracle.predictions.with_raw_response.inflation()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prediction = await response.parse()
        assert_matches_type(PredictionInflationResponse, prediction, path=["response"])

    @parametrize
    async def test_streaming_response_inflation(self, async_client: AsyncJocall3) -> None:
        async with async_client.ai.oracle.predictions.with_streaming_response.inflation() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prediction = await response.parse()
            assert_matches_type(PredictionInflationResponse, prediction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_market_crash(self, async_client: AsyncJocall3) -> None:
        prediction = await async_client.ai.oracle.predictions.market_crash()
        assert_matches_type(PredictionMarketCrashResponse, prediction, path=["response"])

    @parametrize
    async def test_raw_response_market_crash(self, async_client: AsyncJocall3) -> None:
        response = await async_client.ai.oracle.predictions.with_raw_response.market_crash()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prediction = await response.parse()
        assert_matches_type(PredictionMarketCrashResponse, prediction, path=["response"])

    @parametrize
    async def test_streaming_response_market_crash(self, async_client: AsyncJocall3) -> None:
        async with async_client.ai.oracle.predictions.with_streaming_response.market_crash() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prediction = await response.parse()
            assert_matches_type(PredictionMarketCrashResponse, prediction, path=["response"])

        assert cast(Any, response.is_closed) is True
