# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .controls import (
    ControlsResource,
    AsyncControlsResource,
    ControlsResourceWithRawResponse,
    AsyncControlsResourceWithRawResponse,
    ControlsResourceWithStreamingResponse,
    AsyncControlsResourceWithStreamingResponse,
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
from ....types.corporate import card_freeze_params, card_issue_virtual_params, card_issue_physical_params
from ....types.corporate.card_issue_virtual_response import CardIssueVirtualResponse
from ....types.corporate.card_issue_physical_response import CardIssuePhysicalResponse

__all__ = ["CardsResource", "AsyncCardsResource"]


class CardsResource(SyncAPIResource):
    @cached_property
    def controls(self) -> ControlsResource:
        return ControlsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/diplomat-bit/aibank#accessing-raw-response-data-eg-headers
        """
        return CardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/diplomat-bit/aibank#with_streaming_response
        """
        return CardsResourceWithStreamingResponse(self)

    def freeze(
        self,
        card_id: str,
        *,
        frozen: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Toggle Card Lock

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/corporate/cards/{card_id}/freeze",
            body=maybe_transform({"frozen": frozen}, card_freeze_params.CardFreezeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def issue_physical(
        self,
        *,
        holder_name: str,
        shipping_address: card_issue_physical_params.ShippingAddress,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardIssuePhysicalResponse:
        """
        Request Physical Corporate Card

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/corporate/cards/physical",
            body=maybe_transform(
                {
                    "holder_name": holder_name,
                    "shipping_address": shipping_address,
                },
                card_issue_physical_params.CardIssuePhysicalParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardIssuePhysicalResponse,
        )

    def issue_virtual(
        self,
        *,
        holder_name: str,
        monthly_limit: float,
        purpose: str,
        metadata: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardIssueVirtualResponse:
        """
        Issue Corporate Virtual Card

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/corporate/cards/virtual",
            body=maybe_transform(
                {
                    "holder_name": holder_name,
                    "monthly_limit": monthly_limit,
                    "purpose": purpose,
                    "metadata": metadata,
                },
                card_issue_virtual_params.CardIssueVirtualParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardIssueVirtualResponse,
        )


class AsyncCardsResource(AsyncAPIResource):
    @cached_property
    def controls(self) -> AsyncControlsResource:
        return AsyncControlsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/diplomat-bit/aibank#accessing-raw-response-data-eg-headers
        """
        return AsyncCardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/diplomat-bit/aibank#with_streaming_response
        """
        return AsyncCardsResourceWithStreamingResponse(self)

    async def freeze(
        self,
        card_id: str,
        *,
        frozen: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Toggle Card Lock

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/corporate/cards/{card_id}/freeze",
            body=await async_maybe_transform({"frozen": frozen}, card_freeze_params.CardFreezeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def issue_physical(
        self,
        *,
        holder_name: str,
        shipping_address: card_issue_physical_params.ShippingAddress,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardIssuePhysicalResponse:
        """
        Request Physical Corporate Card

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/corporate/cards/physical",
            body=await async_maybe_transform(
                {
                    "holder_name": holder_name,
                    "shipping_address": shipping_address,
                },
                card_issue_physical_params.CardIssuePhysicalParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardIssuePhysicalResponse,
        )

    async def issue_virtual(
        self,
        *,
        holder_name: str,
        monthly_limit: float,
        purpose: str,
        metadata: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardIssueVirtualResponse:
        """
        Issue Corporate Virtual Card

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/corporate/cards/virtual",
            body=await async_maybe_transform(
                {
                    "holder_name": holder_name,
                    "monthly_limit": monthly_limit,
                    "purpose": purpose,
                    "metadata": metadata,
                },
                card_issue_virtual_params.CardIssueVirtualParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardIssueVirtualResponse,
        )


class CardsResourceWithRawResponse:
    def __init__(self, cards: CardsResource) -> None:
        self._cards = cards

        self.freeze = to_raw_response_wrapper(
            cards.freeze,
        )
        self.issue_physical = to_raw_response_wrapper(
            cards.issue_physical,
        )
        self.issue_virtual = to_raw_response_wrapper(
            cards.issue_virtual,
        )

    @cached_property
    def controls(self) -> ControlsResourceWithRawResponse:
        return ControlsResourceWithRawResponse(self._cards.controls)


class AsyncCardsResourceWithRawResponse:
    def __init__(self, cards: AsyncCardsResource) -> None:
        self._cards = cards

        self.freeze = async_to_raw_response_wrapper(
            cards.freeze,
        )
        self.issue_physical = async_to_raw_response_wrapper(
            cards.issue_physical,
        )
        self.issue_virtual = async_to_raw_response_wrapper(
            cards.issue_virtual,
        )

    @cached_property
    def controls(self) -> AsyncControlsResourceWithRawResponse:
        return AsyncControlsResourceWithRawResponse(self._cards.controls)


class CardsResourceWithStreamingResponse:
    def __init__(self, cards: CardsResource) -> None:
        self._cards = cards

        self.freeze = to_streamed_response_wrapper(
            cards.freeze,
        )
        self.issue_physical = to_streamed_response_wrapper(
            cards.issue_physical,
        )
        self.issue_virtual = to_streamed_response_wrapper(
            cards.issue_virtual,
        )

    @cached_property
    def controls(self) -> ControlsResourceWithStreamingResponse:
        return ControlsResourceWithStreamingResponse(self._cards.controls)


class AsyncCardsResourceWithStreamingResponse:
    def __init__(self, cards: AsyncCardsResource) -> None:
        self._cards = cards

        self.freeze = async_to_streamed_response_wrapper(
            cards.freeze,
        )
        self.issue_physical = async_to_streamed_response_wrapper(
            cards.issue_physical,
        )
        self.issue_virtual = async_to_streamed_response_wrapper(
            cards.issue_virtual,
        )

    @cached_property
    def controls(self) -> AsyncControlsResourceWithStreamingResponse:
        return AsyncControlsResourceWithStreamingResponse(self._cards.controls)
