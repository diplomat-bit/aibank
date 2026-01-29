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
from ....types.corporate.treasury import pooling_configure_params

__all__ = ["PoolingResource", "AsyncPoolingResource"]


class PoolingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PoolingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/diplomat-bit/aibank#accessing-raw-response-data-eg-headers
        """
        return PoolingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PoolingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/diplomat-bit/aibank#with_streaming_response
        """
        return PoolingResourceWithStreamingResponse(self)

    def configure(
        self,
        *,
        source_account_ids: SequenceNotStr[str] | Omit = omit,
        target_account_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Configure liquidity pooling

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/corporate/treasury/liquidity/pooling",
            body=maybe_transform(
                {
                    "source_account_ids": source_account_ids,
                    "target_account_id": target_account_id,
                },
                pooling_configure_params.PoolingConfigureParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncPoolingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPoolingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/diplomat-bit/aibank#accessing-raw-response-data-eg-headers
        """
        return AsyncPoolingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPoolingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/diplomat-bit/aibank#with_streaming_response
        """
        return AsyncPoolingResourceWithStreamingResponse(self)

    async def configure(
        self,
        *,
        source_account_ids: SequenceNotStr[str] | Omit = omit,
        target_account_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Configure liquidity pooling

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/corporate/treasury/liquidity/pooling",
            body=await async_maybe_transform(
                {
                    "source_account_ids": source_account_ids,
                    "target_account_id": target_account_id,
                },
                pooling_configure_params.PoolingConfigureParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class PoolingResourceWithRawResponse:
    def __init__(self, pooling: PoolingResource) -> None:
        self._pooling = pooling

        self.configure = to_raw_response_wrapper(
            pooling.configure,
        )


class AsyncPoolingResourceWithRawResponse:
    def __init__(self, pooling: AsyncPoolingResource) -> None:
        self._pooling = pooling

        self.configure = async_to_raw_response_wrapper(
            pooling.configure,
        )


class PoolingResourceWithStreamingResponse:
    def __init__(self, pooling: PoolingResource) -> None:
        self._pooling = pooling

        self.configure = to_streamed_response_wrapper(
            pooling.configure,
        )


class AsyncPoolingResourceWithStreamingResponse:
    def __init__(self, pooling: AsyncPoolingResource) -> None:
        self._pooling = pooling

        self.configure = async_to_streamed_response_wrapper(
            pooling.configure,
        )
