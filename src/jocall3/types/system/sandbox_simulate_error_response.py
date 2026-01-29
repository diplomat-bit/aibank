# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["SandboxSimulateErrorResponse"]


class SandboxSimulateErrorResponse(BaseModel):
    code: str

    message: str

    timestamp: datetime
