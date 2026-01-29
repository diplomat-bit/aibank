# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["SimulateRunMonteCarloResponse"]


class SimulateRunMonteCarloResponse(BaseModel):
    distribution_graph_data: Optional[List[object]] = FieldInfo(alias="distributionGraphData", default=None)

    probability_of_success: Optional[float] = FieldInfo(alias="probabilityOfSuccess", default=None)

    simulation_id: Optional[str] = FieldInfo(alias="simulationId", default=None)
