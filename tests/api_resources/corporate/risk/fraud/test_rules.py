# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3
from tests.utils import assert_matches_type
from jocall3.types.corporate.risk.fraud import RuleListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Jocall3) -> None:
        rule = client.corporate.risk.fraud.rules.create(
            logic={},
            name="name",
        )
        assert rule is None

    @parametrize
    def test_raw_response_create(self, client: Jocall3) -> None:
        response = client.corporate.risk.fraud.rules.with_raw_response.create(
            logic={},
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert rule is None

    @parametrize
    def test_streaming_response_create(self, client: Jocall3) -> None:
        with client.corporate.risk.fraud.rules.with_streaming_response.create(
            logic={},
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert rule is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Jocall3) -> None:
        rule = client.corporate.risk.fraud.rules.update(
            rule_id="ruleId",
        )
        assert rule is None

    @parametrize
    def test_method_update_with_all_params(self, client: Jocall3) -> None:
        rule = client.corporate.risk.fraud.rules.update(
            rule_id="ruleId",
            action="action",
            name="name",
        )
        assert rule is None

    @parametrize
    def test_raw_response_update(self, client: Jocall3) -> None:
        response = client.corporate.risk.fraud.rules.with_raw_response.update(
            rule_id="ruleId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert rule is None

    @parametrize
    def test_streaming_response_update(self, client: Jocall3) -> None:
        with client.corporate.risk.fraud.rules.with_streaming_response.update(
            rule_id="ruleId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert rule is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Jocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.corporate.risk.fraud.rules.with_raw_response.update(
                rule_id="",
            )

    @parametrize
    def test_method_list(self, client: Jocall3) -> None:
        rule = client.corporate.risk.fraud.rules.list()
        assert_matches_type(RuleListResponse, rule, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Jocall3) -> None:
        response = client.corporate.risk.fraud.rules.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleListResponse, rule, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Jocall3) -> None:
        with client.corporate.risk.fraud.rules.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleListResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRules:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncJocall3) -> None:
        rule = await async_client.corporate.risk.fraud.rules.create(
            logic={},
            name="name",
        )
        assert rule is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncJocall3) -> None:
        response = await async_client.corporate.risk.fraud.rules.with_raw_response.create(
            logic={},
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert rule is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncJocall3) -> None:
        async with async_client.corporate.risk.fraud.rules.with_streaming_response.create(
            logic={},
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert rule is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncJocall3) -> None:
        rule = await async_client.corporate.risk.fraud.rules.update(
            rule_id="ruleId",
        )
        assert rule is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncJocall3) -> None:
        rule = await async_client.corporate.risk.fraud.rules.update(
            rule_id="ruleId",
            action="action",
            name="name",
        )
        assert rule is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncJocall3) -> None:
        response = await async_client.corporate.risk.fraud.rules.with_raw_response.update(
            rule_id="ruleId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert rule is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncJocall3) -> None:
        async with async_client.corporate.risk.fraud.rules.with_streaming_response.update(
            rule_id="ruleId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert rule is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncJocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.corporate.risk.fraud.rules.with_raw_response.update(
                rule_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncJocall3) -> None:
        rule = await async_client.corporate.risk.fraud.rules.list()
        assert_matches_type(RuleListResponse, rule, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJocall3) -> None:
        response = await async_client.corporate.risk.fraud.rules.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleListResponse, rule, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJocall3) -> None:
        async with async_client.corporate.risk.fraud.rules.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleListResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True
