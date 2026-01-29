# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3
from tests.utils import assert_matches_type
from jocall3.types.accounts import (
    TransactionListPendingResponse,
    TransactionListArchivedResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTransactions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list_archived(self, client: Jocall3) -> None:
        transaction = client.accounts.transactions.list_archived(
            account_id="accountId",
        )
        assert_matches_type(TransactionListArchivedResponse, transaction, path=["response"])

    @parametrize
    def test_method_list_archived_with_all_params(self, client: Jocall3) -> None:
        transaction = client.accounts.transactions.list_archived(
            account_id="accountId",
            year=0,
        )
        assert_matches_type(TransactionListArchivedResponse, transaction, path=["response"])

    @parametrize
    def test_raw_response_list_archived(self, client: Jocall3) -> None:
        response = client.accounts.transactions.with_raw_response.list_archived(
            account_id="accountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(TransactionListArchivedResponse, transaction, path=["response"])

    @parametrize
    def test_streaming_response_list_archived(self, client: Jocall3) -> None:
        with client.accounts.transactions.with_streaming_response.list_archived(
            account_id="accountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(TransactionListArchivedResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_archived(self, client: Jocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.transactions.with_raw_response.list_archived(
                account_id="",
            )

    @parametrize
    def test_method_list_pending(self, client: Jocall3) -> None:
        transaction = client.accounts.transactions.list_pending(
            "accountId",
        )
        assert_matches_type(TransactionListPendingResponse, transaction, path=["response"])

    @parametrize
    def test_raw_response_list_pending(self, client: Jocall3) -> None:
        response = client.accounts.transactions.with_raw_response.list_pending(
            "accountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(TransactionListPendingResponse, transaction, path=["response"])

    @parametrize
    def test_streaming_response_list_pending(self, client: Jocall3) -> None:
        with client.accounts.transactions.with_streaming_response.list_pending(
            "accountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(TransactionListPendingResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_pending(self, client: Jocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.transactions.with_raw_response.list_pending(
                "",
            )


class TestAsyncTransactions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list_archived(self, async_client: AsyncJocall3) -> None:
        transaction = await async_client.accounts.transactions.list_archived(
            account_id="accountId",
        )
        assert_matches_type(TransactionListArchivedResponse, transaction, path=["response"])

    @parametrize
    async def test_method_list_archived_with_all_params(self, async_client: AsyncJocall3) -> None:
        transaction = await async_client.accounts.transactions.list_archived(
            account_id="accountId",
            year=0,
        )
        assert_matches_type(TransactionListArchivedResponse, transaction, path=["response"])

    @parametrize
    async def test_raw_response_list_archived(self, async_client: AsyncJocall3) -> None:
        response = await async_client.accounts.transactions.with_raw_response.list_archived(
            account_id="accountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(TransactionListArchivedResponse, transaction, path=["response"])

    @parametrize
    async def test_streaming_response_list_archived(self, async_client: AsyncJocall3) -> None:
        async with async_client.accounts.transactions.with_streaming_response.list_archived(
            account_id="accountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(TransactionListArchivedResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_archived(self, async_client: AsyncJocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.transactions.with_raw_response.list_archived(
                account_id="",
            )

    @parametrize
    async def test_method_list_pending(self, async_client: AsyncJocall3) -> None:
        transaction = await async_client.accounts.transactions.list_pending(
            "accountId",
        )
        assert_matches_type(TransactionListPendingResponse, transaction, path=["response"])

    @parametrize
    async def test_raw_response_list_pending(self, async_client: AsyncJocall3) -> None:
        response = await async_client.accounts.transactions.with_raw_response.list_pending(
            "accountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(TransactionListPendingResponse, transaction, path=["response"])

    @parametrize
    async def test_streaming_response_list_pending(self, async_client: AsyncJocall3) -> None:
        async with async_client.accounts.transactions.with_streaming_response.list_pending(
            "accountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(TransactionListPendingResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_pending(self, async_client: AsyncJocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.transactions.with_raw_response.list_pending(
                "",
            )
