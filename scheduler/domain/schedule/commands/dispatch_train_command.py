from dataclasses import dataclass

from diator.requests import Request

from scheduler.domain.schedule.enums import UserRoleEnum
from scheduler.domain.common.identity import Identity


@dataclass(frozen=True, kw_only=True)
class DispatchTrainCommand(Request):
    current_user_role: UserRoleEnum
    train_id: Identity
    ride_id: Identity
