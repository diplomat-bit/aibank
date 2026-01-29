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
from ...types.accounts import overdraft_update_settings_params
from ...types.accounts.overdraft_update_settings_response import OverdraftUpdateSettingsResponse
from ...types.accounts.overdraft_retrieve_settings_response import OverdraftRetrieveSettingsResponse

__all__ = ["OverdraftResource", "AsyncOverdraftResource"]


class OverdraftResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OverdraftResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/diplomat-bit/aibank#accessing-raw-response-data-eg-headers
        """
        return OverdraftResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OverdraftResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/diplomat-bit/aibank#with_streaming_response
        """
        return OverdraftResourceWithStreamingResponse(self)

    def retrieve_settings(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OverdraftRetrieveSettingsResponse:
        """
        Retrieves the current overdraft protection settings for a specific account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/overdraft-settings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OverdraftRetrieveSettingsResponse,
        )

    def update_settings(
        self,
        account_id: str,
        *,
        enabled: bool | Omit = omit,
        fee_preference: str | Omit = omit,
        link_to_savings: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OverdraftUpdateSettingsResponse:
        """
        Updates the overdraft protection settings for a specific account, enabling or
        disabling protection and configuring preferences.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._put(
            f"/accounts/{account_id}/overdraft-settings",
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "fee_preference": fee_preference,
                    "link_to_savings": link_to_savings,
                },
                overdraft_update_settings_params.OverdraftUpdateSettingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OverdraftUpdateSettingsResponse,
        )


class AsyncOverdraftResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOverdraftResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/diplomat-bit/aibank#accessing-raw-response-data-eg-headers
        """
        return AsyncOverdraftResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOverdraftResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/diplomat-bit/aibank#with_streaming_response
        """
        return AsyncOverdraftResourceWithStreamingResponse(self)

    async def retrieve_settings(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OverdraftRetrieveSettingsResponse:
        """
        Retrieves the current overdraft protection settings for a specific account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/overdraft-settings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OverdraftRetrieveSettingsResponse,
        )

    async def update_settings(
        self,
        account_id: str,
        *,
        enabled: bool | Omit = omit,
        fee_preference: str | Omit = omit,
        link_to_savings: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OverdraftUpdateSettingsResponse:
        """
        Updates the overdraft protection settings for a specific account, enabling or
        disabling protection and configuring preferences.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._put(
            f"/accounts/{account_id}/overdraft-settings",
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "fee_preference": fee_preference,
                    "link_to_savings": link_to_savings,
                },
                overdraft_update_settings_params.OverdraftUpdateSettingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OverdraftUpdateSettingsResponse,
        )


class OverdraftResourceWithRawResponse:
    def __init__(self, overdraft: OverdraftResource) -> None:
        self._overdraft = overdraft

        self.retrieve_settings = to_raw_response_wrapper(
            overdraft.retrieve_settings,
        )
        self.update_settings = to_raw_response_wrapper(
            overdraft.update_settings,
        )


class AsyncOverdraftResourceWithRawResponse:
    def __init__(self, overdraft: AsyncOverdraftResource) -> None:
        self._overdraft = overdraft

        self.retrieve_settings = async_to_raw_response_wrapper(
            overdraft.retrieve_settings,
        )
        self.update_settings = async_to_raw_response_wrapper(
            overdraft.update_settings,
        )


class OverdraftResourceWithStreamingResponse:
    def __init__(self, overdraft: OverdraftResource) -> None:
        self._overdraft = overdraft

        self.retrieve_settings = to_streamed_response_wrapper(
            overdraft.retrieve_settings,
        )
        self.update_settings = to_streamed_response_wrapper(
            overdraft.update_settings,
        )


class AsyncOverdraftResourceWithStreamingResponse:
    def __init__(self, overdraft: AsyncOverdraftResource) -> None:
        self._overdraft = overdraft

        self.retrieve_settings = async_to_streamed_response_wrapper(
            overdraft.retrieve_settings,
        )
        self.update_settings = async_to_streamed_response_wrapper(
            overdraft.update_settings,
        )
