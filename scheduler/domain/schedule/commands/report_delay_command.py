from dataclasses import dataclass, field

from diator.requests import Request

from scheduler.domain.common.identity import Identity
from scheduler.domain.schedule.enums import UserRoleEnum


@dataclass(frozen=True, kw_only=True)
class ReportDelayCommand(Request):
    reporter_role: UserRoleEnum
    reporter_id: Identity
    report_id: Identity = field(default_factory=Identity)
    ride_id: Identity
    delay_minutes: int
    comment: str | None = field(default=None)
