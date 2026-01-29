# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .status import (
    StatusResource,
    AsyncStatusResource,
    StatusResourceWithRawResponse,
    AsyncStatusResourceWithRawResponse,
    StatusResourceWithStreamingResponse,
    AsyncStatusResourceWithStreamingResponse,
)
from .sandbox import (
    SandboxResource,
    AsyncSandboxResource,
    SandboxResourceWithRawResponse,
    AsyncSandboxResourceWithRawResponse,
    SandboxResourceWithStreamingResponse,
    AsyncSandboxResourceWithStreamingResponse,
)
from .webhooks import (
    WebhooksResource,
    AsyncWebhooksResource,
    WebhooksResourceWithRawResponse,
    AsyncWebhooksResourceWithRawResponse,
    WebhooksResourceWithStreamingResponse,
    AsyncWebhooksResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .audit_logs import (
    AuditLogsResource,
    AsyncAuditLogsResource,
    AuditLogsResourceWithRawResponse,
    AsyncAuditLogsResourceWithRawResponse,
    AuditLogsResourceWithStreamingResponse,
    AsyncAuditLogsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .verification import (
    VerificationResource,
    AsyncVerificationResource,
    VerificationResourceWithRawResponse,
    AsyncVerificationResourceWithRawResponse,
    VerificationResourceWithStreamingResponse,
    AsyncVerificationResourceWithStreamingResponse,
)
from .notifications import (
    NotificationsResource,
    AsyncNotificationsResource,
    NotificationsResourceWithRawResponse,
    AsyncNotificationsResourceWithRawResponse,
    NotificationsResourceWithStreamingResponse,
    AsyncNotificationsResourceWithStreamingResponse,
)

__all__ = ["SystemResource", "AsyncSystemResource"]


class SystemResource(SyncAPIResource):
    @cached_property
    def status(self) -> StatusResource:
        return StatusResource(self._client)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        return WebhooksResource(self._client)

    @cached_property
    def audit_logs(self) -> AuditLogsResource:
        return AuditLogsResource(self._client)

    @cached_property
    def sandbox(self) -> SandboxResource:
        return SandboxResource(self._client)

    @cached_property
    def verification(self) -> VerificationResource:
        return VerificationResource(self._client)

    @cached_property
    def notifications(self) -> NotificationsResource:
        return NotificationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SystemResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/diplomat-bit/aibank#accessing-raw-response-data-eg-headers
        """
        return SystemResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SystemResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/diplomat-bit/aibank#with_streaming_response
        """
        return SystemResourceWithStreamingResponse(self)


class AsyncSystemResource(AsyncAPIResource):
    @cached_property
    def status(self) -> AsyncStatusResource:
        return AsyncStatusResource(self._client)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        return AsyncWebhooksResource(self._client)

    @cached_property
    def audit_logs(self) -> AsyncAuditLogsResource:
        return AsyncAuditLogsResource(self._client)

    @cached_property
    def sandbox(self) -> AsyncSandboxResource:
        return AsyncSandboxResource(self._client)

    @cached_property
    def verification(self) -> AsyncVerificationResource:
        return AsyncVerificationResource(self._client)

    @cached_property
    def notifications(self) -> AsyncNotificationsResource:
        return AsyncNotificationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSystemResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/diplomat-bit/aibank#accessing-raw-response-data-eg-headers
        """
        return AsyncSystemResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSystemResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/diplomat-bit/aibank#with_streaming_response
        """
        return AsyncSystemResourceWithStreamingResponse(self)


class SystemResourceWithRawResponse:
    def __init__(self, system: SystemResource) -> None:
        self._system = system

    @cached_property
    def status(self) -> StatusResourceWithRawResponse:
        return StatusResourceWithRawResponse(self._system.status)

    @cached_property
    def webhooks(self) -> WebhooksResourceWithRawResponse:
        return WebhooksResourceWithRawResponse(self._system.webhooks)

    @cached_property
    def audit_logs(self) -> AuditLogsResourceWithRawResponse:
        return AuditLogsResourceWithRawResponse(self._system.audit_logs)

    @cached_property
    def sandbox(self) -> SandboxResourceWithRawResponse:
        return SandboxResourceWithRawResponse(self._system.sandbox)

    @cached_property
    def verification(self) -> VerificationResourceWithRawResponse:
        return VerificationResourceWithRawResponse(self._system.verification)

    @cached_property
    def notifications(self) -> NotificationsResourceWithRawResponse:
        return NotificationsResourceWithRawResponse(self._system.notifications)


class AsyncSystemResourceWithRawResponse:
    def __init__(self, system: AsyncSystemResource) -> None:
        self._system = system

    @cached_property
    def status(self) -> AsyncStatusResourceWithRawResponse:
        return AsyncStatusResourceWithRawResponse(self._system.status)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResourceWithRawResponse:
        return AsyncWebhooksResourceWithRawResponse(self._system.webhooks)

    @cached_property
    def audit_logs(self) -> AsyncAuditLogsResourceWithRawResponse:
        return AsyncAuditLogsResourceWithRawResponse(self._system.audit_logs)

    @cached_property
    def sandbox(self) -> AsyncSandboxResourceWithRawResponse:
        return AsyncSandboxResourceWithRawResponse(self._system.sandbox)

    @cached_property
    def verification(self) -> AsyncVerificationResourceWithRawResponse:
        return AsyncVerificationResourceWithRawResponse(self._system.verification)

    @cached_property
    def notifications(self) -> AsyncNotificationsResourceWithRawResponse:
        return AsyncNotificationsResourceWithRawResponse(self._system.notifications)


class SystemResourceWithStreamingResponse:
    def __init__(self, system: SystemResource) -> None:
        self._system = system

    @cached_property
    def status(self) -> StatusResourceWithStreamingResponse:
        return StatusResourceWithStreamingResponse(self._system.status)

    @cached_property
    def webhooks(self) -> WebhooksResourceWithStreamingResponse:
        return WebhooksResourceWithStreamingResponse(self._system.webhooks)

    @cached_property
    def audit_logs(self) -> AuditLogsResourceWithStreamingResponse:
        return AuditLogsResourceWithStreamingResponse(self._system.audit_logs)

    @cached_property
    def sandbox(self) -> SandboxResourceWithStreamingResponse:
        return SandboxResourceWithStreamingResponse(self._system.sandbox)

    @cached_property
    def verification(self) -> VerificationResourceWithStreamingResponse:
        return VerificationResourceWithStreamingResponse(self._system.verification)

    @cached_property
    def notifications(self) -> NotificationsResourceWithStreamingResponse:
        return NotificationsResourceWithStreamingResponse(self._system.notifications)


class AsyncSystemResourceWithStreamingResponse:
    def __init__(self, system: AsyncSystemResource) -> None:
        self._system = system

    @cached_property
    def status(self) -> AsyncStatusResourceWithStreamingResponse:
        return AsyncStatusResourceWithStreamingResponse(self._system.status)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResourceWithStreamingResponse:
        return AsyncWebhooksResourceWithStreamingResponse(self._system.webhooks)

    @cached_property
    def audit_logs(self) -> AsyncAuditLogsResourceWithStreamingResponse:
        return AsyncAuditLogsResourceWithStreamingResponse(self._system.audit_logs)

    @cached_property
    def sandbox(self) -> AsyncSandboxResourceWithStreamingResponse:
        return AsyncSandboxResourceWithStreamingResponse(self._system.sandbox)

    @cached_property
    def verification(self) -> AsyncVerificationResourceWithStreamingResponse:
        return AsyncVerificationResourceWithStreamingResponse(self._system.verification)

    @cached_property
    def notifications(self) -> AsyncNotificationsResourceWithStreamingResponse:
        return AsyncNotificationsResourceWithStreamingResponse(self._system.notifications)
