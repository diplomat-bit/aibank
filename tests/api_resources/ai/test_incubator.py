# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIncubator:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_generate_pitch(self, client: Jocall3) -> None:
        incubator = client.ai.incubator.generate_pitch(
            financial_projections={
                "seedRoundAmount": 2500000,
                "valuationPreMoney": 10000000,
                "projectionYears": 3,
                "revenueForecast": [500000, 2000000, 6000000],
                "profitabilityEstimate": "Achieve profitability within 18 months.",
            },
        )
        assert_matches_type(object, incubator, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_generate_pitch(self, client: Jocall3) -> None:
        response = client.ai.incubator.with_raw_response.generate_pitch(
            financial_projections={
                "seedRoundAmount": 2500000,
                "valuationPreMoney": 10000000,
                "projectionYears": 3,
                "revenueForecast": [500000, 2000000, 6000000],
                "profitabilityEstimate": "Achieve profitability within 18 months.",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        incubator = response.parse()
        assert_matches_type(object, incubator, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_generate_pitch(self, client: Jocall3) -> None:
        with client.ai.incubator.with_streaming_response.generate_pitch(
            financial_projections={
                "seedRoundAmount": 2500000,
                "valuationPreMoney": 10000000,
                "projectionYears": 3,
                "revenueForecast": [500000, 2000000, 6000000],
                "profitabilityEstimate": "Achieve profitability within 18 months.",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            incubator = response.parse()
            assert_matches_type(object, incubator, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIncubator:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_generate_pitch(self, async_client: AsyncJocall3) -> None:
        incubator = await async_client.ai.incubator.generate_pitch(
            financial_projections={
                "seedRoundAmount": 2500000,
                "valuationPreMoney": 10000000,
                "projectionYears": 3,
                "revenueForecast": [500000, 2000000, 6000000],
                "profitabilityEstimate": "Achieve profitability within 18 months.",
            },
        )
        assert_matches_type(object, incubator, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_generate_pitch(self, async_client: AsyncJocall3) -> None:
        response = await async_client.ai.incubator.with_raw_response.generate_pitch(
            financial_projections={
                "seedRoundAmount": 2500000,
                "valuationPreMoney": 10000000,
                "projectionYears": 3,
                "revenueForecast": [500000, 2000000, 6000000],
                "profitabilityEstimate": "Achieve profitability within 18 months.",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        incubator = await response.parse()
        assert_matches_type(object, incubator, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_generate_pitch(self, async_client: AsyncJocall3) -> None:
        async with async_client.ai.incubator.with_streaming_response.generate_pitch(
            financial_projections={
                "seedRoundAmount": 2500000,
                "valuationPreMoney": 10000000,
                "projectionYears": 3,
                "revenueForecast": [500000, 2000000, 6000000],
                "profitabilityEstimate": "Achieve profitability within 18 months.",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            incubator = await response.parse()
            assert_matches_type(object, incubator, path=["response"])

        assert cast(Any, response.is_closed) is True
