# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jocall3 import Jocall3, AsyncJocall3
from tests.utils import assert_matches_type
from jocall3.types.users.me import DeviceListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDevices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Jocall3) -> None:
        device = client.users.me.devices.list()
        assert_matches_type(DeviceListResponse, device, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Jocall3) -> None:
        response = client.users.me.devices.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = response.parse()
        assert_matches_type(DeviceListResponse, device, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Jocall3) -> None:
        with client.users.me.devices.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = response.parse()
            assert_matches_type(DeviceListResponse, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_deregister(self, client: Jocall3) -> None:
        device = client.users.me.devices.deregister(
            "deviceId",
        )
        assert device is None

    @parametrize
    def test_raw_response_deregister(self, client: Jocall3) -> None:
        response = client.users.me.devices.with_raw_response.deregister(
            "deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = response.parse()
        assert device is None

    @parametrize
    def test_streaming_response_deregister(self, client: Jocall3) -> None:
        with client.users.me.devices.with_streaming_response.deregister(
            "deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = response.parse()
            assert device is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_deregister(self, client: Jocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.users.me.devices.with_raw_response.deregister(
                "",
            )

    @parametrize
    def test_method_register(self, client: Jocall3) -> None:
        device = client.users.me.devices.register(
            device_id="deviceId",
            type="type",
        )
        assert device is None

    @parametrize
    def test_method_register_with_all_params(self, client: Jocall3) -> None:
        device = client.users.me.devices.register(
            device_id="deviceId",
            type="type",
            push_token="pushToken",
        )
        assert device is None

    @parametrize
    def test_raw_response_register(self, client: Jocall3) -> None:
        response = client.users.me.devices.with_raw_response.register(
            device_id="deviceId",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = response.parse()
        assert device is None

    @parametrize
    def test_streaming_response_register(self, client: Jocall3) -> None:
        with client.users.me.devices.with_streaming_response.register(
            device_id="deviceId",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = response.parse()
            assert device is None

        assert cast(Any, response.is_closed) is True


class TestAsyncDevices:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncJocall3) -> None:
        device = await async_client.users.me.devices.list()
        assert_matches_type(DeviceListResponse, device, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJocall3) -> None:
        response = await async_client.users.me.devices.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = await response.parse()
        assert_matches_type(DeviceListResponse, device, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJocall3) -> None:
        async with async_client.users.me.devices.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = await response.parse()
            assert_matches_type(DeviceListResponse, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_deregister(self, async_client: AsyncJocall3) -> None:
        device = await async_client.users.me.devices.deregister(
            "deviceId",
        )
        assert device is None

    @parametrize
    async def test_raw_response_deregister(self, async_client: AsyncJocall3) -> None:
        response = await async_client.users.me.devices.with_raw_response.deregister(
            "deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = await response.parse()
        assert device is None

    @parametrize
    async def test_streaming_response_deregister(self, async_client: AsyncJocall3) -> None:
        async with async_client.users.me.devices.with_streaming_response.deregister(
            "deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = await response.parse()
            assert device is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_deregister(self, async_client: AsyncJocall3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.users.me.devices.with_raw_response.deregister(
                "",
            )

    @parametrize
    async def test_method_register(self, async_client: AsyncJocall3) -> None:
        device = await async_client.users.me.devices.register(
            device_id="deviceId",
            type="type",
        )
        assert device is None

    @parametrize
    async def test_method_register_with_all_params(self, async_client: AsyncJocall3) -> None:
        device = await async_client.users.me.devices.register(
            device_id="deviceId",
            type="type",
            push_token="pushToken",
        )
        assert device is None

    @parametrize
    async def test_raw_response_register(self, async_client: AsyncJocall3) -> None:
        response = await async_client.users.me.devices.with_raw_response.register(
            device_id="deviceId",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = await response.parse()
        assert device is None

    @parametrize
    async def test_streaming_response_register(self, async_client: AsyncJocall3) -> None:
        async with async_client.users.me.devices.with_streaming_response.register(
            device_id="deviceId",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = await response.parse()
            assert device is None

        assert cast(Any, response.is_closed) is True
