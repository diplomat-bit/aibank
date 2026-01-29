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
from ....types.ai.oracle import prediction_inflation_params
from ....types.ai.oracle.prediction_inflation_response import PredictionInflationResponse
from ....types.ai.oracle.prediction_market_crash_response import PredictionMarketCrashResponse

__all__ = ["PredictionsResource", "AsyncPredictionsResource"]


class PredictionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PredictionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/diplomat-bit/aibank#accessing-raw-response-data-eg-headers
        """
        return PredictionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PredictionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/diplomat-bit/aibank#with_streaming_response
        """
        return PredictionsResourceWithStreamingResponse(self)

    def inflation(
        self,
        *,
        region: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionInflationResponse:
        """
        Get AI-Driven Inflation Forecast

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ai/oracle/predictions/inflation",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"region": region}, prediction_inflation_params.PredictionInflationParams),
            ),
            cast_to=PredictionInflationResponse,
        )

    def market_crash(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionMarketCrashResponse:
        """Get Market Volatility & Crash Probability"""
        return self._get(
            "/ai/oracle/predictions/market-crash-probability",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PredictionMarketCrashResponse,
        )


class AsyncPredictionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPredictionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/diplomat-bit/aibank#accessing-raw-response-data-eg-headers
        """
        return AsyncPredictionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPredictionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/diplomat-bit/aibank#with_streaming_response
        """
        return AsyncPredictionsResourceWithStreamingResponse(self)

    async def inflation(
        self,
        *,
        region: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionInflationResponse:
        """
        Get AI-Driven Inflation Forecast

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ai/oracle/predictions/inflation",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"region": region}, prediction_inflation_params.PredictionInflationParams
                ),
            ),
            cast_to=PredictionInflationResponse,
        )

    async def market_crash(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionMarketCrashResponse:
        """Get Market Volatility & Crash Probability"""
        return await self._get(
            "/ai/oracle/predictions/market-crash-probability",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PredictionMarketCrashResponse,
        )


class PredictionsResourceWithRawResponse:
    def __init__(self, predictions: PredictionsResource) -> None:
        self._predictions = predictions

        self.inflation = to_raw_response_wrapper(
            predictions.inflation,
        )
        self.market_crash = to_raw_response_wrapper(
            predictions.market_crash,
        )


class AsyncPredictionsResourceWithRawResponse:
    def __init__(self, predictions: AsyncPredictionsResource) -> None:
        self._predictions = predictions

        self.inflation = async_to_raw_response_wrapper(
            predictions.inflation,
        )
        self.market_crash = async_to_raw_response_wrapper(
            predictions.market_crash,
        )


class PredictionsResourceWithStreamingResponse:
    def __init__(self, predictions: PredictionsResource) -> None:
        self._predictions = predictions

        self.inflation = to_streamed_response_wrapper(
            predictions.inflation,
        )
        self.market_crash = to_streamed_response_wrapper(
            predictions.market_crash,
        )


class AsyncPredictionsResourceWithStreamingResponse:
    def __init__(self, predictions: AsyncPredictionsResource) -> None:
        self._predictions = predictions

        self.inflation = async_to_streamed_response_wrapper(
            predictions.inflation,
        )
        self.market_crash = async_to_streamed_response_wrapper(
            predictions.market_crash,
        )
