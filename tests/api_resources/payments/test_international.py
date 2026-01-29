# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3
from tests.utils import assert_matches_type
from jocall3.types.payments import (
    InternationalRetrieveStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInternational:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve_status(self, client: Jocall3) -> None:
        international = client.payments.international.retrieve_status(
            "paymentId",
        )
        assert_matches_type(InternationalRetrieveStatusResponse, international, path=["response"])

    @parametrize
    def test_raw_response_retrieve_status(self, client: Jocall3) -> None:
        response = client.payments.international.with_raw_response.retrieve_status(
            "paymentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        international = response.parse()
        assert_matches_type(InternationalRetrieveStatusResponse, international, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_status(self, client: Jocall3) -> None:
        with client.payments.international.with_streaming_response.retrieve_status(
            "paymentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            international = response.parse()
            assert_matches_type(InternationalRetrieveStatusResponse, international, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_status(self, client: Jocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payment_id` but received ''"):
            client.payments.international.with_raw_response.retrieve_status(
                "",
            )

    @parametrize
    def test_method_send_sepa(self, client: Jocall3) -> None:
        international = client.payments.international.send_sepa(
            amount=0,
            iban="iban",
        )
        assert international is None

    @parametrize
    def test_raw_response_send_sepa(self, client: Jocall3) -> None:
        response = client.payments.international.with_raw_response.send_sepa(
            amount=0,
            iban="iban",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        international = response.parse()
        assert international is None

    @parametrize
    def test_streaming_response_send_sepa(self, client: Jocall3) -> None:
        with client.payments.international.with_streaming_response.send_sepa(
            amount=0,
            iban="iban",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            international = response.parse()
            assert international is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_send_swift(self, client: Jocall3) -> None:
        international = client.payments.international.send_swift(
            amount=0,
            bic="bic",
            currency="currency",
            iban="iban",
        )
        assert international is None

    @parametrize
    def test_raw_response_send_swift(self, client: Jocall3) -> None:
        response = client.payments.international.with_raw_response.send_swift(
            amount=0,
            bic="bic",
            currency="currency",
            iban="iban",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        international = response.parse()
        assert international is None

    @parametrize
    def test_streaming_response_send_swift(self, client: Jocall3) -> None:
        with client.payments.international.with_streaming_response.send_swift(
            amount=0,
            bic="bic",
            currency="currency",
            iban="iban",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            international = response.parse()
            assert international is None

        assert cast(Any, response.is_closed) is True


class TestAsyncInternational:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve_status(self, async_client: AsyncJocall3) -> None:
        international = await async_client.payments.international.retrieve_status(
            "paymentId",
        )
        assert_matches_type(InternationalRetrieveStatusResponse, international, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_status(self, async_client: AsyncJocall3) -> None:
        response = await async_client.payments.international.with_raw_response.retrieve_status(
            "paymentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        international = await response.parse()
        assert_matches_type(InternationalRetrieveStatusResponse, international, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_status(self, async_client: AsyncJocall3) -> None:
        async with async_client.payments.international.with_streaming_response.retrieve_status(
            "paymentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            international = await response.parse()
            assert_matches_type(InternationalRetrieveStatusResponse, international, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_status(self, async_client: AsyncJocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payment_id` but received ''"):
            await async_client.payments.international.with_raw_response.retrieve_status(
                "",
            )

    @parametrize
    async def test_method_send_sepa(self, async_client: AsyncJocall3) -> None:
        international = await async_client.payments.international.send_sepa(
            amount=0,
            iban="iban",
        )
        assert international is None

    @parametrize
    async def test_raw_response_send_sepa(self, async_client: AsyncJocall3) -> None:
        response = await async_client.payments.international.with_raw_response.send_sepa(
            amount=0,
            iban="iban",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        international = await response.parse()
        assert international is None

    @parametrize
    async def test_streaming_response_send_sepa(self, async_client: AsyncJocall3) -> None:
        async with async_client.payments.international.with_streaming_response.send_sepa(
            amount=0,
            iban="iban",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            international = await response.parse()
            assert international is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_send_swift(self, async_client: AsyncJocall3) -> None:
        international = await async_client.payments.international.send_swift(
            amount=0,
            bic="bic",
            currency="currency",
            iban="iban",
        )
        assert international is None

    @parametrize
    async def test_raw_response_send_swift(self, async_client: AsyncJocall3) -> None:
        response = await async_client.payments.international.with_raw_response.send_swift(
            amount=0,
            bic="bic",
            currency="currency",
            iban="iban",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        international = await response.parse()
        assert international is None

    @parametrize
    async def test_streaming_response_send_swift(self, async_client: AsyncJocall3) -> None:
        async with async_client.payments.international.with_streaming_response.send_swift(
            amount=0,
            bic="bic",
            currency="currency",
            iban="iban",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            international = await response.parse()
            assert international is None

        assert cast(Any, response.is_closed) is True
