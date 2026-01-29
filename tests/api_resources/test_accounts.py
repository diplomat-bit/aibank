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
    AccountOpenResponse,
    AccountRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Jocall3) -> None:
        account = client.accounts.retrieve(
            "accountId",
        )
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Jocall3) -> None:
        response = client.accounts.with_raw_response.retrieve(
            "accountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Jocall3) -> None:
        with client.accounts.with_streaming_response.retrieve(
            "accountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountRetrieveResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Jocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Jocall3) -> None:
        account = client.accounts.list()
        assert_matches_type(AccountListResponse, account, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Jocall3) -> None:
        response = client.accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountListResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Jocall3) -> None:
        with client.accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountListResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_close(self, client: Jocall3) -> None:
        account = client.accounts.close(
            "accountId",
        )
        assert account is None

    @parametrize
    def test_raw_response_close(self, client: Jocall3) -> None:
        response = client.accounts.with_raw_response.close(
            "accountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert account is None

    @parametrize
    def test_streaming_response_close(self, client: Jocall3) -> None:
        with client.accounts.with_streaming_response.close(
            "accountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert account is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_close(self, client: Jocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.with_raw_response.close(
                "",
            )

    @parametrize
    def test_method_link(self, client: Jocall3) -> None:
        account = client.accounts.link(
            institution_id="institutionId",
            public_token="publicToken",
        )
        assert_matches_type(AccountLinkResponse, account, path=["response"])

    @parametrize
    def test_raw_response_link(self, client: Jocall3) -> None:
        response = client.accounts.with_raw_response.link(
            institution_id="institutionId",
            public_token="publicToken",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountLinkResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_link(self, client: Jocall3) -> None:
        with client.accounts.with_streaming_response.link(
            institution_id="institutionId",
            public_token="publicToken",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountLinkResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_open(self, client: Jocall3) -> None:
        account = client.accounts.open(
            currency="USD",
            initial_deposit=0,
            product_type="quantum_checking",
        )
        assert_matches_type(AccountOpenResponse, account, path=["response"])

    @parametrize
    def test_method_open_with_all_params(self, client: Jocall3) -> None:
        account = client.accounts.open(
            currency="USD",
            initial_deposit=0,
            product_type="quantum_checking",
            owners=["string"],
        )
        assert_matches_type(AccountOpenResponse, account, path=["response"])

    @parametrize
    def test_raw_response_open(self, client: Jocall3) -> None:
        response = client.accounts.with_raw_response.open(
            currency="USD",
            initial_deposit=0,
            product_type="quantum_checking",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountOpenResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_open(self, client: Jocall3) -> None:
        with client.accounts.with_streaming_response.open(
            currency="USD",
            initial_deposit=0,
            product_type="quantum_checking",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountOpenResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAccounts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncJocall3) -> None:
        account = await async_client.accounts.retrieve(
            "accountId",
        )
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncJocall3) -> None:
        response = await async_client.accounts.with_raw_response.retrieve(
            "accountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncJocall3) -> None:
        async with async_client.accounts.with_streaming_response.retrieve(
            "accountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountRetrieveResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncJocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncJocall3) -> None:
        account = await async_client.accounts.list()
        assert_matches_type(AccountListResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJocall3) -> None:
        response = await async_client.accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountListResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJocall3) -> None:
        async with async_client.accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountListResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_close(self, async_client: AsyncJocall3) -> None:
        account = await async_client.accounts.close(
            "accountId",
        )
        assert account is None

    @parametrize
    async def test_raw_response_close(self, async_client: AsyncJocall3) -> None:
        response = await async_client.accounts.with_raw_response.close(
            "accountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert account is None

    @parametrize
    async def test_streaming_response_close(self, async_client: AsyncJocall3) -> None:
        async with async_client.accounts.with_streaming_response.close(
            "accountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert account is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_close(self, async_client: AsyncJocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.with_raw_response.close(
                "",
            )

    @parametrize
    async def test_method_link(self, async_client: AsyncJocall3) -> None:
        account = await async_client.accounts.link(
            institution_id="institutionId",
            public_token="publicToken",
        )
        assert_matches_type(AccountLinkResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_link(self, async_client: AsyncJocall3) -> None:
        response = await async_client.accounts.with_raw_response.link(
            institution_id="institutionId",
            public_token="publicToken",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountLinkResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_link(self, async_client: AsyncJocall3) -> None:
        async with async_client.accounts.with_streaming_response.link(
            institution_id="institutionId",
            public_token="publicToken",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountLinkResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_open(self, async_client: AsyncJocall3) -> None:
        account = await async_client.accounts.open(
            currency="USD",
            initial_deposit=0,
            product_type="quantum_checking",
        )
        assert_matches_type(AccountOpenResponse, account, path=["response"])

    @parametrize
    async def test_method_open_with_all_params(self, async_client: AsyncJocall3) -> None:
        account = await async_client.accounts.open(
            currency="USD",
            initial_deposit=0,
            product_type="quantum_checking",
            owners=["string"],
        )
        assert_matches_type(AccountOpenResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_open(self, async_client: AsyncJocall3) -> None:
        response = await async_client.accounts.with_raw_response.open(
            currency="USD",
            initial_deposit=0,
            product_type="quantum_checking",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountOpenResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_open(self, async_client: AsyncJocall3) -> None:
        async with async_client.accounts.with_streaming_response.open(
            currency="USD",
            initial_deposit=0,
            product_type="quantum_checking",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountOpenResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True
