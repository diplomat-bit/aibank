# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3
from tests.utils import assert_matches_type
from jocall3.types.corporate import (
    CardIssueVirtualResponse,
    CardIssuePhysicalResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCards:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_freeze(self, client: Jocall3) -> None:
        card = client.corporate.cards.freeze(
            card_id="cardId",
            frozen=True,
        )
        assert card is None

    @parametrize
    def test_raw_response_freeze(self, client: Jocall3) -> None:
        response = client.corporate.cards.with_raw_response.freeze(
            card_id="cardId",
            frozen=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert card is None

    @parametrize
    def test_streaming_response_freeze(self, client: Jocall3) -> None:
        with client.corporate.cards.with_streaming_response.freeze(
            card_id="cardId",
            frozen=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert card is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_freeze(self, client: Jocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            client.corporate.cards.with_raw_response.freeze(
                card_id="",
                frozen=True,
            )

    @parametrize
    def test_method_issue_physical(self, client: Jocall3) -> None:
        card = client.corporate.cards.issue_physical(
            holder_name="holderName",
            shipping_address={},
        )
        assert_matches_type(CardIssuePhysicalResponse, card, path=["response"])

    @parametrize
    def test_method_issue_physical_with_all_params(self, client: Jocall3) -> None:
        card = client.corporate.cards.issue_physical(
            holder_name="holderName",
            shipping_address={
                "city": "city",
                "country": "country",
                "state": "state",
                "street": "street",
                "zip": "zip",
            },
        )
        assert_matches_type(CardIssuePhysicalResponse, card, path=["response"])

    @parametrize
    def test_raw_response_issue_physical(self, client: Jocall3) -> None:
        response = client.corporate.cards.with_raw_response.issue_physical(
            holder_name="holderName",
            shipping_address={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(CardIssuePhysicalResponse, card, path=["response"])

    @parametrize
    def test_streaming_response_issue_physical(self, client: Jocall3) -> None:
        with client.corporate.cards.with_streaming_response.issue_physical(
            holder_name="holderName",
            shipping_address={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(CardIssuePhysicalResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_issue_virtual(self, client: Jocall3) -> None:
        card = client.corporate.cards.issue_virtual(
            holder_name="holderName",
            monthly_limit=0,
            purpose="purpose",
        )
        assert_matches_type(CardIssueVirtualResponse, card, path=["response"])

    @parametrize
    def test_method_issue_virtual_with_all_params(self, client: Jocall3) -> None:
        card = client.corporate.cards.issue_virtual(
            holder_name="holderName",
            monthly_limit=0,
            purpose="purpose",
            metadata={},
        )
        assert_matches_type(CardIssueVirtualResponse, card, path=["response"])

    @parametrize
    def test_raw_response_issue_virtual(self, client: Jocall3) -> None:
        response = client.corporate.cards.with_raw_response.issue_virtual(
            holder_name="holderName",
            monthly_limit=0,
            purpose="purpose",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(CardIssueVirtualResponse, card, path=["response"])

    @parametrize
    def test_streaming_response_issue_virtual(self, client: Jocall3) -> None:
        with client.corporate.cards.with_streaming_response.issue_virtual(
            holder_name="holderName",
            monthly_limit=0,
            purpose="purpose",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(CardIssueVirtualResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCards:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_freeze(self, async_client: AsyncJocall3) -> None:
        card = await async_client.corporate.cards.freeze(
            card_id="cardId",
            frozen=True,
        )
        assert card is None

    @parametrize
    async def test_raw_response_freeze(self, async_client: AsyncJocall3) -> None:
        response = await async_client.corporate.cards.with_raw_response.freeze(
            card_id="cardId",
            frozen=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert card is None

    @parametrize
    async def test_streaming_response_freeze(self, async_client: AsyncJocall3) -> None:
        async with async_client.corporate.cards.with_streaming_response.freeze(
            card_id="cardId",
            frozen=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert card is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_freeze(self, async_client: AsyncJocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            await async_client.corporate.cards.with_raw_response.freeze(
                card_id="",
                frozen=True,
            )

    @parametrize
    async def test_method_issue_physical(self, async_client: AsyncJocall3) -> None:
        card = await async_client.corporate.cards.issue_physical(
            holder_name="holderName",
            shipping_address={},
        )
        assert_matches_type(CardIssuePhysicalResponse, card, path=["response"])

    @parametrize
    async def test_method_issue_physical_with_all_params(self, async_client: AsyncJocall3) -> None:
        card = await async_client.corporate.cards.issue_physical(
            holder_name="holderName",
            shipping_address={
                "city": "city",
                "country": "country",
                "state": "state",
                "street": "street",
                "zip": "zip",
            },
        )
        assert_matches_type(CardIssuePhysicalResponse, card, path=["response"])

    @parametrize
    async def test_raw_response_issue_physical(self, async_client: AsyncJocall3) -> None:
        response = await async_client.corporate.cards.with_raw_response.issue_physical(
            holder_name="holderName",
            shipping_address={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(CardIssuePhysicalResponse, card, path=["response"])

    @parametrize
    async def test_streaming_response_issue_physical(self, async_client: AsyncJocall3) -> None:
        async with async_client.corporate.cards.with_streaming_response.issue_physical(
            holder_name="holderName",
            shipping_address={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(CardIssuePhysicalResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_issue_virtual(self, async_client: AsyncJocall3) -> None:
        card = await async_client.corporate.cards.issue_virtual(
            holder_name="holderName",
            monthly_limit=0,
            purpose="purpose",
        )
        assert_matches_type(CardIssueVirtualResponse, card, path=["response"])

    @parametrize
    async def test_method_issue_virtual_with_all_params(self, async_client: AsyncJocall3) -> None:
        card = await async_client.corporate.cards.issue_virtual(
            holder_name="holderName",
            monthly_limit=0,
            purpose="purpose",
            metadata={},
        )
        assert_matches_type(CardIssueVirtualResponse, card, path=["response"])

    @parametrize
    async def test_raw_response_issue_virtual(self, async_client: AsyncJocall3) -> None:
        response = await async_client.corporate.cards.with_raw_response.issue_virtual(
            holder_name="holderName",
            monthly_limit=0,
            purpose="purpose",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(CardIssueVirtualResponse, card, path=["response"])

    @parametrize
    async def test_streaming_response_issue_virtual(self, async_client: AsyncJocall3) -> None:
        async with async_client.corporate.cards.with_streaming_response.issue_virtual(
            holder_name="holderName",
            monthly_limit=0,
            purpose="purpose",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(CardIssueVirtualResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True
