# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3
from tests.utils import assert_matches_type
from jocall3.types.ai import (
    IncubatorValidateIdeaResponse,
    IncubatorGeneratePitchResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIncubator:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_generate_pitch(self, client: Jocall3) -> None:
        incubator = client.ai.incubator.generate_pitch(
            business_plan="businessPlan",
            financial_projections={},
            founding_team=[{}],
            market_opportunity="marketOpportunity",
        )
        assert_matches_type(IncubatorGeneratePitchResponse, incubator, path=["response"])

    @parametrize
    def test_raw_response_generate_pitch(self, client: Jocall3) -> None:
        response = client.ai.incubator.with_raw_response.generate_pitch(
            business_plan="businessPlan",
            financial_projections={},
            founding_team=[{}],
            market_opportunity="marketOpportunity",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        incubator = response.parse()
        assert_matches_type(IncubatorGeneratePitchResponse, incubator, path=["response"])

    @parametrize
    def test_streaming_response_generate_pitch(self, client: Jocall3) -> None:
        with client.ai.incubator.with_streaming_response.generate_pitch(
            business_plan="businessPlan",
            financial_projections={},
            founding_team=[{}],
            market_opportunity="marketOpportunity",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            incubator = response.parse()
            assert_matches_type(IncubatorGeneratePitchResponse, incubator, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_validate_idea(self, client: Jocall3) -> None:
        incubator = client.ai.incubator.validate_idea(
            concept="concept",
        )
        assert_matches_type(IncubatorValidateIdeaResponse, incubator, path=["response"])

    @parametrize
    def test_raw_response_validate_idea(self, client: Jocall3) -> None:
        response = client.ai.incubator.with_raw_response.validate_idea(
            concept="concept",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        incubator = response.parse()
        assert_matches_type(IncubatorValidateIdeaResponse, incubator, path=["response"])

    @parametrize
    def test_streaming_response_validate_idea(self, client: Jocall3) -> None:
        with client.ai.incubator.with_streaming_response.validate_idea(
            concept="concept",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            incubator = response.parse()
            assert_matches_type(IncubatorValidateIdeaResponse, incubator, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIncubator:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_generate_pitch(self, async_client: AsyncJocall3) -> None:
        incubator = await async_client.ai.incubator.generate_pitch(
            business_plan="businessPlan",
            financial_projections={},
            founding_team=[{}],
            market_opportunity="marketOpportunity",
        )
        assert_matches_type(IncubatorGeneratePitchResponse, incubator, path=["response"])

    @parametrize
    async def test_raw_response_generate_pitch(self, async_client: AsyncJocall3) -> None:
        response = await async_client.ai.incubator.with_raw_response.generate_pitch(
            business_plan="businessPlan",
            financial_projections={},
            founding_team=[{}],
            market_opportunity="marketOpportunity",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        incubator = await response.parse()
        assert_matches_type(IncubatorGeneratePitchResponse, incubator, path=["response"])

    @parametrize
    async def test_streaming_response_generate_pitch(self, async_client: AsyncJocall3) -> None:
        async with async_client.ai.incubator.with_streaming_response.generate_pitch(
            business_plan="businessPlan",
            financial_projections={},
            founding_team=[{}],
            market_opportunity="marketOpportunity",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            incubator = await response.parse()
            assert_matches_type(IncubatorGeneratePitchResponse, incubator, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_validate_idea(self, async_client: AsyncJocall3) -> None:
        incubator = await async_client.ai.incubator.validate_idea(
            concept="concept",
        )
        assert_matches_type(IncubatorValidateIdeaResponse, incubator, path=["response"])

    @parametrize
    async def test_raw_response_validate_idea(self, async_client: AsyncJocall3) -> None:
        response = await async_client.ai.incubator.with_raw_response.validate_idea(
            concept="concept",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        incubator = await response.parse()
        assert_matches_type(IncubatorValidateIdeaResponse, incubator, path=["response"])

    @parametrize
    async def test_streaming_response_validate_idea(self, async_client: AsyncJocall3) -> None:
        async with async_client.ai.incubator.with_streaming_response.validate_idea(
            concept="concept",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            incubator = await response.parse()
            assert_matches_type(IncubatorValidateIdeaResponse, incubator, path=["response"])

        assert cast(Any, response.is_closed) is True
