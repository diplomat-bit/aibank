# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
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
from ....types.ai.incubator import analysis_swot_params, analysis_competitor_scan_params
from ....types.ai.incubator.analysis_swot_response import AnalysisSwotResponse
from ....types.ai.incubator.analysis_competitor_scan_response import AnalysisCompetitorScanResponse

__all__ = ["AnalysisResource", "AsyncAnalysisResource"]


class AnalysisResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AnalysisResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/diplomat-bit/aibank#accessing-raw-response-data-eg-headers
        """
        return AnalysisResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnalysisResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/diplomat-bit/aibank#with_streaming_response
        """
        return AnalysisResourceWithStreamingResponse(self)

    def competitor_scan(
        self,
        *,
        industry: str,
        niche: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalysisCompetitorScanResponse:
        """
        Generate Automated Competitor Landscape

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/incubator/analysis/competitors",
            body=maybe_transform(
                {
                    "industry": industry,
                    "niche": niche,
                },
                analysis_competitor_scan_params.AnalysisCompetitorScanParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnalysisCompetitorScanResponse,
        )

    def swot(
        self,
        *,
        business_context: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalysisSwotResponse:
        """
        Generate AI SWOT Analysis

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/incubator/analysis/swot",
            body=maybe_transform({"business_context": business_context}, analysis_swot_params.AnalysisSwotParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnalysisSwotResponse,
        )


class AsyncAnalysisResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAnalysisResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/diplomat-bit/aibank#accessing-raw-response-data-eg-headers
        """
        return AsyncAnalysisResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnalysisResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/diplomat-bit/aibank#with_streaming_response
        """
        return AsyncAnalysisResourceWithStreamingResponse(self)

    async def competitor_scan(
        self,
        *,
        industry: str,
        niche: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalysisCompetitorScanResponse:
        """
        Generate Automated Competitor Landscape

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/incubator/analysis/competitors",
            body=await async_maybe_transform(
                {
                    "industry": industry,
                    "niche": niche,
                },
                analysis_competitor_scan_params.AnalysisCompetitorScanParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnalysisCompetitorScanResponse,
        )

    async def swot(
        self,
        *,
        business_context: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalysisSwotResponse:
        """
        Generate AI SWOT Analysis

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/incubator/analysis/swot",
            body=await async_maybe_transform(
                {"business_context": business_context}, analysis_swot_params.AnalysisSwotParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnalysisSwotResponse,
        )


class AnalysisResourceWithRawResponse:
    def __init__(self, analysis: AnalysisResource) -> None:
        self._analysis = analysis

        self.competitor_scan = to_raw_response_wrapper(
            analysis.competitor_scan,
        )
        self.swot = to_raw_response_wrapper(
            analysis.swot,
        )


class AsyncAnalysisResourceWithRawResponse:
    def __init__(self, analysis: AsyncAnalysisResource) -> None:
        self._analysis = analysis

        self.competitor_scan = async_to_raw_response_wrapper(
            analysis.competitor_scan,
        )
        self.swot = async_to_raw_response_wrapper(
            analysis.swot,
        )


class AnalysisResourceWithStreamingResponse:
    def __init__(self, analysis: AnalysisResource) -> None:
        self._analysis = analysis

        self.competitor_scan = to_streamed_response_wrapper(
            analysis.competitor_scan,
        )
        self.swot = to_streamed_response_wrapper(
            analysis.swot,
        )


class AsyncAnalysisResourceWithStreamingResponse:
    def __init__(self, analysis: AsyncAnalysisResource) -> None:
        self._analysis = analysis

        self.competitor_scan = async_to_streamed_response_wrapper(
            analysis.competitor_scan,
        )
        self.swot = async_to_streamed_response_wrapper(
            analysis.swot,
        )
