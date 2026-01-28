# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["SimulateRunStandardResponse"]


class SimulateRunStandardResponse(BaseModel):
    risk_analysis: Optional[object] = FieldInfo(alias="riskAnalysis", default=None)
    """AI-driven risk assessment of the simulated scenario."""
