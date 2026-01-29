# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ModelListVersionsResponse", "Model"]


class Model(BaseModel):
    api_model_id: str = FieldInfo(alias="modelId")

    version: str


class ModelListVersionsResponse(BaseModel):
    models: Optional[List[Model]] = None
