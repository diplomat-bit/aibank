# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSanctionScreening:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_screen(self, client: Jocall3) -> None:
        sanction_screening = client.corporate.sanction_screening.screen()
        assert_matches_type(object, sanction_screening, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_screen_with_all_params(self, client: Jocall3) -> None:
        sanction_screening = client.corporate.sanction_screening.screen(
            address={},
        )
        assert_matches_type(object, sanction_screening, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_screen(self, client: Jocall3) -> None:
        response = client.corporate.sanction_screening.with_raw_response.screen()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sanction_screening = response.parse()
        assert_matches_type(object, sanction_screening, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_screen(self, client: Jocall3) -> None:
        with client.corporate.sanction_screening.with_streaming_response.screen() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sanction_screening = response.parse()
            assert_matches_type(object, sanction_screening, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSanctionScreening:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_screen(self, async_client: AsyncJocall3) -> None:
        sanction_screening = await async_client.corporate.sanction_screening.screen()
        assert_matches_type(object, sanction_screening, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_screen_with_all_params(self, async_client: AsyncJocall3) -> None:
        sanction_screening = await async_client.corporate.sanction_screening.screen(
            address={},
        )
        assert_matches_type(object, sanction_screening, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_screen(self, async_client: AsyncJocall3) -> None:
        response = await async_client.corporate.sanction_screening.with_raw_response.screen()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sanction_screening = await response.parse()
        assert_matches_type(object, sanction_screening, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_screen(self, async_client: AsyncJocall3) -> None:
        async with async_client.corporate.sanction_screening.with_streaming_response.screen() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sanction_screening = await response.parse()
            assert_matches_type(object, sanction_screening, path=["response"])

        assert cast(Any, response.is_closed) is True
