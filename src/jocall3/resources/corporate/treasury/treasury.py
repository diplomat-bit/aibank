# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from .pooling import (
    PoolingResource,
    AsyncPoolingResource,
    PoolingResourceWithRawResponse,
    AsyncPoolingResourceWithRawResponse,
    PoolingResourceWithStreamingResponse,
    AsyncPoolingResourceWithStreamingResponse,
)
from .sweeping import (
    SweepingResource,
    AsyncSweepingResource,
    SweepingResourceWithRawResponse,
    AsyncSweepingResourceWithRawResponse,
    SweepingResourceWithStreamingResponse,
    AsyncSweepingResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.corporate import (
    treasury_optimize_liquidity_params,
    treasury_execute_bulk_payouts_params,
    treasury_retrieve_cash_flow_forecast_params,
)
from ....types.corporate.treasury_optimize_liquidity_response import TreasuryOptimizeLiquidityResponse
from ....types.corporate.treasury_retrieve_cash_flow_forecast_response import TreasuryRetrieveCashFlowForecastResponse
from ....types.corporate.treasury_retrieve_liquidity_positions_response import (
    TreasuryRetrieveLiquidityPositionsResponse,
)

__all__ = ["TreasuryResource", "AsyncTreasuryResource"]


class TreasuryResource(SyncAPIResource):
    @cached_property
    def sweeping(self) -> SweepingResource:
        return SweepingResource(self._client)

    @cached_property
    def pooling(self) -> PoolingResource:
        return PoolingResource(self._client)

    @cached_property
    def with_raw_response(self) -> TreasuryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/diplomat-bit/aibank#accessing-raw-response-data-eg-headers
        """
        return TreasuryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TreasuryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/diplomat-bit/aibank#with_streaming_response
        """
        return TreasuryResourceWithStreamingResponse(self)

    def execute_bulk_payouts(
        self,
        *,
        payouts: Iterable[treasury_execute_bulk_payouts_params.Payout],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Execute bulk payouts

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/corporate/treasury/bulk-payouts",
            body=maybe_transform(
                {"payouts": payouts}, treasury_execute_bulk_payouts_params.TreasuryExecuteBulkPayoutsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def optimize_liquidity(
        self,
        *,
        sweep_excess: bool | Omit = omit,
        target_reserve: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TreasuryOptimizeLiquidityResponse:
        """
        AI Liquidity Optimization Engine

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/corporate/treasury/liquidity/optimize",
            body=maybe_transform(
                {
                    "sweep_excess": sweep_excess,
                    "target_reserve": target_reserve,
                },
                treasury_optimize_liquidity_params.TreasuryOptimizeLiquidityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TreasuryOptimizeLiquidityResponse,
        )

    def retrieve_cash_flow_forecast(
        self,
        *,
        horizon_days: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TreasuryRetrieveCashFlowForecastResponse:
        """
        Corporate Cash Flow Projection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/corporate/treasury/cash-flow/forecast",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"horizon_days": horizon_days},
                    treasury_retrieve_cash_flow_forecast_params.TreasuryRetrieveCashFlowForecastParams,
                ),
            ),
            cast_to=TreasuryRetrieveCashFlowForecastResponse,
        )

    def retrieve_liquidity_positions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TreasuryRetrieveLiquidityPositionsResponse:
        """Get current liquidity positions"""
        return self._get(
            "/corporate/treasury/liquidity-positions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TreasuryRetrieveLiquidityPositionsResponse,
        )


class AsyncTreasuryResource(AsyncAPIResource):
    @cached_property
    def sweeping(self) -> AsyncSweepingResource:
        return AsyncSweepingResource(self._client)

    @cached_property
    def pooling(self) -> AsyncPoolingResource:
        return AsyncPoolingResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTreasuryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/diplomat-bit/aibank#accessing-raw-response-data-eg-headers
        """
        return AsyncTreasuryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTreasuryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/diplomat-bit/aibank#with_streaming_response
        """
        return AsyncTreasuryResourceWithStreamingResponse(self)

    async def execute_bulk_payouts(
        self,
        *,
        payouts: Iterable[treasury_execute_bulk_payouts_params.Payout],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Execute bulk payouts

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/corporate/treasury/bulk-payouts",
            body=await async_maybe_transform(
                {"payouts": payouts}, treasury_execute_bulk_payouts_params.TreasuryExecuteBulkPayoutsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def optimize_liquidity(
        self,
        *,
        sweep_excess: bool | Omit = omit,
        target_reserve: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TreasuryOptimizeLiquidityResponse:
        """
        AI Liquidity Optimization Engine

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/corporate/treasury/liquidity/optimize",
            body=await async_maybe_transform(
                {
                    "sweep_excess": sweep_excess,
                    "target_reserve": target_reserve,
                },
                treasury_optimize_liquidity_params.TreasuryOptimizeLiquidityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TreasuryOptimizeLiquidityResponse,
        )

    async def retrieve_cash_flow_forecast(
        self,
        *,
        horizon_days: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TreasuryRetrieveCashFlowForecastResponse:
        """
        Corporate Cash Flow Projection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/corporate/treasury/cash-flow/forecast",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"horizon_days": horizon_days},
                    treasury_retrieve_cash_flow_forecast_params.TreasuryRetrieveCashFlowForecastParams,
                ),
            ),
            cast_to=TreasuryRetrieveCashFlowForecastResponse,
        )

    async def retrieve_liquidity_positions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TreasuryRetrieveLiquidityPositionsResponse:
        """Get current liquidity positions"""
        return await self._get(
            "/corporate/treasury/liquidity-positions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TreasuryRetrieveLiquidityPositionsResponse,
        )


class TreasuryResourceWithRawResponse:
    def __init__(self, treasury: TreasuryResource) -> None:
        self._treasury = treasury

        self.execute_bulk_payouts = to_raw_response_wrapper(
            treasury.execute_bulk_payouts,
        )
        self.optimize_liquidity = to_raw_response_wrapper(
            treasury.optimize_liquidity,
        )
        self.retrieve_cash_flow_forecast = to_raw_response_wrapper(
            treasury.retrieve_cash_flow_forecast,
        )
        self.retrieve_liquidity_positions = to_raw_response_wrapper(
            treasury.retrieve_liquidity_positions,
        )

    @cached_property
    def sweeping(self) -> SweepingResourceWithRawResponse:
        return SweepingResourceWithRawResponse(self._treasury.sweeping)

    @cached_property
    def pooling(self) -> PoolingResourceWithRawResponse:
        return PoolingResourceWithRawResponse(self._treasury.pooling)


class AsyncTreasuryResourceWithRawResponse:
    def __init__(self, treasury: AsyncTreasuryResource) -> None:
        self._treasury = treasury

        self.execute_bulk_payouts = async_to_raw_response_wrapper(
            treasury.execute_bulk_payouts,
        )
        self.optimize_liquidity = async_to_raw_response_wrapper(
            treasury.optimize_liquidity,
        )
        self.retrieve_cash_flow_forecast = async_to_raw_response_wrapper(
            treasury.retrieve_cash_flow_forecast,
        )
        self.retrieve_liquidity_positions = async_to_raw_response_wrapper(
            treasury.retrieve_liquidity_positions,
        )

    @cached_property
    def sweeping(self) -> AsyncSweepingResourceWithRawResponse:
        return AsyncSweepingResourceWithRawResponse(self._treasury.sweeping)

    @cached_property
    def pooling(self) -> AsyncPoolingResourceWithRawResponse:
        return AsyncPoolingResourceWithRawResponse(self._treasury.pooling)


class TreasuryResourceWithStreamingResponse:
    def __init__(self, treasury: TreasuryResource) -> None:
        self._treasury = treasury

        self.execute_bulk_payouts = to_streamed_response_wrapper(
            treasury.execute_bulk_payouts,
        )
        self.optimize_liquidity = to_streamed_response_wrapper(
            treasury.optimize_liquidity,
        )
        self.retrieve_cash_flow_forecast = to_streamed_response_wrapper(
            treasury.retrieve_cash_flow_forecast,
        )
        self.retrieve_liquidity_positions = to_streamed_response_wrapper(
            treasury.retrieve_liquidity_positions,
        )

    @cached_property
    def sweeping(self) -> SweepingResourceWithStreamingResponse:
        return SweepingResourceWithStreamingResponse(self._treasury.sweeping)

    @cached_property
    def pooling(self) -> PoolingResourceWithStreamingResponse:
        return PoolingResourceWithStreamingResponse(self._treasury.pooling)


class AsyncTreasuryResourceWithStreamingResponse:
    def __init__(self, treasury: AsyncTreasuryResource) -> None:
        self._treasury = treasury

        self.execute_bulk_payouts = async_to_streamed_response_wrapper(
            treasury.execute_bulk_payouts,
        )
        self.optimize_liquidity = async_to_streamed_response_wrapper(
            treasury.optimize_liquidity,
        )
        self.retrieve_cash_flow_forecast = async_to_streamed_response_wrapper(
            treasury.retrieve_cash_flow_forecast,
        )
        self.retrieve_liquidity_positions = async_to_streamed_response_wrapper(
            treasury.retrieve_liquidity_positions,
        )

    @cached_property
    def sweeping(self) -> AsyncSweepingResourceWithStreamingResponse:
        return AsyncSweepingResourceWithStreamingResponse(self._treasury.sweeping)

    @cached_property
    def pooling(self) -> AsyncPoolingResourceWithStreamingResponse:
        return AsyncPoolingResourceWithStreamingResponse(self._treasury.pooling)
