# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["SimulateRunStandardResponse", "ScenarioResult"]


class ScenarioResult(BaseModel):
    final_net_worth: Optional[float] = FieldInfo(alias="finalNetWorth", default=None)

    narrative: Optional[str] = None

    scenario_name: Optional[str] = FieldInfo(alias="scenarioName", default=None)


class SimulateRunStandardResponse(BaseModel):
    overall_summary: str = FieldInfo(alias="overallSummary")

    scenario_results: List[ScenarioResult] = FieldInfo(alias="scenarioResults")

    simulation_id: str = FieldInfo(alias="simulationId")
