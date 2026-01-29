# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["AnalysisGenerateSwotResponse"]


class AnalysisGenerateSwotResponse(BaseModel):
    strengths: Optional[List[str]] = None

    weaknesses: Optional[List[str]] = None
