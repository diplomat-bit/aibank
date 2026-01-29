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
from ...types.corporate import sanction_screening_screen_params

__all__ = ["SanctionScreeningResource", "AsyncSanctionScreeningResource"]


class SanctionScreeningResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SanctionScreeningResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/diplomat-bit/aibank#accessing-raw-response-data-eg-headers
        """
        return SanctionScreeningResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SanctionScreeningResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/diplomat-bit/aibank#with_streaming_response
        """
        return SanctionScreeningResourceWithStreamingResponse(self)

    def screen(
        self,
        *,
        address: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Executes a real-time screening of an individual or entity against global
        sanction lists and watchlists.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/corporate/sanction-screening",
            body=maybe_transform({"address": address}, sanction_screening_screen_params.SanctionScreeningScreenParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncSanctionScreeningResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSanctionScreeningResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/diplomat-bit/aibank#accessing-raw-response-data-eg-headers
        """
        return AsyncSanctionScreeningResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSanctionScreeningResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/diplomat-bit/aibank#with_streaming_response
        """
        return AsyncSanctionScreeningResourceWithStreamingResponse(self)

    async def screen(
        self,
        *,
        address: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Executes a real-time screening of an individual or entity against global
        sanction lists and watchlists.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/corporate/sanction-screening",
            body=await async_maybe_transform(
                {"address": address}, sanction_screening_screen_params.SanctionScreeningScreenParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class SanctionScreeningResourceWithRawResponse:
    def __init__(self, sanction_screening: SanctionScreeningResource) -> None:
        self._sanction_screening = sanction_screening

        self.screen = to_raw_response_wrapper(
            sanction_screening.screen,
        )


class AsyncSanctionScreeningResourceWithRawResponse:
    def __init__(self, sanction_screening: AsyncSanctionScreeningResource) -> None:
        self._sanction_screening = sanction_screening

        self.screen = async_to_raw_response_wrapper(
            sanction_screening.screen,
        )


class SanctionScreeningResourceWithStreamingResponse:
    def __init__(self, sanction_screening: SanctionScreeningResource) -> None:
        self._sanction_screening = sanction_screening

        self.screen = to_streamed_response_wrapper(
            sanction_screening.screen,
        )


class AsyncSanctionScreeningResourceWithStreamingResponse:
    def __init__(self, sanction_screening: AsyncSanctionScreeningResource) -> None:
        self._sanction_screening = sanction_screening

        self.screen = async_to_streamed_response_wrapper(
            sanction_screening.screen,
        )
