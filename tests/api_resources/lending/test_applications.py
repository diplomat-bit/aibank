# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3
from tests.utils import assert_matches_type
from jocall3.types.lending import ApplicationRetrieveStatusResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestApplications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve_status(self, client: Jocall3) -> None:
        application = client.lending.applications.retrieve_status(
            "appId",
        )
        assert_matches_type(ApplicationRetrieveStatusResponse, application, path=["response"])

    @parametrize
    def test_raw_response_retrieve_status(self, client: Jocall3) -> None:
        response = client.lending.applications.with_raw_response.retrieve_status(
            "appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(ApplicationRetrieveStatusResponse, application, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_status(self, client: Jocall3) -> None:
        with client.lending.applications.with_streaming_response.retrieve_status(
            "appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(ApplicationRetrieveStatusResponse, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_status(self, client: Jocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.lending.applications.with_raw_response.retrieve_status(
                "",
            )


class TestAsyncApplications:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve_status(self, async_client: AsyncJocall3) -> None:
        application = await async_client.lending.applications.retrieve_status(
            "appId",
        )
        assert_matches_type(ApplicationRetrieveStatusResponse, application, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_status(self, async_client: AsyncJocall3) -> None:
        response = await async_client.lending.applications.with_raw_response.retrieve_status(
            "appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(ApplicationRetrieveStatusResponse, application, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_status(self, async_client: AsyncJocall3) -> None:
        async with async_client.lending.applications.with_streaming_response.retrieve_status(
            "appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(ApplicationRetrieveStatusResponse, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_status(self, async_client: AsyncJocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.lending.applications.with_raw_response.retrieve_status(
                "",
            )
