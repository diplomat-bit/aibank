# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.ai import ad_generate_copy_params, ad_generate_video_params, ad_optimize_campaign_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.ai.ad_list_response import AdListResponse
from ...types.ai.ad_generate_copy_response import AdGenerateCopyResponse
from ...types.ai.ad_generate_video_response import AdGenerateVideoResponse
from ...types.ai.ad_optimize_campaign_response import AdOptimizeCampaignResponse
from ...types.ai.ad_retrieve_operation_status_response import AdRetrieveOperationStatusResponse

__all__ = ["AdsResource", "AsyncAdsResource"]


class AdsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AdsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/diplomat-bit/aibank#accessing-raw-response-data-eg-headers
        """
        return AdsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/diplomat-bit/aibank#with_streaming_response
        """
        return AdsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdListResponse:
        """List All Generated Ad Assets"""
        return self._get(
            "/ai/ads",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdListResponse,
        )

    def generate_copy(
        self,
        *,
        product_description: str,
        target_audience: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdGenerateCopyResponse:
        """
        Generate High-Conversion Ad Copy

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/ads/generate/copy",
            body=maybe_transform(
                {
                    "product_description": product_description,
                    "target_audience": target_audience,
                },
                ad_generate_copy_params.AdGenerateCopyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdGenerateCopyResponse,
        )

    def generate_video(
        self,
        *,
        length_seconds: Literal[15, 30, 60],
        prompt: str,
        style: Literal["Cinematic", "Minimalist", "Cyberpunk", "Professional"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdGenerateVideoResponse:
        """
        Generate a Standard Video Ad with Veo 2.0

        Args:
          prompt: Visual description

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/ads/generate/video",
            body=maybe_transform(
                {
                    "length_seconds": length_seconds,
                    "prompt": prompt,
                    "style": style,
                },
                ad_generate_video_params.AdGenerateVideoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdGenerateVideoResponse,
        )

    def optimize_campaign(
        self,
        *,
        campaign_data: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdOptimizeCampaignResponse:
        """
        AI Campaign Efficiency Optimizer

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/ads/optimize",
            body=maybe_transform(
                {"campaign_data": campaign_data}, ad_optimize_campaign_params.AdOptimizeCampaignParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdOptimizeCampaignResponse,
        )

    def retrieve_operation_status(
        self,
        operation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdRetrieveOperationStatusResponse:
        """
        Poll for Video Gen Status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not operation_id:
            raise ValueError(f"Expected a non-empty value for `operation_id` but received {operation_id!r}")
        return self._get(
            f"/ai/ads/operations/{operation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdRetrieveOperationStatusResponse,
        )


class AsyncAdsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAdsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/diplomat-bit/aibank#accessing-raw-response-data-eg-headers
        """
        return AsyncAdsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/diplomat-bit/aibank#with_streaming_response
        """
        return AsyncAdsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdListResponse:
        """List All Generated Ad Assets"""
        return await self._get(
            "/ai/ads",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdListResponse,
        )

    async def generate_copy(
        self,
        *,
        product_description: str,
        target_audience: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdGenerateCopyResponse:
        """
        Generate High-Conversion Ad Copy

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/ads/generate/copy",
            body=await async_maybe_transform(
                {
                    "product_description": product_description,
                    "target_audience": target_audience,
                },
                ad_generate_copy_params.AdGenerateCopyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdGenerateCopyResponse,
        )

    async def generate_video(
        self,
        *,
        length_seconds: Literal[15, 30, 60],
        prompt: str,
        style: Literal["Cinematic", "Minimalist", "Cyberpunk", "Professional"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdGenerateVideoResponse:
        """
        Generate a Standard Video Ad with Veo 2.0

        Args:
          prompt: Visual description

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/ads/generate/video",
            body=await async_maybe_transform(
                {
                    "length_seconds": length_seconds,
                    "prompt": prompt,
                    "style": style,
                },
                ad_generate_video_params.AdGenerateVideoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdGenerateVideoResponse,
        )

    async def optimize_campaign(
        self,
        *,
        campaign_data: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdOptimizeCampaignResponse:
        """
        AI Campaign Efficiency Optimizer

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/ads/optimize",
            body=await async_maybe_transform(
                {"campaign_data": campaign_data}, ad_optimize_campaign_params.AdOptimizeCampaignParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdOptimizeCampaignResponse,
        )

    async def retrieve_operation_status(
        self,
        operation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdRetrieveOperationStatusResponse:
        """
        Poll for Video Gen Status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not operation_id:
            raise ValueError(f"Expected a non-empty value for `operation_id` but received {operation_id!r}")
        return await self._get(
            f"/ai/ads/operations/{operation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdRetrieveOperationStatusResponse,
        )


class AdsResourceWithRawResponse:
    def __init__(self, ads: AdsResource) -> None:
        self._ads = ads

        self.list = to_raw_response_wrapper(
            ads.list,
        )
        self.generate_copy = to_raw_response_wrapper(
            ads.generate_copy,
        )
        self.generate_video = to_raw_response_wrapper(
            ads.generate_video,
        )
        self.optimize_campaign = to_raw_response_wrapper(
            ads.optimize_campaign,
        )
        self.retrieve_operation_status = to_raw_response_wrapper(
            ads.retrieve_operation_status,
        )


class AsyncAdsResourceWithRawResponse:
    def __init__(self, ads: AsyncAdsResource) -> None:
        self._ads = ads

        self.list = async_to_raw_response_wrapper(
            ads.list,
        )
        self.generate_copy = async_to_raw_response_wrapper(
            ads.generate_copy,
        )
        self.generate_video = async_to_raw_response_wrapper(
            ads.generate_video,
        )
        self.optimize_campaign = async_to_raw_response_wrapper(
            ads.optimize_campaign,
        )
        self.retrieve_operation_status = async_to_raw_response_wrapper(
            ads.retrieve_operation_status,
        )


class AdsResourceWithStreamingResponse:
    def __init__(self, ads: AdsResource) -> None:
        self._ads = ads

        self.list = to_streamed_response_wrapper(
            ads.list,
        )
        self.generate_copy = to_streamed_response_wrapper(
            ads.generate_copy,
        )
        self.generate_video = to_streamed_response_wrapper(
            ads.generate_video,
        )
        self.optimize_campaign = to_streamed_response_wrapper(
            ads.optimize_campaign,
        )
        self.retrieve_operation_status = to_streamed_response_wrapper(
            ads.retrieve_operation_status,
        )


class AsyncAdsResourceWithStreamingResponse:
    def __init__(self, ads: AsyncAdsResource) -> None:
        self._ads = ads

        self.list = async_to_streamed_response_wrapper(
            ads.list,
        )
        self.generate_copy = async_to_streamed_response_wrapper(
            ads.generate_copy,
        )
        self.generate_video = async_to_streamed_response_wrapper(
            ads.generate_video,
        )
        self.optimize_campaign = async_to_streamed_response_wrapper(
            ads.optimize_campaign,
        )
        self.retrieve_operation_status = async_to_streamed_response_wrapper(
            ads.retrieve_operation_status,
        )
