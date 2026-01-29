# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.sustainability import impact_project_search_params
from ...types.sustainability.impact_project_search_response import ImpactProjectSearchResponse
from ...types.sustainability.impact_portfolio_analysis_response import ImpactPortfolioAnalysisResponse

__all__ = ["ImpactResource", "AsyncImpactResource"]


class ImpactResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ImpactResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/diplomat-bit/aibank#accessing-raw-response-data-eg-headers
        """
        return ImpactResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ImpactResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/diplomat-bit/aibank#with_streaming_response
        """
        return ImpactResourceWithStreamingResponse(self)

    def portfolio_analysis(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImpactPortfolioAnalysisResponse:
        """ESG Portfolio Impact Analysis"""
        return self._get(
            "/sustainability/impact/portfolio",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImpactPortfolioAnalysisResponse,
        )

    def project_search(
        self,
        *,
        continent: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImpactProjectSearchResponse:
        """
        Search Global Green Projects

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/sustainability/impact/projects",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"continent": continent}, impact_project_search_params.ImpactProjectSearchParams),
            ),
            cast_to=ImpactProjectSearchResponse,
        )


class AsyncImpactResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncImpactResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/diplomat-bit/aibank#accessing-raw-response-data-eg-headers
        """
        return AsyncImpactResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncImpactResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/diplomat-bit/aibank#with_streaming_response
        """
        return AsyncImpactResourceWithStreamingResponse(self)

    async def portfolio_analysis(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImpactPortfolioAnalysisResponse:
        """ESG Portfolio Impact Analysis"""
        return await self._get(
            "/sustainability/impact/portfolio",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImpactPortfolioAnalysisResponse,
        )

    async def project_search(
        self,
        *,
        continent: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImpactProjectSearchResponse:
        """
        Search Global Green Projects

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/sustainability/impact/projects",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"continent": continent}, impact_project_search_params.ImpactProjectSearchParams
                ),
            ),
            cast_to=ImpactProjectSearchResponse,
        )


class ImpactResourceWithRawResponse:
    def __init__(self, impact: ImpactResource) -> None:
        self._impact = impact

        self.portfolio_analysis = to_raw_response_wrapper(
            impact.portfolio_analysis,
        )
        self.project_search = to_raw_response_wrapper(
            impact.project_search,
        )


class AsyncImpactResourceWithRawResponse:
    def __init__(self, impact: AsyncImpactResource) -> None:
        self._impact = impact

        self.portfolio_analysis = async_to_raw_response_wrapper(
            impact.portfolio_analysis,
        )
        self.project_search = async_to_raw_response_wrapper(
            impact.project_search,
        )


class ImpactResourceWithStreamingResponse:
    def __init__(self, impact: ImpactResource) -> None:
        self._impact = impact

        self.portfolio_analysis = to_streamed_response_wrapper(
            impact.portfolio_analysis,
        )
        self.project_search = to_streamed_response_wrapper(
            impact.project_search,
        )


class AsyncImpactResourceWithStreamingResponse:
    def __init__(self, impact: AsyncImpactResource) -> None:
        self._impact = impact

        self.portfolio_analysis = async_to_streamed_response_wrapper(
            impact.portfolio_analysis,
        )
        self.project_search = async_to_streamed_response_wrapper(
            impact.project_search,
        )
