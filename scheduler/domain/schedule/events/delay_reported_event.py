from dataclasses import dataclass, field
from datetime import timedelta

from diator.events import DomainEvent

from scheduler.domain.common.identity import Identity
from scheduler.domain.schedule.enums import DelayReportStatusEnum


@dataclass(frozen=True, kw_only=True)
class DelayReportedEvent(DomainEvent):
    report_id: Identity
    reporter_id: Identity
    ride_id: Identity
    delay_delta: timedelta
    comment: str | None = field(default=None)
    status: DelayReportStatusEnum = field(default=DelayReportStatusEnum.REPORTED)
