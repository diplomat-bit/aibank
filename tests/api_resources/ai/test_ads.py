# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3
from tests.utils import assert_matches_type
from jocall3.types.ai import (
    AdListResponse,
    AdGenerateCopyResponse,
    AdGetOperationResponse,
    AdGenerateVideoResponse,
    AdOptimizeCampaignResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAds:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Jocall3) -> None:
        ad = client.ai.ads.list()
        assert_matches_type(AdListResponse, ad, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Jocall3) -> None:
        response = client.ai.ads.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = response.parse()
        assert_matches_type(AdListResponse, ad, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Jocall3) -> None:
        with client.ai.ads.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = response.parse()
            assert_matches_type(AdListResponse, ad, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_generate_copy(self, client: Jocall3) -> None:
        ad = client.ai.ads.generate_copy(
            product_description="productDescription",
            target_audience="targetAudience",
        )
        assert_matches_type(AdGenerateCopyResponse, ad, path=["response"])

    @parametrize
    def test_raw_response_generate_copy(self, client: Jocall3) -> None:
        response = client.ai.ads.with_raw_response.generate_copy(
            product_description="productDescription",
            target_audience="targetAudience",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = response.parse()
        assert_matches_type(AdGenerateCopyResponse, ad, path=["response"])

    @parametrize
    def test_streaming_response_generate_copy(self, client: Jocall3) -> None:
        with client.ai.ads.with_streaming_response.generate_copy(
            product_description="productDescription",
            target_audience="targetAudience",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = response.parse()
            assert_matches_type(AdGenerateCopyResponse, ad, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_generate_video(self, client: Jocall3) -> None:
        ad = client.ai.ads.generate_video(
            length_seconds=15,
            prompt="prompt",
            style="Cinematic",
        )
        assert_matches_type(AdGenerateVideoResponse, ad, path=["response"])

    @parametrize
    def test_raw_response_generate_video(self, client: Jocall3) -> None:
        response = client.ai.ads.with_raw_response.generate_video(
            length_seconds=15,
            prompt="prompt",
            style="Cinematic",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = response.parse()
        assert_matches_type(AdGenerateVideoResponse, ad, path=["response"])

    @parametrize
    def test_streaming_response_generate_video(self, client: Jocall3) -> None:
        with client.ai.ads.with_streaming_response.generate_video(
            length_seconds=15,
            prompt="prompt",
            style="Cinematic",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = response.parse()
            assert_matches_type(AdGenerateVideoResponse, ad, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_operation(self, client: Jocall3) -> None:
        ad = client.ai.ads.get_operation(
            "operationId",
        )
        assert_matches_type(AdGetOperationResponse, ad, path=["response"])

    @parametrize
    def test_raw_response_get_operation(self, client: Jocall3) -> None:
        response = client.ai.ads.with_raw_response.get_operation(
            "operationId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = response.parse()
        assert_matches_type(AdGetOperationResponse, ad, path=["response"])

    @parametrize
    def test_streaming_response_get_operation(self, client: Jocall3) -> None:
        with client.ai.ads.with_streaming_response.get_operation(
            "operationId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = response.parse()
            assert_matches_type(AdGetOperationResponse, ad, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_operation(self, client: Jocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `operation_id` but received ''"):
            client.ai.ads.with_raw_response.get_operation(
                "",
            )

    @parametrize
    def test_method_optimize_campaign(self, client: Jocall3) -> None:
        ad = client.ai.ads.optimize_campaign(
            campaign_data={},
        )
        assert_matches_type(AdOptimizeCampaignResponse, ad, path=["response"])

    @parametrize
    def test_raw_response_optimize_campaign(self, client: Jocall3) -> None:
        response = client.ai.ads.with_raw_response.optimize_campaign(
            campaign_data={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = response.parse()
        assert_matches_type(AdOptimizeCampaignResponse, ad, path=["response"])

    @parametrize
    def test_streaming_response_optimize_campaign(self, client: Jocall3) -> None:
        with client.ai.ads.with_streaming_response.optimize_campaign(
            campaign_data={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = response.parse()
            assert_matches_type(AdOptimizeCampaignResponse, ad, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAds:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncJocall3) -> None:
        ad = await async_client.ai.ads.list()
        assert_matches_type(AdListResponse, ad, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJocall3) -> None:
        response = await async_client.ai.ads.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = await response.parse()
        assert_matches_type(AdListResponse, ad, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJocall3) -> None:
        async with async_client.ai.ads.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = await response.parse()
            assert_matches_type(AdListResponse, ad, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_generate_copy(self, async_client: AsyncJocall3) -> None:
        ad = await async_client.ai.ads.generate_copy(
            product_description="productDescription",
            target_audience="targetAudience",
        )
        assert_matches_type(AdGenerateCopyResponse, ad, path=["response"])

    @parametrize
    async def test_raw_response_generate_copy(self, async_client: AsyncJocall3) -> None:
        response = await async_client.ai.ads.with_raw_response.generate_copy(
            product_description="productDescription",
            target_audience="targetAudience",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = await response.parse()
        assert_matches_type(AdGenerateCopyResponse, ad, path=["response"])

    @parametrize
    async def test_streaming_response_generate_copy(self, async_client: AsyncJocall3) -> None:
        async with async_client.ai.ads.with_streaming_response.generate_copy(
            product_description="productDescription",
            target_audience="targetAudience",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = await response.parse()
            assert_matches_type(AdGenerateCopyResponse, ad, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_generate_video(self, async_client: AsyncJocall3) -> None:
        ad = await async_client.ai.ads.generate_video(
            length_seconds=15,
            prompt="prompt",
            style="Cinematic",
        )
        assert_matches_type(AdGenerateVideoResponse, ad, path=["response"])

    @parametrize
    async def test_raw_response_generate_video(self, async_client: AsyncJocall3) -> None:
        response = await async_client.ai.ads.with_raw_response.generate_video(
            length_seconds=15,
            prompt="prompt",
            style="Cinematic",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = await response.parse()
        assert_matches_type(AdGenerateVideoResponse, ad, path=["response"])

    @parametrize
    async def test_streaming_response_generate_video(self, async_client: AsyncJocall3) -> None:
        async with async_client.ai.ads.with_streaming_response.generate_video(
            length_seconds=15,
            prompt="prompt",
            style="Cinematic",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = await response.parse()
            assert_matches_type(AdGenerateVideoResponse, ad, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_operation(self, async_client: AsyncJocall3) -> None:
        ad = await async_client.ai.ads.get_operation(
            "operationId",
        )
        assert_matches_type(AdGetOperationResponse, ad, path=["response"])

    @parametrize
    async def test_raw_response_get_operation(self, async_client: AsyncJocall3) -> None:
        response = await async_client.ai.ads.with_raw_response.get_operation(
            "operationId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = await response.parse()
        assert_matches_type(AdGetOperationResponse, ad, path=["response"])

    @parametrize
    async def test_streaming_response_get_operation(self, async_client: AsyncJocall3) -> None:
        async with async_client.ai.ads.with_streaming_response.get_operation(
            "operationId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = await response.parse()
            assert_matches_type(AdGetOperationResponse, ad, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_operation(self, async_client: AsyncJocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `operation_id` but received ''"):
            await async_client.ai.ads.with_raw_response.get_operation(
                "",
            )

    @parametrize
    async def test_method_optimize_campaign(self, async_client: AsyncJocall3) -> None:
        ad = await async_client.ai.ads.optimize_campaign(
            campaign_data={},
        )
        assert_matches_type(AdOptimizeCampaignResponse, ad, path=["response"])

    @parametrize
    async def test_raw_response_optimize_campaign(self, async_client: AsyncJocall3) -> None:
        response = await async_client.ai.ads.with_raw_response.optimize_campaign(
            campaign_data={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = await response.parse()
        assert_matches_type(AdOptimizeCampaignResponse, ad, path=["response"])

    @parametrize
    async def test_streaming_response_optimize_campaign(self, async_client: AsyncJocall3) -> None:
        async with async_client.ai.ads.with_streaming_response.optimize_campaign(
            campaign_data={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = await response.parse()
            assert_matches_type(AdOptimizeCampaignResponse, ad, path=["response"])

        assert cast(Any, response.is_closed) is True
