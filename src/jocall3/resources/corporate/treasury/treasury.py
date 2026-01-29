# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from ....types.corporate import treasury_forecast_cash_flow_params
from ....types.corporate.treasury_forecast_cash_flow_response import TreasuryForecastCashFlowResponse
from ....types.corporate.treasury_get_liquidity_positions_response import TreasuryGetLiquidityPositionsResponse

__all__ = ["TreasuryResource", "AsyncTreasuryResource"]


class TreasuryResource(SyncAPIResource):
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
        forecast_horizon_days: int | Omit = omit,
        include_scenario_analysis: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TreasuryForecastCashFlowResponse:
        """
        Retrieves an advanced AI-driven cash flow forecast for the organization,
        projecting liquidity, identifying potential surpluses or deficits, and providing
        recommendations for optimal treasury management.

        Args:
          forecast_horizon_days: The number of days into the future for which to generate the cash flow forecast
              (e.g., 30, 90, 180).

          include_scenario_analysis: If true, the forecast will include best-case and worst-case scenario analysis
              alongside the most likely projection.

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
                    {
                        "forecast_horizon_days": forecast_horizon_days,
                        "include_scenario_analysis": include_scenario_analysis,
                    },
                    treasury_forecast_cash_flow_params.TreasuryForecastCashFlowParams,
                ),
            ),
            cast_to=TreasuryForecastCashFlowResponse,
        )

    def get_liquidity_positions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TreasuryGetLiquidityPositionsResponse:
        """
        Provides a real-time overview of the organization's liquidity across all
        accounts, currencies, and short-term investments.
        """
        return self._get(
            "/corporate/treasury/liquidity-positions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TreasuryGetLiquidityPositionsResponse,
        )


class AsyncTreasuryResource(AsyncAPIResource):
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
        forecast_horizon_days: int | Omit = omit,
        include_scenario_analysis: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TreasuryForecastCashFlowResponse:
        """
        Retrieves an advanced AI-driven cash flow forecast for the organization,
        projecting liquidity, identifying potential surpluses or deficits, and providing
        recommendations for optimal treasury management.

        Args:
          forecast_horizon_days: The number of days into the future for which to generate the cash flow forecast
              (e.g., 30, 90, 180).

          include_scenario_analysis: If true, the forecast will include best-case and worst-case scenario analysis
              alongside the most likely projection.

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
                    {
                        "forecast_horizon_days": forecast_horizon_days,
                        "include_scenario_analysis": include_scenario_analysis,
                    },
                    treasury_forecast_cash_flow_params.TreasuryForecastCashFlowParams,
                ),
            ),
            cast_to=TreasuryForecastCashFlowResponse,
        )

    async def get_liquidity_positions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TreasuryGetLiquidityPositionsResponse:
        """
        Provides a real-time overview of the organization's liquidity across all
        accounts, currencies, and short-term investments.
        """
        return await self._get(
            "/corporate/treasury/liquidity-positions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TreasuryGetLiquidityPositionsResponse,
        )


class TreasuryResourceWithRawResponse:
    def __init__(self, treasury: TreasuryResource) -> None:
        self._treasury = treasury

        self.forecast_cash_flow = to_raw_response_wrapper(
            treasury.forecast_cash_flow,
        )
        self.get_liquidity_positions = to_raw_response_wrapper(
            treasury.get_liquidity_positions,
        )


class AsyncTreasuryResourceWithRawResponse:
    def __init__(self, treasury: AsyncTreasuryResource) -> None:
        self._treasury = treasury

        self.forecast_cash_flow = async_to_raw_response_wrapper(
            treasury.forecast_cash_flow,
        )
        self.get_liquidity_positions = async_to_raw_response_wrapper(
            treasury.get_liquidity_positions,
        )


class TreasuryResourceWithStreamingResponse:
    def __init__(self, treasury: TreasuryResource) -> None:
        self._treasury = treasury

        self.forecast_cash_flow = to_streamed_response_wrapper(
            treasury.forecast_cash_flow,
        )
        self.get_liquidity_positions = to_streamed_response_wrapper(
            treasury.get_liquidity_positions,
        )


class AsyncTreasuryResourceWithStreamingResponse:
    def __init__(self, treasury: AsyncTreasuryResource) -> None:
        self._treasury = treasury

        self.forecast_cash_flow = async_to_streamed_response_wrapper(
            treasury.forecast_cash_flow,
        )
        self.get_liquidity_positions = async_to_streamed_response_wrapper(
            treasury.get_liquidity_positions,
        )
