# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["NotificationSendParams"]


class NotificationSendParams(TypedDict, total=False):
    body: Required[str]

    title: Required[str]

    user_id: Required[str]
