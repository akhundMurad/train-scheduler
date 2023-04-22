from dataclasses import dataclass, field
from datetime import timedelta

from scheduler.domain.common.entity import Entity
from scheduler.domain.common.identity import Identity
from scheduler.domain.schedule.enums import DelayReportStatusEnum


@dataclass(kw_only=True, eq=False)
class DelayReport(Entity):
    reporter_id: Identity
    ride_id: Identity
    delay_delta: timedelta
    comment: str | None = field(default=None)
    status: DelayReportStatusEnum = field(default=DelayReportStatusEnum.REPORTED)
