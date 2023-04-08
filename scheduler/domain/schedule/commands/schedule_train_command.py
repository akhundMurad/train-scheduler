from dataclasses import dataclass
from datetime import datetime

from diator.requests import Request

from scheduler.domain.common.identity import Identity
from scheduler.domain.schedule.enums import UserRoleEnum


@dataclass(frozen=True, kw_only=True)
class ScheduleTrainCommand(Request):
    current_user_role: UserRoleEnum
    current_user_id: Identity
    train_id: Identity
    departure_time: datetime
    arriving_time: datetime
    start_station: str
    end_station: str
