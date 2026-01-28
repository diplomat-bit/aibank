# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3
from tests.utils import assert_matches_type
from jocall3.types import (
    AccountLinkResponse,
    AccountListResponse,
    AccountRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Jocall3) -> None:
        account = client.accounts.retrieve(
            "acc_chase_checking_4567",
        )
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Jocall3) -> None:
        response = client.accounts.with_raw_response.retrieve(
            "acc_chase_checking_4567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Jocall3) -> None:
        with client.accounts.with_streaming_response.retrieve(
            "acc_chase_checking_4567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountRetrieveResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Jocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Jocall3) -> None:
        account = client.accounts.list()
        assert_matches_type(AccountListResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Jocall3) -> None:
        account = client.accounts.list(
            limit=0,
            offset=0,
        )
        assert_matches_type(AccountListResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Jocall3) -> None:
        response = client.accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountListResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Jocall3) -> None:
        with client.accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountListResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_link(self, client: Jocall3) -> None:
        account = client.accounts.link(
            country_code="US",
            institution_name="Bank of America",
        )
        assert_matches_type(AccountLinkResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_link(self, client: Jocall3) -> None:
        response = client.accounts.with_raw_response.link(
            country_code="US",
            institution_name="Bank of America",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountLinkResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_link(self, client: Jocall3) -> None:
        with client.accounts.with_streaming_response.link(
            country_code="US",
            institution_name="Bank of America",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountLinkResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAccounts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncJocall3) -> None:
        account = await async_client.accounts.retrieve(
            "acc_chase_checking_4567",
        )
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncJocall3) -> None:
        response = await async_client.accounts.with_raw_response.retrieve(
            "acc_chase_checking_4567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncJocall3) -> None:
        async with async_client.accounts.with_streaming_response.retrieve(
            "acc_chase_checking_4567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountRetrieveResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncJocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncJocall3) -> None:
        account = await async_client.accounts.list()
        assert_matches_type(AccountListResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncJocall3) -> None:
        account = await async_client.accounts.list(
            limit=0,
            offset=0,
        )
        assert_matches_type(AccountListResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJocall3) -> None:
        response = await async_client.accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountListResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJocall3) -> None:
        async with async_client.accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountListResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_link(self, async_client: AsyncJocall3) -> None:
        account = await async_client.accounts.link(
            country_code="US",
            institution_name="Bank of America",
        )
        assert_matches_type(AccountLinkResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_link(self, async_client: AsyncJocall3) -> None:
        response = await async_client.accounts.with_raw_response.link(
            country_code="US",
            institution_name="Bank of America",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountLinkResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_link(self, async_client: AsyncJocall3) -> None:
        async with async_client.accounts.with_streaming_response.link(
            country_code="US",
            institution_name="Bank of America",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountLinkResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True
