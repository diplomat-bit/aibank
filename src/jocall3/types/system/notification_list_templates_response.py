# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["NotificationListTemplatesResponse", "NotificationListTemplatesResponseItem"]


class NotificationListTemplatesResponseItem(BaseModel):
    id: str

    channel: Literal["email", "push", "sms"]

    name: str

    body: Optional[str] = None


NotificationListTemplatesResponse: TypeAlias = List[NotificationListTemplatesResponseItem]
