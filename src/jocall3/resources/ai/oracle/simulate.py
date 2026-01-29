# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.ai.oracle import (
    simulate_run_advanced_params,
    simulate_run_standard_params,
    simulate_run_monte_carlo_params,
)
from ....types.ai.oracle.simulate_run_advanced_response import SimulateRunAdvancedResponse
from ....types.ai.oracle.simulate_run_standard_response import SimulateRunStandardResponse
from ....types.ai.oracle.simulate_run_monte_carlo_response import SimulateRunMonteCarloResponse

__all__ = ["SimulateResource", "AsyncSimulateResource"]


class SimulateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SimulateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/diplomat-bit/aibank#accessing-raw-response-data-eg-headers
        """
        return SimulateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimulateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/diplomat-bit/aibank#with_streaming_response
        """
        return SimulateResourceWithStreamingResponse(self)

    def run_advanced(
        self,
        *,
        prompt: str,
        scenarios: Iterable[simulate_run_advanced_params.Scenario],
        global_economic_factors: object | Omit = omit,
        personal_assumptions: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulateRunAdvancedResponse:
        """
        Run an Advanced Multi-Variable Financial Simulation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/oracle/simulate/advanced",
            body=maybe_transform(
                {
                    "prompt": prompt,
                    "scenarios": scenarios,
                    "global_economic_factors": global_economic_factors,
                    "personal_assumptions": personal_assumptions,
                },
                simulate_run_advanced_params.SimulateRunAdvancedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulateRunAdvancedResponse,
        )

    def run_monte_carlo(
        self,
        *,
        iterations: int,
        variables: SequenceNotStr[str],
        confidence_interval: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulateRunMonteCarloResponse:
        """
        Run a Probabilistic Monte Carlo Simulation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/oracle/simulate/monte-carlo",
            body=maybe_transform(
                {
                    "iterations": iterations,
                    "variables": variables,
                    "confidence_interval": confidence_interval,
                },
                simulate_run_monte_carlo_params.SimulateRunMonteCarloParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulateRunMonteCarloResponse,
        )

    def run_standard(
        self,
        *,
        prompt: str,
        parameters: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulateRunStandardResponse:
        """
        Run a 'What-If' Financial Simulation (Standard)

        Args:
          prompt: Describe the financial scenario

          parameters: Key variables like duration, rate, or amount

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/oracle/simulate",
            body=maybe_transform(
                {
                    "prompt": prompt,
                    "parameters": parameters,
                },
                simulate_run_standard_params.SimulateRunStandardParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulateRunStandardResponse,
        )


class AsyncSimulateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSimulateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/diplomat-bit/aibank#accessing-raw-response-data-eg-headers
        """
        return AsyncSimulateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimulateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/diplomat-bit/aibank#with_streaming_response
        """
        return AsyncSimulateResourceWithStreamingResponse(self)

    async def run_advanced(
        self,
        *,
        prompt: str,
        scenarios: Iterable[simulate_run_advanced_params.Scenario],
        global_economic_factors: object | Omit = omit,
        personal_assumptions: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulateRunAdvancedResponse:
        """
        Run an Advanced Multi-Variable Financial Simulation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/oracle/simulate/advanced",
            body=await async_maybe_transform(
                {
                    "prompt": prompt,
                    "scenarios": scenarios,
                    "global_economic_factors": global_economic_factors,
                    "personal_assumptions": personal_assumptions,
                },
                simulate_run_advanced_params.SimulateRunAdvancedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulateRunAdvancedResponse,
        )

    async def run_monte_carlo(
        self,
        *,
        iterations: int,
        variables: SequenceNotStr[str],
        confidence_interval: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulateRunMonteCarloResponse:
        """
        Run a Probabilistic Monte Carlo Simulation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/oracle/simulate/monte-carlo",
            body=await async_maybe_transform(
                {
                    "iterations": iterations,
                    "variables": variables,
                    "confidence_interval": confidence_interval,
                },
                simulate_run_monte_carlo_params.SimulateRunMonteCarloParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulateRunMonteCarloResponse,
        )

    async def run_standard(
        self,
        *,
        prompt: str,
        parameters: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulateRunStandardResponse:
        """
        Run a 'What-If' Financial Simulation (Standard)

        Args:
          prompt: Describe the financial scenario

          parameters: Key variables like duration, rate, or amount

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/oracle/simulate",
            body=await async_maybe_transform(
                {
                    "prompt": prompt,
                    "parameters": parameters,
                },
                simulate_run_standard_params.SimulateRunStandardParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulateRunStandardResponse,
        )


class SimulateResourceWithRawResponse:
    def __init__(self, simulate: SimulateResource) -> None:
        self._simulate = simulate

        self.run_advanced = to_raw_response_wrapper(
            simulate.run_advanced,
        )
        self.run_monte_carlo = to_raw_response_wrapper(
            simulate.run_monte_carlo,
        )
        self.run_standard = to_raw_response_wrapper(
            simulate.run_standard,
        )


class AsyncSimulateResourceWithRawResponse:
    def __init__(self, simulate: AsyncSimulateResource) -> None:
        self._simulate = simulate

        self.run_advanced = async_to_raw_response_wrapper(
            simulate.run_advanced,
        )
        self.run_monte_carlo = async_to_raw_response_wrapper(
            simulate.run_monte_carlo,
        )
        self.run_standard = async_to_raw_response_wrapper(
            simulate.run_standard,
        )


class SimulateResourceWithStreamingResponse:
    def __init__(self, simulate: SimulateResource) -> None:
        self._simulate = simulate

        self.run_advanced = to_streamed_response_wrapper(
            simulate.run_advanced,
        )
        self.run_monte_carlo = to_streamed_response_wrapper(
            simulate.run_monte_carlo,
        )
        self.run_standard = to_streamed_response_wrapper(
            simulate.run_standard,
        )


class AsyncSimulateResourceWithStreamingResponse:
    def __init__(self, simulate: AsyncSimulateResource) -> None:
        self._simulate = simulate

        self.run_advanced = async_to_streamed_response_wrapper(
            simulate.run_advanced,
        )
        self.run_monte_carlo = async_to_streamed_response_wrapper(
            simulate.run_monte_carlo,
        )
        self.run_standard = async_to_streamed_response_wrapper(
            simulate.run_standard,
        )
