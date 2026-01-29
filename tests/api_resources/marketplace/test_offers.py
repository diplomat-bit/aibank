# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3
from tests.utils import assert_matches_type
from jocall3.types.marketplace import OfferListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOffers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Jocall3) -> None:
        offer = client.marketplace.offers.list()
        assert_matches_type(OfferListResponse, offer, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Jocall3) -> None:
        response = client.marketplace.offers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        offer = response.parse()
        assert_matches_type(OfferListResponse, offer, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Jocall3) -> None:
        with client.marketplace.offers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            offer = response.parse()
            assert_matches_type(OfferListResponse, offer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_redeem(self, client: Jocall3) -> None:
        offer = client.marketplace.offers.redeem(
            "offerId",
        )
        assert offer is None

    @parametrize
    def test_raw_response_redeem(self, client: Jocall3) -> None:
        response = client.marketplace.offers.with_raw_response.redeem(
            "offerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        offer = response.parse()
        assert offer is None

    @parametrize
    def test_streaming_response_redeem(self, client: Jocall3) -> None:
        with client.marketplace.offers.with_streaming_response.redeem(
            "offerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            offer = response.parse()
            assert offer is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_redeem(self, client: Jocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `offer_id` but received ''"):
            client.marketplace.offers.with_raw_response.redeem(
                "",
            )


class TestAsyncOffers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncJocall3) -> None:
        offer = await async_client.marketplace.offers.list()
        assert_matches_type(OfferListResponse, offer, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJocall3) -> None:
        response = await async_client.marketplace.offers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        offer = await response.parse()
        assert_matches_type(OfferListResponse, offer, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJocall3) -> None:
        async with async_client.marketplace.offers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            offer = await response.parse()
            assert_matches_type(OfferListResponse, offer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_redeem(self, async_client: AsyncJocall3) -> None:
        offer = await async_client.marketplace.offers.redeem(
            "offerId",
        )
        assert offer is None

    @parametrize
    async def test_raw_response_redeem(self, async_client: AsyncJocall3) -> None:
        response = await async_client.marketplace.offers.with_raw_response.redeem(
            "offerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        offer = await response.parse()
        assert offer is None

    @parametrize
    async def test_streaming_response_redeem(self, async_client: AsyncJocall3) -> None:
        async with async_client.marketplace.offers.with_streaming_response.redeem(
            "offerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            offer = await response.parse()
            assert offer is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_redeem(self, async_client: AsyncJocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `offer_id` but received ''"):
            await async_client.marketplace.offers.with_raw_response.redeem(
                "",
            )
