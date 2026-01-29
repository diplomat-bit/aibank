# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3
from tests.utils import assert_matches_type
from jocall3.types.ai.incubator import (
    AnalysisSwotResponse,
    AnalysisCompetitorScanResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAnalysis:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_competitor_scan(self, client: Jocall3) -> None:
        analysis = client.ai.incubator.analysis.competitor_scan(
            industry="industry",
            niche="niche",
        )
        assert_matches_type(AnalysisCompetitorScanResponse, analysis, path=["response"])

    @parametrize
    def test_raw_response_competitor_scan(self, client: Jocall3) -> None:
        response = client.ai.incubator.analysis.with_raw_response.competitor_scan(
            industry="industry",
            niche="niche",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analysis = response.parse()
        assert_matches_type(AnalysisCompetitorScanResponse, analysis, path=["response"])

    @parametrize
    def test_streaming_response_competitor_scan(self, client: Jocall3) -> None:
        with client.ai.incubator.analysis.with_streaming_response.competitor_scan(
            industry="industry",
            niche="niche",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analysis = response.parse()
            assert_matches_type(AnalysisCompetitorScanResponse, analysis, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_swot(self, client: Jocall3) -> None:
        analysis = client.ai.incubator.analysis.swot(
            business_context="businessContext",
        )
        assert_matches_type(AnalysisSwotResponse, analysis, path=["response"])

    @parametrize
    def test_raw_response_swot(self, client: Jocall3) -> None:
        response = client.ai.incubator.analysis.with_raw_response.swot(
            business_context="businessContext",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analysis = response.parse()
        assert_matches_type(AnalysisSwotResponse, analysis, path=["response"])

    @parametrize
    def test_streaming_response_swot(self, client: Jocall3) -> None:
        with client.ai.incubator.analysis.with_streaming_response.swot(
            business_context="businessContext",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analysis = response.parse()
            assert_matches_type(AnalysisSwotResponse, analysis, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAnalysis:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_competitor_scan(self, async_client: AsyncJocall3) -> None:
        analysis = await async_client.ai.incubator.analysis.competitor_scan(
            industry="industry",
            niche="niche",
        )
        assert_matches_type(AnalysisCompetitorScanResponse, analysis, path=["response"])

    @parametrize
    async def test_raw_response_competitor_scan(self, async_client: AsyncJocall3) -> None:
        response = await async_client.ai.incubator.analysis.with_raw_response.competitor_scan(
            industry="industry",
            niche="niche",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analysis = await response.parse()
        assert_matches_type(AnalysisCompetitorScanResponse, analysis, path=["response"])

    @parametrize
    async def test_streaming_response_competitor_scan(self, async_client: AsyncJocall3) -> None:
        async with async_client.ai.incubator.analysis.with_streaming_response.competitor_scan(
            industry="industry",
            niche="niche",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analysis = await response.parse()
            assert_matches_type(AnalysisCompetitorScanResponse, analysis, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_swot(self, async_client: AsyncJocall3) -> None:
        analysis = await async_client.ai.incubator.analysis.swot(
            business_context="businessContext",
        )
        assert_matches_type(AnalysisSwotResponse, analysis, path=["response"])

    @parametrize
    async def test_raw_response_swot(self, async_client: AsyncJocall3) -> None:
        response = await async_client.ai.incubator.analysis.with_raw_response.swot(
            business_context="businessContext",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analysis = await response.parse()
        assert_matches_type(AnalysisSwotResponse, analysis, path=["response"])

    @parametrize
    async def test_streaming_response_swot(self, async_client: AsyncJocall3) -> None:
        async with async_client.ai.incubator.analysis.with_streaming_response.swot(
            business_context="businessContext",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analysis = await response.parse()
            assert_matches_type(AnalysisSwotResponse, analysis, path=["response"])

        assert cast(Any, response.is_closed) is True
