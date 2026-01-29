# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3
from tests.utils import assert_matches_type
from jocall3.types.ai.oracle import (
    SimulateRunAdvancedResponse,
    SimulateRunStandardResponse,
    SimulateRunMonteCarloResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSimulate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_run_advanced(self, client: Jocall3) -> None:
        simulate = client.ai.oracle.simulate.run_advanced(
            prompt="prompt",
            scenarios=[{"name": "name"}],
        )
        assert_matches_type(SimulateRunAdvancedResponse, simulate, path=["response"])

    @parametrize
    def test_method_run_advanced_with_all_params(self, client: Jocall3) -> None:
        simulate = client.ai.oracle.simulate.run_advanced(
            prompt="prompt",
            scenarios=[
                {
                    "name": "name",
                    "description": "description",
                    "variables": {"foo": "bar"},
                }
            ],
            global_economic_factors={},
            personal_assumptions={},
        )
        assert_matches_type(SimulateRunAdvancedResponse, simulate, path=["response"])

    @parametrize
    def test_raw_response_run_advanced(self, client: Jocall3) -> None:
        response = client.ai.oracle.simulate.with_raw_response.run_advanced(
            prompt="prompt",
            scenarios=[{"name": "name"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulate = response.parse()
        assert_matches_type(SimulateRunAdvancedResponse, simulate, path=["response"])

    @parametrize
    def test_streaming_response_run_advanced(self, client: Jocall3) -> None:
        with client.ai.oracle.simulate.with_streaming_response.run_advanced(
            prompt="prompt",
            scenarios=[{"name": "name"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulate = response.parse()
            assert_matches_type(SimulateRunAdvancedResponse, simulate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_run_monte_carlo(self, client: Jocall3) -> None:
        simulate = client.ai.oracle.simulate.run_monte_carlo(
            iterations=100,
            variables=["inflation", "oil_prices"],
        )
        assert_matches_type(SimulateRunMonteCarloResponse, simulate, path=["response"])

    @parametrize
    def test_method_run_monte_carlo_with_all_params(self, client: Jocall3) -> None:
        simulate = client.ai.oracle.simulate.run_monte_carlo(
            iterations=100,
            variables=["inflation", "oil_prices"],
            confidence_interval=0,
        )
        assert_matches_type(SimulateRunMonteCarloResponse, simulate, path=["response"])

    @parametrize
    def test_raw_response_run_monte_carlo(self, client: Jocall3) -> None:
        response = client.ai.oracle.simulate.with_raw_response.run_monte_carlo(
            iterations=100,
            variables=["inflation", "oil_prices"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulate = response.parse()
        assert_matches_type(SimulateRunMonteCarloResponse, simulate, path=["response"])

    @parametrize
    def test_streaming_response_run_monte_carlo(self, client: Jocall3) -> None:
        with client.ai.oracle.simulate.with_streaming_response.run_monte_carlo(
            iterations=100,
            variables=["inflation", "oil_prices"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulate = response.parse()
            assert_matches_type(SimulateRunMonteCarloResponse, simulate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_run_standard(self, client: Jocall3) -> None:
        simulate = client.ai.oracle.simulate.run_standard(
            prompt="prompt",
        )
        assert_matches_type(SimulateRunStandardResponse, simulate, path=["response"])

    @parametrize
    def test_method_run_standard_with_all_params(self, client: Jocall3) -> None:
        simulate = client.ai.oracle.simulate.run_standard(
            prompt="prompt",
            parameters={},
        )
        assert_matches_type(SimulateRunStandardResponse, simulate, path=["response"])

    @parametrize
    def test_raw_response_run_standard(self, client: Jocall3) -> None:
        response = client.ai.oracle.simulate.with_raw_response.run_standard(
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulate = response.parse()
        assert_matches_type(SimulateRunStandardResponse, simulate, path=["response"])

    @parametrize
    def test_streaming_response_run_standard(self, client: Jocall3) -> None:
        with client.ai.oracle.simulate.with_streaming_response.run_standard(
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulate = response.parse()
            assert_matches_type(SimulateRunStandardResponse, simulate, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSimulate:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_run_advanced(self, async_client: AsyncJocall3) -> None:
        simulate = await async_client.ai.oracle.simulate.run_advanced(
            prompt="prompt",
            scenarios=[{"name": "name"}],
        )
        assert_matches_type(SimulateRunAdvancedResponse, simulate, path=["response"])

    @parametrize
    async def test_method_run_advanced_with_all_params(self, async_client: AsyncJocall3) -> None:
        simulate = await async_client.ai.oracle.simulate.run_advanced(
            prompt="prompt",
            scenarios=[
                {
                    "name": "name",
                    "description": "description",
                    "variables": {"foo": "bar"},
                }
            ],
            global_economic_factors={},
            personal_assumptions={},
        )
        assert_matches_type(SimulateRunAdvancedResponse, simulate, path=["response"])

    @parametrize
    async def test_raw_response_run_advanced(self, async_client: AsyncJocall3) -> None:
        response = await async_client.ai.oracle.simulate.with_raw_response.run_advanced(
            prompt="prompt",
            scenarios=[{"name": "name"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulate = await response.parse()
        assert_matches_type(SimulateRunAdvancedResponse, simulate, path=["response"])

    @parametrize
    async def test_streaming_response_run_advanced(self, async_client: AsyncJocall3) -> None:
        async with async_client.ai.oracle.simulate.with_streaming_response.run_advanced(
            prompt="prompt",
            scenarios=[{"name": "name"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulate = await response.parse()
            assert_matches_type(SimulateRunAdvancedResponse, simulate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_run_monte_carlo(self, async_client: AsyncJocall3) -> None:
        simulate = await async_client.ai.oracle.simulate.run_monte_carlo(
            iterations=100,
            variables=["inflation", "oil_prices"],
        )
        assert_matches_type(SimulateRunMonteCarloResponse, simulate, path=["response"])

    @parametrize
    async def test_method_run_monte_carlo_with_all_params(self, async_client: AsyncJocall3) -> None:
        simulate = await async_client.ai.oracle.simulate.run_monte_carlo(
            iterations=100,
            variables=["inflation", "oil_prices"],
            confidence_interval=0,
        )
        assert_matches_type(SimulateRunMonteCarloResponse, simulate, path=["response"])

    @parametrize
    async def test_raw_response_run_monte_carlo(self, async_client: AsyncJocall3) -> None:
        response = await async_client.ai.oracle.simulate.with_raw_response.run_monte_carlo(
            iterations=100,
            variables=["inflation", "oil_prices"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulate = await response.parse()
        assert_matches_type(SimulateRunMonteCarloResponse, simulate, path=["response"])

    @parametrize
    async def test_streaming_response_run_monte_carlo(self, async_client: AsyncJocall3) -> None:
        async with async_client.ai.oracle.simulate.with_streaming_response.run_monte_carlo(
            iterations=100,
            variables=["inflation", "oil_prices"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulate = await response.parse()
            assert_matches_type(SimulateRunMonteCarloResponse, simulate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_run_standard(self, async_client: AsyncJocall3) -> None:
        simulate = await async_client.ai.oracle.simulate.run_standard(
            prompt="prompt",
        )
        assert_matches_type(SimulateRunStandardResponse, simulate, path=["response"])

    @parametrize
    async def test_method_run_standard_with_all_params(self, async_client: AsyncJocall3) -> None:
        simulate = await async_client.ai.oracle.simulate.run_standard(
            prompt="prompt",
            parameters={},
        )
        assert_matches_type(SimulateRunStandardResponse, simulate, path=["response"])

    @parametrize
    async def test_raw_response_run_standard(self, async_client: AsyncJocall3) -> None:
        response = await async_client.ai.oracle.simulate.with_raw_response.run_standard(
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulate = await response.parse()
        assert_matches_type(SimulateRunStandardResponse, simulate, path=["response"])

    @parametrize
    async def test_streaming_response_run_standard(self, async_client: AsyncJocall3) -> None:
        async with async_client.ai.oracle.simulate.with_streaming_response.run_standard(
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulate = await response.parse()
            assert_matches_type(SimulateRunStandardResponse, simulate, path=["response"])

        assert cast(Any, response.is_closed) is True
