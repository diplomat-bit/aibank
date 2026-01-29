# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .sweeping import (
    SweepingResource,
    AsyncSweepingResource,
    SweepingResourceWithRawResponse,
    AsyncSweepingResourceWithRawResponse,
    SweepingResourceWithStreamingResponse,
    AsyncSweepingResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ....types.corporate import treasury_manage_liquidity_params, treasury_forecast_cash_flow_params
from ....types.corporate.treasury_manage_liquidity_response import TreasuryManageLiquidityResponse
from ....types.corporate.treasury_forecast_cash_flow_response import TreasuryForecastCashFlowResponse

__all__ = ["TreasuryResource", "AsyncTreasuryResource"]


class TreasuryResource(SyncAPIResource):
    @cached_property
    def sweeping(self) -> SweepingResource:
        return SweepingResource(self._client)

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

    def forecast_cash_flow(
        self,
        *,
        horizon_days: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TreasuryForecastCashFlowResponse:
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
                    {"horizon_days": horizon_days}, treasury_forecast_cash_flow_params.TreasuryForecastCashFlowParams
                ),
            ),
            cast_to=TreasuryForecastCashFlowResponse,
        )

    def manage_liquidity(
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
    ) -> TreasuryManageLiquidityResponse:
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
                treasury_manage_liquidity_params.TreasuryManageLiquidityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TreasuryManageLiquidityResponse,
        )


class AsyncTreasuryResource(AsyncAPIResource):
    @cached_property
    def sweeping(self) -> AsyncSweepingResource:
        return AsyncSweepingResource(self._client)

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

    async def forecast_cash_flow(
        self,
        *,
        horizon_days: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TreasuryForecastCashFlowResponse:
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
                    {"horizon_days": horizon_days}, treasury_forecast_cash_flow_params.TreasuryForecastCashFlowParams
                ),
            ),
            cast_to=TreasuryForecastCashFlowResponse,
        )

    async def manage_liquidity(
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
    ) -> TreasuryManageLiquidityResponse:
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
                treasury_manage_liquidity_params.TreasuryManageLiquidityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TreasuryManageLiquidityResponse,
        )


class TreasuryResourceWithRawResponse:
    def __init__(self, treasury: TreasuryResource) -> None:
        self._treasury = treasury

        self.forecast_cash_flow = to_raw_response_wrapper(
            treasury.forecast_cash_flow,
        )
        self.manage_liquidity = to_raw_response_wrapper(
            treasury.manage_liquidity,
        )

    @cached_property
    def sweeping(self) -> SweepingResourceWithRawResponse:
        return SweepingResourceWithRawResponse(self._treasury.sweeping)


class AsyncTreasuryResourceWithRawResponse:
    def __init__(self, treasury: AsyncTreasuryResource) -> None:
        self._treasury = treasury

        self.forecast_cash_flow = async_to_raw_response_wrapper(
            treasury.forecast_cash_flow,
        )
        self.manage_liquidity = async_to_raw_response_wrapper(
            treasury.manage_liquidity,
        )

    @cached_property
    def sweeping(self) -> AsyncSweepingResourceWithRawResponse:
        return AsyncSweepingResourceWithRawResponse(self._treasury.sweeping)


class TreasuryResourceWithStreamingResponse:
    def __init__(self, treasury: TreasuryResource) -> None:
        self._treasury = treasury

        self.forecast_cash_flow = to_streamed_response_wrapper(
            treasury.forecast_cash_flow,
        )
        self.manage_liquidity = to_streamed_response_wrapper(
            treasury.manage_liquidity,
        )

    @cached_property
    def sweeping(self) -> SweepingResourceWithStreamingResponse:
        return SweepingResourceWithStreamingResponse(self._treasury.sweeping)


class AsyncTreasuryResourceWithStreamingResponse:
    def __init__(self, treasury: AsyncTreasuryResource) -> None:
        self._treasury = treasury

        self.forecast_cash_flow = async_to_streamed_response_wrapper(
            treasury.forecast_cash_flow,
        )
        self.manage_liquidity = async_to_streamed_response_wrapper(
            treasury.manage_liquidity,
        )

    @cached_property
    def sweeping(self) -> AsyncSweepingResourceWithStreamingResponse:
        return AsyncSweepingResourceWithStreamingResponse(self._treasury.sweeping)
