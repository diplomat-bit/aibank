# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3
from tests.utils import assert_matches_type
from jocall3.types import LendingGetStatusResponse, LendingSubmitApplicationResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLending:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_status(self, client: Jocall3) -> None:
        lending = client.lending.get_status(
            "appId",
        )
        assert_matches_type(LendingGetStatusResponse, lending, path=["response"])

    @parametrize
    def test_raw_response_get_status(self, client: Jocall3) -> None:
        response = client.lending.with_raw_response.get_status(
            "appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lending = response.parse()
        assert_matches_type(LendingGetStatusResponse, lending, path=["response"])

    @parametrize
    def test_streaming_response_get_status(self, client: Jocall3) -> None:
        with client.lending.with_streaming_response.get_status(
            "appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lending = response.parse()
            assert_matches_type(LendingGetStatusResponse, lending, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_status(self, client: Jocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.lending.with_raw_response.get_status(
                "",
            )

    @parametrize
    def test_method_submit_application(self, client: Jocall3) -> None:
        lending = client.lending.submit_application(
            amount=0,
            employment_data={
                "employer": "employer",
                "monthly_income": 0,
            },
            loan_type="MORTGAGE",
            term_months=0,
        )
        assert_matches_type(LendingSubmitApplicationResponse, lending, path=["response"])

    @parametrize
    def test_method_submit_application_with_all_params(self, client: Jocall3) -> None:
        lending = client.lending.submit_application(
            amount=0,
            employment_data={
                "employer": "employer",
                "monthly_income": 0,
                "tenure_months": 0,
            },
            loan_type="MORTGAGE",
            term_months=0,
            assets=[{}],
            collateral_id="collateralId",
            liabilities=[{}],
        )
        assert_matches_type(LendingSubmitApplicationResponse, lending, path=["response"])

    @parametrize
    def test_raw_response_submit_application(self, client: Jocall3) -> None:
        response = client.lending.with_raw_response.submit_application(
            amount=0,
            employment_data={
                "employer": "employer",
                "monthly_income": 0,
            },
            loan_type="MORTGAGE",
            term_months=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lending = response.parse()
        assert_matches_type(LendingSubmitApplicationResponse, lending, path=["response"])

    @parametrize
    def test_streaming_response_submit_application(self, client: Jocall3) -> None:
        with client.lending.with_streaming_response.submit_application(
            amount=0,
            employment_data={
                "employer": "employer",
                "monthly_income": 0,
            },
            loan_type="MORTGAGE",
            term_months=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lending = response.parse()
            assert_matches_type(LendingSubmitApplicationResponse, lending, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLending:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_status(self, async_client: AsyncJocall3) -> None:
        lending = await async_client.lending.get_status(
            "appId",
        )
        assert_matches_type(LendingGetStatusResponse, lending, path=["response"])

    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncJocall3) -> None:
        response = await async_client.lending.with_raw_response.get_status(
            "appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lending = await response.parse()
        assert_matches_type(LendingGetStatusResponse, lending, path=["response"])

    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncJocall3) -> None:
        async with async_client.lending.with_streaming_response.get_status(
            "appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lending = await response.parse()
            assert_matches_type(LendingGetStatusResponse, lending, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_status(self, async_client: AsyncJocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.lending.with_raw_response.get_status(
                "",
            )

    @parametrize
    async def test_method_submit_application(self, async_client: AsyncJocall3) -> None:
        lending = await async_client.lending.submit_application(
            amount=0,
            employment_data={
                "employer": "employer",
                "monthly_income": 0,
            },
            loan_type="MORTGAGE",
            term_months=0,
        )
        assert_matches_type(LendingSubmitApplicationResponse, lending, path=["response"])

    @parametrize
    async def test_method_submit_application_with_all_params(self, async_client: AsyncJocall3) -> None:
        lending = await async_client.lending.submit_application(
            amount=0,
            employment_data={
                "employer": "employer",
                "monthly_income": 0,
                "tenure_months": 0,
            },
            loan_type="MORTGAGE",
            term_months=0,
            assets=[{}],
            collateral_id="collateralId",
            liabilities=[{}],
        )
        assert_matches_type(LendingSubmitApplicationResponse, lending, path=["response"])

    @parametrize
    async def test_raw_response_submit_application(self, async_client: AsyncJocall3) -> None:
        response = await async_client.lending.with_raw_response.submit_application(
            amount=0,
            employment_data={
                "employer": "employer",
                "monthly_income": 0,
            },
            loan_type="MORTGAGE",
            term_months=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lending = await response.parse()
        assert_matches_type(LendingSubmitApplicationResponse, lending, path=["response"])

    @parametrize
    async def test_streaming_response_submit_application(self, async_client: AsyncJocall3) -> None:
        async with async_client.lending.with_streaming_response.submit_application(
            amount=0,
            employment_data={
                "employer": "employer",
                "monthly_income": 0,
            },
            loan_type="MORTGAGE",
            term_months=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lending = await response.parse()
            assert_matches_type(LendingSubmitApplicationResponse, lending, path=["response"])

        assert cast(Any, response.is_closed) is True
