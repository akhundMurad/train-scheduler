from dataclasses import dataclass

from diator.requests import Request

from scheduler.domain.common.identity import Identity
from scheduler.domain.schedule.enums import RideStatusEnum, UserRoleEnum


@dataclass(frozen=True, kw_only=True)
class UpdateRideStatusCommand(Request):
    current_user_role: UserRoleEnum
    train_id: Identity
    ride_id: Identity
    new_status: RideStatusEnum
