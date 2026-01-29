# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AgentGetPromptsResponse"]


class AgentGetPromptsResponse(BaseModel):
    system_prompt: Optional[str] = FieldInfo(alias="systemPrompt", default=None)

    version: Optional[str] = None
