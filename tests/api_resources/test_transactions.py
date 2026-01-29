# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3
from tests.utils import assert_matches_type
from jocall3.types import (
    TransactionListResponse,
)
from jocall3.types.shared import Transaction

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTransactions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Jocall3) -> None:
        transaction = client.transactions.retrieve(
            "transactionId",
        )
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Jocall3) -> None:
        response = client.transactions.with_raw_response.retrieve(
            "transactionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Jocall3) -> None:
        with client.transactions.with_streaming_response.retrieve(
            "transactionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(Transaction, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Jocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transaction_id` but received ''"):
            client.transactions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Jocall3) -> None:
        transaction = client.transactions.list()
        assert_matches_type(TransactionListResponse, transaction, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Jocall3) -> None:
        transaction = client.transactions.list(
            limit=0,
            max_amount=0,
            min_amount=0,
            offset=0,
            type="type",
        )
        assert_matches_type(TransactionListResponse, transaction, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Jocall3) -> None:
        response = client.transactions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(TransactionListResponse, transaction, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Jocall3) -> None:
        with client.transactions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(TransactionListResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_add_notes(self, client: Jocall3) -> None:
        transaction = client.transactions.add_notes(
            transaction_id="transactionId",
            notes="notes",
        )
        assert transaction is None

    @parametrize
    def test_raw_response_add_notes(self, client: Jocall3) -> None:
        response = client.transactions.with_raw_response.add_notes(
            transaction_id="transactionId",
            notes="notes",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert transaction is None

    @parametrize
    def test_streaming_response_add_notes(self, client: Jocall3) -> None:
        with client.transactions.with_streaming_response.add_notes(
            transaction_id="transactionId",
            notes="notes",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert transaction is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add_notes(self, client: Jocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transaction_id` but received ''"):
            client.transactions.with_raw_response.add_notes(
                transaction_id="",
                notes="notes",
            )

    @parametrize
    def test_method_categorize(self, client: Jocall3) -> None:
        transaction = client.transactions.categorize(
            transaction_id="transactionId",
            category="category",
        )
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    def test_method_categorize_with_all_params(self, client: Jocall3) -> None:
        transaction = client.transactions.categorize(
            transaction_id="transactionId",
            category="category",
            apply_to_future=True,
        )
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    def test_raw_response_categorize(self, client: Jocall3) -> None:
        response = client.transactions.with_raw_response.categorize(
            transaction_id="transactionId",
            category="category",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    def test_streaming_response_categorize(self, client: Jocall3) -> None:
        with client.transactions.with_streaming_response.categorize(
            transaction_id="transactionId",
            category="category",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(Transaction, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_categorize(self, client: Jocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transaction_id` but received ''"):
            client.transactions.with_raw_response.categorize(
                transaction_id="",
                category="category",
            )

    @parametrize
    def test_method_dispute(self, client: Jocall3) -> None:
        transaction = client.transactions.dispute(
            transaction_id="transactionId",
            reason="fraudulent",
        )
        assert transaction is None

    @parametrize
    def test_method_dispute_with_all_params(self, client: Jocall3) -> None:
        transaction = client.transactions.dispute(
            transaction_id="transactionId",
            reason="fraudulent",
            evidence_files=["string"],
        )
        assert transaction is None

    @parametrize
    def test_raw_response_dispute(self, client: Jocall3) -> None:
        response = client.transactions.with_raw_response.dispute(
            transaction_id="transactionId",
            reason="fraudulent",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert transaction is None

    @parametrize
    def test_streaming_response_dispute(self, client: Jocall3) -> None:
        with client.transactions.with_streaming_response.dispute(
            transaction_id="transactionId",
            reason="fraudulent",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert transaction is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_dispute(self, client: Jocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transaction_id` but received ''"):
            client.transactions.with_raw_response.dispute(
                transaction_id="",
                reason="fraudulent",
            )

    @parametrize
    def test_method_split(self, client: Jocall3) -> None:
        transaction = client.transactions.split(
            transaction_id="transactionId",
            splits=[{}],
        )
        assert transaction is None

    @parametrize
    def test_raw_response_split(self, client: Jocall3) -> None:
        response = client.transactions.with_raw_response.split(
            transaction_id="transactionId",
            splits=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert transaction is None

    @parametrize
    def test_streaming_response_split(self, client: Jocall3) -> None:
        with client.transactions.with_streaming_response.split(
            transaction_id="transactionId",
            splits=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert transaction is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_split(self, client: Jocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transaction_id` but received ''"):
            client.transactions.with_raw_response.split(
                transaction_id="",
                splits=[{}],
            )


class TestAsyncTransactions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncJocall3) -> None:
        transaction = await async_client.transactions.retrieve(
            "transactionId",
        )
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncJocall3) -> None:
        response = await async_client.transactions.with_raw_response.retrieve(
            "transactionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncJocall3) -> None:
        async with async_client.transactions.with_streaming_response.retrieve(
            "transactionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(Transaction, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncJocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transaction_id` but received ''"):
            await async_client.transactions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncJocall3) -> None:
        transaction = await async_client.transactions.list()
        assert_matches_type(TransactionListResponse, transaction, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncJocall3) -> None:
        transaction = await async_client.transactions.list(
            limit=0,
            max_amount=0,
            min_amount=0,
            offset=0,
            type="type",
        )
        assert_matches_type(TransactionListResponse, transaction, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJocall3) -> None:
        response = await async_client.transactions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(TransactionListResponse, transaction, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJocall3) -> None:
        async with async_client.transactions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(TransactionListResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_add_notes(self, async_client: AsyncJocall3) -> None:
        transaction = await async_client.transactions.add_notes(
            transaction_id="transactionId",
            notes="notes",
        )
        assert transaction is None

    @parametrize
    async def test_raw_response_add_notes(self, async_client: AsyncJocall3) -> None:
        response = await async_client.transactions.with_raw_response.add_notes(
            transaction_id="transactionId",
            notes="notes",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert transaction is None

    @parametrize
    async def test_streaming_response_add_notes(self, async_client: AsyncJocall3) -> None:
        async with async_client.transactions.with_streaming_response.add_notes(
            transaction_id="transactionId",
            notes="notes",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert transaction is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add_notes(self, async_client: AsyncJocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transaction_id` but received ''"):
            await async_client.transactions.with_raw_response.add_notes(
                transaction_id="",
                notes="notes",
            )

    @parametrize
    async def test_method_categorize(self, async_client: AsyncJocall3) -> None:
        transaction = await async_client.transactions.categorize(
            transaction_id="transactionId",
            category="category",
        )
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    async def test_method_categorize_with_all_params(self, async_client: AsyncJocall3) -> None:
        transaction = await async_client.transactions.categorize(
            transaction_id="transactionId",
            category="category",
            apply_to_future=True,
        )
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    async def test_raw_response_categorize(self, async_client: AsyncJocall3) -> None:
        response = await async_client.transactions.with_raw_response.categorize(
            transaction_id="transactionId",
            category="category",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    async def test_streaming_response_categorize(self, async_client: AsyncJocall3) -> None:
        async with async_client.transactions.with_streaming_response.categorize(
            transaction_id="transactionId",
            category="category",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(Transaction, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_categorize(self, async_client: AsyncJocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transaction_id` but received ''"):
            await async_client.transactions.with_raw_response.categorize(
                transaction_id="",
                category="category",
            )

    @parametrize
    async def test_method_dispute(self, async_client: AsyncJocall3) -> None:
        transaction = await async_client.transactions.dispute(
            transaction_id="transactionId",
            reason="fraudulent",
        )
        assert transaction is None

    @parametrize
    async def test_method_dispute_with_all_params(self, async_client: AsyncJocall3) -> None:
        transaction = await async_client.transactions.dispute(
            transaction_id="transactionId",
            reason="fraudulent",
            evidence_files=["string"],
        )
        assert transaction is None

    @parametrize
    async def test_raw_response_dispute(self, async_client: AsyncJocall3) -> None:
        response = await async_client.transactions.with_raw_response.dispute(
            transaction_id="transactionId",
            reason="fraudulent",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert transaction is None

    @parametrize
    async def test_streaming_response_dispute(self, async_client: AsyncJocall3) -> None:
        async with async_client.transactions.with_streaming_response.dispute(
            transaction_id="transactionId",
            reason="fraudulent",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert transaction is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_dispute(self, async_client: AsyncJocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transaction_id` but received ''"):
            await async_client.transactions.with_raw_response.dispute(
                transaction_id="",
                reason="fraudulent",
            )

    @parametrize
    async def test_method_split(self, async_client: AsyncJocall3) -> None:
        transaction = await async_client.transactions.split(
            transaction_id="transactionId",
            splits=[{}],
        )
        assert transaction is None

    @parametrize
    async def test_raw_response_split(self, async_client: AsyncJocall3) -> None:
        response = await async_client.transactions.with_raw_response.split(
            transaction_id="transactionId",
            splits=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert transaction is None

    @parametrize
    async def test_streaming_response_split(self, async_client: AsyncJocall3) -> None:
        async with async_client.transactions.with_streaming_response.split(
            transaction_id="transactionId",
            splits=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert transaction is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_split(self, async_client: AsyncJocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transaction_id` but received ''"):
            await async_client.transactions.with_raw_response.split(
                transaction_id="",
                splits=[{}],
            )
