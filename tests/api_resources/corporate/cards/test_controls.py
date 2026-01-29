# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestControls:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Jocall3) -> None:
        control = client.corporate.cards.controls.update(
            card_id="cardId",
        )
        assert control is None

    @parametrize
    def test_method_update_with_all_params(self, client: Jocall3) -> None:
        control = client.corporate.cards.controls.update(
            card_id="cardId",
            allowed_categories=["string"],
            geo_restriction=["string"],
            monthly_limit=0,
        )
        assert control is None

    @parametrize
    def test_raw_response_update(self, client: Jocall3) -> None:
        response = client.corporate.cards.controls.with_raw_response.update(
            card_id="cardId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        control = response.parse()
        assert control is None

    @parametrize
    def test_streaming_response_update(self, client: Jocall3) -> None:
        with client.corporate.cards.controls.with_streaming_response.update(
            card_id="cardId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            control = response.parse()
            assert control is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Jocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            client.corporate.cards.controls.with_raw_response.update(
                card_id="",
            )


class TestAsyncControls:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncJocall3) -> None:
        control = await async_client.corporate.cards.controls.update(
            card_id="cardId",
        )
        assert control is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncJocall3) -> None:
        control = await async_client.corporate.cards.controls.update(
            card_id="cardId",
            allowed_categories=["string"],
            geo_restriction=["string"],
            monthly_limit=0,
        )
        assert control is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncJocall3) -> None:
        response = await async_client.corporate.cards.controls.with_raw_response.update(
            card_id="cardId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        control = await response.parse()
        assert control is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncJocall3) -> None:
        async with async_client.corporate.cards.controls.with_streaming_response.update(
            card_id="cardId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            control = await response.parse()
            assert control is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncJocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            await async_client.corporate.cards.controls.with_raw_response.update(
                card_id="",
            )
