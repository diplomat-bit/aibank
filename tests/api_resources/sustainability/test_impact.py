# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3
from tests.utils import assert_matches_type
from jocall3.types.sustainability import (
    ImpactListGreenProjectsResponse,
    ImpactRetrievePortfolioAnalysisResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestImpact:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list_green_projects(self, client: Jocall3) -> None:
        impact = client.sustainability.impact.list_green_projects()
        assert_matches_type(ImpactListGreenProjectsResponse, impact, path=["response"])

    @parametrize
    def test_method_list_green_projects_with_all_params(self, client: Jocall3) -> None:
        impact = client.sustainability.impact.list_green_projects(
            continent="continent",
        )
        assert_matches_type(ImpactListGreenProjectsResponse, impact, path=["response"])

    @parametrize
    def test_raw_response_list_green_projects(self, client: Jocall3) -> None:
        response = client.sustainability.impact.with_raw_response.list_green_projects()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        impact = response.parse()
        assert_matches_type(ImpactListGreenProjectsResponse, impact, path=["response"])

    @parametrize
    def test_streaming_response_list_green_projects(self, client: Jocall3) -> None:
        with client.sustainability.impact.with_streaming_response.list_green_projects() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            impact = response.parse()
            assert_matches_type(ImpactListGreenProjectsResponse, impact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_portfolio_analysis(self, client: Jocall3) -> None:
        impact = client.sustainability.impact.retrieve_portfolio_analysis()
        assert_matches_type(ImpactRetrievePortfolioAnalysisResponse, impact, path=["response"])

    @parametrize
    def test_raw_response_retrieve_portfolio_analysis(self, client: Jocall3) -> None:
        response = client.sustainability.impact.with_raw_response.retrieve_portfolio_analysis()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        impact = response.parse()
        assert_matches_type(ImpactRetrievePortfolioAnalysisResponse, impact, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_portfolio_analysis(self, client: Jocall3) -> None:
        with client.sustainability.impact.with_streaming_response.retrieve_portfolio_analysis() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            impact = response.parse()
            assert_matches_type(ImpactRetrievePortfolioAnalysisResponse, impact, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncImpact:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list_green_projects(self, async_client: AsyncJocall3) -> None:
        impact = await async_client.sustainability.impact.list_green_projects()
        assert_matches_type(ImpactListGreenProjectsResponse, impact, path=["response"])

    @parametrize
    async def test_method_list_green_projects_with_all_params(self, async_client: AsyncJocall3) -> None:
        impact = await async_client.sustainability.impact.list_green_projects(
            continent="continent",
        )
        assert_matches_type(ImpactListGreenProjectsResponse, impact, path=["response"])

    @parametrize
    async def test_raw_response_list_green_projects(self, async_client: AsyncJocall3) -> None:
        response = await async_client.sustainability.impact.with_raw_response.list_green_projects()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        impact = await response.parse()
        assert_matches_type(ImpactListGreenProjectsResponse, impact, path=["response"])

    @parametrize
    async def test_streaming_response_list_green_projects(self, async_client: AsyncJocall3) -> None:
        async with async_client.sustainability.impact.with_streaming_response.list_green_projects() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            impact = await response.parse()
            assert_matches_type(ImpactListGreenProjectsResponse, impact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_portfolio_analysis(self, async_client: AsyncJocall3) -> None:
        impact = await async_client.sustainability.impact.retrieve_portfolio_analysis()
        assert_matches_type(ImpactRetrievePortfolioAnalysisResponse, impact, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_portfolio_analysis(self, async_client: AsyncJocall3) -> None:
        response = await async_client.sustainability.impact.with_raw_response.retrieve_portfolio_analysis()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        impact = await response.parse()
        assert_matches_type(ImpactRetrievePortfolioAnalysisResponse, impact, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_portfolio_analysis(self, async_client: AsyncJocall3) -> None:
        async with async_client.sustainability.impact.with_streaming_response.retrieve_portfolio_analysis() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            impact = await response.parse()
            assert_matches_type(ImpactRetrievePortfolioAnalysisResponse, impact, path=["response"])

        assert cast(Any, response.is_closed) is True
