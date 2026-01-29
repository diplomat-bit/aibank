# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.corporate.cards import control_update_params

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
        allowed_categories: SequenceNotStr[str] | Omit = omit,
        geo_restriction: SequenceNotStr[str] | Omit = omit,
        monthly_limit: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update Spending Limits & MCC Controls

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/corporate/cards/{card_id}/controls",
            body=maybe_transform(
                {
                    "allowed_categories": allowed_categories,
                    "geo_restriction": geo_restriction,
                    "monthly_limit": monthly_limit,
                },
                control_update_params.ControlUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
        allowed_categories: SequenceNotStr[str] | Omit = omit,
        geo_restriction: SequenceNotStr[str] | Omit = omit,
        monthly_limit: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update Spending Limits & MCC Controls

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/corporate/cards/{card_id}/controls",
            body=await async_maybe_transform(
                {
                    "allowed_categories": allowed_categories,
                    "geo_restriction": geo_restriction,
                    "monthly_limit": monthly_limit,
                },
                control_update_params.ControlUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
