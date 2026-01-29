# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3
from tests.utils import assert_matches_type
from jocall3.types.accounts import OverdraftRetrieveSettingsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOverdraft:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve_settings(self, client: Jocall3) -> None:
        overdraft = client.accounts.overdraft.retrieve_settings(
            "accountId",
        )
        assert_matches_type(OverdraftRetrieveSettingsResponse, overdraft, path=["response"])

    @parametrize
    def test_raw_response_retrieve_settings(self, client: Jocall3) -> None:
        response = client.accounts.overdraft.with_raw_response.retrieve_settings(
            "accountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        overdraft = response.parse()
        assert_matches_type(OverdraftRetrieveSettingsResponse, overdraft, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_settings(self, client: Jocall3) -> None:
        with client.accounts.overdraft.with_streaming_response.retrieve_settings(
            "accountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            overdraft = response.parse()
            assert_matches_type(OverdraftRetrieveSettingsResponse, overdraft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_settings(self, client: Jocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.overdraft.with_raw_response.retrieve_settings(
                "",
            )

    @parametrize
    def test_method_update_settings(self, client: Jocall3) -> None:
        overdraft = client.accounts.overdraft.update_settings(
            account_id="accountId",
        )
        assert overdraft is None

    @parametrize
    def test_method_update_settings_with_all_params(self, client: Jocall3) -> None:
        overdraft = client.accounts.overdraft.update_settings(
            account_id="accountId",
            enabled=True,
            limit=0,
        )
        assert overdraft is None

    @parametrize
    def test_raw_response_update_settings(self, client: Jocall3) -> None:
        response = client.accounts.overdraft.with_raw_response.update_settings(
            account_id="accountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        overdraft = response.parse()
        assert overdraft is None

    @parametrize
    def test_streaming_response_update_settings(self, client: Jocall3) -> None:
        with client.accounts.overdraft.with_streaming_response.update_settings(
            account_id="accountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            overdraft = response.parse()
            assert overdraft is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_settings(self, client: Jocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.overdraft.with_raw_response.update_settings(
                account_id="",
            )


class TestAsyncOverdraft:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve_settings(self, async_client: AsyncJocall3) -> None:
        overdraft = await async_client.accounts.overdraft.retrieve_settings(
            "accountId",
        )
        assert_matches_type(OverdraftRetrieveSettingsResponse, overdraft, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_settings(self, async_client: AsyncJocall3) -> None:
        response = await async_client.accounts.overdraft.with_raw_response.retrieve_settings(
            "accountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        overdraft = await response.parse()
        assert_matches_type(OverdraftRetrieveSettingsResponse, overdraft, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_settings(self, async_client: AsyncJocall3) -> None:
        async with async_client.accounts.overdraft.with_streaming_response.retrieve_settings(
            "accountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            overdraft = await response.parse()
            assert_matches_type(OverdraftRetrieveSettingsResponse, overdraft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_settings(self, async_client: AsyncJocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.overdraft.with_raw_response.retrieve_settings(
                "",
            )

    @parametrize
    async def test_method_update_settings(self, async_client: AsyncJocall3) -> None:
        overdraft = await async_client.accounts.overdraft.update_settings(
            account_id="accountId",
        )
        assert overdraft is None

    @parametrize
    async def test_method_update_settings_with_all_params(self, async_client: AsyncJocall3) -> None:
        overdraft = await async_client.accounts.overdraft.update_settings(
            account_id="accountId",
            enabled=True,
            limit=0,
        )
        assert overdraft is None

    @parametrize
    async def test_raw_response_update_settings(self, async_client: AsyncJocall3) -> None:
        response = await async_client.accounts.overdraft.with_raw_response.update_settings(
            account_id="accountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        overdraft = await response.parse()
        assert overdraft is None

    @parametrize
    async def test_streaming_response_update_settings(self, async_client: AsyncJocall3) -> None:
        async with async_client.accounts.overdraft.with_streaming_response.update_settings(
            account_id="accountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            overdraft = await response.parse()
            assert overdraft is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_settings(self, async_client: AsyncJocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.overdraft.with_raw_response.update_settings(
                account_id="",
            )
