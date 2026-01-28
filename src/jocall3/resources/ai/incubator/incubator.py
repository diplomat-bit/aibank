# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.ai import incubator_generate_pitch_params
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options

__all__ = ["IncubatorResource", "AsyncIncubatorResource"]


class IncubatorResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IncubatorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/diplomat-bit/aibank#accessing-raw-response-data-eg-headers
        """
        return IncubatorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IncubatorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/diplomat-bit/aibank#with_streaming_response
        """
        return IncubatorResourceWithStreamingResponse(self)

    def generate_pitch(
        self,
        *,
        financial_projections: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Submits a detailed business plan to the Quantum Weaver AI for rigorous analysis,
        market validation, and seed funding consideration. This initiates the AI-driven
        incubation journey, aiming to transform innovative ideas into commercially
        successful ventures.

        Args:
          financial_projections: Key financial metrics and projections for the next 3-5 years.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/incubator/pitch",
            body=maybe_transform(
                {"financial_projections": financial_projections},
                incubator_generate_pitch_params.IncubatorGeneratePitchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncIncubatorResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIncubatorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/diplomat-bit/aibank#accessing-raw-response-data-eg-headers
        """
        return AsyncIncubatorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIncubatorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/diplomat-bit/aibank#with_streaming_response
        """
        return AsyncIncubatorResourceWithStreamingResponse(self)

    async def generate_pitch(
        self,
        *,
        financial_projections: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Submits a detailed business plan to the Quantum Weaver AI for rigorous analysis,
        market validation, and seed funding consideration. This initiates the AI-driven
        incubation journey, aiming to transform innovative ideas into commercially
        successful ventures.

        Args:
          financial_projections: Key financial metrics and projections for the next 3-5 years.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/incubator/pitch",
            body=await async_maybe_transform(
                {"financial_projections": financial_projections},
                incubator_generate_pitch_params.IncubatorGeneratePitchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class IncubatorResourceWithRawResponse:
    def __init__(self, incubator: IncubatorResource) -> None:
        self._incubator = incubator

        self.generate_pitch = to_raw_response_wrapper(
            incubator.generate_pitch,
        )


class AsyncIncubatorResourceWithRawResponse:
    def __init__(self, incubator: AsyncIncubatorResource) -> None:
        self._incubator = incubator

        self.generate_pitch = async_to_raw_response_wrapper(
            incubator.generate_pitch,
        )


class IncubatorResourceWithStreamingResponse:
    def __init__(self, incubator: IncubatorResource) -> None:
        self._incubator = incubator

        self.generate_pitch = to_streamed_response_wrapper(
            incubator.generate_pitch,
        )


class AsyncIncubatorResourceWithStreamingResponse:
    def __init__(self, incubator: AsyncIncubatorResource) -> None:
        self._incubator = incubator

        self.generate_pitch = async_to_streamed_response_wrapper(
            incubator.generate_pitch,
        )
