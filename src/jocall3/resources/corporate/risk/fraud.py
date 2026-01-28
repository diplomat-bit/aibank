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
from ....types.corporate.risk import fraud_list_rules_params

__all__ = ["FraudResource", "AsyncFraudResource"]


class FraudResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FraudResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/diplomat-bit/aibank#accessing-raw-response-data-eg-headers
        """
        return FraudResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FraudResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/diplomat-bit/aibank#with_streaming_response
        """
        return FraudResourceWithStreamingResponse(self)

    def list_rules(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Retrieves a list of AI-powered fraud detection rules currently active for the
        organization, including their parameters, thresholds, and associated actions
        (e.g., flag, block, alert).

        Args:
          limit: Maximum number of items to return in a single page.

          offset: Number of items to skip before starting to collect the result set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/corporate/risk/fraud/rules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    fraud_list_rules_params.FraudListRulesParams,
                ),
            ),
            cast_to=object,
        )


class AsyncFraudResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFraudResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/diplomat-bit/aibank#accessing-raw-response-data-eg-headers
        """
        return AsyncFraudResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFraudResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/diplomat-bit/aibank#with_streaming_response
        """
        return AsyncFraudResourceWithStreamingResponse(self)

    async def list_rules(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Retrieves a list of AI-powered fraud detection rules currently active for the
        organization, including their parameters, thresholds, and associated actions
        (e.g., flag, block, alert).

        Args:
          limit: Maximum number of items to return in a single page.

          offset: Number of items to skip before starting to collect the result set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/corporate/risk/fraud/rules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    fraud_list_rules_params.FraudListRulesParams,
                ),
            ),
            cast_to=object,
        )


class FraudResourceWithRawResponse:
    def __init__(self, fraud: FraudResource) -> None:
        self._fraud = fraud

        self.list_rules = to_raw_response_wrapper(
            fraud.list_rules,
        )


class AsyncFraudResourceWithRawResponse:
    def __init__(self, fraud: AsyncFraudResource) -> None:
        self._fraud = fraud

        self.list_rules = async_to_raw_response_wrapper(
            fraud.list_rules,
        )


class FraudResourceWithStreamingResponse:
    def __init__(self, fraud: FraudResource) -> None:
        self._fraud = fraud

        self.list_rules = to_streamed_response_wrapper(
            fraud.list_rules,
        )


class AsyncFraudResourceWithStreamingResponse:
    def __init__(self, fraud: AsyncFraudResource) -> None:
        self._fraud = fraud

        self.list_rules = async_to_streamed_response_wrapper(
            fraud.list_rules,
        )
