# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3
from tests.utils import assert_matches_type
from jocall3.types.corporate import (
    TreasuryManageLiquidityResponse,
    TreasuryForecastCashFlowResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTreasury:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_forecast_cash_flow(self, client: Jocall3) -> None:
        treasury = client.corporate.treasury.forecast_cash_flow()
        assert_matches_type(TreasuryForecastCashFlowResponse, treasury, path=["response"])

    @parametrize
    def test_method_forecast_cash_flow_with_all_params(self, client: Jocall3) -> None:
        treasury = client.corporate.treasury.forecast_cash_flow(
            horizon_days=0,
        )
        assert_matches_type(TreasuryForecastCashFlowResponse, treasury, path=["response"])

    @parametrize
    def test_raw_response_forecast_cash_flow(self, client: Jocall3) -> None:
        response = client.corporate.treasury.with_raw_response.forecast_cash_flow()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        treasury = response.parse()
        assert_matches_type(TreasuryForecastCashFlowResponse, treasury, path=["response"])

    @parametrize
    def test_streaming_response_forecast_cash_flow(self, client: Jocall3) -> None:
        with client.corporate.treasury.with_streaming_response.forecast_cash_flow() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            treasury = response.parse()
            assert_matches_type(TreasuryForecastCashFlowResponse, treasury, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_manage_liquidity(self, client: Jocall3) -> None:
        treasury = client.corporate.treasury.manage_liquidity()
        assert_matches_type(TreasuryManageLiquidityResponse, treasury, path=["response"])

    @parametrize
    def test_method_manage_liquidity_with_all_params(self, client: Jocall3) -> None:
        treasury = client.corporate.treasury.manage_liquidity(
            sweep_excess=True,
            target_reserve=0,
        )
        assert_matches_type(TreasuryManageLiquidityResponse, treasury, path=["response"])

    @parametrize
    def test_raw_response_manage_liquidity(self, client: Jocall3) -> None:
        response = client.corporate.treasury.with_raw_response.manage_liquidity()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        treasury = response.parse()
        assert_matches_type(TreasuryManageLiquidityResponse, treasury, path=["response"])

    @parametrize
    def test_streaming_response_manage_liquidity(self, client: Jocall3) -> None:
        with client.corporate.treasury.with_streaming_response.manage_liquidity() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            treasury = response.parse()
            assert_matches_type(TreasuryManageLiquidityResponse, treasury, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTreasury:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_forecast_cash_flow(self, async_client: AsyncJocall3) -> None:
        treasury = await async_client.corporate.treasury.forecast_cash_flow()
        assert_matches_type(TreasuryForecastCashFlowResponse, treasury, path=["response"])

    @parametrize
    async def test_method_forecast_cash_flow_with_all_params(self, async_client: AsyncJocall3) -> None:
        treasury = await async_client.corporate.treasury.forecast_cash_flow(
            horizon_days=0,
        )
        assert_matches_type(TreasuryForecastCashFlowResponse, treasury, path=["response"])

    @parametrize
    async def test_raw_response_forecast_cash_flow(self, async_client: AsyncJocall3) -> None:
        response = await async_client.corporate.treasury.with_raw_response.forecast_cash_flow()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        treasury = await response.parse()
        assert_matches_type(TreasuryForecastCashFlowResponse, treasury, path=["response"])

    @parametrize
    async def test_streaming_response_forecast_cash_flow(self, async_client: AsyncJocall3) -> None:
        async with async_client.corporate.treasury.with_streaming_response.forecast_cash_flow() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            treasury = await response.parse()
            assert_matches_type(TreasuryForecastCashFlowResponse, treasury, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_manage_liquidity(self, async_client: AsyncJocall3) -> None:
        treasury = await async_client.corporate.treasury.manage_liquidity()
        assert_matches_type(TreasuryManageLiquidityResponse, treasury, path=["response"])

    @parametrize
    async def test_method_manage_liquidity_with_all_params(self, async_client: AsyncJocall3) -> None:
        treasury = await async_client.corporate.treasury.manage_liquidity(
            sweep_excess=True,
            target_reserve=0,
        )
        assert_matches_type(TreasuryManageLiquidityResponse, treasury, path=["response"])

    @parametrize
    async def test_raw_response_manage_liquidity(self, async_client: AsyncJocall3) -> None:
        response = await async_client.corporate.treasury.with_raw_response.manage_liquidity()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        treasury = await response.parse()
        assert_matches_type(TreasuryManageLiquidityResponse, treasury, path=["response"])

    @parametrize
    async def test_streaming_response_manage_liquidity(self, async_client: AsyncJocall3) -> None:
        async with async_client.corporate.treasury.with_streaming_response.manage_liquidity() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            treasury = await response.parse()
            assert_matches_type(TreasuryManageLiquidityResponse, treasury, path=["response"])

        assert cast(Any, response.is_closed) is True
