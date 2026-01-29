# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3
from tests.utils import assert_matches_type
from jocall3._utils import parse_date
from jocall3.types.corporate import (
    ComplianceScreenPepResponse,
    ComplianceScreenSanctionsResponse,
    ComplianceScreenAdverseMediaResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompliance:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_screen_adverse_media(self, client: Jocall3) -> None:
        compliance = client.corporate.compliance.screen_adverse_media(
            query="query",
        )
        assert_matches_type(ComplianceScreenAdverseMediaResponse, compliance, path=["response"])

    @parametrize
    def test_method_screen_adverse_media_with_all_params(self, client: Jocall3) -> None:
        compliance = client.corporate.compliance.screen_adverse_media(
            query="query",
            depth="shallow",
        )
        assert_matches_type(ComplianceScreenAdverseMediaResponse, compliance, path=["response"])

    @parametrize
    def test_raw_response_screen_adverse_media(self, client: Jocall3) -> None:
        response = client.corporate.compliance.with_raw_response.screen_adverse_media(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compliance = response.parse()
        assert_matches_type(ComplianceScreenAdverseMediaResponse, compliance, path=["response"])

    @parametrize
    def test_streaming_response_screen_adverse_media(self, client: Jocall3) -> None:
        with client.corporate.compliance.with_streaming_response.screen_adverse_media(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compliance = response.parse()
            assert_matches_type(ComplianceScreenAdverseMediaResponse, compliance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_screen_pep(self, client: Jocall3) -> None:
        compliance = client.corporate.compliance.screen_pep(
            full_name="fullName",
        )
        assert_matches_type(ComplianceScreenPepResponse, compliance, path=["response"])

    @parametrize
    def test_method_screen_pep_with_all_params(self, client: Jocall3) -> None:
        compliance = client.corporate.compliance.screen_pep(
            full_name="fullName",
            dob=parse_date("2019-12-27"),
        )
        assert_matches_type(ComplianceScreenPepResponse, compliance, path=["response"])

    @parametrize
    def test_raw_response_screen_pep(self, client: Jocall3) -> None:
        response = client.corporate.compliance.with_raw_response.screen_pep(
            full_name="fullName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compliance = response.parse()
        assert_matches_type(ComplianceScreenPepResponse, compliance, path=["response"])

    @parametrize
    def test_streaming_response_screen_pep(self, client: Jocall3) -> None:
        with client.corporate.compliance.with_streaming_response.screen_pep(
            full_name="fullName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compliance = response.parse()
            assert_matches_type(ComplianceScreenPepResponse, compliance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_screen_sanctions(self, client: Jocall3) -> None:
        compliance = client.corporate.compliance.screen_sanctions(
            entities=[{}],
        )
        assert_matches_type(ComplianceScreenSanctionsResponse, compliance, path=["response"])

    @parametrize
    def test_method_screen_sanctions_with_all_params(self, client: Jocall3) -> None:
        compliance = client.corporate.compliance.screen_sanctions(
            entities=[
                {
                    "country": "country",
                    "name": "name",
                }
            ],
            check_type="standard",
        )
        assert_matches_type(ComplianceScreenSanctionsResponse, compliance, path=["response"])

    @parametrize
    def test_raw_response_screen_sanctions(self, client: Jocall3) -> None:
        response = client.corporate.compliance.with_raw_response.screen_sanctions(
            entities=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compliance = response.parse()
        assert_matches_type(ComplianceScreenSanctionsResponse, compliance, path=["response"])

    @parametrize
    def test_streaming_response_screen_sanctions(self, client: Jocall3) -> None:
        with client.corporate.compliance.with_streaming_response.screen_sanctions(
            entities=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compliance = response.parse()
            assert_matches_type(ComplianceScreenSanctionsResponse, compliance, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCompliance:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_screen_adverse_media(self, async_client: AsyncJocall3) -> None:
        compliance = await async_client.corporate.compliance.screen_adverse_media(
            query="query",
        )
        assert_matches_type(ComplianceScreenAdverseMediaResponse, compliance, path=["response"])

    @parametrize
    async def test_method_screen_adverse_media_with_all_params(self, async_client: AsyncJocall3) -> None:
        compliance = await async_client.corporate.compliance.screen_adverse_media(
            query="query",
            depth="shallow",
        )
        assert_matches_type(ComplianceScreenAdverseMediaResponse, compliance, path=["response"])

    @parametrize
    async def test_raw_response_screen_adverse_media(self, async_client: AsyncJocall3) -> None:
        response = await async_client.corporate.compliance.with_raw_response.screen_adverse_media(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compliance = await response.parse()
        assert_matches_type(ComplianceScreenAdverseMediaResponse, compliance, path=["response"])

    @parametrize
    async def test_streaming_response_screen_adverse_media(self, async_client: AsyncJocall3) -> None:
        async with async_client.corporate.compliance.with_streaming_response.screen_adverse_media(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compliance = await response.parse()
            assert_matches_type(ComplianceScreenAdverseMediaResponse, compliance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_screen_pep(self, async_client: AsyncJocall3) -> None:
        compliance = await async_client.corporate.compliance.screen_pep(
            full_name="fullName",
        )
        assert_matches_type(ComplianceScreenPepResponse, compliance, path=["response"])

    @parametrize
    async def test_method_screen_pep_with_all_params(self, async_client: AsyncJocall3) -> None:
        compliance = await async_client.corporate.compliance.screen_pep(
            full_name="fullName",
            dob=parse_date("2019-12-27"),
        )
        assert_matches_type(ComplianceScreenPepResponse, compliance, path=["response"])

    @parametrize
    async def test_raw_response_screen_pep(self, async_client: AsyncJocall3) -> None:
        response = await async_client.corporate.compliance.with_raw_response.screen_pep(
            full_name="fullName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compliance = await response.parse()
        assert_matches_type(ComplianceScreenPepResponse, compliance, path=["response"])

    @parametrize
    async def test_streaming_response_screen_pep(self, async_client: AsyncJocall3) -> None:
        async with async_client.corporate.compliance.with_streaming_response.screen_pep(
            full_name="fullName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compliance = await response.parse()
            assert_matches_type(ComplianceScreenPepResponse, compliance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_screen_sanctions(self, async_client: AsyncJocall3) -> None:
        compliance = await async_client.corporate.compliance.screen_sanctions(
            entities=[{}],
        )
        assert_matches_type(ComplianceScreenSanctionsResponse, compliance, path=["response"])

    @parametrize
    async def test_method_screen_sanctions_with_all_params(self, async_client: AsyncJocall3) -> None:
        compliance = await async_client.corporate.compliance.screen_sanctions(
            entities=[
                {
                    "country": "country",
                    "name": "name",
                }
            ],
            check_type="standard",
        )
        assert_matches_type(ComplianceScreenSanctionsResponse, compliance, path=["response"])

    @parametrize
    async def test_raw_response_screen_sanctions(self, async_client: AsyncJocall3) -> None:
        response = await async_client.corporate.compliance.with_raw_response.screen_sanctions(
            entities=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compliance = await response.parse()
        assert_matches_type(ComplianceScreenSanctionsResponse, compliance, path=["response"])

    @parametrize
    async def test_streaming_response_screen_sanctions(self, async_client: AsyncJocall3) -> None:
        async with async_client.corporate.compliance.with_streaming_response.screen_sanctions(
            entities=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compliance = await response.parse()
            assert_matches_type(ComplianceScreenSanctionsResponse, compliance, path=["response"])

        assert cast(Any, response.is_closed) is True
