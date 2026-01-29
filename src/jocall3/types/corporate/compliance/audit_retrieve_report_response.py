# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AuditRetrieveReportResponse"]


class AuditRetrieveReportResponse(BaseModel):
    audit_id: str = FieldInfo(alias="auditId")

    overall_compliance_score: int = FieldInfo(alias="overallComplianceScore")

    status: str

    audit_date: Optional[datetime] = FieldInfo(alias="auditDate", default=None)

    findings: Optional[List[object]] = None
