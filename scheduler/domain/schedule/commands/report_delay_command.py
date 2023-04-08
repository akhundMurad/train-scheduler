from dataclasses import dataclass, field

from diator.requests import Request

from scheduler.domain.common.identity import Identity
from scheduler.domain.schedule.enums import UserRoleEnum


@dataclass(frozen=True, kw_only=True)
class ReportDelayCommand(Request):
    reported_role: UserRoleEnum
    reported_id: Identity
    ride_id: Identity
    comment: str | None = field(default=None)
