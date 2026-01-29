# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.corporate.cards.control_update_response import ControlUpdateResponse

__all__ = ["ControlsResource", "AsyncControlsResource"]


class ControlsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ControlsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/diplomat-bit/aibank#accessing-raw-response-data-eg-headers
        """
        return ControlsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ControlsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/diplomat-bit/aibank#with_streaming_response
        """
        return ControlsResourceWithStreamingResponse(self)

    def update(
        self,
        card_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ControlUpdateResponse:
        """
        Updates the sophisticated spending controls, limits, and policy overrides for a
        specific corporate card, enabling real-time adjustments for security and budget
        adherence.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return self._put(
            f"/corporate/cards/{card_id}/controls",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ControlUpdateResponse,
        )


class AsyncControlsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncControlsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/diplomat-bit/aibank#accessing-raw-response-data-eg-headers
        """
        return AsyncControlsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncControlsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/diplomat-bit/aibank#with_streaming_response
        """
        return AsyncControlsResourceWithStreamingResponse(self)

    async def update(
        self,
        card_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ControlUpdateResponse:
        """
        Updates the sophisticated spending controls, limits, and policy overrides for a
        specific corporate card, enabling real-time adjustments for security and budget
        adherence.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return await self._put(
            f"/corporate/cards/{card_id}/controls",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ControlUpdateResponse,
        )


class ControlsResourceWithRawResponse:
    def __init__(self, controls: ControlsResource) -> None:
        self._controls = controls

        self.update = to_raw_response_wrapper(
            controls.update,
        )


class AsyncControlsResourceWithRawResponse:
    def __init__(self, controls: AsyncControlsResource) -> None:
        self._controls = controls

        self.update = async_to_raw_response_wrapper(
            controls.update,
        )


class ControlsResourceWithStreamingResponse:
    def __init__(self, controls: ControlsResource) -> None:
        self._controls = controls

        self.update = to_streamed_response_wrapper(
            controls.update,
        )


class AsyncControlsResourceWithStreamingResponse:
    def __init__(self, controls: AsyncControlsResource) -> None:
        self._controls = controls

        self.update = async_to_streamed_response_wrapper(
            controls.update,
        )
