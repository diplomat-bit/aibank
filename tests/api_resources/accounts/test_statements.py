# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from jocall3 import Jocall3, AsyncJocall3
from tests.utils import assert_matches_type
from jocall3._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from jocall3.types.accounts import StatementListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStatements:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Jocall3) -> None:
        statement = client.accounts.statements.list(
            "accountId",
        )
        assert_matches_type(StatementListResponse, statement, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Jocall3) -> None:
        response = client.accounts.statements.with_raw_response.list(
            "accountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statement = response.parse()
        assert_matches_type(StatementListResponse, statement, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Jocall3) -> None:
        with client.accounts.statements.with_streaming_response.list(
            "accountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statement = response.parse()
            assert_matches_type(StatementListResponse, statement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Jocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.statements.with_raw_response.list(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download(self, client: Jocall3, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/accountId/statements/statementId/pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        statement = client.accounts.statements.download(
            statement_id="statementId",
            account_id="accountId",
        )
        assert statement.is_closed
        assert statement.json() == {"foo": "bar"}
        assert cast(Any, statement.is_closed) is True
        assert isinstance(statement, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_download(self, client: Jocall3, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/accountId/statements/statementId/pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        statement = client.accounts.statements.with_raw_response.download(
            statement_id="statementId",
            account_id="accountId",
        )

        assert statement.is_closed is True
        assert statement.http_request.headers.get("X-Stainless-Lang") == "python"
        assert statement.json() == {"foo": "bar"}
        assert isinstance(statement, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_download(self, client: Jocall3, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/accountId/statements/statementId/pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.accounts.statements.with_streaming_response.download(
            statement_id="statementId",
            account_id="accountId",
        ) as statement:
            assert not statement.is_closed
            assert statement.http_request.headers.get("X-Stainless-Lang") == "python"

            assert statement.json() == {"foo": "bar"}
            assert cast(Any, statement.is_closed) is True
            assert isinstance(statement, StreamedBinaryAPIResponse)

        assert cast(Any, statement.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_download(self, client: Jocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.statements.with_raw_response.download(
                statement_id="statementId",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `statement_id` but received ''"):
            client.accounts.statements.with_raw_response.download(
                statement_id="",
                account_id="accountId",
            )


class TestAsyncStatements:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncJocall3) -> None:
        statement = await async_client.accounts.statements.list(
            "accountId",
        )
        assert_matches_type(StatementListResponse, statement, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJocall3) -> None:
        response = await async_client.accounts.statements.with_raw_response.list(
            "accountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statement = await response.parse()
        assert_matches_type(StatementListResponse, statement, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJocall3) -> None:
        async with async_client.accounts.statements.with_streaming_response.list(
            "accountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statement = await response.parse()
            assert_matches_type(StatementListResponse, statement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncJocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.statements.with_raw_response.list(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download(self, async_client: AsyncJocall3, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/accountId/statements/statementId/pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        statement = await async_client.accounts.statements.download(
            statement_id="statementId",
            account_id="accountId",
        )
        assert statement.is_closed
        assert await statement.json() == {"foo": "bar"}
        assert cast(Any, statement.is_closed) is True
        assert isinstance(statement, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_download(self, async_client: AsyncJocall3, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/accountId/statements/statementId/pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        statement = await async_client.accounts.statements.with_raw_response.download(
            statement_id="statementId",
            account_id="accountId",
        )

        assert statement.is_closed is True
        assert statement.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await statement.json() == {"foo": "bar"}
        assert isinstance(statement, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_download(self, async_client: AsyncJocall3, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/accountId/statements/statementId/pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.accounts.statements.with_streaming_response.download(
            statement_id="statementId",
            account_id="accountId",
        ) as statement:
            assert not statement.is_closed
            assert statement.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await statement.json() == {"foo": "bar"}
            assert cast(Any, statement.is_closed) is True
            assert isinstance(statement, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, statement.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_download(self, async_client: AsyncJocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.statements.with_raw_response.download(
                statement_id="statementId",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `statement_id` but received ''"):
            await async_client.accounts.statements.with_raw_response.download(
                statement_id="",
                account_id="accountId",
            )
