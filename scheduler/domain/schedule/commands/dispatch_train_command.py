from dataclasses import dataclass

from diator.requests import Request

from scheduler.domain.common.identity import Identity
from scheduler.domain.schedule.enums import UserRoleEnum


@dataclass(frozen=True, kw_only=True)
class DispatchTrainCommand(Request):
    current_user_role: UserRoleEnum
    ride_id: Identity
