# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3
from tests.utils import assert_matches_type
from jocall3.types import CorporateOnboardEntityResponse
from jocall3._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCorporate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_onboard_entity(self, client: Jocall3) -> None:
        corporate = client.corporate.onboard_entity(
            entity_type="LLC",
            jurisdiction="DE",
            legal_name="legalName",
            tax_id="taxId",
        )
        assert_matches_type(CorporateOnboardEntityResponse, corporate, path=["response"])

    @parametrize
    def test_method_onboard_entity_with_all_params(self, client: Jocall3) -> None:
        corporate = client.corporate.onboard_entity(
            entity_type="LLC",
            jurisdiction="DE",
            legal_name="legalName",
            tax_id="taxId",
            beneficial_owners=[
                {
                    "id": "id",
                    "email": "dev@stainless.com",
                    "identity_verified": True,
                    "name": "name",
                    "address": {
                        "city": "city",
                        "country": "country",
                        "street": "street",
                        "state": "state",
                        "zip": "zip",
                    },
                    "preferences": {"foo": "bar"},
                    "security_status": {
                        "last_login": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "two_factor_enabled": True,
                    },
                }
            ],
        )
        assert_matches_type(CorporateOnboardEntityResponse, corporate, path=["response"])

    @parametrize
    def test_raw_response_onboard_entity(self, client: Jocall3) -> None:
        response = client.corporate.with_raw_response.onboard_entity(
            entity_type="LLC",
            jurisdiction="DE",
            legal_name="legalName",
            tax_id="taxId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        corporate = response.parse()
        assert_matches_type(CorporateOnboardEntityResponse, corporate, path=["response"])

    @parametrize
    def test_streaming_response_onboard_entity(self, client: Jocall3) -> None:
        with client.corporate.with_streaming_response.onboard_entity(
            entity_type="LLC",
            jurisdiction="DE",
            legal_name="legalName",
            tax_id="taxId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            corporate = response.parse()
            assert_matches_type(CorporateOnboardEntityResponse, corporate, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCorporate:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_onboard_entity(self, async_client: AsyncJocall3) -> None:
        corporate = await async_client.corporate.onboard_entity(
            entity_type="LLC",
            jurisdiction="DE",
            legal_name="legalName",
            tax_id="taxId",
        )
        assert_matches_type(CorporateOnboardEntityResponse, corporate, path=["response"])

    @parametrize
    async def test_method_onboard_entity_with_all_params(self, async_client: AsyncJocall3) -> None:
        corporate = await async_client.corporate.onboard_entity(
            entity_type="LLC",
            jurisdiction="DE",
            legal_name="legalName",
            tax_id="taxId",
            beneficial_owners=[
                {
                    "id": "id",
                    "email": "dev@stainless.com",
                    "identity_verified": True,
                    "name": "name",
                    "address": {
                        "city": "city",
                        "country": "country",
                        "street": "street",
                        "state": "state",
                        "zip": "zip",
                    },
                    "preferences": {"foo": "bar"},
                    "security_status": {
                        "last_login": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "two_factor_enabled": True,
                    },
                }
            ],
        )
        assert_matches_type(CorporateOnboardEntityResponse, corporate, path=["response"])

    @parametrize
    async def test_raw_response_onboard_entity(self, async_client: AsyncJocall3) -> None:
        response = await async_client.corporate.with_raw_response.onboard_entity(
            entity_type="LLC",
            jurisdiction="DE",
            legal_name="legalName",
            tax_id="taxId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        corporate = await response.parse()
        assert_matches_type(CorporateOnboardEntityResponse, corporate, path=["response"])

    @parametrize
    async def test_streaming_response_onboard_entity(self, async_client: AsyncJocall3) -> None:
        async with async_client.corporate.with_streaming_response.onboard_entity(
            entity_type="LLC",
            jurisdiction="DE",
            legal_name="legalName",
            tax_id="taxId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            corporate = await response.parse()
            assert_matches_type(CorporateOnboardEntityResponse, corporate, path=["response"])

        assert cast(Any, response.is_closed) is True
