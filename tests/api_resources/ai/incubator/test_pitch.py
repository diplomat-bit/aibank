# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3
from tests.utils import assert_matches_type
from jocall3.types.ai.incubator import PitchRetrieveDetailsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPitch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve_details(self, client: Jocall3) -> None:
        pitch = client.ai.incubator.pitch.retrieve_details(
            "pitchId",
        )
        assert_matches_type(PitchRetrieveDetailsResponse, pitch, path=["response"])

    @parametrize
    def test_raw_response_retrieve_details(self, client: Jocall3) -> None:
        response = client.ai.incubator.pitch.with_raw_response.retrieve_details(
            "pitchId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pitch = response.parse()
        assert_matches_type(PitchRetrieveDetailsResponse, pitch, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_details(self, client: Jocall3) -> None:
        with client.ai.incubator.pitch.with_streaming_response.retrieve_details(
            "pitchId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pitch = response.parse()
            assert_matches_type(PitchRetrieveDetailsResponse, pitch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_details(self, client: Jocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pitch_id` but received ''"):
            client.ai.incubator.pitch.with_raw_response.retrieve_details(
                "",
            )

    @parametrize
    def test_method_submit_feedback(self, client: Jocall3) -> None:
        pitch = client.ai.incubator.pitch.submit_feedback(
            pitch_id="pitchId",
            answers=[{}],
        )
        assert pitch is None

    @parametrize
    def test_raw_response_submit_feedback(self, client: Jocall3) -> None:
        response = client.ai.incubator.pitch.with_raw_response.submit_feedback(
            pitch_id="pitchId",
            answers=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pitch = response.parse()
        assert pitch is None

    @parametrize
    def test_streaming_response_submit_feedback(self, client: Jocall3) -> None:
        with client.ai.incubator.pitch.with_streaming_response.submit_feedback(
            pitch_id="pitchId",
            answers=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pitch = response.parse()
            assert pitch is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_submit_feedback(self, client: Jocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pitch_id` but received ''"):
            client.ai.incubator.pitch.with_raw_response.submit_feedback(
                pitch_id="",
                answers=[{}],
            )


class TestAsyncPitch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve_details(self, async_client: AsyncJocall3) -> None:
        pitch = await async_client.ai.incubator.pitch.retrieve_details(
            "pitchId",
        )
        assert_matches_type(PitchRetrieveDetailsResponse, pitch, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_details(self, async_client: AsyncJocall3) -> None:
        response = await async_client.ai.incubator.pitch.with_raw_response.retrieve_details(
            "pitchId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pitch = await response.parse()
        assert_matches_type(PitchRetrieveDetailsResponse, pitch, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_details(self, async_client: AsyncJocall3) -> None:
        async with async_client.ai.incubator.pitch.with_streaming_response.retrieve_details(
            "pitchId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pitch = await response.parse()
            assert_matches_type(PitchRetrieveDetailsResponse, pitch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_details(self, async_client: AsyncJocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pitch_id` but received ''"):
            await async_client.ai.incubator.pitch.with_raw_response.retrieve_details(
                "",
            )

    @parametrize
    async def test_method_submit_feedback(self, async_client: AsyncJocall3) -> None:
        pitch = await async_client.ai.incubator.pitch.submit_feedback(
            pitch_id="pitchId",
            answers=[{}],
        )
        assert pitch is None

    @parametrize
    async def test_raw_response_submit_feedback(self, async_client: AsyncJocall3) -> None:
        response = await async_client.ai.incubator.pitch.with_raw_response.submit_feedback(
            pitch_id="pitchId",
            answers=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pitch = await response.parse()
        assert pitch is None

    @parametrize
    async def test_streaming_response_submit_feedback(self, async_client: AsyncJocall3) -> None:
        async with async_client.ai.incubator.pitch.with_streaming_response.submit_feedback(
            pitch_id="pitchId",
            answers=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pitch = await response.parse()
            assert pitch is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_submit_feedback(self, async_client: AsyncJocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pitch_id` but received ''"):
            await async_client.ai.incubator.pitch.with_raw_response.submit_feedback(
                pitch_id="",
                answers=[{}],
            )
