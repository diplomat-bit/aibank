# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ...types import lending_submit_application_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .decisions import (
    DecisionsResource,
    AsyncDecisionsResource,
    DecisionsResourceWithRawResponse,
    AsyncDecisionsResourceWithRawResponse,
    DecisionsResourceWithStreamingResponse,
    AsyncDecisionsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.lending_get_status_response import LendingGetStatusResponse
from ...types.lending_submit_application_response import LendingSubmitApplicationResponse

__all__ = ["LendingResource", "AsyncLendingResource"]


class LendingResource(SyncAPIResource):
    @cached_property
    def decisions(self) -> DecisionsResource:
        return DecisionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> LendingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/diplomat-bit/aibank#accessing-raw-response-data-eg-headers
        """
        return LendingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LendingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/diplomat-bit/aibank#with_streaming_response
        """
        return LendingResourceWithStreamingResponse(self)

    def get_status(
        self,
        app_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LendingGetStatusResponse:
        """
        Track Loan Processing

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return self._get(
            f"/lending/applications/{app_id}/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LendingGetStatusResponse,
        )

    def submit_application(
        self,
        *,
        amount: float,
        employment_data: lending_submit_application_params.EmploymentData,
        loan_type: Literal["MORTGAGE", "PERSONAL", "AUTO", "BUSINESS_EXPANSION"],
        term_months: int,
        assets: Iterable[object] | Omit = omit,
        collateral_id: str | Omit = omit,
        liabilities: Iterable[object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LendingSubmitApplicationResponse:
        """
        Submit Advanced Credit Application

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/lending/applications",
            body=maybe_transform(
                {
                    "amount": amount,
                    "employment_data": employment_data,
                    "loan_type": loan_type,
                    "term_months": term_months,
                    "assets": assets,
                    "collateral_id": collateral_id,
                    "liabilities": liabilities,
                },
                lending_submit_application_params.LendingSubmitApplicationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LendingSubmitApplicationResponse,
        )


class AsyncLendingResource(AsyncAPIResource):
    @cached_property
    def decisions(self) -> AsyncDecisionsResource:
        return AsyncDecisionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLendingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/diplomat-bit/aibank#accessing-raw-response-data-eg-headers
        """
        return AsyncLendingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLendingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/diplomat-bit/aibank#with_streaming_response
        """
        return AsyncLendingResourceWithStreamingResponse(self)

    async def get_status(
        self,
        app_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LendingGetStatusResponse:
        """
        Track Loan Processing

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return await self._get(
            f"/lending/applications/{app_id}/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LendingGetStatusResponse,
        )

    async def submit_application(
        self,
        *,
        amount: float,
        employment_data: lending_submit_application_params.EmploymentData,
        loan_type: Literal["MORTGAGE", "PERSONAL", "AUTO", "BUSINESS_EXPANSION"],
        term_months: int,
        assets: Iterable[object] | Omit = omit,
        collateral_id: str | Omit = omit,
        liabilities: Iterable[object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LendingSubmitApplicationResponse:
        """
        Submit Advanced Credit Application

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/lending/applications",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "employment_data": employment_data,
                    "loan_type": loan_type,
                    "term_months": term_months,
                    "assets": assets,
                    "collateral_id": collateral_id,
                    "liabilities": liabilities,
                },
                lending_submit_application_params.LendingSubmitApplicationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LendingSubmitApplicationResponse,
        )


class LendingResourceWithRawResponse:
    def __init__(self, lending: LendingResource) -> None:
        self._lending = lending

        self.get_status = to_raw_response_wrapper(
            lending.get_status,
        )
        self.submit_application = to_raw_response_wrapper(
            lending.submit_application,
        )

    @cached_property
    def decisions(self) -> DecisionsResourceWithRawResponse:
        return DecisionsResourceWithRawResponse(self._lending.decisions)


class AsyncLendingResourceWithRawResponse:
    def __init__(self, lending: AsyncLendingResource) -> None:
        self._lending = lending

        self.get_status = async_to_raw_response_wrapper(
            lending.get_status,
        )
        self.submit_application = async_to_raw_response_wrapper(
            lending.submit_application,
        )

    @cached_property
    def decisions(self) -> AsyncDecisionsResourceWithRawResponse:
        return AsyncDecisionsResourceWithRawResponse(self._lending.decisions)


class LendingResourceWithStreamingResponse:
    def __init__(self, lending: LendingResource) -> None:
        self._lending = lending

        self.get_status = to_streamed_response_wrapper(
            lending.get_status,
        )
        self.submit_application = to_streamed_response_wrapper(
            lending.submit_application,
        )

    @cached_property
    def decisions(self) -> DecisionsResourceWithStreamingResponse:
        return DecisionsResourceWithStreamingResponse(self._lending.decisions)


class AsyncLendingResourceWithStreamingResponse:
    def __init__(self, lending: AsyncLendingResource) -> None:
        self._lending = lending

        self.get_status = async_to_streamed_response_wrapper(
            lending.get_status,
        )
        self.submit_application = async_to_streamed_response_wrapper(
            lending.submit_application,
        )

    @cached_property
    def decisions(self) -> AsyncDecisionsResourceWithStreamingResponse:
        return AsyncDecisionsResourceWithStreamingResponse(self._lending.decisions)
