# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3
from tests.utils import assert_matches_type
from jocall3.types.corporate import (
    TreasuryOptimizeLiquidityResponse,
    TreasuryRetrieveCashFlowForecastResponse,
    TreasuryRetrieveLiquidityPositionsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTreasury:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_execute_bulk_payouts(self, client: Jocall3) -> None:
        treasury = client.corporate.treasury.execute_bulk_payouts(
            payouts=[{}],
        )
        assert treasury is None

    @parametrize
    def test_raw_response_execute_bulk_payouts(self, client: Jocall3) -> None:
        response = client.corporate.treasury.with_raw_response.execute_bulk_payouts(
            payouts=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        treasury = response.parse()
        assert treasury is None

    @parametrize
    def test_streaming_response_execute_bulk_payouts(self, client: Jocall3) -> None:
        with client.corporate.treasury.with_streaming_response.execute_bulk_payouts(
            payouts=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            treasury = response.parse()
            assert treasury is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_optimize_liquidity(self, client: Jocall3) -> None:
        treasury = client.corporate.treasury.optimize_liquidity()
        assert_matches_type(TreasuryOptimizeLiquidityResponse, treasury, path=["response"])

    @parametrize
    def test_method_optimize_liquidity_with_all_params(self, client: Jocall3) -> None:
        treasury = client.corporate.treasury.optimize_liquidity(
            sweep_excess=True,
            target_reserve=0,
        )
        assert_matches_type(TreasuryOptimizeLiquidityResponse, treasury, path=["response"])

    @parametrize
    def test_raw_response_optimize_liquidity(self, client: Jocall3) -> None:
        response = client.corporate.treasury.with_raw_response.optimize_liquidity()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        treasury = response.parse()
        assert_matches_type(TreasuryOptimizeLiquidityResponse, treasury, path=["response"])

    @parametrize
    def test_streaming_response_optimize_liquidity(self, client: Jocall3) -> None:
        with client.corporate.treasury.with_streaming_response.optimize_liquidity() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            treasury = response.parse()
            assert_matches_type(TreasuryOptimizeLiquidityResponse, treasury, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_cash_flow_forecast(self, client: Jocall3) -> None:
        treasury = client.corporate.treasury.retrieve_cash_flow_forecast()
        assert_matches_type(TreasuryRetrieveCashFlowForecastResponse, treasury, path=["response"])

    @parametrize
    def test_method_retrieve_cash_flow_forecast_with_all_params(self, client: Jocall3) -> None:
        treasury = client.corporate.treasury.retrieve_cash_flow_forecast(
            horizon_days=0,
        )
        assert_matches_type(TreasuryRetrieveCashFlowForecastResponse, treasury, path=["response"])

    @parametrize
    def test_raw_response_retrieve_cash_flow_forecast(self, client: Jocall3) -> None:
        response = client.corporate.treasury.with_raw_response.retrieve_cash_flow_forecast()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        treasury = response.parse()
        assert_matches_type(TreasuryRetrieveCashFlowForecastResponse, treasury, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_cash_flow_forecast(self, client: Jocall3) -> None:
        with client.corporate.treasury.with_streaming_response.retrieve_cash_flow_forecast() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            treasury = response.parse()
            assert_matches_type(TreasuryRetrieveCashFlowForecastResponse, treasury, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_liquidity_positions(self, client: Jocall3) -> None:
        treasury = client.corporate.treasury.retrieve_liquidity_positions()
        assert_matches_type(TreasuryRetrieveLiquidityPositionsResponse, treasury, path=["response"])

    @parametrize
    def test_raw_response_retrieve_liquidity_positions(self, client: Jocall3) -> None:
        response = client.corporate.treasury.with_raw_response.retrieve_liquidity_positions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        treasury = response.parse()
        assert_matches_type(TreasuryRetrieveLiquidityPositionsResponse, treasury, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_liquidity_positions(self, client: Jocall3) -> None:
        with client.corporate.treasury.with_streaming_response.retrieve_liquidity_positions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            treasury = response.parse()
            assert_matches_type(TreasuryRetrieveLiquidityPositionsResponse, treasury, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTreasury:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_execute_bulk_payouts(self, async_client: AsyncJocall3) -> None:
        treasury = await async_client.corporate.treasury.execute_bulk_payouts(
            payouts=[{}],
        )
        assert treasury is None

    @parametrize
    async def test_raw_response_execute_bulk_payouts(self, async_client: AsyncJocall3) -> None:
        response = await async_client.corporate.treasury.with_raw_response.execute_bulk_payouts(
            payouts=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        treasury = await response.parse()
        assert treasury is None

    @parametrize
    async def test_streaming_response_execute_bulk_payouts(self, async_client: AsyncJocall3) -> None:
        async with async_client.corporate.treasury.with_streaming_response.execute_bulk_payouts(
            payouts=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            treasury = await response.parse()
            assert treasury is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_optimize_liquidity(self, async_client: AsyncJocall3) -> None:
        treasury = await async_client.corporate.treasury.optimize_liquidity()
        assert_matches_type(TreasuryOptimizeLiquidityResponse, treasury, path=["response"])

    @parametrize
    async def test_method_optimize_liquidity_with_all_params(self, async_client: AsyncJocall3) -> None:
        treasury = await async_client.corporate.treasury.optimize_liquidity(
            sweep_excess=True,
            target_reserve=0,
        )
        assert_matches_type(TreasuryOptimizeLiquidityResponse, treasury, path=["response"])

    @parametrize
    async def test_raw_response_optimize_liquidity(self, async_client: AsyncJocall3) -> None:
        response = await async_client.corporate.treasury.with_raw_response.optimize_liquidity()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        treasury = await response.parse()
        assert_matches_type(TreasuryOptimizeLiquidityResponse, treasury, path=["response"])

    @parametrize
    async def test_streaming_response_optimize_liquidity(self, async_client: AsyncJocall3) -> None:
        async with async_client.corporate.treasury.with_streaming_response.optimize_liquidity() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            treasury = await response.parse()
            assert_matches_type(TreasuryOptimizeLiquidityResponse, treasury, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_cash_flow_forecast(self, async_client: AsyncJocall3) -> None:
        treasury = await async_client.corporate.treasury.retrieve_cash_flow_forecast()
        assert_matches_type(TreasuryRetrieveCashFlowForecastResponse, treasury, path=["response"])

    @parametrize
    async def test_method_retrieve_cash_flow_forecast_with_all_params(self, async_client: AsyncJocall3) -> None:
        treasury = await async_client.corporate.treasury.retrieve_cash_flow_forecast(
            horizon_days=0,
        )
        assert_matches_type(TreasuryRetrieveCashFlowForecastResponse, treasury, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_cash_flow_forecast(self, async_client: AsyncJocall3) -> None:
        response = await async_client.corporate.treasury.with_raw_response.retrieve_cash_flow_forecast()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        treasury = await response.parse()
        assert_matches_type(TreasuryRetrieveCashFlowForecastResponse, treasury, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_cash_flow_forecast(self, async_client: AsyncJocall3) -> None:
        async with async_client.corporate.treasury.with_streaming_response.retrieve_cash_flow_forecast() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            treasury = await response.parse()
            assert_matches_type(TreasuryRetrieveCashFlowForecastResponse, treasury, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_liquidity_positions(self, async_client: AsyncJocall3) -> None:
        treasury = await async_client.corporate.treasury.retrieve_liquidity_positions()
        assert_matches_type(TreasuryRetrieveLiquidityPositionsResponse, treasury, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_liquidity_positions(self, async_client: AsyncJocall3) -> None:
        response = await async_client.corporate.treasury.with_raw_response.retrieve_liquidity_positions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        treasury = await response.parse()
        assert_matches_type(TreasuryRetrieveLiquidityPositionsResponse, treasury, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_liquidity_positions(self, async_client: AsyncJocall3) -> None:
        async with async_client.corporate.treasury.with_streaming_response.retrieve_liquidity_positions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            treasury = await response.parse()
            assert_matches_type(TreasuryRetrieveLiquidityPositionsResponse, treasury, path=["response"])

        assert cast(Any, response.is_closed) is True
