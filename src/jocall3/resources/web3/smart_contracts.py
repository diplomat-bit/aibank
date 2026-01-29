# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.web3 import smart_contract_deploy_params
from ..._base_client import make_request_options

__all__ = ["SmartContractsResource", "AsyncSmartContractsResource"]


class SmartContractsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SmartContractsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/diplomat-bit/aibank#accessing-raw-response-data-eg-headers
        """
        return SmartContractsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SmartContractsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/diplomat-bit/aibank#with_streaming_response
        """
        return SmartContractsResourceWithStreamingResponse(self)

    def deploy(
        self,
        *,
        abi: object,
        bytecode: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deploy Financial Smart Contract

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/web3/contracts/deploy",
            body=maybe_transform(
                {
                    "abi": abi,
                    "bytecode": bytecode,
                },
                smart_contract_deploy_params.SmartContractDeployParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSmartContractsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSmartContractsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/diplomat-bit/aibank#accessing-raw-response-data-eg-headers
        """
        return AsyncSmartContractsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSmartContractsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/diplomat-bit/aibank#with_streaming_response
        """
        return AsyncSmartContractsResourceWithStreamingResponse(self)

    async def deploy(
        self,
        *,
        abi: object,
        bytecode: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deploy Financial Smart Contract

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/web3/contracts/deploy",
            body=await async_maybe_transform(
                {
                    "abi": abi,
                    "bytecode": bytecode,
                },
                smart_contract_deploy_params.SmartContractDeployParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SmartContractsResourceWithRawResponse:
    def __init__(self, smart_contracts: SmartContractsResource) -> None:
        self._smart_contracts = smart_contracts

        self.deploy = to_raw_response_wrapper(
            smart_contracts.deploy,
        )


class AsyncSmartContractsResourceWithRawResponse:
    def __init__(self, smart_contracts: AsyncSmartContractsResource) -> None:
        self._smart_contracts = smart_contracts

        self.deploy = async_to_raw_response_wrapper(
            smart_contracts.deploy,
        )


class SmartContractsResourceWithStreamingResponse:
    def __init__(self, smart_contracts: SmartContractsResource) -> None:
        self._smart_contracts = smart_contracts

        self.deploy = to_streamed_response_wrapper(
            smart_contracts.deploy,
        )


class AsyncSmartContractsResourceWithStreamingResponse:
    def __init__(self, smart_contracts: AsyncSmartContractsResource) -> None:
        self._smart_contracts = smart_contracts

        self.deploy = async_to_streamed_response_wrapper(
            smart_contracts.deploy,
        )
