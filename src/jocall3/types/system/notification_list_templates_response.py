# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["NotificationListTemplatesResponse", "NotificationListTemplatesResponseItem"]


class NotificationListTemplatesResponseItem(BaseModel):
    id: str

    channel: str

    name: str


NotificationListTemplatesResponse: TypeAlias = List[NotificationListTemplatesResponseItem]
