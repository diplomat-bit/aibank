# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3
from tests.utils import assert_matches_type
from jocall3.types.ai import AgentGetPromptsResponse, AgentGetCapabilitiesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgent:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_capabilities(self, client: Jocall3) -> None:
        agent = client.ai.agent.get_capabilities()
        assert_matches_type(AgentGetCapabilitiesResponse, agent, path=["response"])

    @parametrize
    def test_raw_response_get_capabilities(self, client: Jocall3) -> None:
        response = client.ai.agent.with_raw_response.get_capabilities()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentGetCapabilitiesResponse, agent, path=["response"])

    @parametrize
    def test_streaming_response_get_capabilities(self, client: Jocall3) -> None:
        with client.ai.agent.with_streaming_response.get_capabilities() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentGetCapabilitiesResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_prompts(self, client: Jocall3) -> None:
        agent = client.ai.agent.get_prompts()
        assert_matches_type(AgentGetPromptsResponse, agent, path=["response"])

    @parametrize
    def test_raw_response_get_prompts(self, client: Jocall3) -> None:
        response = client.ai.agent.with_raw_response.get_prompts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentGetPromptsResponse, agent, path=["response"])

    @parametrize
    def test_streaming_response_get_prompts(self, client: Jocall3) -> None:
        with client.ai.agent.with_streaming_response.get_prompts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentGetPromptsResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_prompts(self, client: Jocall3) -> None:
        agent = client.ai.agent.update_prompts(
            system_prompt="systemPrompt",
        )
        assert agent is None

    @parametrize
    def test_raw_response_update_prompts(self, client: Jocall3) -> None:
        response = client.ai.agent.with_raw_response.update_prompts(
            system_prompt="systemPrompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert agent is None

    @parametrize
    def test_streaming_response_update_prompts(self, client: Jocall3) -> None:
        with client.ai.agent.with_streaming_response.update_prompts(
            system_prompt="systemPrompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert agent is None

        assert cast(Any, response.is_closed) is True


class TestAsyncAgent:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_capabilities(self, async_client: AsyncJocall3) -> None:
        agent = await async_client.ai.agent.get_capabilities()
        assert_matches_type(AgentGetCapabilitiesResponse, agent, path=["response"])

    @parametrize
    async def test_raw_response_get_capabilities(self, async_client: AsyncJocall3) -> None:
        response = await async_client.ai.agent.with_raw_response.get_capabilities()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentGetCapabilitiesResponse, agent, path=["response"])

    @parametrize
    async def test_streaming_response_get_capabilities(self, async_client: AsyncJocall3) -> None:
        async with async_client.ai.agent.with_streaming_response.get_capabilities() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentGetCapabilitiesResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_prompts(self, async_client: AsyncJocall3) -> None:
        agent = await async_client.ai.agent.get_prompts()
        assert_matches_type(AgentGetPromptsResponse, agent, path=["response"])

    @parametrize
    async def test_raw_response_get_prompts(self, async_client: AsyncJocall3) -> None:
        response = await async_client.ai.agent.with_raw_response.get_prompts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentGetPromptsResponse, agent, path=["response"])

    @parametrize
    async def test_streaming_response_get_prompts(self, async_client: AsyncJocall3) -> None:
        async with async_client.ai.agent.with_streaming_response.get_prompts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentGetPromptsResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_prompts(self, async_client: AsyncJocall3) -> None:
        agent = await async_client.ai.agent.update_prompts(
            system_prompt="systemPrompt",
        )
        assert agent is None

    @parametrize
    async def test_raw_response_update_prompts(self, async_client: AsyncJocall3) -> None:
        response = await async_client.ai.agent.with_raw_response.update_prompts(
            system_prompt="systemPrompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert agent is None

    @parametrize
    async def test_streaming_response_update_prompts(self, async_client: AsyncJocall3) -> None:
        async with async_client.ai.agent.with_streaming_response.update_prompts(
            system_prompt="systemPrompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert agent is None

        assert cast(Any, response.is_closed) is True
