# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAdvisor:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_chat(self, client: Jocall3) -> None:
        advisor = client.ai.advisor.chat()
        assert_matches_type(object, advisor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_chat_with_all_params(self, client: Jocall3) -> None:
        advisor = client.ai.advisor.chat(
            function_response={},
        )
        assert_matches_type(object, advisor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_chat(self, client: Jocall3) -> None:
        response = client.ai.advisor.with_raw_response.chat()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        advisor = response.parse()
        assert_matches_type(object, advisor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_chat(self, client: Jocall3) -> None:
        with client.ai.advisor.with_streaming_response.chat() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            advisor = response.parse()
            assert_matches_type(object, advisor, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAdvisor:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_chat(self, async_client: AsyncJocall3) -> None:
        advisor = await async_client.ai.advisor.chat()
        assert_matches_type(object, advisor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_chat_with_all_params(self, async_client: AsyncJocall3) -> None:
        advisor = await async_client.ai.advisor.chat(
            function_response={},
        )
        assert_matches_type(object, advisor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_chat(self, async_client: AsyncJocall3) -> None:
        response = await async_client.ai.advisor.with_raw_response.chat()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        advisor = await response.parse()
        assert_matches_type(object, advisor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_chat(self, async_client: AsyncJocall3) -> None:
        async with async_client.ai.advisor.with_streaming_response.chat() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            advisor = await response.parse()
            assert_matches_type(object, advisor, path=["response"])

        assert cast(Any, response.is_closed) is True
