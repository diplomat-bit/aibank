# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3
from tests.utils import assert_matches_type
from jocall3.types.ai import AdvisorChatResponse, AdvisorRetrieveHistoryResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAdvisor:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_chat(self, client: Jocall3) -> None:
        advisor = client.ai.advisor.chat(
            message="message",
        )
        assert_matches_type(AdvisorChatResponse, advisor, path=["response"])

    @parametrize
    def test_method_chat_with_all_params(self, client: Jocall3) -> None:
        advisor = client.ai.advisor.chat(
            message="message",
            context_account_ids=["string"],
            mode="mode",
            stream=True,
        )
        assert_matches_type(AdvisorChatResponse, advisor, path=["response"])

    @parametrize
    def test_raw_response_chat(self, client: Jocall3) -> None:
        response = client.ai.advisor.with_raw_response.chat(
            message="message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        advisor = response.parse()
        assert_matches_type(AdvisorChatResponse, advisor, path=["response"])

    @parametrize
    def test_streaming_response_chat(self, client: Jocall3) -> None:
        with client.ai.advisor.with_streaming_response.chat(
            message="message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            advisor = response.parse()
            assert_matches_type(AdvisorChatResponse, advisor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_history(self, client: Jocall3) -> None:
        advisor = client.ai.advisor.retrieve_history()
        assert_matches_type(AdvisorRetrieveHistoryResponse, advisor, path=["response"])

    @parametrize
    def test_raw_response_retrieve_history(self, client: Jocall3) -> None:
        response = client.ai.advisor.with_raw_response.retrieve_history()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        advisor = response.parse()
        assert_matches_type(AdvisorRetrieveHistoryResponse, advisor, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_history(self, client: Jocall3) -> None:
        with client.ai.advisor.with_streaming_response.retrieve_history() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            advisor = response.parse()
            assert_matches_type(AdvisorRetrieveHistoryResponse, advisor, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAdvisor:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_chat(self, async_client: AsyncJocall3) -> None:
        advisor = await async_client.ai.advisor.chat(
            message="message",
        )
        assert_matches_type(AdvisorChatResponse, advisor, path=["response"])

    @parametrize
    async def test_method_chat_with_all_params(self, async_client: AsyncJocall3) -> None:
        advisor = await async_client.ai.advisor.chat(
            message="message",
            context_account_ids=["string"],
            mode="mode",
            stream=True,
        )
        assert_matches_type(AdvisorChatResponse, advisor, path=["response"])

    @parametrize
    async def test_raw_response_chat(self, async_client: AsyncJocall3) -> None:
        response = await async_client.ai.advisor.with_raw_response.chat(
            message="message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        advisor = await response.parse()
        assert_matches_type(AdvisorChatResponse, advisor, path=["response"])

    @parametrize
    async def test_streaming_response_chat(self, async_client: AsyncJocall3) -> None:
        async with async_client.ai.advisor.with_streaming_response.chat(
            message="message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            advisor = await response.parse()
            assert_matches_type(AdvisorChatResponse, advisor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_history(self, async_client: AsyncJocall3) -> None:
        advisor = await async_client.ai.advisor.retrieve_history()
        assert_matches_type(AdvisorRetrieveHistoryResponse, advisor, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_history(self, async_client: AsyncJocall3) -> None:
        response = await async_client.ai.advisor.with_raw_response.retrieve_history()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        advisor = await response.parse()
        assert_matches_type(AdvisorRetrieveHistoryResponse, advisor, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_history(self, async_client: AsyncJocall3) -> None:
        async with async_client.ai.advisor.with_streaming_response.retrieve_history() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            advisor = await response.parse()
            assert_matches_type(AdvisorRetrieveHistoryResponse, advisor, path=["response"])

        assert cast(Any, response.is_closed) is True
