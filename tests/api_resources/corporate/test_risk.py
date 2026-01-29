# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3
from tests.utils import assert_matches_type
from jocall3.types.corporate import RiskStressTestResponse, RiskGetExposureResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRisk:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_exposure(self, client: Jocall3) -> None:
        risk = client.corporate.risk.get_exposure()
        assert_matches_type(RiskGetExposureResponse, risk, path=["response"])

    @parametrize
    def test_raw_response_get_exposure(self, client: Jocall3) -> None:
        response = client.corporate.risk.with_raw_response.get_exposure()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        risk = response.parse()
        assert_matches_type(RiskGetExposureResponse, risk, path=["response"])

    @parametrize
    def test_streaming_response_get_exposure(self, client: Jocall3) -> None:
        with client.corporate.risk.with_streaming_response.get_exposure() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            risk = response.parse()
            assert_matches_type(RiskGetExposureResponse, risk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_stress_test(self, client: Jocall3) -> None:
        risk = client.corporate.risk.stress_test(
            scenario_type="BANK_RUN",
        )
        assert_matches_type(RiskStressTestResponse, risk, path=["response"])

    @parametrize
    def test_method_stress_test_with_all_params(self, client: Jocall3) -> None:
        risk = client.corporate.risk.stress_test(
            scenario_type="BANK_RUN",
            intensity=0,
        )
        assert_matches_type(RiskStressTestResponse, risk, path=["response"])

    @parametrize
    def test_raw_response_stress_test(self, client: Jocall3) -> None:
        response = client.corporate.risk.with_raw_response.stress_test(
            scenario_type="BANK_RUN",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        risk = response.parse()
        assert_matches_type(RiskStressTestResponse, risk, path=["response"])

    @parametrize
    def test_streaming_response_stress_test(self, client: Jocall3) -> None:
        with client.corporate.risk.with_streaming_response.stress_test(
            scenario_type="BANK_RUN",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            risk = response.parse()
            assert_matches_type(RiskStressTestResponse, risk, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRisk:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_exposure(self, async_client: AsyncJocall3) -> None:
        risk = await async_client.corporate.risk.get_exposure()
        assert_matches_type(RiskGetExposureResponse, risk, path=["response"])

    @parametrize
    async def test_raw_response_get_exposure(self, async_client: AsyncJocall3) -> None:
        response = await async_client.corporate.risk.with_raw_response.get_exposure()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        risk = await response.parse()
        assert_matches_type(RiskGetExposureResponse, risk, path=["response"])

    @parametrize
    async def test_streaming_response_get_exposure(self, async_client: AsyncJocall3) -> None:
        async with async_client.corporate.risk.with_streaming_response.get_exposure() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            risk = await response.parse()
            assert_matches_type(RiskGetExposureResponse, risk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_stress_test(self, async_client: AsyncJocall3) -> None:
        risk = await async_client.corporate.risk.stress_test(
            scenario_type="BANK_RUN",
        )
        assert_matches_type(RiskStressTestResponse, risk, path=["response"])

    @parametrize
    async def test_method_stress_test_with_all_params(self, async_client: AsyncJocall3) -> None:
        risk = await async_client.corporate.risk.stress_test(
            scenario_type="BANK_RUN",
            intensity=0,
        )
        assert_matches_type(RiskStressTestResponse, risk, path=["response"])

    @parametrize
    async def test_raw_response_stress_test(self, async_client: AsyncJocall3) -> None:
        response = await async_client.corporate.risk.with_raw_response.stress_test(
            scenario_type="BANK_RUN",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        risk = await response.parse()
        assert_matches_type(RiskStressTestResponse, risk, path=["response"])

    @parametrize
    async def test_streaming_response_stress_test(self, async_client: AsyncJocall3) -> None:
        async with async_client.corporate.risk.with_streaming_response.stress_test(
            scenario_type="BANK_RUN",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            risk = await response.parse()
            assert_matches_type(RiskStressTestResponse, risk, path=["response"])

        assert cast(Any, response.is_closed) is True
