# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .tools import (
    ToolsResource,
    AsyncToolsResource,
    ToolsResourceWithRawResponse,
    AsyncToolsResourceWithRawResponse,
    ToolsResourceWithStreamingResponse,
    AsyncToolsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.ai import advisor_chat_params, advisor_history_params
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options

__all__ = ["AdvisorResource", "AsyncAdvisorResource"]


class AdvisorResource(SyncAPIResource):
    @cached_property
    def tools(self) -> ToolsResource:
        return ToolsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AdvisorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/diplomat-bit/aibank#accessing-raw-response-data-eg-headers
        """
        return AdvisorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdvisorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/diplomat-bit/aibank#with_streaming_response
        """
        return AdvisorResourceWithStreamingResponse(self)

    def chat(
        self,
        *,
        function_response: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Initiates or continues a sophisticated conversation with Quantum, the AI
        Advisor.

        Quantum can provide advanced financial insights, execute complex tasks
        via an expanding suite of intelligent tools, and learn from user interactions to
        offer hyper-personalized guidance.

        Args:
          function_response: Optional: The output from a tool function that the AI previously requested to be
              executed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/advisor/chat",
            body=maybe_transform({"function_response": function_response}, advisor_chat_params.AdvisorChatParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def history(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        session_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Fetches the full conversation history with the Quantum AI Advisor for a given
        session or user.

        Args:
          limit: Maximum number of items to return in a single page.

          offset: Number of items to skip before starting to collect the result set.

          session_id: Optional: Filter history by a specific session ID. If omitted, recent
              conversations will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ai/advisor/chat/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "session_id": session_id,
                    },
                    advisor_history_params.AdvisorHistoryParams,
                ),
            ),
            cast_to=object,
        )


class AsyncAdvisorResource(AsyncAPIResource):
    @cached_property
    def tools(self) -> AsyncToolsResource:
        return AsyncToolsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAdvisorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/diplomat-bit/aibank#accessing-raw-response-data-eg-headers
        """
        return AsyncAdvisorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdvisorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/diplomat-bit/aibank#with_streaming_response
        """
        return AsyncAdvisorResourceWithStreamingResponse(self)

    async def chat(
        self,
        *,
        function_response: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Initiates or continues a sophisticated conversation with Quantum, the AI
        Advisor.

        Quantum can provide advanced financial insights, execute complex tasks
        via an expanding suite of intelligent tools, and learn from user interactions to
        offer hyper-personalized guidance.

        Args:
          function_response: Optional: The output from a tool function that the AI previously requested to be
              executed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/advisor/chat",
            body=await async_maybe_transform(
                {"function_response": function_response}, advisor_chat_params.AdvisorChatParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def history(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        session_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Fetches the full conversation history with the Quantum AI Advisor for a given
        session or user.

        Args:
          limit: Maximum number of items to return in a single page.

          offset: Number of items to skip before starting to collect the result set.

          session_id: Optional: Filter history by a specific session ID. If omitted, recent
              conversations will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ai/advisor/chat/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "session_id": session_id,
                    },
                    advisor_history_params.AdvisorHistoryParams,
                ),
            ),
            cast_to=object,
        )


class AdvisorResourceWithRawResponse:
    def __init__(self, advisor: AdvisorResource) -> None:
        self._advisor = advisor

        self.chat = to_raw_response_wrapper(
            advisor.chat,
        )
        self.history = to_raw_response_wrapper(
            advisor.history,
        )

    @cached_property
    def tools(self) -> ToolsResourceWithRawResponse:
        return ToolsResourceWithRawResponse(self._advisor.tools)


class AsyncAdvisorResourceWithRawResponse:
    def __init__(self, advisor: AsyncAdvisorResource) -> None:
        self._advisor = advisor

        self.chat = async_to_raw_response_wrapper(
            advisor.chat,
        )
        self.history = async_to_raw_response_wrapper(
            advisor.history,
        )

    @cached_property
    def tools(self) -> AsyncToolsResourceWithRawResponse:
        return AsyncToolsResourceWithRawResponse(self._advisor.tools)


class AdvisorResourceWithStreamingResponse:
    def __init__(self, advisor: AdvisorResource) -> None:
        self._advisor = advisor

        self.chat = to_streamed_response_wrapper(
            advisor.chat,
        )
        self.history = to_streamed_response_wrapper(
            advisor.history,
        )

    @cached_property
    def tools(self) -> ToolsResourceWithStreamingResponse:
        return ToolsResourceWithStreamingResponse(self._advisor.tools)


class AsyncAdvisorResourceWithStreamingResponse:
    def __init__(self, advisor: AsyncAdvisorResource) -> None:
        self._advisor = advisor

        self.chat = async_to_streamed_response_wrapper(
            advisor.chat,
        )
        self.history = async_to_streamed_response_wrapper(
            advisor.history,
        )

    @cached_property
    def tools(self) -> AsyncToolsResourceWithStreamingResponse:
        return AsyncToolsResourceWithStreamingResponse(self._advisor.tools)
