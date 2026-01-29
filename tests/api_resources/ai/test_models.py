# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3
from tests.utils import assert_matches_type
from jocall3.types.ai import ModelFineTuneResponse, ModelListVersionsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestModels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_fine_tune(self, client: Jocall3) -> None:
        model = client.ai.models.fine_tune(
            base_model="base_model",
            training_data_url="https://example.com",
        )
        assert_matches_type(ModelFineTuneResponse, model, path=["response"])

    @parametrize
    def test_method_fine_tune_with_all_params(self, client: Jocall3) -> None:
        model = client.ai.models.fine_tune(
            base_model="base_model",
            training_data_url="https://example.com",
            hyperparameters={},
        )
        assert_matches_type(ModelFineTuneResponse, model, path=["response"])

    @parametrize
    def test_raw_response_fine_tune(self, client: Jocall3) -> None:
        response = client.ai.models.with_raw_response.fine_tune(
            base_model="base_model",
            training_data_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelFineTuneResponse, model, path=["response"])

    @parametrize
    def test_streaming_response_fine_tune(self, client: Jocall3) -> None:
        with client.ai.models.with_streaming_response.fine_tune(
            base_model="base_model",
            training_data_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelFineTuneResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_versions(self, client: Jocall3) -> None:
        model = client.ai.models.list_versions()
        assert_matches_type(ModelListVersionsResponse, model, path=["response"])

    @parametrize
    def test_raw_response_list_versions(self, client: Jocall3) -> None:
        response = client.ai.models.with_raw_response.list_versions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelListVersionsResponse, model, path=["response"])

    @parametrize
    def test_streaming_response_list_versions(self, client: Jocall3) -> None:
        with client.ai.models.with_streaming_response.list_versions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelListVersionsResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncModels:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_fine_tune(self, async_client: AsyncJocall3) -> None:
        model = await async_client.ai.models.fine_tune(
            base_model="base_model",
            training_data_url="https://example.com",
        )
        assert_matches_type(ModelFineTuneResponse, model, path=["response"])

    @parametrize
    async def test_method_fine_tune_with_all_params(self, async_client: AsyncJocall3) -> None:
        model = await async_client.ai.models.fine_tune(
            base_model="base_model",
            training_data_url="https://example.com",
            hyperparameters={},
        )
        assert_matches_type(ModelFineTuneResponse, model, path=["response"])

    @parametrize
    async def test_raw_response_fine_tune(self, async_client: AsyncJocall3) -> None:
        response = await async_client.ai.models.with_raw_response.fine_tune(
            base_model="base_model",
            training_data_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(ModelFineTuneResponse, model, path=["response"])

    @parametrize
    async def test_streaming_response_fine_tune(self, async_client: AsyncJocall3) -> None:
        async with async_client.ai.models.with_streaming_response.fine_tune(
            base_model="base_model",
            training_data_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelFineTuneResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_versions(self, async_client: AsyncJocall3) -> None:
        model = await async_client.ai.models.list_versions()
        assert_matches_type(ModelListVersionsResponse, model, path=["response"])

    @parametrize
    async def test_raw_response_list_versions(self, async_client: AsyncJocall3) -> None:
        response = await async_client.ai.models.with_raw_response.list_versions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(ModelListVersionsResponse, model, path=["response"])

    @parametrize
    async def test_streaming_response_list_versions(self, async_client: AsyncJocall3) -> None:
        async with async_client.ai.models.with_streaming_response.list_versions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelListVersionsResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True
